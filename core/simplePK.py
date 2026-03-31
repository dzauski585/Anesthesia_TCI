class SimplePKModel:
    """
    1-compartment pharmacokinetic model using Euler integration.
    
    This is a simplified teaching model. It assumes all drug distributes
    to a single well-stirred compartment and is eliminated at a rate
    proportional to concentration (first-order kinetics).
    
    Units: concentration in ug/mL, time in minutes, volume in liters.
    """
 
    def __init__(self, weight: float):
        """
        Initialize with patient weight (kg).
        Uses simplified Marsh parameters for a single compartment.
        """
        # V1 = how big the 'bucket' is (liters)
        # Marsh central compartment: 0.228 liters per kg of body weight
        # For 70 kg patient: V1 = 0.228 * 70 = 15.96 liters
        self.V1 = 0.228 * weight
 
        # Cl = how fast the body clears drug (liters/min)
        # Marsh elimination clearance: 0.119 L/min per kg
        # For 70 kg: Cl = 0.119 * 70 = 8.33 L/min
        self.Cl = 0.119 * weight
 
        # Current drug concentration (ug/mL). Starts at 0 = no drug.
        self.concentration = 0.0
 
        # Track elapsed time for history recording
        self.time = 0.0
 
    def bolus(self, dose_mg: float):
        """
        Instantly inject a bolus dose.
        
        The entire dose enters the compartment at once.
        Concentration increases by dose / volume.
        
        Args:
            dose_mg: Bolus dose in milligrams
        """
        dose_ug = dose_mg * 1000
        concentration_increase = dose_ug / (self.V1 * 1000)
        self.concentration += concentration_increase

 
    def update(self, infusion_rate_ug_min: float, dt: float):
        """
        Advance simulation by dt minutes using Euler integration.
        
        Args:
            infusion_rate_ug_min: Continuous infusion rate (ug/min).
                A typical propofol maintenance rate is 400-600 ug/kg/min.
                For 70 kg: 400*70 = 28,000 ug/min to 600*70 = 42,000 ug/min.
                Hmm, that seems high. Let's check units:
                Actually, infusion rates are often expressed as ug/kg/min.
                28,000-42,000 ug/min is 28-42 mg/min. That's about right.
            dt: Time step in minutes (use 0.1 = 6 seconds)
        """

        rate_in = infusion_rate_ug_min / (self.V1 * 1000)  # ug/mL/min
        k10 = self.Cl / self.V1
        rate_out = k10 * self.concentration  # ug/mL/min
 
        dC_dt = rate_in - rate_out
        
        self.concentration += dC_dt * dt #euler step applying the change
        self.concentration = max(0, self.concentration) #conc cant be negative
 
        self.time += dt
 
    def get_concentration(self) -> float:
        """Return current drug concentration in ug/mL."""
        return self.concentration
 
    def reset(self):
        """Reset to initial state (no drug, time=0)."""
        self.concentration = 0.0
        self.time = 0.0
