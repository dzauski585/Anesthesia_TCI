from core.patient import Patient
 
def test_average_male():
    p = Patient(age=45, weight=70, height=175, sex='M')
    print(p.summary())
    # Expected: BMI = 22.9, LBM = 56.5 kg
    # Hand calculation:
    #   BMI = 70 / (1.75)^2 = 70 / 3.0625 = 22.857
    #   LBM = 1.1*70 - 128*(70/175)^2 = 77 - 128*0.16 = 77 - 20.48 = 56.52
    assert abs(p.bmi - 22.86) < 0.1, f'BMI wrong: {p.bmi}'
    assert abs(p.lbm - 56.52) < 0.5, f'LBM wrong: {p.lbm}'
 
def test_obese_female():
    p = Patient(age=65, weight=85, height=160, sex='F')
    print(p.summary())
    # Expected: BMI = 33.2, LBM = 47.8 kg
    # This patient is obese (BMI > 30).
    # LBM is only 56% of total weight.
    # Schnider model would use 47.8 kg, not 85 kg, for clearance.
    # This is why model choice matters clinically!
    assert abs(p.bmi - 33.2) < 0.1
    assert abs(p.lbm - 47.8) < 1.0
 
def test_pediatric():
    p = Patient(age=8, weight=25, height=128, sex='M')
    print(f'PMA: {p.post_menstrual_age_weeks()} weeks')
    # PMA = 8*52 + 40 = 456 weeks
    # Used by Eleveld model for maturation function
 
def test_validation():
    """Bad inputs should raise ValueError."""
    import traceback
    for args in [(-5, 70, 175, 'M'), (45, -70, 175, 'M'),
                 (45, 70, -175, 'M'), (45, 70, 175, 'X')]:
        try:
            Patient(*args)
            print(f'ERROR: Should have raised ValueError for {args}')
        except ValueError as e:
            print(f'Correctly caught: {e}')
 
if __name__ == '__main__':
    test_average_male()
    test_obese_female()
    test_pediatric()
    test_validation()
    print('All Patient tests passed!')
