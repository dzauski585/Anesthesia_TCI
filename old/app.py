"""
app.py
------
Main Streamlit entry point. Four tabs:
    Tab 1 — Live:             real-time multi-drug anesthetic, pause/resume,
                              add boluses and rate changes during the run
    Tab 2 — Simulation:       multi-drug anesthetic specified upfront,
                              full run output with wake-up and predictors
    Tab 3 — Model Comparison: single drug, multiple PK models overlaid,
                              VitalsDB case overlay lives here
    Tab 4 — Closed Loop TCI:  automated controller, BIS + hemodynamic targets

Build order recommendation:
    Tab 2 → Tab 3 → Tab 1 → Tab 4
    (each depends on the previous being verified)

Adding a new drug or model:
    Edit config/drugs.py only — appears in all dropdowns automatically.

Changing colors or plot style:
    Edit config/theme.py only.

Changing unit options per drug:
    Edit config/drugs.py — rate_units and bolus_units lists per drug.
"""

import streamlit as st
from config.drugs import DRUGS
from config.theme import COLORS, PLOT

st.set_page_config(page_title="Anesthesia Simulator", layout="wide")
st.title("Anesthesia Simulator")

tab1, tab2, tab3, tab4 = st.tabs([
    "▶  Live",
    "📈  Simulation",
    "🔬  Model Comparison",
    "🔁  Closed Loop TCI",
])


# ============================================================================
# SHARED SIDEBAR — patient demographics only.
# Drug selection is now per-tab since Live/Simulation support multiple drugs
# while Model Comparison and Closed Loop work with a single drug at a time.
# ============================================================================

with st.sidebar:

    st.header("Patient")

    # TODO: Replace number_input with slider+number combos once UI style decided.
    #       Suggested ranges: age 1-100, weight 30-200 kg, height 100-220 cm.
    #       Combined pattern using columns:
    #           col_s, col_n = st.columns([3, 1])
    #           age = col_s.slider("Age", 1, 100, 40, label_visibility="collapsed")
    #           age = col_n.number_input("Age", value=age, label_visibility="visible")
    age    = st.number_input("Age",          value=40,  min_value=1,   max_value=100)
    weight = st.number_input("Weight (kg)",  value=70,  min_value=30,  max_value=250)
    height = st.number_input("Height (cm)",  value=170, min_value=100, max_value=220)

    # TODO: Style as horizontal radio buttons.
    #       sex = st.radio("Sex", ["M", "F"], horizontal=True)
    sex = st.selectbox("Sex", ["M", "F"])

    st.divider()
    st.header("Display")

    # TODO: Expand into full theme selector (light/dark/high contrast/print)
    #       driven entirely by config/theme.py. Theme choice stored in
    #       st.session_state so it persists across tab switches.
    show_bis = st.checkbox("Show BIS",  value=True)
    show_map = st.checkbox("Show MAP",  value=False)  # enable when map_pd.py ready
    show_hr  = st.checkbox("Show HR",   value=False)  # enable when hr_pd.py ready

    # TODO: Add Ce/Cp toggle here so it applies globally across all tabs.
    #       conc_mode = st.radio("Concentration", ["Ce — effect site", "Cp — plasma"],
    #                            horizontal=True)
    st.caption("Ce / Cp toggle — coming soon")

    st.divider()
    st.caption("v0.1 — simulation only, not for clinical use")


# ============================================================================
# SHARED HELPER — multi-drug active drug list
# Used by both Live and Simulation tabs.
# Stored in st.session_state so it persists across reruns.
#
# Structure of st.session_state.active_drugs:
#   [
#     {
#       'drug':        'propofol',
#       'model':       'Marsh',
#       'bolus_mg':    105.0,        # canonical mg
#       'rate_mg_min': 0.7,          # canonical mg/min
#       'stop_min':    None,         # None = run for full duration
#       'color':       '#4C72B0',    # auto-assigned from COLORS
#     },
#     { 'drug': 'remifentanil', ... },
#   ]
#
# TODO: Implement add/edit/remove actions on this list.
#       Each action calls st.rerun() so the drug table re-renders.
# ============================================================================

