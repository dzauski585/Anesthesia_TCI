# TCI Simulator — Streamlit Build Guide

A step-by-step guide to building the front end for your TCI simulator, matching the choices you locked in:

- **Sidebar** for the patient, **main panel** for dosing + plots
- **Sliders with a typed override** for every patient field
- **Editable event grid** (`st.data_editor`) for dosing
- **Bolus and infusion** both supported in one grid
- **Your 8 drugs**, no others; **no pediatric models**
- **Model dropdown only for the first instance of a drug** — the model is then fixed for the whole simulation
- **Plots selectable**: Cp, Ce, BIS, any combination
- **Overlay** (my pick — see Step 7), **linear default with a log toggle**
- **User-selectable clinical readouts**
- No scenario sharing

Work through it top to bottom. Each step adds to one file, `app.py`, and every step runs. A tiny placeholder engine is included so the app works *before* your Weeks 8–16 library is finished — you swap it for the real thing in Step 6.

---

## Step 0 — Setup and project layout

```
tci-app/
├── app.py                 # the Streamlit UI you build here
├── engine.py              # thin adapter over your library (with a stub fallback)
└── tci/                   # your Weeks 8–16 library (patient, models, pd, predict)
```

Install:

```bash
pip install streamlit pandas numpy matplotlib scipy
```

Run at any point with:

```bash
streamlit run app.py
```

**The interface contract.** Keep the UI a thin skin over the library. The app only needs these four things from `tci/`:

- `Patient(age, weight, height, sex, pregnant=False, renal=False)`
- `build_model(drug, model_name, patient)` → an object with `.simulate(...)`
- `model.simulate(events, t_end, dt)` → returns `t, cp, ce` arrays (per drug)
- helpers: `bis_from_ce(ce)`, `p_event(CeP, CeR, ...)`, `time_to_wake(...)`

As long as `simulate()` returns arrays in a stable shape, the whole UI drops onto it.

---

## Step 1 — App skeleton and layout

```python
# app.py
import streamlit as st

st.set_page_config(page_title="TCI Simulator", layout="wide")

st.title("TCI Simulator")
st.caption("Teaching and simulation tool — not for clinical use.")

# main panel gets two columns: dosing (left), results (right)
dose_col, plot_col = st.columns([1, 1.3], gap="large")
```

Run it. You get a title, a caption, and an empty two-column body. The sidebar comes next.

---

## Step 2 — Patient panel (sidebar, slider + typed override)

You wanted a slider you can also type into. Streamlit has no single widget for that, so pair a `slider` with a `number_input` and keep them in sync through `session_state`. This helper does it once and reuses everywhere.

```python
def slider_with_override(label, lo, hi, default, step, key, unit=""):
    """A slider and a number box bound to the same value."""
    if key not in st.session_state:
        st.session_state[key] = default

    def _from_slider():  st.session_state[key] = st.session_state[key + "_sl"]
    def _from_number():  st.session_state[key] = st.session_state[key + "_nb"]

    c1, c2 = st.columns([3, 1])
    c1.slider(label, lo, hi, st.session_state[key], step,
              key=key + "_sl", on_change=_from_slider)
    c2.number_input(unit or " ", lo, hi, st.session_state[key], step,
                    key=key + "_nb", on_change=_from_number, label_visibility="hidden")
    return st.session_state[key]
```

Now build the sidebar:

```python
with st.sidebar:
    st.header("Patient")
    age    = slider_with_override("Age (yr)",    18, 100, 45,  1,   "age",  "yr")
    weight = slider_with_override("Weight (kg)", 30, 200, 70,  1,   "wt",   "kg")
    height = slider_with_override("Height (cm)", 130, 210, 170, 1,  "ht",   "cm")
    sex    = st.radio("Sex", ["Male", "Female"], horizontal=True)

    st.divider()
    st.subheader("Covariates")
    pregnant = st.checkbox("Pregnant (term)")
    renal    = st.checkbox("Severe renal impairment")
    st.caption("Covariate scaling is a directional teaching default (Week 19), not a validated model.")

patient = dict(age=age, weight=weight, height=height, sex=sex,
               pregnant=pregnant, renal=renal)
```

The covariate checkboxes map straight onto your Week 19 scaling factors when you wire the engine.

---

## Step 3 — The drug + model registry (your 8, no peds)

