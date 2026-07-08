"""
config.py  --  the declarative drug + theme registry (#3).

ONE place to describe each drug: which models are available, which display
units the dropdowns offer, the reference lines to draw, and the plot colour.
The app builds its UI and plots by READING this data, so adding a drug means
editing this file (plus one `if` line in dosing.py for any new unit) and
nothing else.

Nothing here does maths; it is pure configuration.
"""

from __future__ import annotations

from models import (MarshModel, SchniderModel, EleveldModel,
                    MintoModel, FentanylModel, HannivoortModel,
                    KetamineModel, MethadoneModel)


# drug -> configuration.  'models' maps a display name to a model CLASS
# (constructed later with a Patient).  Reference lines are in the drug's own
# concentration units; None means "do not draw".
DRUGS: dict[str, dict] = {
    "propofol": {
        "models": {"Marsh": MarshModel, "Schnider": SchniderModel,
                   "Eleveld": EleveldModel},
        "rate_units": ["mcg/kg/min", "mg/kg/hr", "mg/hr", "mg/min"],
        "bolus_units": ["mg", "mg/kg"],
        "klass": "Hypnotic",
        "color": "#4C72B0",
        "wakeup_ce": 1.2,      # ug/mL effect-site: below this, likely awake
        "awake_ce": 1.5,
        "ce50_bis": 3.0,       # ug/mL for BIS 50 (population)
    },
    "remifentanil": {
        "models": {"Minto": MintoModel},
        "rate_units": ["mcg/kg/min", "mcg/kg/hr", "ng/kg/min"],
        "bolus_units": ["mcg", "mcg/kg"],
        "klass": "Opioid",
        "color": "#C44E52",
        "wakeup_ce": None, "awake_ce": None, "ce50_bis": None,
        "note": "Organ-independent (esterase metabolism).",
    },
    "fentanyl": {
        "models": {"CABG (PMID 11927479)": FentanylModel},
        "rate_units": ["mcg/kg/hr", "mcg/kg/min", "mcg/hr"],
        "bolus_units": ["mcg", "mcg/kg"],
        "klass": "Opioid",
        "color": "#DD8452",
        "wakeup_ce": None, "awake_ce": None, "ce50_bis": None,
        "note": "Organ-DEPENDENT: clearance falls in severe liver disease / CHF.",
    },
    "dexmedetomidine": {
        "models": {"Hannivoort": HannivoortModel},
        "rate_units": ["mcg/kg/hr", "mcg/kg/min"],
        "bolus_units": ["mcg", "mcg/kg"],
        "klass": "Alpha-2 / Sedative",
        "color": "#55A868",
        "wakeup_ce": None, "awake_ce": None, "ce50_bis": None,
    },
    "ketamine": {
        "models": {"Illustrative": KetamineModel},
        "rate_units": ["mg/kg/hr", "mcg/kg/min", "mg/hr"],
        "bolus_units": ["mg", "mg/kg"],
        "klass": "NMDA antagonist",
        "color": "#8172B3",
        "wakeup_ce": None, "awake_ce": None, "ce50_bis": None,
        "note": "ILLUSTRATIVE parameters. Additive (not synergistic) with "
                "propofol for hypnosis.",
    },
    "methadone": {
        "models": {"Illustrative": MethadoneModel},
        "rate_units": ["mg/hr", "mg/min"],
        "bolus_units": ["mg", "mg/kg"],
        "klass": "Opioid (long-acting)",
        "color": "#937860",
        "wakeup_ce": None, "awake_ce": None, "ce50_bis": None,
        "note": "ILLUSTRATIVE only -- NOT a dosing model.",
    },
}

DRUG_OPTIONS: list[str] = list(DRUGS.keys())

# drugs grouped by pharmacological class (for grouped dropdowns, if wanted)
DRUG_CLASSES: dict[str, list[str]] = {}
for _name, _cfg in DRUGS.items():
    DRUG_CLASSES.setdefault(_cfg["klass"], []).append(_name)


def get_models(drug: str) -> dict:
    """Display-name -> model class for one drug."""
    return DRUGS[drug]["models"]


def get_reference_lines(drug: str) -> dict:
    """Reference-line values for the plot; None entries are skipped by the UI."""
    cfg = DRUGS[drug]
    return {"wakeup_ce": cfg.get("wakeup_ce"),
            "awake_ce": cfg.get("awake_ce"),
            "ce50_bis": cfg.get("ce50_bis")}


def drug_color(drug: str) -> str:
    return DRUGS[drug].get("color", "#333333")


if __name__ == "__main__":
    assert "propofol" in DRUGS and "fentanyl" in DRUGS
    assert "Schnider" in get_models("propofol")
    assert DRUG_CLASSES["Opioid"]              # remi + fentanyl + (methadone is its own)
    print("Drugs:", DRUG_OPTIONS)
    print("Classes:", {k: v for k, v in DRUG_CLASSES.items()})
    print("config.py self-tests passed.")
