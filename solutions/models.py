"""
models.py  --  PK model engine + drug models  (TEACHING / RESEARCH ONLY)

Engine: one derivative function (`pkpd_deriv`) integrated by SciPy's solve_ivp.
The derivative reads like the PK equations; solve_ivp does the stepping. A
2-compartment drug is just k13 = k31 = 0 (its third compartment stays empty).
Boluses are instantaneous jumps, so the engine integrates piecewise between
bolus times and adds each bolus to the state at its event time.

Base class has TWO initialisers so each model is entered in the format its
paper uses (this kills a whole class of unit-conversion bugs):
    _init_from_clearances(...)      -> Schnider, Eleveld, Minto, Fentanyl, dex
    _init_from_rate_constants(...)  -> Marsh

Every model takes a Patient object (patient.py) for body size.

NOTE ON ELEVELD: covariate SLOPES are an approximate reconstruction; the
reference-individual anchors (verified) are checked by the self-test. Verify
slopes vs Eleveld 2018 (BJA 120:942-959 Table 2) before trusting Eleveld away
from a ~70 kg adult. Ketamine/methadone are ILLUSTRATIVE only, not for dosing.
"""

import math
import numpy as np
from scipy.integrate import solve_ivp

from patient import al_sallami_ffm        # for the Eleveld reference individual


# ----------------------------------------------------------------------
# Eleveld helper functions
# ----------------------------------------------------------------------
def f_aging(x, age):
    return math.exp(x * (age - 35.0))


def f_sigmoid(x, e50, lam):
    return x ** lam / (x ** lam + e50 ** lam)


# ----------------------------------------------------------------------
# The model's differential equations -- THIS is the model, in code.
# ----------------------------------------------------------------------
def pkpd_deriv(t, y, infusion_func, V1, k10, k12, k13, k21, k31, ke0):
    """Rates of change of [A1, A2, A3, Ce]. A* are amounts; Ce is the
    effect-site concentration. Each line matches a compartment equation."""
    A1, A2, A3, Ce = y
    Cp = A1 / V1
    rate = infusion_func(t)
    dA1 = rate - (k10 + k12 + k13) * A1 + k21 * A2 + k31 * A3
    dA2 = k12 * A1 - k21 * A2
    dA3 = k13 * A1 - k31 * A3
    dCe = ke0 * (Cp - Ce)
    return [dA1, dA2, dA3, dCe]


