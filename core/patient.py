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
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0:
            raise ValueError(f"You entered {age}, age must be greater than 0" )
        
        if not isinstance(height, float):
            raise TypeError("Height must be a number in cm.")
        if height < 0:
            raise ValueError(f"You entered {height}, height must be greater than 0" )
        
        if not isinstance(weight, float):
            raise TypeError("Age must be an integer.")
        if weight < 0:
            raise ValueError(f"You entered {weight}, weight must be greater than 0" )
        
        if not isinstance(sex, str):
            raise TypeError("Sex must be a str.")
        if sex not in ("M", "F"):
            raise ValueError(f"You entered {sex}, sex must be M or F" )
 
        # ---- Store raw parameters ----
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        
        # ---- Calculate derived values ----
        self.bmi = self._calculate_bmi()
        self.lbm = self._calculate_lbm()

    def _calculate_bmi(self) -> float:
        """BMI = weight_kg / (height_m)^2"""
        height_m = self.height / 100
        bmi = self.weight / (height_m **2)
        return bmi
 
    def _calculate_lbm(self) -> float:
        """Lean Body Mass using the James formula."""
        if self.sex == "M":
            lbm = 1.1 * self.weight - 128 * (self.weight / self.height) ** 2
        else:
            lbm = 1.07 * self.weight - 148 * (self.weight / self.height) ** 2
        
        return lbm
 
    def post_menstrual_age_weeks(self) -> float:
        """
        For Eleveld pediatric model.
        PMA = gestational age + postnatal age.
        For adults, this is an approximation.
        For actual pediatric use, you would need exact gestational age.
        40 weeks gestation assumed
        """
        post_menstrual_age = (self.age * 52) + 40
        return post_menstrual_age
 
    def summary(self) -> str:
        """Return formatted string of all patient parameters."""
        return (f"Patient: {self.age}yo {self.sex}, {self.weight}kg, {self.height}cm, BMI={self.bmi}, LBM={self.lbm}kg")

    def __repr__(self) -> str:
        """Makes print(patient) useful for debugging."""
        return (f"Patient (age={self.age}, weight={self.weight}, height={self.height}, sex={self.sex})")
