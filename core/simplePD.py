class simplePD:
    """
    Maps drug concentration to BIS using the Hill equation.
    The Hill equation models receptor saturation: effect increases
    steeply near EC50, then plateaus as receptors become occupied.
    """
 
    def __init__(self):
        self.BIS0 = 100     # Baseline BIS (awake, no drug)
        self.Emax = 100     # Maximum BIS reduction possible
        self.EC50 = 3.4     # Concentration for 50% max effect (ug/mL)
        self.gamma = 1.6    # Steepness (Hill coefficient)
        # gamma = 1: gentle curve (large therapeutic window)
        # gamma = 5: steep curve (narrow window, almost on/off)
        # gamma = 1.6: moderate (some forgiveness if you overshoot)
 
    def calculate_bis(self, concentration: float) -> float:
        """
        BIS = BIS0 - Emax * (C^gamma) / (EC50^gamma + C^gamma)
        """
        # TODO: Handle concentration <= 0 (return BIS0 = 100)
        # TODO: Calculate numerator = concentration ** self.gamma
        # TODO: Calculate denominator = self.EC50 ** self.gamma + numerator
        # TODO: effect = self.Emax * (numerator / denominator)
        # TODO: bis = self.BIS0 - effect
        # TODO: return max(0, min(100, bis))  # clamp to valid range
        pass