# ----------------------------------------------------------------------
# The engine
# ----------------------------------------------------------------------
class ThreeCompartmentModel:
    """Mammillary 1/2/3-compartment model + effect site, solved by solve_ivp."""

    MODEL_NAME = "base"
    DRUG_NAME = "generic"

    # --- two ways to set up; a subclass __init__ calls exactly ONE of them ---
    def _init_from_rate_constants(self, V1, k10, k12, k13, k21, k31, ke0,
                                  units="mg", conc_unit="ug/mL"):
        """For models published as rate constants (Marsh)."""
        self.V1 = V1
        self.k10, self.k12, self.k13 = k10, k12, k13
        self.k21, self.k31 = k21, k31
        self.ke0 = ke0
        self.units, self.conc_unit = units, conc_unit

    def _init_from_clearances(self, V1, V2, V3, Cl1, Cl2, Cl3, ke0,
                              units="mg", conc_unit="ug/mL"):
        """For models published as volumes + clearances (Schnider, Eleveld,
        Minto, Fentanyl, dex). A clearance (L/min) over the volume it leaves (L)
        is a first-order rate constant (per min); convert, then hand off."""
        self._init_from_rate_constants(
            V1=V1,
            k10=Cl1 / V1,            # elimination out of the body
            k12=Cl2 / V1,            # central -> fast peripheral
            k13=Cl3 / V1,            # central -> slow peripheral
            k21=Cl2 / V2,            # fast peripheral -> central
            k31=Cl3 / V3,            # slow peripheral -> central
            ke0=ke0, units=units, conc_unit=conc_unit,
        )

    def _params(self, infusion_func):
        return (infusion_func, self.V1, self.k10, self.k12, self.k13,
                self.k21, self.k31, self.ke0)

    def simulate(self, infusion_func=None, boluses=None,
                 t_end=60.0, dt=1 / 6, max_step=0.5):
        """Run a simulation. infusion_func(t)->rate per min; boluses=[(t,dose)].
        dt = output grid spacing; max_step <= spacing of any infusion change.
        Returns dict(t, cp, ce, X) with X = amounts history (n x 3)."""
        if infusion_func is None:
            infusion_func = lambda t: 0.0
        boluses = sorted(boluses or [])
        grid = np.arange(0.0, t_end + dt / 2, dt)

        bolus_times = sorted({bt for (bt, _d) in boluses if 0.0 < bt < t_end})
        bounds = [0.0] + bolus_times + [t_end]

        params = self._params(infusion_func)
        y = np.zeros(4)
        T_chunks, Y_chunks = [], []
        for i in range(len(bounds) - 1):
            ta, tb = bounds[i], bounds[i + 1]
            for (bt, dose) in boluses:
                if abs(bt - ta) < 1e-9:
                    y = y + np.array([dose, 0.0, 0.0, 0.0])
            sol = solve_ivp(pkpd_deriv, (ta, tb), y, args=params,
                            method="LSODA", max_step=max_step,
                            dense_output=True, rtol=1e-6, atol=1e-9)
            y = sol.y[:, -1]
            last = (i == len(bounds) - 2)
            if last:
                seg = grid[(grid >= ta - 1e-9) & (grid <= tb + 1e-9)]
            else:
                seg = grid[(grid >= ta - 1e-9) & (grid < tb - 1e-9)]
            if len(seg) > 0:
                T_chunks.append(seg)
                Y_chunks.append(sol.sol(seg))
        T = np.concatenate(T_chunks)
        Y = np.concatenate(Y_chunks, axis=1)
        return dict(t=T, cp=Y[0] / self.V1, ce=Y[3], X=Y[:3].T)


# ======================================================================
# Propofol
# ======================================================================
class MarshModel(ThreeCompartmentModel):
    """Marsh 1991 (weight only). Published as RATE CONSTANTS.
    ke0=0.26 /min is the effect-site value this course uses throughout (the
    original Diprifusor did PLASMA targeting with no effect site; some pumps use
    a 'modified Marsh' ke0=1.2 /min instead). Keep 0.26 so the hand-worked
    time-to-peak-effect exercises in Weeks 5-6 stay consistent."""
    MODEL_NAME, DRUG_NAME = "Marsh", "Propofol"

    def __init__(self, patient, ke0=0.26):
        w = patient.weight
        self._init_from_rate_constants(
            V1=0.228 * w, k10=0.119, k12=0.112, k13=0.0419,
            k21=0.055, k31=0.0033, ke0=ke0, units="mg", conc_unit="ug/mL")


class SchniderModel(ThreeCompartmentModel):
    """Schnider 1998/1999. Published as VOLUMES + CLEARANCES; uses James LBM."""
    MODEL_NAME, DRUG_NAME = "Schnider", "Propofol"

    def __init__(self, patient):
        age, w, h, lbm = patient.age, patient.weight, patient.height, patient.lbm
        V1 = 4.27
        V2 = max(1.0, 18.9 - 0.391 * (age - 53))
        V3 = 238.0
        Cl1 = 1.89 + 0.0456 * (w - 77) - 0.0681 * (lbm - 59) + 0.0264 * (h - 177)
        Cl2 = 1.29 - 0.024 * (age - 53)
        Cl3 = 0.836
        self._init_from_clearances(V1, V2, V3, Cl1, Cl2, Cl3, ke0=0.456,
                                   units="mg", conc_unit="ug/mL")


