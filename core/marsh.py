class MarshModel:
    """3-compartment propofol PK model with effect-site (Marsh 1991)."""
    def __init__(self, patient):
        weight = patient.weight
        # Marsh parameters
        self.V1 = 0.228 * weight
        self.V2 = 0.463 * weight
        self.V3 = 2.893 * weight
        self.Cl1 = 0.119 * weight
        self.Cl2 = 0.112 * weight
        self.Cl3 = 0.042 * weight

        self.c1 = 0.0  # central concentration ug/mL
        self.c2 = 0.0  # fast peripheral
        self.c3 = 0.0  # slow peripheral
        self.time = 0.0

    def bolus(self, dose_mg):
        self.c1 += (dose_mg * 1000) / (self.V1 * 1000)

    def update(self, rate_mg_min, dt):
        # rate constants
        k10 = self.Cl1 / self.V1
        k12 = self.Cl2 / self.V1
        k21 = self.Cl2 / self.V2
        k13 = self.Cl3 / self.V1
        k31 = self.Cl3 / self.V3

        infusion = (rate_mg_min * 1000) / (self.V1 * 1000)  # ug/mL/min

        dc1 = infusion - (k10 + k12 + k13)*self.c1 + k21*self.c2 + k31*self.c3
        dc2 = k12*self.c1 - k21*self.c2
        dc3 = k13*self.c1 - k31*self.c3

        self.c1 += dc1 * dt
        self.c2 += dc2 * dt
        self.c3 += dc3 * dt
        self.c1 = max(0, self.c1)
        self.time += dt