Define the eight drugs and, for each, the model options. Drugs with a single model won't show a dropdown at all (Step 5).

```python
DRUGS = {
    "Propofol":        ["Eleveld", "Schnider", "Marsh"],   # Eleveld is the default
    "Remifentanil":    ["Minto", "Eleveld"],
    "Fentanyl":        ["Shafer"],
    "Dexmedetomidine": ["Hannivoort"],
    "Ketamine":        ["Illustrative"],
    "Methadone":       ["Illustrative"],
    "Sufentanil":      ["Gepts"],          # keep or drop to match your library
    "Alfentanil":      ["Maitre"],
}
# ^ Replace the last two with whatever your 8th/9th actually are; the point is the shape.
DRUG_NAMES = list(DRUGS.keys())
UNITS = {d: ("µg/mL" if d in ("Propofol", "Ketamine", "Methadone") else "ng/mL")
         for d in DRUG_NAMES}
```

> The default model is whichever is **first** in each list — so `Propofol → Eleveld`, matching the TCI default you chose.

---

## Step 4 — The editable event grid (bolus + infusion)

One grid drives everything. `num_rows="dynamic"` lets you add and delete rows; `column_config` turns columns into dropdowns and typed numbers.

```python
import pandas as pd

DEFAULT_EVENTS = pd.DataFrame([
    {"Time (min)": 0.0, "Drug": "Propofol", "Type": "bolus",
     "Dose": 150.0, "Unit": "mg", "End (min)": None},
    {"Time (min)": 0.0, "Drug": "Remifentanil", "Type": "infusion",
     "Dose": 0.25, "Unit": "µg/kg/min", "End (min)": 30.0},
])

with dose_col:
    st.subheader("Dosing")
    events = st.data_editor(
        DEFAULT_EVENTS,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Time (min)": st.column_config.NumberColumn(min_value=0.0, step=0.5, format="%.1f"),
            "Drug": st.column_config.SelectboxColumn(options=DRUG_NAMES, required=True),
            "Type": st.column_config.SelectboxColumn(options=["bolus", "infusion"], required=True),
            "Dose": st.column_config.NumberColumn(min_value=0.0, step=0.5, format="%.3f"),
            "Unit": st.column_config.SelectboxColumn(
                options=["mg", "µg", "mg/kg", "µg/kg/min", "mg/kg/h", "mL/h", "ng/kg/min"]),
            "End (min)": st.column_config.NumberColumn(
                min_value=0.0, step=0.5, format="%.1f",
                help="Infusion end time. Leave blank for a bolus."),
        },
        key="event_grid",
    )
    sim_length = st.number_input("Simulation length (min)", 5.0, 480.0, 60.0, 5.0)
```

Bolus rows ignore *End*; infusion rows use it. Unit conversion (mL/h, µg/kg/min → mg/min) is your Week 12 dosing engine's job — the grid just collects the human numbers.

---

## Step 5 — One model per drug, chosen once

The rule: the **first time a drug appears**, you pick its model; that choice governs every later event for that drug. Implement it by deriving the unique drugs from the grid and rendering one selectbox per drug that actually has a choice.

```python
with dose_col:
    used_drugs = [d for d in DRUG_NAMES if d in set(events["Drug"].dropna())]
    st.markdown("**Model per drug**")
    chosen_models = {}
    for d in used_drugs:
        opts = DRUGS[d]
        if len(opts) == 1:
            chosen_models[d] = opts[0]
            st.caption(f"{d}: {opts[0]} (only model)")
        else:
            chosen_models[d] = st.selectbox(f"{d} model", opts, key=f"model_{d}")
    # chosen_models is now locked for the whole run — one model per drug.
```

Because the selectbox is keyed by drug, its value persists across reruns and is applied uniformly. No per-event model column, exactly as you wanted.

---

## Step 6 — Run the simulation

First the **engine adapter** with a stub, so the app runs today. Put this in `engine.py`.

