"""
patient.py  --  the Patient object (TEACHING / RESEARCH ONLY)

One small object holds the demographics and the derived body-size numbers the
PK models need, so every model asks `patient.lbm` instead of re-deriving it
(and possibly disagreeing). One source of truth for body size.

Body-size quantities provided:
    bmi             - body mass index (kg/m^2)
    lbm             - lean body mass, James 1976 (used by Schnider)
    ffm             - fat-free mass, Al-Sallami 2015 (used by Eleveld)
    ibw             - ideal body weight, Devine 1974
    adjusted_weight - adjusted body weight, Servin (for the obese)

NOTE: organ-function inputs (hepatic class, renal function) and pregnancy are
deliberately NOT modelled here. For this drug set they are either small drivers
or not codeable into the standard TCI models; the one PK feature that matters
for high-extraction drugs (propofol, fentanyl, ketamine) is cardiac output,
which is handled as a simulation input, not a Patient attribute.
"""

from __future__ import annotations


# ----------------------------------------------------------------------
# Stand-alone body-size formulas (also importable by the models)
# ----------------------------------------------------------------------
def james_lbm(weight, height_cm, sex):
    """Lean body mass (kg), James 1976. weight kg, height cm.

    Known quirk: this formula *falls* at very high BMI, which makes Schnider
    behave oddly in the morbidly obese. That is a property of Schnider, not a
    bug here. Eleveld avoids it by using fat-free mass instead.
    """
    if sex == "male" or sex == 0:
        return 1.1 * weight - 128 * (weight / height_cm) ** 2
    return 1.07 * weight - 148 * (weight / height_cm) ** 2


def al_sallami_ffm(weight, height_cm, age, sex):
    """Fat-free mass (kg), Al-Sallami 2015. Used by the Eleveld model."""
    bmi = weight / (height_cm / 100.0) ** 2
    if sex == "male" or sex == 0:
        return (0.88 + (1 - 0.88) / (1 + (age / 13.4) ** -12.7)) \
               * (9270 * weight) / (6680 + 216 * bmi)
    return (1.11 + (1 - 1.11) / (1 + (age / 7.1) ** -1.1)) \
           * (9270 * weight) / (8780 + 244 * bmi)


def devine_ibw(height_cm, sex):
    """Ideal body weight (kg), Devine 1974. height cm."""
    inches_over_5ft = max(0.0, (height_cm / 2.54) - 60.0)
    if sex == "male" or sex == 0:
        return 50.0 + 2.3 * inches_over_5ft
    return 45.5 + 2.3 * inches_over_5ft


# ----------------------------------------------------------------------
# The Patient
# ----------------------------------------------------------------------
class Patient:
    """Demographics + derived body-size numbers. Created once, read by models.

    sex is normalised to the string "male" or "female" so the models can test
    it consistently.
    """

    def __init__(self, age, weight, height, sex):
        if age <= 0 or weight <= 0 or height <= 0:
            raise ValueError("age, weight, height must all be positive.")
        self.age = age                     # years
        self.weight = weight               # kilograms (total body weight)
        self.height = height               # centimetres
        self.sex = "male" if str(sex).lower().startswith("m") else "female"

        # Derived body-size numbers computed once and stored.
        self.bmi = self.weight / (self.height / 100.0) ** 2
        self.lbm = james_lbm(self.weight, self.height, self.sex)
        self.ffm = al_sallami_ffm(self.weight, self.height, self.age, self.sex)
        self.ibw = devine_ibw(self.height, self.sex)
        self.adjusted_weight = self.ibw + 0.4 * (self.weight - self.ibw)

    def __repr__(self):
        return (f"Patient(age={self.age}, weight={self.weight}kg, "
                f"height={self.height}cm, sex={self.sex}, "
                f"lbm={self.lbm:.1f}kg, ffm={self.ffm:.1f}kg, bmi={self.bmi:.1f})")


if __name__ == "__main__":
    p = Patient(40, 70, 175, "male")
    print(p)
    # James LBM for a 70 kg / 175 cm male ~ 56 kg
    assert 50 < p.lbm < 62, p.lbm
    # Devine IBW for 175 cm male = 50 + 2.3*(68.9-60) ~ 70.5 kg
    assert 68 < p.ibw < 73, p.ibw
    f = Patient(40, 70, 175, "female")
    assert f.lbm < p.lbm                      # female LBM lower at same size
    print("patient.py self-tests passed.")
