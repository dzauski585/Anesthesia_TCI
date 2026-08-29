class Patient:
    """
    Class for patient values to be used in PK/PD models. 
    Functions exists for storing patient attributes along with BMI and LBM calculation
    
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
        
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        

