from Simple_one_compartment.patient import Patient
from Simple_one_compartment.simplePK import SimplePKModel
from Simple_one_compartment.simplePD import simplePD 


class AnesthesiaSimulator:
    def __init__(self, patient: Patient):
        self.patient = patient
        self.pk = SimplePKModel(patient.weight)
        self.pd = simplePD()

 
    def run(self, bolus_mg, infusion_rate_ug_kg_min, duration_min, dt=0.1):
        infusion_rate_ug_min = infusion_rate_ug_kg_min * self.patient.weight
        times, concs, bis_vals = [], [], []
        self.pk.bolus(bolus_mg)  # Give bolus at t=0
        n_steps = int(duration_min / dt)
        for _ in range(n_steps):
            self.pk.update(infusion_rate_ug_min, dt)
            c = self.pk.get_concentration()
            b = self.pd.calculate_bis(c)
            times.append(self.pk.time)
            concs.append(c)
            bis_vals.append(b)
        return {'times': times, 'concentrations': concs, 'bis': bis_vals}
    