```python
# engine.py
import numpy as np

try:
    from tci import Patient, build_model, bis_from_ce, p_event, time_to_wake
    HAVE_LIBRARY = True
except Exception:
    HAVE_LIBRARY = False

def simulate(patient, events, chosen_models, t_end, dt=0.1):
    """Return {'t': array, 'drugs': {name: {'cp':.., 'ce':..}}}."""
    t = np.arange(0, t_end + dt, dt)

    if HAVE_LIBRARY:
        p = Patient(**patient)
        out = {"t": t, "drugs": {}}
        for drug, model_name in chosen_models.items():
            model = build_model(drug, model_name, p)
            rows = [e for e in events.to_dict("records") if e["Drug"] == drug]
            cp, ce = model.simulate(rows, t_end=t_end, dt=dt)   # your library
            out["drugs"][drug] = {"cp": cp, "ce": ce}
        return out

    # ---- STUB fallback: crude single-exponential so the UI is testable ----
    out = {"t": t, "drugs": {}}
    for drug in chosen_models:
        rows = [e for e in events.to_dict("records") if e["Drug"] == drug]
        cp = np.zeros_like(t)
        for e in rows:
            k = 0.1
            if e["Type"] == "bolus":
                cp += (e["Dose"] / 30.0) * np.exp(-k * np.clip(t - e["Time (min)"], 0, None)) \
                      * (t >= e["Time (min)"])
            else:
                end = e["End (min)"] or t_end
                rate = e["Dose"] / 20.0
                cp += rate * (1 - np.exp(-k * np.clip(t - e["Time (min)"], 0, None))) \
                      * ((t >= e["Time (min)"]) & (t <= end))
        ce = np.copy(cp)  # stub: no lag
        for i in range(1, len(t)):
            ce[i] = ce[i-1] + 0.26 * (cp[i] - ce[i-1]) * dt
        out["drugs"][drug] = {"cp": cp, "ce": ce}
    return out
```

Then, in `app.py`, run and cache:

```python
import engine

@st.cache_data
def run_sim(patient, events_records, chosen_models, sim_length):
    import pandas as pd
    ev = pd.DataFrame(events_records)
    return engine.simulate(patient, ev, chosen_models, sim_length)

result = run_sim(patient, events.to_dict("records"), chosen_models, sim_length)
```

Now the app produces curves — stubbed at first, real once `tci/` imports cleanly.

---

## Step 7 — Plots (selectable Cp / Ce / BIS; overlay; linear + log)

**On the two design questions you flagged:**

- **Overlay, not stacked.** Cp and Ce share units and belong on one axis so you can *see the lag between them* — that comparison is the whole point, and stacking hides it. BIS is a different scale (0–100), so it goes on a **secondary y-axis**. One chart, two axes.
- **Linear default, log toggle.** Clinical TCI displays are linear (you read absolute targets like 3.0 µg/mL). Semi-log is a PK-analysis convention that straightens exponential decay — useful sometimes, so it's a toggle, off by default.

```python
import matplotlib.pyplot as plt
from engine import HAVE_LIBRARY

with plot_col:
    st.subheader("Concentrations")
    traces = st.multiselect("Show", ["Cp", "Ce", "BIS"], default=["Cp", "Ce"])
    logy = st.toggle("Log scale (concentration)", value=False)

    fig, ax = plt.subplots(figsize=(7, 4))
    for drug, series in result["drugs"].items():
        if "Cp" in traces:
            ax.plot(result["t"], series["cp"], label=f"{drug} Cp")
        if "Ce" in traces:
            ax.plot(result["t"], series["ce"], "--", label=f"{drug} Ce")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Concentration")
    if logy:
        ax.set_yscale("log")

    if "BIS" in traces:
        ax2 = ax.twinx()
        # BIS from the propofol effect site (extend to a combined surface later)
        prop = result["drugs"].get("Propofol")
        if prop is not None:
            if HAVE_LIBRARY:
                from tci import bis_from_ce
                bis = bis_from_ce(prop["ce"])
            else:
                bis = 93 * (1 - prop["ce"]**2 / (3.0**2 + prop["ce"]**2))  # stub Hill
            ax2.plot(result["t"], bis, color="crimson", alpha=0.7, label="BIS")
            ax2.set_ylabel("BIS"); ax2.set_ylim(0, 100)

    ax.legend(loc="upper right", fontsize=8)
    st.pyplot(fig)
```

> Multi-drug note: if you overlay several drugs with different units (µg/mL vs ng/mL), label each trace and consider one axis per drug family, or focus the plot on the hypnotic. For a single hypnotic + one opioid this reads cleanly as written.

---

## Step 8 — Clinical readouts (user picks which)

Let the user check which readouts to show; compute only those. These map to Week 16 (wake-up) and Week 18 (endpoints).

