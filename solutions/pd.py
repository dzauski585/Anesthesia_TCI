"""
pd.py  --  pharmacodynamics: the BIS model, plus the wake-up predictor.

BISModel is written to the engine's PD interface: it receives a dict of
effect-site concentrations by drug (ce_by_drug) and returns a BIS number.
Propofol is the hypnotic driver; if remifentanil is present the two are
combined on a synergistic response surface (interactions.py). Other drugs are
deliberately NOT folded into BIS by default (ketamine can paradoxically raise
BIS; dexmedetomidine's BIS effect is secondary) -- a safe, honest default.

The wake-up predictor and decrement curve integrate the model FORWARD from the
current state with NO infusion, reusing pkpd_deriv from models.py.
"""

import numpy as np
from scipy.integrate import solve_ivp

from models import pkpd_deriv
from interactions import response_surface, lookup_interaction


# ----------------------------------------------------------------------
# Plain Hill helpers (single drug)
# ----------------------------------------------------------------------
def hill_effect(Ce, E0, Emax, Ce50, gamma):
    frac = Ce ** gamma / (Ce50 ** gamma + Ce ** gamma)
    return E0 + (Emax - E0) * frac


def bis_from_ce(Ce, E0=93.0, Emin=0.0, Ce50=3.0, gamma=1.6):
    """Propofol effect-site concentration -> BIS-like number (awake ~93)."""
    Ce = np.asarray(Ce, dtype=float)
    frac = Ce ** gamma / (Ce50 ** gamma + Ce ** gamma)
    return E0 - (E0 - Emin) * frac


# ----------------------------------------------------------------------
# The BIS model (engine PD interface)
# ----------------------------------------------------------------------
class BISModel:
    """Effect-site concentrations -> BIS. Stateless (BIS has no memory)."""

    def __init__(self, e0=93.0, emin=0.0, ce50_prop=3.0, gamma=1.6,
                 ce50_remi_hypnotic=20.0):
        self.e0 = e0
        self.emin = emin
        self.ce50_prop = ce50_prop          # ug/mL
        self.gamma = gamma
        self.ce50_remi = ce50_remi_hypnotic  # ng/mL (remi alone weakly hypnotic)

    def _effect(self, ce_prop, ce_remi):
        """Combined hypnotic effect 0..1. With ce_remi=0 this reduces to the
        propofol Hill curve; remifentanil adds synergy (dose-sparing)."""
        alpha = lookup_interaction("propofol", "remifentanil")["alpha"]
        return response_surface(ce_prop, self.ce50_prop,
                                ce_remi, self.ce50_remi,
                                alpha=alpha, gamma=self.gamma)

    def calculate(self, ce_by_drug: dict) -> float:
        """BIS at one instant from a dict like {'propofol': 2.1, ...}."""
        cp = ce_by_drug.get("propofol", 0.0)
        cr = ce_by_drug.get("remifentanil", 0.0)
        eff = self._effect(cp, cr)
        return float(self.e0 - (self.e0 - self.emin) * eff)

    def calculate_series(self, ce_by_drug: dict) -> np.ndarray:
        """BIS over a whole run; ce_by_drug holds arrays per drug."""
        n = len(next(iter(ce_by_drug.values())))
        cp = np.asarray(ce_by_drug.get("propofol", np.zeros(n)), dtype=float)
        cr = np.asarray(ce_by_drug.get("remifentanil", np.zeros(n)), dtype=float)
        eff = self._effect(cp, cr)
        return self.e0 - (self.e0 - self.emin) * eff


# ----------------------------------------------------------------------
# Wake-up predictor and context-sensitive decrement (solve_ivp)
# ----------------------------------------------------------------------
def _zero(t):
    return 0.0


def time_to_wake(model, x0, ce0, wake_ce=1.2, max_min=240, max_step=0.5):
    """Minutes until effect-site concentration falls below wake_ce after all
    infusions stop now. None if it would not within max_min. Uses a solve_ivp
    terminal event at the Ce = wake_ce crossing."""
    if ce0 < wake_ce:
        return 0.0
    y0 = [x0[0], x0[1], x0[2], ce0]
    params = (_zero, model.V1, model.k10, model.k12, model.k13,
              model.k21, model.k31, model.ke0)

    def wake_event(t, y, *args):
        return y[3] - wake_ce
    wake_event.terminal = True
    wake_event.direction = -1

    sol = solve_ivp(pkpd_deriv, (0.0, max_min), y0, args=params,
                    method="LSODA", max_step=max_step, events=wake_event,
                    rtol=1e-6, atol=1e-9)
    if sol.t_events[0].size > 0:
        return float(sol.t_events[0][0])
    return None


def decrement_curve(model, x0, ce0, fractions=(0.1, 0.2, 0.3, 0.4, 0.5,
                                               0.6, 0.7, 0.8, 0.9),
                    max_min=600, dt=0.1, max_step=0.5):
    """Context-sensitive decrement times from the current state: minutes for Ce
    to fall each fraction below ce0 (0.5 = context-sensitive half-time)."""
    y0 = [x0[0], x0[1], x0[2], ce0]
    params = (_zero, model.V1, model.k10, model.k12, model.k13,
              model.k21, model.k31, model.ke0)
    grid = np.arange(0.0, max_min + dt / 2, dt)
    sol = solve_ivp(pkpd_deriv, (0.0, max_min), y0, args=params,
                    method="LSODA", max_step=max_step, t_eval=grid,
                    rtol=1e-6, atol=1e-9)
    ce = sol.y[3]
    out = {}
    for f in fractions:
        below = np.where(ce <= ce0 * (1 - f))[0]
        out[f] = float(grid[below[0]]) if below.size > 0 else None
    return out


if __name__ == "__main__":
    assert abs(bis_from_ce(3.0) - 46.5) < 0.5      # ~BIS 46-47 at Ce50
    bis = BISModel()
    # propofol alone: matches the Hill curve
    assert abs(bis.calculate({"propofol": 3.0}) - bis_from_ce(3.0)) < 1e-6
    # adding remifentanil deepens hypnosis (BIS falls) at the same propofol Ce
    deeper = bis.calculate({"propofol": 3.0, "remifentanil": 6.0})
    assert deeper < bis.calculate({"propofol": 3.0})
    print("BIS prop-only @3.0 = %.1f ; prop+remi = %.1f" %
          (bis.calculate({"propofol": 3.0}), deeper))

    from patient import Patient
    from models import MarshModel
    from dosing import make_infusion_func
    m = MarshModel(Patient(40, 70, 175, "male"))
    short = m.simulate(make_infusion_func([(0, 5, 11.7)]), t_end=5, dt=1 / 6)
    long = m.simulate(make_infusion_func([(0, 120, 11.7)]), t_end=120, dt=1 / 6)
    tw_s = time_to_wake(m, short["X"][-1], short["ce"][-1], wake_ce=1.0)
    tw_l = time_to_wake(m, long["X"][-1], long["ce"][-1], wake_ce=1.0)
    print("Wake after 5 min: %.1f min ; after 120 min: %.1f min" % (tw_s, tw_l))
    print("pd.py self-tests passed.")
