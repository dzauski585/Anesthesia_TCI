"""
dosing.py  --  turn clinical dosing into model inputs.

Conventions: propofol/ketamine/methadone in mg; remifentanil/dexmedetomidine
in micrograms (mcg). Concentrations must match the drug's unit.
"""


# ----------------------------------------------------------------------
# Infusion schedules
# ----------------------------------------------------------------------
def make_infusion_func(segments):
    """segments: list of (start_min, end_min, rate_per_min) -> f(t)->rate.

    Overlapping segments for the same drug are summed (rarely needed)."""
    def f(t):
        total = 0.0
        for (start, end, rate) in segments:
            if start <= t < end:
                total += rate
        return total
    return f


# ----------------------------------------------------------------------
# Unit converters  (your guardrails -- always route clinical numbers here)
# ----------------------------------------------------------------------
def mcgkgmin_to_permin(rate, weight):          # e.g. propofol 150 mcg/kg/min
    return rate * weight                       # -> mcg/min (then /1000 for mg)

def mgkgmin_to_permin(rate, weight):
    return rate * weight                       # -> mg/min

def mgkgh_to_permin(rate, weight):             # Roberts uses mg/kg/h
    return rate * weight / 60.0                # -> mg/min

def mcgkgh_to_permin(rate, weight):            # dexmedetomidine often mcg/kg/h
    return rate * weight / 60.0                # -> mcg/min

def mlh_to_massmin(rate_mlh, conc_per_ml):     # pump rate -> mass/min
    return rate_mlh * conc_per_ml / 60.0


# ----------------------------------------------------------------------
# Canonical dispatchers  (Week 12)
# ----------------------------------------------------------------------
# Every model works in ONE mass unit: mg (propofol/ketamine/methadone) or mcg
# (remifentanil/dexmedetomidine/fentanyl). The event grid, however, lets the
# user pick any label. These two functions are the single guardrail the UI must
# route every rate and every bolus through: they convert whatever the user typed
# into <drug_unit>/min (rates) or <drug_unit> (boluses), so a rate and a bolus
# can never silently arrive in the wrong unit. drug_unit is the model's .units.
_MASS_TO_MG = {"mg": 1.0, "mcg": 1e-3, "ng": 1e-6}   # 1 unit -> this many mg


def _to_drug_mass(value, from_mass, drug_unit):
    """Scale a mass in `from_mass` into the drug's own mass unit."""
    return value * (_MASS_TO_MG[from_mass] / _MASS_TO_MG[drug_unit])


def event_rate_to_permin(amount, unit, weight, drug_unit):
    """An infusion-row rate (any offered label) -> rate in <drug_unit>/min.

    Handles weight-based (/kg), per-hour (/h), and per-minute forms across the
    mg / mcg / ng mass families, then normalises to the drug's mass unit."""
    u = unit.strip().replace("/hr", "/h")
    if   u == "mg/kg/min":   val, m = amount * weight,        "mg"
    elif u == "mcg/kg/min":  val, m = amount * weight,        "mcg"
    elif u == "ng/kg/min":   val, m = amount * weight,        "ng"
    elif u == "mg/kg/h":     val, m = amount * weight / 60.0, "mg"
    elif u == "mcg/kg/h":    val, m = amount * weight / 60.0, "mcg"
    elif u == "mg/h":        val, m = amount / 60.0,          "mg"
    elif u == "mcg/h":       val, m = amount / 60.0,          "mcg"
    elif u == "mg/min":      val, m = amount,                 "mg"
    elif u == "mcg/min":     val, m = amount,                 "mcg"
    else:                    val, m = amount,                 drug_unit  # assume canonical
    return _to_drug_mass(val, m, drug_unit)


def event_dose_to_mass(amount, unit, weight, drug_unit):
    """A bolus-row amount (mg, mg/kg, mcg, mcg/kg, ng) -> dose in <drug_unit>.

    This is the fix for the old bug where a bolus row's unit was ignored and a
    'mg/kg' entry was treated as raw mg."""
    u = unit.strip()
    if   u == "mg":      val, m = amount,          "mg"
    elif u == "mg/kg":   val, m = amount * weight, "mg"
    elif u == "mcg":     val, m = amount,          "mcg"
    elif u == "mcg/kg":  val, m = amount * weight, "mcg"
    elif u == "ng":      val, m = amount,          "ng"
    else:                val, m = amount,          drug_unit
    return _to_drug_mass(val, m, drug_unit)