if 'active_drugs' not in st.session_state:
    st.session_state.active_drugs = []


def render_drug_table(tab_key: str):
    """
    Render the active drug list as a simple table with Edit and Remove buttons.
    tab_key is a unique string prefix to avoid widget ID collisions between tabs.

    TODO: Wire up Edit button to open an inline form (st.expander or st.popover)
          pre-filled with the drug's current settings.
    TODO: Wire up Remove button to delete the entry from st.session_state.active_drugs
          and call st.rerun().
    TODO: Auto-assign a distinct color from COLORS['drug_palette'] to each drug
          entry on add, so plot lines are always distinguishable.
    TODO: Show a warning row if the same drug is added twice (two pumps at
          different rates is unusual but valid — warn, don't block).
    """
    if not st.session_state.active_drugs:
        st.caption("No drugs added yet.")
        return

    for i, entry in enumerate(st.session_state.active_drugs):
        col_name, col_rate, col_edit, col_remove = st.columns([3, 3, 1, 1])
        col_name.markdown(f"**{entry['drug'].title()}** — {entry['model']}")
        col_rate.caption(f"{entry['rate_mg_min']:.3f} mg/min")
        # TODO: if col_edit.button("✏", key=f"{tab_key}_edit_{i}"): open edit form
        # TODO: if col_remove.button("✕", key=f"{tab_key}_remove_{i}"):
        #           st.session_state.active_drugs.pop(i); st.rerun()


def render_add_drug_form(tab_key: str):
    """
    Inline form for adding a drug to the active drug list.

    TODO: Replace st.expander with st.popover once Streamlit >= 1.31.
    TODO: Replace fixed unit strings with dynamic dropdowns from
          DRUGS[drug]['rate_units'] and DRUGS[drug]['bolus_units'].
    TODO: Call to_canonical_dose() and to_canonical_rate() from units.py
          so the engine always receives mg and mg/min regardless of display unit.
    TODO: Add quick-select bolus buttons for common doses, e.g.:
              cols = st.columns(3)
              if cols[0].button("1 mg/kg",   key=...): bolus_val = 1.0
              if cols[1].button("1.5 mg/kg", key=...): bolus_val = 1.5
              if cols[2].button("2 mg/kg",   key=...): bolus_val = 2.0
    TODO: Show inline clinical range warning beneath rate/bolus inputs
          using drugconfig.check_rate() / check_bolus() results.
    TODO: Add per-drug stop time input:
              stop_min = st.number_input("Stop at (min)", value=0,
                         help="0 = run for full simulation duration")
    """
    with st.expander("+ Add drug"):
        drug  = st.selectbox("Drug",  list(DRUGS.keys()),                    key=f"{tab_key}_drug")
        model = st.selectbox("Model", list(DRUGS[drug]['models'].keys()),    key=f"{tab_key}_model")

        # TODO: Replace with unit-aware inputs from DRUGS[drug]['bolus_units']
        #       and DRUGS[drug]['rate_units'] once units.py is wired in.
        bolus_val = st.number_input("Bolus dose (mg/kg)", value=0.0, min_value=0.0,
                                    step=0.1, key=f"{tab_key}_bolus")
        rate_val  = st.number_input("Infusion rate (mg/kg/hr)", value=10.0, min_value=0.0,
                                    step=0.5,  key=f"{tab_key}_rate")
        st.caption("Per-drug stop time — coming soon")

        if st.button("Add to anesthetic", key=f"{tab_key}_add"):
            st.session_state.active_drugs.append({
                'drug':        drug,
                'model':       model,
                # TODO: replace with to_canonical_dose() / to_canonical_rate()
                'bolus_mg':    bolus_val * weight,
                'rate_mg_min': rate_val  * weight / 60,
                'stop_min':    None,
                'color':       COLORS.get(drug, '#888888'),
            })
            st.rerun()


# ============================================================================
# TAB 2 — SIMULATION
# Multi-drug anesthetic specified upfront. Full run at once, no real-time.
# Build this first — easiest to verify engine output before adding complexity.
# ============================================================================