```python
with plot_col:
    st.subheader("Clinical readouts")
    picks = st.multiselect(
        "Show readouts",
        ["Peak Ce", "Time to peak Ce", "Wake-up time",
         "P(unresponsive)", "P(no response to laryngoscopy)"],
        default=["Peak Ce", "Wake-up time"],
    )

    import numpy as np
    prop = result["drugs"].get("Propofol")
    remi = result["drugs"].get("Remifentanil")
    t = result["t"]
    cols = st.columns(2)

    def show(i, label, value):
        cols[i % 2].metric(label, value)

    i = 0
    if prop is not None and "Peak Ce" in picks:
        show(i, "Propofol peak Ce", f"{prop['ce'].max():.2f}"); i += 1
    if prop is not None and "Time to peak Ce" in picks:
        show(i, "Time to peak Ce", f"{t[int(np.argmax(prop['ce']))]:.1f} min"); i += 1
    if "Wake-up time" in picks:
        if HAVE_LIBRARY:
            from tci import time_to_wake
            wt = time_to_wake(result)   # adapt to your predictor's signature
            show(i, "Wake-up", f"{wt:.0f} min" if wt else "> window"); i += 1
        else:
            show(i, "Wake-up", "connect library"); i += 1
    if prop is not None and remi is not None and \
       ("P(unresponsive)" in picks or "P(no response to laryngoscopy)" in picks):
        if HAVE_LIBRARY:
            from tci import p_event
            ceP, ceR = prop["ce"], remi["ce"]
            if "P(unresponsive)" in picks:
                p = p_event(ceP, ceR, 2.8, 1e9, 0.0, 1.5).max()   # LoR params
                show(i, "P(unresponsive) peak", f"{p*100:.0f}%"); i += 1
            if "P(no response to laryngoscopy)" in picks:
                p = p_event(ceP, ceR, 3.0, 3.0, 3.0, 4.0).max()   # laryngoscopy params
                show(i, "P(no response, laryngoscopy) peak", f"{p*100:.0f}%"); i += 1
```

Swap the placeholder response-surface constants for the published values you settle on in Week 18.

---

## Step 9 (optional) — TCI target mode

Your Week 17 solver turns this from a forward simulator into a real TCI. Add a mode switch above the grid; when in target mode, the grid is replaced by a target entry and the solver produces the regimen.

```python
with dose_col:
    mode = st.radio("Mode", ["Manual dosing", "TCI target"], horizontal=True)

if mode == "TCI target":
    with dose_col:
        target_type = st.radio("Target", ["Effect-site (Ce)", "Plasma (Cp)"],
                               horizontal=True, index=0)   # effect-site default
        target = st.number_input("Target concentration", 0.5, 8.0, 3.0, 0.1)
        tci_drug = st.selectbox("Drug", ["Propofol"])       # start with propofol/Eleveld
    if HAVE_LIBRARY:
        from tci import build_model, Patient, tci_solve
        model = build_model(tci_drug, chosen_models.get(tci_drug, "Eleveld"),
                            Patient(**patient))
        regimen = tci_solve(model, target, effect_site=target_type.startswith("Effect"),
                            t_end=sim_length)   # returns the bolus+infusion schedule
        # feed `regimen` into engine.simulate the same way as manual events
```

Effect-site + Eleveld is the default, exactly as you chose; the plasma/Marsh/Schnider paths are one toggle away.

---

## Step 10 — Polish

- **Reset button:** `if st.button("Reset"): st.session_state.clear(); st.rerun()`
- **Persistent disclaimer:** keep the "not for clinical use" caption visible near the plot.
- **Layout:** patient in the sidebar, dosing left, plots + readouts right — already done.
- **Performance:** `@st.cache_data` on `run_sim` means it only recomputes when inputs change.

---

## Build order recap

1. Skeleton + layout → 2. Patient sidebar → 3. Drug registry → 4. Event grid →
5. One-model-per-drug → 6. Engine adapter (stub → real) → 7. Plots → 8. Readouts →
9. TCI mode (optional) → 10. Polish.

Build 1–8 against the stub first; the UI will be fully working with placeholder curves. Then finish `tci/` (Weeks 8–16) and the `try: from tci import ...` in `engine.py` flips it to real numbers with **no UI changes**. That clean seam is the payoff of keeping the interface a thin skin over a tested library.
