import matplotlib.pyplot as plt
from Simple_one_compartment.patient import Patient
from Simple_one_compartment.AnesthesiaSimulator import AnesthesiaSimulator
 
def plot_simulation(results, title='Propofol Simulation'): 
    fig, axes = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    axes[0].plot(results['times'], results['concentrations'], 'b-', linewidth=1.5)
    axes[0].set_ylabel('Concentration (ug/mL)')
    axes[0].set_title(title)
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(results['times'], results['bis'], 'g-', linewidth=1.5)
    axes[1].axhline(y=40, color='r', linestyle='--', alpha=0.5, label='BIS 40')
    axes[1].axhline(y=60, color='r', linestyle='--', alpha=0.5, label='BIS 60')
    axes[1].set_ylabel('BIS')
    axes[1].set_ylim(0, 105)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    plt.xlabel('Time (min)')
    plt.tight_layout()
    plt.show()


# Create patient and simulator
patient = Patient(age= 50, weight=70, height=170, sex='M')
simulator = AnesthesiaSimulator(patient)

# Run simulation
results = simulator.run(
    bolus_mg=120,
    infusion_rate_ug_kg_min=150, 
    duration_min=60
)

# Pass results directly to plotter
plot_simulation(results, title='Propofol Simulation')

#python -m Simple_one_compartment.visualization