with tab2:
    st.subheader("Simulation")

    col_inputs, col_plot = st.columns([1, 2])

    with col_inputs:

        st.markdown("**Duration**")
        dur = st.number_input("Total duration (min)", value=60, min_value=1, max_value=600)

        st.markdown("**Drugs**")
        render_drug_table("sim")
        render_add_drug_form("sim")

        # TODO: Add "Clear all drugs" button.
        #       if st.button("Clear all", key="sim_clear"):
        #           st.session_state.active_drugs = []; st.rerun()

        st.divider()
        st.markdown("**Protocols**")

        # TODO: Auto-generate protocol checkboxes from a protocols registry
        #       rather than hardcoding each one here.
        #       Pattern:
        #           from config.protocols import PROTOCOLS
        #           selected_protocols = []
        #           for name, fn in PROTOCOLS.items():
        #               if st.checkbox(name, key=f"sim_proto_{name}"):
        #                   selected_protocols.append(fn)
        run_roberts = st.checkbox(
            "Overlay Roberts Scheme (1981)",
            help="Propofol only. 1 mg/kg bolus then 10/8/6 mg/kg/hr.",
            key="sim_roberts"
        )

        st.divider()
        run_button = st.button("Run Simulation", type="primary",
                               use_container_width=True, key="sim_run")

    with col_plot:
        if run_button:
            if not st.session_state.active_drugs:
                st.warning("Add at least one drug before running.")
            else:
                # TODO: Build patient and engine for each drug in active_drugs.
                #       Pattern:
                #           from core.engine import SimulationEngine
                #           from core.patient import Patient
                #           patient = Patient(int(age), weight, height, sex)
                #           engines = {}
                #           for entry in st.session_state.active_drugs:
                #               ModelClass = DRUGS[entry['drug']]['models'][entry['model']]
                #               pk  = ModelClass(patient)
                #               eng = SimulationEngine(pk, pd_models={...})
                #               stop = entry['stop_min'] or dur
                #               schedule = [(stop, entry['rate_mg_min']),
                #                           (dur - stop, 0.0)]  # coast after stop
                #               eng.run(entry['bolus_mg'], schedule)
                #               engines[entry['drug']] = eng
                st.info("Engine not yet connected — wire up core/engine.py here.")

                # TODO: Plot all drugs on shared time axis.
                #       Each drug: own concentration subplot or overlaid with
                #       distinct color from entry['color'].
                #       BIS driven by the hypnotic drug Ce only.
                #       Pattern:
                #           fig = build_multi_drug_figure(engines, show_bis,
                #                                         show_map, show_hr, PLOT)
                #           st.pyplot(fig)
                st.caption("Multi-drug concentration + BIS plot — coming soon")

                # TODO: If run_roberts and 'propofol' in engines:
                #           from core.protocols.roberts import roberts_schedule
                #           r_bolus, r_sched = roberts_schedule(weight)
                #           roberts_eng = SimulationEngine(MarshModel(patient), {})
                #           roberts_eng.run(r_bolus, r_sched)
                #           # overlay on same plot axes
                st.caption("Roberts protocol overlay — coming soon")

                # TODO: Predictor metric cards below the plot.
                #       wakeup = engines['propofol'].time_to_wakeup(threshold=1.0)
                #       st.metric("Est. wake-up after stop", f"{wakeup:.1f} min")
                #       p = engines['propofol'].p_no_laryngoscopy_response()
                #       st.metric("P(no laryngoscopy response)", f"{p*100:.0f}%")
                st.caption("Wake-up predictor — coming soon")
                st.caption("Laryngoscopy response predictor — coming soon")


# ============================================================================
# TAB 1 — LIVE
# Real-time multi-drug anesthetic. Time advances when unpaused.
# User adds boluses and rate changes at any point.
# Back-timing: enter a past time to reconstruct what was running.
# ============================================================================