class EleveldModel(ThreeCompartmentModel):
    """Eleveld 2018 general-purpose propofol. *** Covariate slopes approximate;
    verify vs Table 2. *** Anchors (reference individual) are checked by the test."""
    MODEL_NAME, DRUG_NAME = "Eleveld", "Propofol"

    def __init__(self, patient, opioids=False):
        age, w, h, sex = patient.age, patient.weight, patient.height, patient.sex
        AGEr, HGTr, WGTr = 35.0, 170.0, 70.0
        male = (sex == "male")
        V1r, V2r, V3r = 6.28, 25.5, 273.0
        CLr, Q2r, Q3r, KE0r = 1.79, 1.75, 1.11, 0.146

        ffm = patient.ffm
        ffm_r = al_sallami_ffm(WGTr, HGTr, AGEr, "male")
        pma = age * 52.0 + 40.0
        pma_r = AGEr * 52.0 + 40.0

        f_v1 = lambda x: f_sigmoid(x, 3.6, 1.0)
        V1 = V1r * f_v1(w) / f_v1(WGTr)
        V2 = V2r * (w / WGTr) * f_aging(-0.0156, age) / f_aging(-0.0156, AGEr)
        V3 = V3r * (ffm / ffm_r)
        mat, mat_r = f_sigmoid(pma, 296.0, 9.06), f_sigmoid(pma_r, 296.0, 9.06)
        female_factor = 1.0 if male else 1.15
        Cl1 = CLr * (w / WGTr) ** 0.75 * (mat / mat_r) * female_factor
        Cl2 = Q2r * (V2 / V2r) ** 0.75
        Cl3 = Q3r * (V3 / V3r) ** 0.75
        ke0 = KE0r * (w / 70.0) ** -0.25
        self._init_from_clearances(V1, V2, V3, Cl1, Cl2, Cl3, ke0=ke0,
                                   units="mg", conc_unit="ug/mL")


# ======================================================================
# Opioids
# ======================================================================
class MintoModel(ThreeCompartmentModel):
    """Minto 1997 remifentanil. VOLUMES + CLEARANCES; age + James LBM.
    Organ-INDEPENDENT (esterase metabolism) -- the contrast to fentanyl below."""
    MODEL_NAME, DRUG_NAME = "Minto", "Remifentanil"

    def __init__(self, patient):
        age, lbm = patient.age, patient.lbm
        V1 = 5.1 - 0.0201 * (age - 40) + 0.072 * (lbm - 55)
        V2 = 9.82 - 0.0811 * (age - 40) + 0.108 * (lbm - 55)
        V3 = 5.42
        Cl1 = 2.6 - 0.0162 * (age - 40) + 0.0191 * (lbm - 55)
        Cl2 = 2.05 - 0.0301 * (age - 40)
        Cl3 = 0.076 - 0.00113 * (age - 40)
        ke0 = 0.595 - 0.007 * (age - 40)
        self._init_from_clearances(V1, V2, V3, Cl1, Cl2, Cl3, ke0=ke0,
                                   units="mcg", conc_unit="ng/mL")


class FentanylModel(ThreeCompartmentModel):
    """Fentanyl, 3-compartment model VALIDATED IN CABG PATIENTS
    (Anesthesiology 2002; PMID 11927479) -- apt for a cardiac population.
    Published as VOLUMES + CLEARANCES. The classic alternative is Shafer 1990
    (Anesthesiology 73:1091-1102). ke0 from Scott-Stanski 1987 (VERIFY).
    Unlike remifentanil, fentanyl clearance falls in severe liver disease / CHF."""
    MODEL_NAME, DRUG_NAME = "Fentanyl-CABG", "Fentanyl"

    def __init__(self, patient, ke0=0.147):
        # Fixed parameters from the CABG validation (≈70 kg adult range).
        self._init_from_clearances(
            V1=15.0, V2=20.0, V3=86.1,
            Cl1=1.08, Cl2=4.90, Cl3=2.60,
            ke0=ke0, units="mcg", conc_unit="ng/mL")


# ======================================================================
# Dexmedetomidine
# ======================================================================
class HannivoortModel(ThreeCompartmentModel):
    """Hannivoort 2015 dexmedetomidine (allometric, per 70 kg). VOLUMES +
    CLEARANCES. ke0 from PD literature (slow) -- VERIFY."""
    MODEL_NAME, DRUG_NAME = "Hannivoort", "Dexmedetomidine"

    def __init__(self, patient, ke0=0.12):
        F = patient.weight / 70.0
        self._init_from_clearances(
            V1=1.78 * F, V2=30.3 * F, V3=52.0 * F,
            Cl1=0.686 * F ** 0.75, Cl2=2.98 * F ** 0.75, Cl3=0.602 * F ** 0.75,
            ke0=ke0, units="mcg", conc_unit="ng/mL")


