"""
covariates.py  --  special populations: pregnancy & renal  (Week 19)

patient.py deliberately does NOT bake pregnancy or renal state into the standard
models. This module is the honest alternative the course argues for: explicit,
user-editable scaling factors applied ON TOP of a base model, defaulting to the
physiologic direction, never presented as a validated population model.

Mechanism: a model stores V1 and six rate constants. Scaling every VOLUME by fv
and every CLEARANCE by fcl is equivalent to
    V1  -> fv * V1
    k_ij -> (fcl / fv) * k_ij     (for all six rate constants)
    ke0  unchanged
because each k is a clearance divided by a volume. steady-state maintenance rate
= Ct*CL scales by fcl; the peak from a fixed bolus (Cp0 = dose/V1) scales by 1/fv.

*** These multipliers are directionally-correct TEACHING defaults, not validated
models. Keep them visible and editable in the UI; never present a
covariate-adjusted number as clinical guidance. ***
Physiology: pregnancy at term raises cardiac output / hepatic blood flow
(clearance up for flow-limited drugs) and total body water (volumes up). Renal
failure leaves the parent PK of these four drugs essentially unchanged -- the
real effects are on inactive metabolites (remifentanil acid) or are
pharmacodynamic (dexmedetomidine sedation prolonged).
"""

import copy


# Midpoints of the Week 19 ranges. (CL factor, V factor).  None = "no accepted
# parametric adjustment" -> treated as 1.0 with a caveat.
PREGNANCY = {
    "propofol":        (1.35, 1.30),
    "remifentanil":    (1.30, 1.20),
    "fentanyl":        (1.20, 1.10),
    "dexmedetomidine": (1.00, 1.00),   # human pregnancy PK sparse -> provisional
}

# Renal (severe): parent PK of all four is essentially unchanged. Dex needs a
# PHARMACODYNAMIC dose reduction (prolonged sedation), not a PK change -- so the
# PK factors stay 1.0 and the note carries the clinical action.
RENAL = {
    "propofol":        (1.00, 1.00),
    "remifentanil":    (1.00, 1.00),   # GR90291 accumulates but ~1/4600 potency
    "fentanyl":        (1.00, 1.00),
    "dexmedetomidine": (1.00, 1.00),   # PK unchanged; reduce maintenance (PD)
}


def scaled_model(model, cl_factor=1.0, v_factor=1.0):
    """Return a copy of `model` with all clearances x cl_factor and all volumes
    x v_factor. ke0 is unchanged. The original model is not mutated."""
    m = copy.copy(model)
    fk = cl_factor / v_factor
    m.V1 = model.V1 * v_factor
    m.k10 = model.k10 * fk
    m.k12 = model.k12 * fk
    m.k13 = model.k13 * fk
    m.k21 = model.k21 * fk
    m.k31 = model.k31 * fk
    return m


def apply_covariates(model, drug_name, pregnant=False, renal=False,
                     factors=None):
    """Apply pregnancy and/or renal scaling to a base model.

    factors: optional {'cl': x, 'v': y} to override the table (the UI should
    expose these as editable numbers). Returns a new, scaled model."""
    cl, v = 1.0, 1.0
    if pregnant:
        pcl, pv = PREGNANCY.get(drug_name, (1.0, 1.0))
        cl *= pcl; v *= pv
    if renal:
        rcl, rv = RENAL.get(drug_name, (1.0, 1.0))
        cl *= rcl; v *= rv
    if factors:
        cl *= factors.get("cl", 1.0); v *= factors.get("v", 1.0)
    return scaled_model(model, cl_factor=cl, v_factor=v)


if __name__ == "__main__":
    from patient import Patient
    from models import EleveldModel, MintoModel

    base = EleveldModel(Patient(30, 70, 170, "female"))
    CL0, V10 = base.k10 * base.V1, base.V1

    preg = apply_covariates(base, "propofol", pregnant=True)
    CL1, V11 = preg.k10 * preg.V1, preg.V1
    # clearance scales by the CL factor, V1 by the V factor
    assert abs(CL1 / CL0 - 1.35) < 1e-6, CL1 / CL0
    assert abs(V11 / V10 - 1.30) < 1e-6, V11 / V10
    print("Propofol pregnancy: CL x%.2f, V1 x%.2f" % (CL1 / CL0, V11 / V10))

    # Exercise 19.1: steady-state maintenance rate = Ct*CL rises with CL
    remi = MintoModel(Patient(30, 70, 170, "female"))
    remi_p = apply_covariates(remi, "remifentanil", pregnant=True)
    rate_ratio = (remi_p.k10 * remi_p.V1) / (remi.k10 * remi.V1)
    assert abs(rate_ratio - 1.30) < 1e-6
    print("Remi pregnancy: hold-rate x%.2f (needs ~30%% more to hold target)" % rate_ratio)

    # renal leaves parent PK unchanged for all four
    ren = apply_covariates(base, "propofol", renal=True)
    assert abs(ren.k10 * ren.V1 - CL0) < 1e-9 and abs(ren.V1 - V10) < 1e-9
    print("Propofol renal: PK unchanged (as expected).")
    print("covariates.py self-tests passed.")
