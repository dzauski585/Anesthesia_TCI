from core.simplePD import simplePD

pd = simplePD

assert pd.calculate_bis(0) == 100          # No drug = awake
assert abs(pd.calculate_bis(3.4) - 50) < 1 # At EC50 = 50% effect BY DEFINITION
assert pd.calculate_bis(6.0) < 35          # Deep anesthesia
assert pd.calculate_bis(10) < 25           # Very deep