# ----------------------------------------------------------------------
# Ketofol: two drugs, one syringe, one pump rate
# ----------------------------------------------------------------------
def ketofol_concentrations(propofol_mg, ketamine_mg, total_volume_ml):
    """Given the amounts mixed and the final volume, return per-mL strengths.

    Example: 500 mg propofol (a 50 mL 1% bottle) + 200 mg ketamine in 50 mL
    -> (10.0 mg/mL propofol, 4.0 mg/mL ketamine)."""
    return (propofol_mg / total_volume_ml, ketamine_mg / total_volume_ml)


def ketofol_segments(rate_mlh_segments, propofol_conc, ketamine_conc):
    """One shared list of (start, end, mL/h) -> two mass/min schedules.

    Returns (propofol_segments, ketamine_segments), each in mass/min, ready
    for make_infusion_func()."""
    prop = [(s, e, mlh_to_massmin(r, propofol_conc)) for (s, e, r) in rate_mlh_segments]
    ket = [(s, e, mlh_to_massmin(r, ketamine_conc)) for (s, e, r) in rate_mlh_segments]
    return prop, ket


# ----------------------------------------------------------------------
# Roberts / Bristol manual regimen (mg/kg/h): 10 (10 min), 8 (10 min), 6
# ----------------------------------------------------------------------
def roberts_regimen(weight, total_min=240, bolus_mgkg=1.0):
    """Return (boluses, infusion_func) for the classic 10-8-6 mg/kg/h scheme."""
    boluses = [(0.0, bolus_mgkg * weight)]
    segments = [
        (0, 10,        mgkgh_to_permin(10, weight)),
        (10, 20,       mgkgh_to_permin(8,  weight)),
        (20, total_min, mgkgh_to_permin(6, weight)),
    ]
    return boluses, make_infusion_func(segments)


if __name__ == "__main__":
    # checks against Vol 1/2 hand calculations
    assert abs(mgkgmin_to_permin(0.15, 70) - 10.5) < 1e-9
    assert abs(mlh_to_massmin(70, 10) - 11.6667) < 1e-3
    pc, kc = ketofol_concentrations(500, 200, 50)
    assert (pc, kc) == (10.0, 4.0)
    b, inf = roberts_regimen(70)
    assert b == [(0.0, 70.0)]
    assert abs(inf(5) - 11.6667) < 1e-3        # 700 mg/h = 11.67 mg/min
    assert abs(inf(15) - 9.3333) < 1e-3
    assert abs(inf(30) - 7.0) < 1e-3

    # canonical dispatchers (Week 12)
    # propofol (mg drug): 9 mg/kg/hr @70kg -> 10.5 mg/min
    assert abs(event_rate_to_permin(9.0, "mg/kg/hr", 70, "mg") - 10.5) < 1e-9
    # remifentanil (mcg drug): 0.25 mcg/kg/min @70kg -> 17.5 mcg/min
    assert abs(event_rate_to_permin(0.25, "mcg/kg/min", 70, "mcg") - 17.5) < 1e-9
    # remi in ng/kg/min: 250 ng/kg/min @70kg -> 17.5 mcg/min (was silently wrong before)
    assert abs(event_rate_to_permin(250.0, "ng/kg/min", 70, "mcg") - 17.5) < 1e-6
    # ketamine (mg drug) given in mcg/kg/min: 250 mcg/kg/min @70kg -> 17.5 mg/min
    assert abs(event_rate_to_permin(250.0, "mcg/kg/min", 70, "mg") - 17.5) < 1e-6
    # boluses now honour their unit
    assert abs(event_dose_to_mass(140.0, "mg", 70, "mg") - 140.0) < 1e-9
    assert abs(event_dose_to_mass(2.0, "mg/kg", 70, "mg") - 140.0) < 1e-9   # was 2.0 before the fix
    assert abs(event_dose_to_mass(1.0, "mcg/kg", 70, "mcg") - 70.0) < 1e-9
    print("dosing.py self-tests passed.")
