"""
app.py  --  tabbed Streamlit UI.  EDUCATIONAL USE ONLY -- not a medical device.

Run:  streamlit run app.py

Sidebar builds a Patient (one source of body-size truth, shared by every tab).
The drug menus and units come from config.DRUGS. The Simulator tab drives a
multi-drug SimulationEngine, so adding a drug to config.py makes it usable here
with no change to this file.

Tabs: Simulator | Model comparison | VitalDB validation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from patient import Patient
from models import EleveldModel
from dosing import (make_infusion_func, mgkgh_to_permin,
                    event_rate_to_permin, event_dose_to_mass)
from pd import BISModel, time_to_wake
from engine import SimulationEngine
from interactions import response_surface, lookup_interaction
from config import DRUGS, DRUG_OPTIONS, get_models, drug_color
from validation import (varvel_metrics, load_case_data, case_demographics,
                        reconstruct_propofol_mgmin)

st.set_page_config(page_title="Teaching TCI Simulator", layout="wide")
st.title("Teaching TCI / TIVA Simulator")
st.caption("Educational and research use only. Not a medical device. "
           "Do not use for clinical decisions.")

# ---- shared patient (sidebar) ----
with st.sidebar:
    st.header("Patient")
    age = st.number_input("Age (yr)", 1, 100, 60)
    sex = st.selectbox("Sex", ["male", "female"])
    weight = st.number_input("Weight (kg)", 3.0, 200.0, 70.0)
    height = st.number_input("Height (cm)", 50.0, 210.0, 175.0)
    duration = st.number_input("Duration (min)", 10, 600, 120)
    patient = Patient(age, weight, height, sex)
    st.caption(f"LBM {patient.lbm:.1f} kg · FFM {patient.ffm:.1f} kg · "
               f"IBW {patient.ibw:.1f} kg · BMI {patient.bmi:.1f}")


def build_plan_for_drug(events, drug, weight, duration, drug_unit):
    """Event table -> {'infusion': func, 'boluses': [(t,dose)]} for one drug.

    drug_unit is the model's mass unit ('mg' or 'mcg'); every rate AND every
    bolus is normalised to it through dosing.py, so the bolus 'unit' column is
    now honoured (a 'mg/kg' entry scales by weight instead of being read raw)."""
    segs, bols = [], []
    rows = events[events["drug"] == drug].sort_values("time_min").reset_index(drop=True)
    inf_rows = rows[rows["type"] == "infusion"]
    for _, r in rows.iterrows():
        if r["type"] == "bolus":
            dose = event_dose_to_mass(float(r["amount"]), r["unit"], weight, drug_unit)
            bols.append((float(r["time_min"]), dose))
        else:
            start = float(r["time_min"])
            later = inf_rows[inf_rows["time_min"] > start]["time_min"]
            end = float(later.min()) if len(later) else float(duration)
            rate = event_rate_to_permin(float(r["amount"]), r["unit"], weight, drug_unit)
            segs.append((start, end, rate))
    return {"infusion": make_infusion_func(segs), "boluses": bols}


tab_sim, tab_compare, tab_validate = st.tabs(
    ["Simulator", "Model comparison", "VitalDB validation"])

# ======================================================================
# TAB 1 -- SIMULATOR (multi-drug engine)
# ======================================================================
with tab_sim:
    st.subheader("Drug events")
    default = pd.DataFrame({
        "time_min": [0, 0, 0],
        "drug":     ["propofol", "propofol", "remifentanil"],
        "type":     ["bolus", "infusion", "infusion"],
        "amount":   [140.0, 9.0, 0.25],
        "unit":     ["mg", "mg/kg/hr", "mcg/kg/min"],
    })
    events = st.data_editor(default, num_rows="dynamic", use_container_width=True)
    prop_model_name = st.selectbox("Propofol model",
                                   list(get_models("propofol")), index=0)
    st.caption("Drugs available: " + ", ".join(DRUG_OPTIONS) +
               ". Add a row with any of these in the 'drug' column.")

    if st.button("Run simulation", type="primary"):
        drugs = [d for d in events["drug"].unique() if d in DRUGS]
        pk_models = {}
        for d in drugs:
            if d == "propofol":
                cls = get_models("propofol")[prop_model_name]
            else:
                cls = list(get_models(d).values())[0]
            pk_models[d] = cls(patient)
        engine = SimulationEngine(pk_models, {"bis": BISModel()}, dt=1 / 6)
        plan = {d: build_plan_for_drug(events, d, weight, duration,
                                       pk_models[d].units) for d in drugs}
        res = engine.run(plan, duration)

        n = len(drugs)
        fig, axes = plt.subplots(n + 1, 1, figsize=(9, 2.2 * (n + 1)), sharex=True)
        axes = np.atleast_1d(axes)
        for i, d in enumerate(drugs):
            axes[i].plot(res["t"], res["cp"][d], "--", color=drug_color(d),
                         alpha=0.7, label="Cp")
            axes[i].plot(res["t"], res["ce"][d], "-", color=drug_color(d),
                         label="Ce")
            axes[i].set_ylabel(f"{d}\n({pk_models[d].conc_unit})")
            axes[i].legend(loc="upper right", fontsize=8)
        axes[-1].plot(res["t"], res["pd"]["bis"], "k-")
        axes[-1].axhspan(40, 60, color="green", alpha=0.1)
        axes[-1].set_ylabel("BIS"); axes[-1].set_ylim(0, 100)
        axes[-1].set_xlabel("min")
        st.pyplot(fig)

        cols = st.columns(3)
        if "propofol" in res["ce"]:
            cols[0].metric("Propofol Ce (end)",
                           f"{res['ce']['propofol'][-1]:.2f} ug/mL")
            tw = time_to_wake(pk_models["propofol"], engine.X["propofol"][-1],
                              res["ce"]["propofol"][-1], wake_ce=1.2)
            cols[2].metric("Wake-up if stopped now",
                           f"{tw:.0f} min" if tw else ">window")
        cols[1].metric("BIS (end)", f"{res['pd']['bis'][-1]:.0f}")

        if "propofol" in res["ce"] and "remifentanil" in res["ce"]:
            info = lookup_interaction("propofol", "remifentanil")
            p = response_surface(res["ce"]["propofol"][-1], 5.0,
                                 res["ce"]["remifentanil"][-1], 5.0,
                                 alpha=info["alpha"], gamma=5.0)
            (st.success if p >= 0.9 else st.warning)(
                f"Tolerance of laryngoscopy P={p:.2f} [{info['kind']}].")
            st.caption("Interaction constants illustrative; use Bouillon 2004 "
                       "for the real propofol-remifentanil surface.")

# ======================================================================
# TAB 2 -- MODEL COMPARISON
# ======================================================================
with tab_compare:
    st.subheader("Same patient, same dosing, different propofol model")
    sample = st.radio("Sample patient",
                      ["Use sidebar patient", "Young fit (30y/80kg/180cm/M)",
                       "Elderly light (80y/55kg/160cm/F)"], index=0)
    if sample.startswith("Young"):
        pt = Patient(30, 80, 180, "male")
    elif sample.startswith("Elderly"):
        pt = Patient(80, 55, 160, "female")
    else:
        pt = patient

    bolus_mgkg = st.slider("Induction bolus (mg/kg)", 0.0, 3.0, 2.0, 0.5)
    inf_mgkgh = st.slider("Maintenance (mg/kg/h)", 0.0, 15.0, 9.0, 1.0)

    if st.button("Compare models"):
        boluses = [(0.0, bolus_mgkg * pt.weight)]
        inf = make_infusion_func([(0, 60, mgkgh_to_permin(inf_mgkgh, pt.weight))])
        fig, ax = plt.subplots(figsize=(9, 4))
        for name, cls in get_models("propofol").items():
            r = cls(pt).simulate(inf, boluses, t_end=60)
            ax.plot(r["t"], r["cp"], label=f"{name} Cp")
        ax.set_xlabel("min"); ax.set_ylabel("Propofol Cp (ug/mL)")
        ax.set_title(f"{pt.age}y / {pt.weight}kg / {pt.height}cm / {pt.sex}")
        ax.legend()
        st.pyplot(fig)

# ======================================================================
# TAB 3 -- VITALDB VALIDATION
# ======================================================================
with tab_validate:
    st.subheader("Validate against a real VitalDB case")
    st.write("Requires `pip install vitaldb` and network access.")
    caseid = st.number_input("VitalDB case id", 1, 6388, 1)

    @st.cache_data(show_spinner=True)
    def _load(cid):
        data, names = load_case_data(cid)
        demo = case_demographics(cid)
        return data, names, demo

    if st.button("Load and validate"):
        try:
            data, names, demo = _load(int(caseid))
            st.write("Demographics:", demo)
            idx = {n: i for i, n in enumerate(names)}
            rate_mlh = data[:, idx["Orchestra/PPF20_RATE"]]
            pump_ce = data[:, idx["Orchestra/PPF20_CE"]]
            mgmin = reconstruct_propofol_mgmin(rate_mlh)

            secs = np.arange(len(mgmin))
            inf = lambda t: float(mgmin[min(int(t * 60), len(mgmin) - 1)])
            model = EleveldModel(Patient(demo["age"], demo["weight"],
                                         demo["height"], demo["sex"]))
            sim = model.simulate(inf, t_end=len(mgmin) / 60.0,
                                 dt=1 / 60, max_step=1 / 60)
            my_ce = np.interp(secs, sim["t"] * 60.0, sim["ce"])

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(secs / 60.0, pump_ce, label="pump-reported Ce")
            ax.plot(secs / 60.0, my_ce, label="my Eleveld Ce")
            ax.set_xlabel("min"); ax.set_ylabel("Propofol Ce (ug/mL)"); ax.legend()
            st.pyplot(fig)
            st.write("Varvel (my Ce vs pump Ce):", varvel_metrics(pump_ce, my_ce))
        except Exception as exc:
            st.error(f"Could not load/validate: {exc}")
            st.info("Install vitaldb and ensure network access, or verify track "
                    "names/units for this case.")
