"""
solver.py  --  inverse TCI: target -> infusion scheme  (Week 17)

Every other file runs FORWARD (a regimen -> concentration curves). A real TCI
pump runs the inverse: you name a target concentration and it computes, and
continuously recomputes, the infusion that reaches and holds it. This file is
the Week 17 solution, built on the same pkpd_deriv engine as models.py.

Two modes (the user toggles; effect-site is the clinical default):

  Plasma targeting (BET) -- hold Cp = target. Bolus fills the central
  compartment (Ct*V1); the maintenance infusion replaces what leaves it. Early
  on the peripheries are empty and pull hard, so the rate starts high and decays
  to the steady-state rate Ct*CL.

  Effect-site targeting (Shafer-Gregg) -- drive Ce to target as fast as
  possible by deliberately overshooting plasma: a bolus sized so Ce peaks
  exactly at target, then hold Cp = target Ce (which pins dCe/dt = 0).

The output is a regimen -- boluses + infusion segments -- in the SAME shape the
SimulationEngine consumes, so a solved target can be fed straight back through
the forward engine or the app.

TEACHING SKELETON. A production TCI also caps pump rate, forbids negative
infusion (pause, never remove), and recomputes on a fixed clock. Validate any
solver against stanpumpR or a published BET table before trusting a number.
"""

import numpy as np
from scipy.integrate import solve_ivp

from models import pkpd_deriv
from dosing import make_infusion_func


def _step(state, model, rate, dt):
    """Advance [A1,A2,A3,Ce] by one cycle of length dt at a constant rate."""
    params = (lambda t: rate, model.V1, model.k10, model.k12, model.k13,
              model.k21, model.k31, model.ke0)
    sol = solve_ivp(pkpd_deriv, (0.0, dt), state, args=params,
                    method="LSODA", max_step=dt, rtol=1e-6, atol=1e-9)
    return sol.y[:, -1]


def infusion_to_hold_cp(state, target, model, dt):
    """Rate (mass/min) that lands Cp exactly on target after the next cycle.

    Predict A1 with the pump OFF, then top up the difference. A pump cannot go
    negative, so the rate is floored at zero (it pauses instead)."""
    free = _step(state, model, 0.0, dt)      # predict A1 with no infusion
    needed_A1 = target * model.V1
    return max(0.0, (needed_A1 - free[0]) / dt)


def induction_bolus_for_ce(model, target_ce, t_end=10.0, dt=1 / 60):
    """Bolus that makes Ce peak at target_ce. Simulate a 1-mass-unit bolus,
    find the effect-site peak it produces, then scale linearly."""
    state = np.array([1.0, 0.0, 0.0, 0.0])
    peak, t = 0.0, 0.0
    while t < t_end:
        state = _step(state, model, 0.0, dt)
        peak = max(peak, state[3])
        t += dt
    return target_ce / peak


def tci_solve(model, target, effect_site=True, t_end=60.0, dt=1 / 6):
    """Solve a constant-target TCI. Returns a dict with the regimen (boluses +
    infusion segments, ready for the engine) and the achieved t/cp/ce arrays."""
    state = np.zeros(4)
    bolus = (induction_bolus_for_ce(model, target) if effect_site
             else target * model.V1)
    state[0] += bolus
    boluses = [(0.0, float(bolus))]

    segs = []
    T, CP, CE = [0.0], [state[0] / model.V1], [state[3]]
    holding = not effect_site      # plasma holds immediately; effect-site waits
    t = 0.0
    while t < t_end - 1e-9:
        rate = infusion_to_hold_cp(state, target, model, dt) if holding else 0.0
        segs.append((t, t + dt, rate))
        state = _step(state, model, rate, dt)
        t += dt
        if effect_site and not holding and state[3] >= target * 0.995:
            holding = True         # Ce has arrived; switch to plasma-hold
        T.append(t); CP.append(state[0] / model.V1); CE.append(state[3])

    return dict(boluses=boluses, segments=segs,
                infusion=make_infusion_func(segs),
                t=np.array(T), cp=np.array(CP), ce=np.array(CE))


if __name__ == "__main__":
    from patient import Patient
    from models import EleveldModel

    m = EleveldModel(Patient(35, 70, 170, "male"))
    CL = m.k10 * m.V1

    # --- Plasma BET, target 3.0 ug/mL (Week 17 by-hand anchors) ---
    plas = tci_solve(m, 3.0, effect_site=False, t_end=60)
    bolus = plas["boluses"][0][1]
    early = plas["segments"][0][2]
    late = plas["segments"][-1][2]
    print("PLASMA target 3.0:")
    print("  bolus       = %.1f mg  (Ct*V1 = %.1f)" % (bolus, 3.0 * m.V1))
    print("  early rate  = %.1f mg/min" % early)
    print("  late rate   = %.2f mg/min  (Ct*CL = %.2f, still decaying toward it)" % (late, 3.0 * CL))
    print("  Cp late     = %.2f ug/mL" % plas["cp"][-1])
    assert abs(bolus - 3.0 * m.V1) < 1e-6                 # bolus = Ct*V1 exactly
    assert early > 2.0 * (3.0 * CL)                       # front-loads ~2.4x steady state
    assert late < early                                   # rate decays as peripheries fill
    assert late > 3.0 * CL                                # still above Ct*CL at 60 min (V3 slow)
    assert abs(plas["cp"][-1] - 3.0) < 0.15               # holds the plasma target

    # --- Effect-site Shafer-Gregg, target 3.0 ug/mL ---
    eff = tci_solve(m, 3.0, effect_site=True, t_end=60)
    print("EFFECT-SITE target 3.0:")
    print("  bolus       = %.1f mg  (> plasma bolus: deliberate overshoot)" % eff["boluses"][0][1])
    print("  peak Ce     = %.2f ug/mL" % eff["ce"].max())
    print("  Ce late     = %.2f ug/mL" % eff["ce"][-1])
    assert eff["boluses"][0][1] > bolus                   # bigger bolus than plasma mode
    assert abs(eff["ce"].max() - 3.0) < 0.3              # Ce peaks near target
    assert abs(eff["ce"][-1] - 3.0) < 0.2               # and is held there
    print("solver.py self-tests passed.")
