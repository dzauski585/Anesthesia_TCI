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
        
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age <= 0:
            raise ValueError(f"You entered {age}, age must be greater than 0" )
        
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number(float)")
        if weight <=0:
            raise ValueError(f"You entered {weight}, weight must be greater than 0")
        
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number(float)")
        if height <=0:
            raise ValueError(f"You entered {height}, height must be greater than 0")
        
        if not isinstance(sex, str):
            raise TypeError("Sex must be a letter(str)")
        if sex not in ("M", "F"):
            raise ValueError(f"You entered {sex}, sex must be M or F")
      
        
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        
        self.bmi = self._calculate_bmi()
        self.lbm = self._calculate_lbm()
        self.ibw = self._calculate_ibw()
        self.ffm = self._calculate_ffm()
                
        self.adjusted_weight = self.ibw + 0.4 * (self.weight - self.ibw) #adjusted body weight for morbid obesity. 
        #Servin F, Farinotti R, Haberer JP, Desmonts JM. Propofol infusion for maintenance of anesthesia in morbidly obese patients receiving nitrous oxide: a clinical and pharmacokinetic study. 
        #Anesthesiology. 1993;78(4):657–665.
        
    def _calculate_bmi(self) -> float:
        """BMI = weight_kg / (height_m)^2"""
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi
    
    def _calculate_lbm(self) -> float:
            """Lean Body Mass using the James formula. For Schneider"""
            if self.sex == "M":
                lbm = 1.1 * self.weight - 128 * (self.weight / self.height) ** 2
            else:
                lbm = 1.07 * self.weight - 148 * (self.weight / self.height) ** 2
            
            return lbm
        
    def _calculate_ibw(self) -> float:
        """Ideal Body Weight using Lemmens formula. Can be used for obese patients. 
            Lemmens HJM, Brodsky JB, Bernstein DP. Estimating ideal body weight — a new formula. Obes Surg. 2005;15:1082–1083.
        """
        height_m = self.height / 100
        ibw = 22 * (height_m **2)
        return ibw
        
    def _calculate_ffm(self) -> float:
        """Fat-Free Mass using Al-Sallami formula. For Eleveld.
        Al-Sallami HS, Goulding A, Grant A, et al. Prediction of fat-free mass in children. Clin Pharmacokinet. 2015;54:1169–1178.
        """
        bmi = self.bmi
        if self.sex == 'M':
            maturation = 0.88 + ((1 - 0.88) / (1 + (self.age / 13.4) ** (-12.7)))
            return maturation * (9270 * self.weight / (6680 + 216 * bmi))
        else:
            maturation = 1.11 + ((1 - 1.11) / (1 + (self.age / 7.1) ** (-1.1)))
            return maturation * (9270 * self.weight / (8780 + 244 * bmi))
    
     
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
        return (f"Patient: {self.age}yo{self.sex}, {self.weight}kg, {self.height}cm, BMI ={self.bmi: .1f}, LBM ={self.lbm: .2f}kg")
    
    def __repr__(self) -> str:
        """Makes print(patient) useful for debugging."""
        return (f"Patient (age={self.age}, weight={self.weight}, height={self.height}, sex={self.sex})")        

