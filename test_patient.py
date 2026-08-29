"""
Text-based validation tests for patient.py.

Why this file exists:
    You can't trust a calculation you haven't checked. Before Patient
    feeds numbers into a drug model, you want proof that BMI, LBM, etc.
    are actually computing what you think they're computing -- against
    numbers you worked out independently (by hand, or from a paper).

How to run it:
    From this folder, in the VS Code integrated terminal:
        python test_patient.py
    If every check passes, you'll see "All tests passed!" at the bottom.
    If a check fails, Python raises an AssertionError and tells you
    exactly which line failed -- read that message, it's not an error
    to fear, it's the whole point of writing the test.

Pattern: each test is a small function with no arguments that does
some asserts. main() runs each one in isolation, catches the first
line to print each one's name and pass/fail, so results don't just print in a wall of text.
"""

from claude_solutions.patient import Patient


# ---------------------------------------------------------------------------
# WORKED EXAMPLE -- fully written, read this one closely before you write
# your own. It checks that bad input actually gets rejected.
# ---------------------------------------------------------------------------
def test_invalid_age_raises_error():
    """Patient(age=-5, ...) should raise ValueError, not silently accept it."""
    try:
        # This call SHOULD fail. We're deliberately passing a bad age.
        Patient(age=-5, weight=70, height=170, sex="M")

        # If we get to this line, Patient did NOT raise -- that's a bug,
        # so we force the test to fail on purpose.
        assert False, "Patient accepted age=-5 without raising ValueError"

    except ValueError:
        # This is the branch we WANT to land in. Catching the specific
        # exception type (ValueError) rather than a bare `except:` means
        # we only forgive the error we're testing for -- any other kind
        # of crash (e.g. a real bug raising TypeError) still surfaces.
        pass


# ---------------------------------------------------------------------------
# YOUR TURN -- fill these in. Each docstring has the reference numbers
# you need; you write the Patient(...) call and the assert.
# ---------------------------------------------------------------------------
def test_bmi_known_value():
    """
    A 40yo M, 70 kg, 170 cm patient has BMI = weight / (height_m ** 2)
                                              = 70 / (1.70 ** 2)
                                              = 24.22  (rounded to 2 dp)

    TODO:
        1. Create that Patient.
        2. Assert patient.bmi rounds to 24.22.
           (Floats are rarely EXACTLY equal -- use round(patient.bmi, 2) == 24.22,
           not patient.bmi == 24.22.)
    """
    pass  # <- delete this line once you've written the test


def test_lbm_differs_by_sex():
    """
    Same age/weight/height, only sex changes -- LBM uses a different
    formula for M vs F (see patient.py's _calculate_lbm docstring), so
    the two results should NOT be equal. Reference values, both age 53,
    77 kg, 177 cm:
        sex='M' -> LBM ~= 60.48
        sex='F' -> LBM ~= 54.38

    TODO:
        1. Create both patients.
        2. Assert each patient's LBM is close to its reference value
           (round to 2 dp and compare, same trick as above).
        3. Assert the two LBM values are not equal to each other --
           this is the check that actually proves sex changes the formula.
    """
    pass  # <- delete this line once you've written the test


# ---------------------------------------------------------------------------
# Test runner -- you don't need to touch this.
# ---------------------------------------------------------------------------
def main():
    tests = [
        test_invalid_age_raises_error,
        test_bmi_known_value,
        test_lbm_differs_by_sex,
    ]
    for test in tests:
        test()
        print(f"  ok  {test.__name__}")
    print("All tests passed!")


if __name__ == "__main__":
    main()
