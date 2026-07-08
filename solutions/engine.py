"""
engine.py  --  the SimulationEngine (#2).

Holds a DICT of PK models (one per active drug) and a DICT of PD models
(BIS, ...). It runs each drug's pharmacokinetics independently -- drugs do not
change each other's PK; they only combine in their EFFECT -- and then hands the
whole set of effect-site concentrations to each PD model at once. That shared
`ce_by_drug` bundle is what makes interactions (ketofol, propofol+remi) and
multi-output PD possible without changing the engine.

Because drug PK is independent and solve_ivp is a batch integrator, the engine
runs each drug in one batch call and combines at the PD layer (rather than
stepping tick-by-tick). A tick-by-tick variant would be added only for a live
closed loop (Week 20).

Canonical units (set in the models/dosing layer): rate per minute, time min.
"""

from __future__ import annotations

from pd import decrement_curve


class SimulationEngine:
    def __init__(self, pk_models: dict, pd_models: dict | None = None,
                 dt: float = 1 / 6):
        """
        pk_models : {'propofol': MarshModel(patient), 'remifentanil': MintoModel(patient)}
        pd_models : {'bis': BISModel()}   (any subset, or {} for a comparison run)
        dt        : output grid spacing in minutes
        """
        self.pk_models = pk_models
        self.pd_models = pd_models or {}
        self.dt = dt
        self._reset()

    def _reset(self):
        self.t = None
        self.cp: dict = {}      # plasma concentration arrays, per drug
        self.ce: dict = {}      # effect-site arrays, per drug
        self.X: dict = {}       # amount-history arrays, per drug (for wake-up)
        self.pd_out: dict = {}  # PD output arrays, per PD model name

    def run(self, plan: dict, duration: float, max_step: float = 0.5) -> dict:
        """Run a protocol.

        plan = {'propofol':     {'boluses': [(0.0, 140.0)], 'infusion': func},
                'remifentanil':  {'infusion': func}}
        A drug missing from `plan` simply gets no drug. `infusion` is a
        function t->rate/min (build it with dosing.make_infusion_func);
        `boluses` is a list of (time_min, dose).
        """
        self._reset()
        for name, pk in self.pk_models.items():
            p = plan.get(name, {})
            sim = pk.simulate(infusion_func=p.get("infusion"),
                              boluses=p.get("boluses"),
                              t_end=duration, dt=self.dt, max_step=max_step)
            self.t = sim["t"]
            self.cp[name] = sim["cp"]
            self.ce[name] = sim["ce"]
            self.X[name] = sim["X"]
        # every PD model receives the SAME ce_by_drug dict
        for pdname, pdmodel in self.pd_models.items():
            self.pd_out[pdname] = pdmodel.calculate_series(self.ce)
        return self.results()

    def results(self) -> dict:
        return dict(t=self.t, cp=self.cp, ce=self.ce, pd=self.pd_out)

    @property
    def current_ce(self) -> dict:
        """Most recent effect-site concentration per drug (0.0 before a run)."""
        return {name: (arr[-1] if len(arr) else 0.0)
                for name, arr in self.ce.items()}

    def compute_csht(self, drug_name: str, durations_min: list,
                     infusion_func, threshold_fraction: float = 0.5) -> list:
        """Context-sensitive half-time curve for one drug: for each infusion
        duration, infuse then stop and time the fall to threshold_fraction of
        the stop concentration. Uses simulate() (no mutation of live state)."""
        pk = self.pk_models[drug_name]
        out = []
        for D in durations_min:
            sim = pk.simulate(infusion_func=infusion_func, t_end=D, dt=self.dt)
            ce0 = sim["ce"][-1]
            if ce0 < 1e-6:
                out.append(None)
                continue
            dec = decrement_curve(pk, sim["X"][-1], ce0,
                                  fractions=(threshold_fraction,),
                                  max_min=600, dt=self.dt)
            out.append(dec[threshold_fraction])
        return out


if __name__ == "__main__":
    from patient import Patient
    from models import MarshModel, MintoModel
    from pd import BISModel
    from dosing import make_infusion_func

    p = Patient(40, 70, 175, "male")
    eng = SimulationEngine(
        pk_models={"propofol": MarshModel(p), "remifentanil": MintoModel(p)},
        pd_models={"bis": BISModel()}, dt=1 / 6)

    plan = {
        "propofol": {"boluses": [(0.0, 100.0)],
                     "infusion": make_infusion_func([(0, 60, 11.7)])},
        # 0.15 mcg/kg/min x 70 kg = 10.5 mcg/min (remi model works in mcg)
        "remifentanil": {"infusion": make_infusion_func([(0, 60, 0.15 * 70)])},
    }
    res = eng.run(plan, duration=60)
    print("time points:", len(res["t"]))
    print("final propofol Ce = %.2f ug/mL" % res["ce"]["propofol"][-1])
    print("final remifentanil Ce = %.2f ng/mL" % res["ce"]["remifentanil"][-1])
    print("final BIS = %.0f" % res["pd"]["bis"][-1])
    assert res["ce"]["remifentanil"][-1] > 1.0   # remi is actually present now
    assert res["pd"]["bis"][-1] < 60             # surgical depth with prop+remi

    # CSHT grows with infusion duration
    inf = make_infusion_func([(0, 600, 11.7)])
    csht = eng.compute_csht("propofol", [10, 60, 120], inf)
    print("propofol CSHT (10/60/120 min):", [round(c, 1) for c in csht])
    assert csht[0] < csht[1] < csht[2]
    print("engine.py self-tests passed.")
