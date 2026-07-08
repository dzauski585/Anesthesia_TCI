"""
validation.py  --  compare model predictions against real VitalDB cases.

VitalDB gives pump-reported concentrations and physiologic signals (BIS, HR,
MAP), NOT blood assays. So this validates (a) your engine vs the pump's engine
given identical dosing, and (b) your predicted Ce vs a measured PD signal.

`pip install vitaldb` to use the data functions. Varvel metrics need no network.
"""

import numpy as np


# ----------------------------------------------------------------------
# Varvel predictive-performance metrics (no network needed)
# ----------------------------------------------------------------------
def varvel_metrics(measured, predicted):
    """MDPE (bias), MDAPE (inaccuracy), Wobble. Inputs same length/units."""
    measured = np.asarray(measured, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    ok = (predicted > 0) & np.isfinite(measured) & np.isfinite(predicted)
    pe = (measured[ok] - predicted[ok]) / predicted[ok] * 100.0
    mdpe = float(np.median(pe))
    mdape = float(np.median(np.abs(pe)))
    wobble = float(np.median(np.abs(pe - mdpe)))
    return dict(MDPE=mdpe, MDAPE=mdape, Wobble=wobble, n=int(ok.sum()))


# ----------------------------------------------------------------------
# VitalDB access (requires `pip install vitaldb`)
# ----------------------------------------------------------------------
def find_tiva_cases(tracks=("Orchestra/PPF20_RATE", "BIS/BIS")):
    import vitaldb
    return vitaldb.find_cases(list(tracks))


def load_case_data(caseid,
                   tracks=("Orchestra/PPF20_RATE", "Orchestra/PPF20_CE",
                           "BIS/BIS", "Solar8000/HR", "Solar8000/ART_MBP"),
                   interval=1.0):
    """Return (data_array, track_names). Columns follow `tracks` order.
    interval=1.0 -> one row per second."""
    import vitaldb
    data = vitaldb.load_case(caseid, list(tracks), interval=interval)
    return data, list(tracks)


def case_demographics(caseid):
    import vitaldb
    clin = vitaldb.load_clinical_data()
    row = clin[clin["caseid"] == caseid].iloc[0]
    return dict(age=float(row["age"]), sex=str(row["sex"]),
                weight=float(row["weight"]), height=float(row["height"]))


def reconstruct_propofol_mgmin(rate_mlh_track, syringe_mg_per_ml=20.0):
    """PPF20 = 20 mg/mL syringe. Pump *_RATE is mL/h. -> mg/min per second."""
    rate = np.asarray(rate_mlh_track, dtype=float)
    rate = np.nan_to_num(rate, nan=0.0)
    return rate * syringe_mg_per_ml / 60.0       # mg/min


if __name__ == "__main__":
    # Varvel hand-check from Vol 1
    out = varvel_metrics([3.3, 3.6, 5.5], [3.0, 4.0, 5.0])
    assert abs(out["MDPE"] - 10) < 1e-9 and abs(out["MDAPE"] - 10) < 1e-9
    assert abs(out["Wobble"] - 0) < 1e-9
    print("varvel_metrics OK:", out)
    print("(VitalDB functions require `pip install vitaldb` + network.)")