with tab1:
    st.subheader("Live")

    col_controls, col_liveplot = st.columns([1, 2])

    with col_controls:

        # TODO: Pause/resume with st.session_state.
        #       if 'live_running' not in st.session_state:
        #           st.session_state.live_running = False
        #       label = "⏸ Pause" if st.session_state.live_running else "▶ Start"
        #       if st.button(label, use_container_width=True, key="live_toggle"):
        #           st.session_state.live_running = not st.session_state.live_running
        st.caption("Start / Pause — coming soon")

        st.markdown("**Active drugs**")

        # TODO: Live and Simulation tabs could share active_drugs or have
        #       separate lists. Recommend separate — use 'live_drugs' key for
        #       the live session so a simulation run doesn't alter live state.
        render_drug_table("live")
        render_add_drug_form("live")

        st.divider()
        st.markdown("**Give bolus now**")

        # TODO: Wire up to engine.bolus() at current live simulation time.
        #       bolus_drug = st.selectbox("Drug",
        #                       [e['drug'] for e in st.session_state.active_drugs],
        #                       key="live_bolus_drug")
        #       bolus_dose = st.number_input("Dose (mg/kg)", key="live_bolus_dose")
        #       bolus_unit = st.selectbox("Unit",
        #                       DRUGS[bolus_drug]['bolus_units'],
        #                       key="live_bolus_unit")
        #       if st.button("Give Bolus", key="live_give_bolus"):
        #           engines[bolus_drug].bolus(to_canonical_dose(bolus_dose,
        #                                     bolus_unit, weight))
        st.caption("Live bolus entry — coming soon")

        st.markdown("**Change rate**")

        # TODO: Wire up to engine from the next simulation tick onward.
        #       rate_drug = st.selectbox("Drug", ..., key="live_rate_drug")
        #       new_rate  = st.number_input("New rate", key="live_new_rate")
        #       rate_unit = st.selectbox("Unit",
        #                       DRUGS[rate_drug]['rate_units'], key="live_rate_unit")
        #       if st.button("Set Rate", key="live_set_rate"):
        #           st.session_state.current_rates[rate_drug] = \
        #               to_canonical_rate(new_rate, rate_unit, weight)
        st.caption("Live rate change — coming soon")

        st.divider()
        st.markdown("**Back-timing**")

        # TODO: Allow user to enter doses/rates at past times to reconstruct
        #       the pharmacokinetic state.
        #       Useful for working out what was running 30 min ago.
        #       Replay engine from t=0 with a user-supplied event log:
        #           events = [{'time': 5, 'drug': 'propofol', 'bolus_mg': 140},
        #                     {'time': 0, 'drug': 'propofol', 'rate_mg_min': 0.7}]
        #       back_time = st.number_input("Reconstruct from (min ago)", value=0,
        #                                   key="live_backtime")
        st.caption("Back-timing — coming soon")

    with col_liveplot:

        # TODO: Live updating plot using st.empty().
        #       plot_placeholder = st.empty()
        #       import time
        #       while st.session_state.get('live_running', False):
        #           for drug, eng in engines.items():
        #               rate = st.session_state.current_rates.get(drug, 0.0)
        #               eng.step(rate)
        #           fig = build_multi_drug_figure(engines, show_bis, show_map,
        #                                         show_hr, PLOT)
        #           plot_placeholder.pyplot(fig)
        #           time.sleep(0.1)   # 0.1 min per tick = 6 sec real time per sim-min
        #           st.rerun()        # required for Streamlit to refresh the plot
        st.caption("Live multi-drug plot — coming soon")

        # TODO: Live metric cards updated each tick.
        #       Use st.metric() with delta= to show trend direction (↑/↓).
        #       col_bis, col_map, col_hr = st.columns(3)
        #       col_bis.metric("BIS",        f"{current_bis:.0f}", f"{bis_delta:+.1f}")
        #       col_map.metric("MAP (mmHg)", f"{current_map:.0f}", f"{map_delta:+.1f}")
        #       col_hr.metric("HR (bpm)",    f"{current_hr:.0f}",  f"{hr_delta:+.1f}")
        st.caption("Live BIS / MAP / HR metrics — coming soon")


# ============================================================================
# TAB 3 — MODEL COMPARISON
# Single drug, multiple PK models overlaid on the same plot.
# VitalsDB case overlay lives here — inherently a comparison task.
# Teaching use: load a real case, enter what was given, see how well each
# model predicted the actual measured concentration.
# ============================================================================

