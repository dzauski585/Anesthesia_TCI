class Patient:
    """
    Represents a patient for pharmacokinetic calculations.
    
    Stores demographics and automatically calculates derived values
    (BMI, LBM) that PK models need. Once created, patient data does
    not change during a simulation.
    
    Usage:
        patient = Patient(age=45, weight=70, height=175, sex='M')
        print(patient.bmi)   # 22.9
        print(patient.lbm)   # 56.5
    """
 
    def __init__(self, age: int, weight: float, height: float, sex: str):
        """
        Args:
            age: Patient age in years (must be > 0)
            weight: Patient weight in kg (must be > 0)
            height: Patient height in cm (must be > 0)
            sex: 'M' for male or 'F' for female
        
        Raises:
            ValueError: If any input is out of range
        """
        # ---- Input validation ----

            #TODO
 
        # ---- Store raw parameters ----
        #TODO
        
        # ---- Calculate derived values ----

          #TODO

 
    def _calculate_bmi(self) -> float:
        """BMI = weight_kg / (height_m)^2"""
        # TODO: Convert height from cm to meters
        #   height_m = self.height / 100
        # TODO: Calculate and return BMI
        #   return self.weight / (height_m ** 2)
        pass
 
    def _calculate_lbm(self) -> float:
        """Lean Body Mass using the James formula."""
        # TODO: Implement based on self.sex
        # if self.sex == 'M':
        #     return 1.1 * self.weight - 128 * (self.weight / self.height) ** 2
        # else:
        #     return 1.07 * self.weight - 148 * (self.weight / self.height) ** 2
        pass
 
    def post_menstrual_age_weeks(self) -> float:
        """
        For Eleveld pediatric model.
        PMA = gestational age + postnatal age.
        For adults, this is an approximation.
        For actual pediatric use, you would need exact gestational age.
        """
        return (self.age * 52) + 40  # 40 weeks gestation assumed
 
    def summary(self) -> str:
        """Return formatted string of all patient parameters."""
        # TODO: Return a string like:
        # 'Patient: 45yo M, 70.0kg, 175.0cm, BMI=22.9, LBM=56.5kg'
        pass
 
    def __repr__(self) -> str:
        """Makes print(patient) useful for debugging."""
        #TODO