# ======================================================================
# Ketamine and methadone (ILLUSTRATIVE -- see the course)
# ======================================================================
class KetamineModel(ThreeCompartmentModel):
    """ILLUSTRATIVE racemic-ketamine 3-compartment (teaching). VOLUMES +
    CLEARANCES. High-extraction (CL ~ liver blood flow). Not validated here."""
    MODEL_NAME, DRUG_NAME = "Ketamine-illustrative", "Ketamine"

    def __init__(self, patient, ke0=0.4):
        F = patient.weight / 70.0
        self._init_from_clearances(
            V1=20.0 * F, V2=100.0 * F, V3=80.0 * F,
            Cl1=1.0 * F ** 0.75, Cl2=1.2 * F ** 0.75, Cl3=0.5 * F ** 0.75,
            ke0=ke0, units="mg", conc_unit="ug/mL")


class MethadoneModel(ThreeCompartmentModel):
    """ILLUSTRATIVE 2-compartment methadone (k13=k31=0). NOT FOR DOSING -- only
    to show very-long-half-life / context-sensitive behaviour."""
    MODEL_NAME, DRUG_NAME = "Methadone-illustrative", "Methadone"

    def __init__(self, patient, ke0=0.08):
        F = patient.weight / 70.0
        # publish-as-clearances with a zero third compartment -> 2-compartment
        self._init_from_clearances(
            V1=8.0 * F, V2=300.0 * F, V3=1.0,        # V3 unused (Cl3=0)
            Cl1=0.10 * F ** 0.75, Cl2=0.40 * F ** 0.75, Cl3=0.0,
            ke0=ke0, units="mg", conc_unit="ug/mL")


# ----------------------------------------------------------------------
# Self-tests
# ----------------------------------------------------------------------
if __name__ == "__main__":
    from patient import Patient

    ref = Patient(53, 77, 177, "male")
    s = SchniderModel(ref)
    V2 = (s.k12 * s.V1) / s.k21                      # recover V2 = Cl2/k21
    assert abs(s.V1 - 4.27) < 1e-6 and abs(V2 - 18.9) < 1e-3
    print("Schnider OK:  V1=%.3f L, V2=%.3f L" % (s.V1, V2))

    m = MintoModel(Patient(40, 70, 170, "male"))
    V3 = (m.k13 * m.V1) / m.k31
    assert abs(V3 - 5.42) < 1e-3
    print("Minto OK:     V1=%.3f L, V3=%.3f L" % (m.V1, V3))

    e = EleveldModel(Patient(35, 70, 170, "male"))
    CL = e.k10 * e.V1
    assert abs(e.V1 - 6.28) < 1e-3 and abs(CL - 1.79) < 1e-2 and abs(e.ke0 - 0.146) < 1e-3
    print("Eleveld OK:   V1=%.3f L, CL=%.3f L/min, ke0=%.3f" % (e.V1, CL, e.ke0))

    f = FentanylModel(Patient(65, 75, 175, "male"))
    CLf, V3f = f.k10 * f.V1, (f.k13 * f.V1) / f.k31
    assert abs(f.V1 - 15.0) < 1e-6 and abs(CLf - 1.08) < 1e-3 and abs(V3f - 86.1) < 1e-2
    print("Fentanyl OK:  V1=%.1f L, CL=%.3f L/min, V3=%.1f L" % (f.V1, CLf, V3f))

    mar = MarshModel(Patient(40, 70, 175, "male"))
    r = mar.simulate(boluses=[(0.0, 100.0)], t_end=10, dt=1 / 6)
    assert abs(r["cp"][0] - 100.0 / mar.V1) < 1e-6
    print("Marsh OK:     peak Cp after 100 mg = %.3f ug/mL" % r["cp"][0])

    meth = MethadoneModel(Patient(40, 70, 175, "male"))
    rm = meth.simulate(boluses=[(0.0, 10.0)], t_end=60, dt=1 / 6)
    assert np.isfinite(rm["cp"]).all() and abs(meth.k13) < 1e-12
    print("Methadone OK: 2-compartment (k13=k31=0) ran; Cp(60)=%.4f" % rm["cp"][-1])

    print("\nAll model self-tests passed.")
