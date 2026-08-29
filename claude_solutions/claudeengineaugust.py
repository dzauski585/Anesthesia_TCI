"""PK engine: Drug, from_clearances, deriv, Simulation.

Patients and drug models live in their own modules and import Drug from here.
This file imports neither, which is what makes drugs swappable.

Times are in minutes. steps_per_min sets the resolution, so an event at
minute 12 with 6 steps per minute is step 72 exactly.

Dose each drug in its natural unit and the concentration comes out right:
mg / litres = ug/mL for propofol, ug / litres = ng/mL for opioids and dex.
"""

import numpy as np
from scipy.integrate import solve_ivp


class Drug:
    """Seven numbers. V1 in litres, every k per minute.
    The unit strings are labels for your axes; the maths never reads them."""

    def __init__(self, name, V1, k10, k12, k13, k21, k31, ke0,
                 dose_unit="mg", conc_unit="ug/mL"):
        self.name = name
        self.V1 = V1
        self.k10 = k10
        self.k12 = k12
        self.k13 = k13
        self.k21 = k21
        self.k31 = k31
        self.ke0 = ke0
        self.dose_unit = dose_unit
        self.conc_unit = conc_unit


def from_clearances(name, V1, V2, V3, Cl1, Cl2, Cl3, ke0,
                    dose_unit="mg", conc_unit="ug/mL"):
    """For models published as volumes + clearances (Schnider, Minto, Eleveld).
    A clearance (L/min) over the volume it drains (L) is a rate constant.
    Models published as rate constants (Marsh) call Drug() directly."""
    return Drug(name, V1,
                k10=Cl1 / V1, k12=Cl2 / V1, k13=Cl3 / V1,
                k21=Cl2 / V2, k31=Cl3 / V3, ke0=ke0,
                dose_unit=dose_unit, conc_unit=conc_unit)


def deriv(t, y, drug, rate):
    """How fast A1, A2, A3, Ce are changing right now.

    A1-A3 are amounts of drug. Ce is a concentration: the effect site is too
    small to hold real mass, so it lags plasma without drawing from it.
    """
    A1, A2, A3, Ce = y
    Cp = A1 / drug.V1

    dA1 = rate + drug.k21 * A2 + drug.k31 * A3 - (drug.k10 + drug.k12 + drug.k13) * A1
    dA2 = drug.k12 * A1 - drug.k21 * A2
    dA3 = drug.k13 * A1 - drug.k31 * A3
    dCe = drug.ke0 * (Cp - Ce)
    return dA1, dA2, dA3, dCe


class Simulation:
    """One drug, one schedule, one result.

        sim = Simulation(drug, t_end=60)
        sim.bolus(0, 160)      # 160 mg at minute 0
        sim.rate(0, 13)        # 13 mg/min from minute 0
        sim.rate(12, 8)        # 8 mg/min from minute 12
        sim.run()
        plt.plot(sim.t, sim.ce)

    Edit the schedule and call run() again. It rebuilds from minute 0 every
    time, so there is nothing to reset.
    """

    def __init__(self, drug, t_end=60.0, steps_per_min=6):
        self.drug = drug
        self.t_end = t_end
        self.steps_per_min = steps_per_min
        self.schedule = []
        self.t = None
        self.cp = None
        self.ce = None

    def bolus(self, at, dose):
        self.schedule.append((at, "bolus", dose))

    def rate(self, at, dose_per_min):
        self.schedule.append((at, "rate", dose_per_min))

    def clear(self):
        self.schedule = []

    def run(self):
        n = int(self.t_end * self.steps_per_min) + 1
        t = np.arange(n) / self.steps_per_min
        cp = np.zeros(n)
        ce = np.zeros(n)
        events = sorted(self.schedule)

        y = [0.0, 0.0, 0.0, 0.0]     # A1, A2, A3, Ce
        rate = 0.0                   # dose per minute

        for i in range(n):
            for at, kind, dose in events:
                if i == at * self.steps_per_min:
                    if kind == "bolus":
                        y[0] = y[0] + dose
                    else:
                        rate = dose

            cp[i] = y[0] / self.drug.V1
            ce[i] = y[3]

            if i < n - 1:
                sol = solve_ivp(deriv, (t[i], t[i + 1]), y,
                                args=(self.drug, rate),
                                rtol=1e-8, atol=1e-10)
                y = list(sol.y[:, -1])

        self.t = t
        self.cp = cp
        self.ce = ce

    def ce_at(self, minute):
        return self.ce[minute * self.steps_per_min]


if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    marsh = Drug("Propofol (Marsh)", V1=0.228 * 80,
                 k10=0.119, k12=0.112, k13=0.0419,
                 k21=0.055, k31=0.0033, ke0=0.26)

    sim = Simulation(marsh, t_end=60.0)
    sim.bolus(0, 160)
    sim.rate(0, 13)
    sim.rate(12, 8)
    sim.bolus(30, 40)
    sim.rate(45, 0)
    sim.run()

    plt.figure(figsize=(8, 4))
    plt.plot(sim.t, sim.cp, lw=1, alpha=0.5, label="Cp")
    plt.plot(sim.t, sim.ce, lw=2, label="Ce")
    plt.xlabel("time (min)")
    plt.ylabel(f"{sim.drug.name}  ({sim.drug.conc_unit})")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig("run.png", dpi=120)

    for minute in [1, 12, 30, 45, 60]:
        print(f"{minute:3d} min   Ce {sim.ce_at(minute):5.2f}")