with tab3:
    st.subheader("Model Comparison")

    col_cmp_inputs, col_cmp_plot = st.columns([1, 2])

    with col_cmp_inputs:

        st.markdown("**Drug**")

        # Single drug only — comparison is per-drug
        cmp_drug = st.selectbox("Drug", list(DRUGS.keys()), key="cmp_drug")

        st.markdown("**Select models**")

        # TODO: Auto-generate checkboxes from DRUGS[cmp_drug]['models'].
        #       All models checked by default.
        #       Pattern:
        #           selected_models = []
        #           for mname in DRUGS[cmp_drug]['models']:
        #               if st.checkbox(mname, value=True, key=f"cmp_mdl_{mname}"):
        #                   selected_models.append(mname)
        st.caption("Model checkboxes — auto-generated from config/drugs.py (coming soon)")

        st.divider()
        st.markdown("**Dosing**")

        # TODO: Replace with unit-aware inputs driven by DRUGS[cmp_drug].
        cmp_bolus = st.number_input("Bolus (mg/kg)", value=1.5, min_value=0.0,
                                    step=0.1, key="cmp_bolus")
        cmp_rate  = st.number_input("Infusion rate (mg/kg/hr)", value=10.0, min_value=0.0,
                                    step=0.5, key="cmp_rate")
        cmp_dur   = st.number_input("Duration (min)", value=60, min_value=1, key="cmp_dur")

        st.divider()
        st.markdown("**Protocols**")

        # TODO: Show Roberts checkbox only when cmp_drug == 'propofol'.
        #       if cmp_drug == 'propofol':
        #           cmp_roberts = st.checkbox("Overlay Roberts Scheme")
        st.caption("Roberts overlay (propofol only) — coming soon")

        st.divider()
        st.markdown("**VitalsDB**")

        # TODO: Load a real recorded case and overlay on the model predictions.
        #       use_vitalsdb = st.checkbox("Overlay VitalsDB case")
        #       if use_vitalsdb:
        #           from data.vitalsdb import load_case_list, load_case
        #           case_id  = st.selectbox("Case", load_case_list())
        #           case_data = load_case(case_id)
        #           # Plots actual recorded drug rates and measured concentrations
        #           # alongside model predictions for direct comparison.
        #           # Primary teaching use: did the model predict what actually happened?
        st.caption("VitalsDB case overlay — coming soon")

        cmp_run = st.button("Compare Models", type="primary",
                            use_container_width=True, key="cmp_run")

    with col_cmp_plot:
        if cmp_run:
            # TODO: Run each selected model with identical bolus + schedule.
            #       Pattern:
            #           from core.engine import SimulationEngine
            #           from core.patient import Patient
            #           patient  = Patient(int(age), weight, height, sex)
            #           results  = {}
            #           for mname in selected_models:
            #               ModelClass = DRUGS[cmp_drug]['models'][mname]
            #               pk  = ModelClass(patient)
            #               eng = SimulationEngine(pk, pd_models={})
            #               eng.run(cmp_bolus * weight,
            #                       [(cmp_dur, cmp_rate * weight / 60)])
            #               results[mname] = eng.results()
            st.info("Engine not yet connected — wire up core/engine.py here.")

            # TODO: Plot all model Ce/Cp curves on the same axis.
            #       Distinct color per model, legend, target concentration line.
            #       If VitalsDB loaded: overlay actual measured concentration as
            #       scatter points so model vs reality is immediately visible.
            #       Pattern:
            #           fig, ax = plt.subplots(figsize=PLOT['figsize'])
            #           for mname, res in results.items():
            #               ax.plot(res['times'], res['ce'], label=mname)
            #           if case_data:
            #               ax.scatter(case_data['times'], case_data['measured_conc'],
            #                          label='VitalsDB actual', marker='x', color='black')
            #           ax.legend(); st.pyplot(fig)
            st.caption("Model comparison plot — coming soon")

            # TODO: Summary table below the plot.
            #       Columns: Model | Mean Ce (steady state) | Time to Ce > 3 µg/mL |
            #                Time to Ce < 1 µg/mL (wake-up) | Peak Cp
            #       Use st.dataframe() with column formatting.
            st.caption("Summary comparison table — coming soon")


