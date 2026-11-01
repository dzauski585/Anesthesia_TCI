class Drug:

    def __init__(self, name, V1, k10, k12, k13, k21, k31, ke0,
                 dose_unit="mg", conc_unit="µg/mL"):
        self.name = name
        self.V1 = V1
        self.k10 = k10
        self.k12 = k12
        self.k13 = k13
        self.k21 = k21
        self.k31 = k31
        self.ke0 = ke0
        self.dose_unit = dose_unit
        self.conc_unit = conc_unit

    def __repr__(self):
        return f"Drug({self.name}, V1={self.V1}, k10={self.k10}, k12={self.k12}, k13={self.k13}, k21={self.k21}, k31={self.k31}, ke0={self.ke0})"


def drug_from_clearances(name, V1, V2, V3, Cl1, Cl2, Cl3, ke0, **units):
    
    k10 = Cl1 / V1
    k12 = Cl2 / V1
    k13 = Cl3 / V1
    k21 = Cl2 / V2
    k31 = Cl3 / V3

    return Drug(name, V1, k10, k12, k13, k21, k31, ke0, **units)


def marsh_drug(patient):
    """Marsh B, White M, Morton N, Kenny GN. Pharmacokinetic model driven infusion of propofol in children. Br J Anaesth 1991;67:41–8"""
    V1 = 0.228 * patient.weight    
    return Drug("Propofol (Marsh)", V1, 0.119, 0.112, 0.0419, 0.055, 0.0033, 0.26)