# ============================================================================
# TAB 4 — CLOSED LOOP TCI
# PID controller adjusts propofol rate automatically to hit BIS target.
# Optional: second controller for remifentanil → MAP target.
# Build last — depends on Tab 2 engine being fully verified.
# ============================================================================

with tab4:
    st.subheader("Closed Loop TCI")

    col_cl_inputs, col_cl_plot = st.columns([1, 2])

    with col_cl_inputs:

        st.markdown("**Drug & Model**")

        # Propofol only initially — add remifentanil second controller later
        cl_drug  = st.selectbox("Drug",  list(DRUGS.keys()),                     key="cl_drug")
        cl_model = st.selectbox("Model", list(DRUGS[cl_drug]['models'].keys()),  key="cl_model")

        # TODO: Add second drug row for remifentanil MAP control once
        #       propofol BIS loop is verified and stable.

        st.divider()
        st.markdown("**Targets**")

        # TODO: Replace number_input with sliders.
        #       bis_target = st.slider("BIS target", 20, 70, 45, key="cl_bis_target")
        #       map_target = st.slider("MAP target (mmHg)", 50, 110, 70, key="cl_map_target")
        st.caption("BIS target slider — coming soon")
        st.caption("MAP target slider — coming soon")

        st.divider()
        st.markdown("**Controller tuning**")

        # TODO: Start with P controller only, add I and D once basic loop works.
        #       kp = st.number_input("Kp (proportional)", value=1.0, key="cl_kp")
        #       ki = st.number_input("Ki (integral)",     value=0.1, key="cl_ki")
        #       kd = st.number_input("Kd (derivative)",   value=0.0, key="cl_kd")
        st.caption("PID gain inputs (Kp, Ki, Kd) — coming soon")

        # TODO: Safety rate limits — prevent clinically unsafe jumps.
        #       max_rate_mgkghr  = st.number_input("Max rate (mg/kg/hr)", value=20.0)
        #       max_delta_per_min = st.number_input("Max Δ rate/min", value=2.0)
        st.caption("Safety rate limits — coming soon")

        st.divider()
        cl_dur = st.number_input("Simulation duration (min)", value=60,
                                 min_value=1, key="cl_dur")

        cl_run = st.button("Start Closed Loop", type="primary",
                           use_container_width=True, key="cl_run")

    with col_cl_plot:
        if cl_run:
            # TODO: Wire up PID controller and engine.
            #       Pattern:
            #           from core.controllers.pid import PIDController
            #           from core.engine import SimulationEngine
            #           from core.patient import Patient
            #           patient = Patient(int(age), weight, height, sex)
            #           ModelClass = DRUGS[cl_drug]['models'][cl_model]
            #           pk  = ModelClass(patient)
            #           eng = SimulationEngine(pk, pd_models={'bis': BISModel()})
            #           ctrl = PIDController(target=bis_target, kp=kp, ki=ki, kd=kd,
            #                               max_rate=max_rate * weight / 60,
            #                               max_delta=max_delta * weight / 60)
            #           for _ in range(int(cl_dur / 0.1)):
            #               current_bis = eng.results()['bis'][-1] if eng.results()['bis'] else 100
            #               new_rate = ctrl.update(current_bis)
            #               eng.step(new_rate)
            st.info("Closed loop — wire up after Tab 2 engine is verified.")

            # TODO: Two-panel plot:
            #       Top: BIS over time with target line (red dashed)
            #       Bottom: infusion rate over time — shows controller behaviour.
            #       Use COLORS from config/theme.py.
            st.caption("BIS + infusion rate plot — coming soon")

            # TODO: Controller status metrics displayed as st.metric() cards.
            #       col_bis, col_rate, col_err = st.columns(3)
            #       col_bis.metric("Current BIS",   f"{current_bis:.0f}")
            #       col_rate.metric("Current rate",  f"{current_rate:.2f} mg/min")
            #       col_err.metric("BIS error",      f"{bis_error:+.1f}")
            #       Add a warning banner if integral windup detected (rate saturated).
            st.caption("Controller status metrics — coming soon")