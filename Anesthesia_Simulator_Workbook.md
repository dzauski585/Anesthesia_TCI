# PART 1 — TCI SIMULATOR (Python)

The rule for all of Part 1: **numbers that change per drug live in `pk_models.py`. Math that's the same for every drug lives in `engine.py`.** When you're unsure where something goes, ask: "does this change if I switch drugs?"

---

## Week 1 — A `Drug` class and the Marsh model

**Goal:** `marsh_drug(patient)` returns a `Drug` holding the six Marsh numbers plus `ke0`.

**New concepts (Python):** a plain data class; a *factory function* (a function whose job is to build and return an object); keeping the interface consistent across many drugs.

**Read first:** [Python tutorial: Classes](https://docs.python.org/3/tutorial/classes.html) · [Python tutorial: keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

### Starter code — `pk_models.py`

```python
class Drug:
    """Rate constants for a 3-compartment model with an effect site.
    The engine reads these. It never needs to know which drug this is."""

    def __init__(self, name, V1, k10, k12, k13, k21, k31, ke0,
                 dose_unit="mg", conc_unit="µg/mL"):
        self.name = name
        # TODO: store every argument on self

    def __repr__(self):
        # TODO: one line showing name, V1 and k10 is plenty for debugging
        ...


def drug_from_clearances(name, V1, V2, V3, Cl1, Cl2, Cl3, ke0, **units):
    """Many papers publish volumes + clearances, not rate constants.
    Convert once, here, so no other code ever has to."""
    # Conversion (standard PK):  k10 = Cl1/V1   k12 = Cl2/V1   k13 = Cl3/V1
    #                             k21 = Cl2/V2   k31 = Cl3/V3
    # TODO: compute the five rate constants, then build and return a Drug
    ...


def marsh_drug(patient):
    """Marsh B et al. Br J Anaesth 1991;67:41-48.
    Only V1 scales with weight. The rate constants are FIXED."""
    # Marsh: V1 = 0.228 L/kg × weight
    #        k10 0.119, k12 0.112, k13 0.0419, k21 0.055, k31 0.0033 (/min, fixed)
    #        ke0 0.26 /min
    # TODO: return a Drug built from these
    ...
```

### Your tasks

1. Fill in `Drug.__init__` and `__repr__`.
2. Write `marsh_drug(patient)`.
3. Write `drug_from_clearances`. You won't use it until Week 5, but write it now while the shape is fresh.
4. Create `test_pk_models.py` with two tests:
   - 70 kg → `V1` rounds to 15.96.
   - 70 kg vs 90 kg → `k10` is equal and `V1` is different. This test catches the old bug where weight crept into the rate constants.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>Drug.__init__</code></b>: Hint 1</summary>

Every argument becomes an attribute. The pattern is the same one you used in `Patient`.

</details>
<details>
<summary><b><code>Drug.__init__</code></b>: Hint 2 (nearly the answer)</summary>

```python
self.V1 = V1
self.k10 = k10
# ...one line per argument, including dose_unit and conc_unit
```

</details>

<details>
<summary><b><code>__repr__</code></b>: Hint 1</summary>

It must *return* a string, not print one. f-strings with format specs (`:.2f`) keep it short.

</details>
<details>
<summary><b><code>__repr__</code></b>: Hint 2 (nearly the answer)</summary>

```python
return f"Drug({self.name!r}, V1={self.V1:.2f}, k10={self.k10:.3f})"
```

</details>

<details>
<summary><b><code>drug_from_clearances</code></b>: Hint 1</summary>

Compute five local variables, then call `Drug(...)` with the arguments in the order its `__init__` expects. `**units` passes the unit labels straight through.

</details>
<details>
<summary><b><code>drug_from_clearances</code></b>: Hint 2 (nearly the answer)</summary>

```python
k10 = Cl1 / V1
# ... k12, k13, k21, k31
return Drug(name, V1, k10, k12, k13, k21, k31, ke0, **units)
```

</details>

<details>
<summary><b><code>marsh_drug</code></b>: Hint 1</summary>

Only one line does any arithmetic. Everything else is a literal number from the table.

</details>
<details>
<summary><b><code>marsh_drug</code></b>: Hint 2 (nearly the answer)</summary>

```python
V1 = 0.228 * patient.weight
return Drug("Propofol (Marsh)", V1, 0.119, 0.112, 0.0419, 0.055, 0.0033, ke0=0.26)
```

</details>


### Things to consider

- Why does `marsh_drug` take the whole `Patient` when it only reads `.weight`? Because every drug function will take a `Patient`. Then later code can call `model_fn(patient)` without caring which model it holds. Write `schnider_drug(patient)` in Week 5 and see how nice this is.
- `**units` in the signature collects any extra keyword arguments into a dict and passes them through. Look it up: "python kwargs". It's worth understanding now.
- Comparing floats with `==` is risky. Prefer `round(x, 2) == 15.96` or `abs(x - 15.96) < 1e-6`.

### Checkpoint

| 70 kg Marsh | value |
|---|---|
| V1 | 15.96 L |
| k10 / k12 / k13 | 0.119 / 0.112 / 0.0419 |
| k21 / k31 | 0.055 / 0.0033 |
| 90 kg V1 | 20.52 L (everything else unchanged) |

**References:** Marsh B, White M, Morton N, Kenny GN. Pharmacokinetic model driven infusion of propofol in children. *Br J Anaesth* 1991;67:41–8

---

## Week 2 — The physics: `deriv()`

**Goal:** one function that, given the current state, returns how fast each compartment is changing.

**New concepts (Python):** tuple unpacking; returning several values; testing one function completely on its own before it's buried in a loop.

### Starter code — `engine.py`

```python
def deriv(t, y, drug, rate):
    """Rates of change for [A1, A2, A3, Ce].
    t    : time (min). solve_ivp passes it in, even though we don't use it
    y    : [A1, A2, A3, Ce]  amounts in mg (A) and effect-site conc (Ce)
    drug : a Drug
    rate : current infusion rate into A1 (mg/min)
    """
    A1, A2, A3, Ce = y          # unpack: one name per position
    Cp = A1 / drug.V1

    # The model:
    #   dA1/dt = rate − (k10 + k12 + k13)·A1 + k21·A2 + k31·A3
    #   dA2/dt = k12·A1 − k21·A2
    #   dA3/dt = k13·A1 − k31·A3
    #   dCe/dt = ke0·(Cp − Ce)
    # TODO: one line of Python per equation (the constants live on `drug`)
    # TODO: return all four, in the same order as y
    ...
```

### Your tasks

1. Fill in `deriv`. Use five short lines, one per equation. Don't write one giant expression.
2. In a scratch file, call `deriv(0, [100, 0, 0, 0], marsh_drug(Patient(40, 70, 170, "M")), 0)` and print the result.
3. Turn that into `test_engine.py::test_deriv_bolus`. Allow a tolerance: `abs(dA1 - (-27.29)) < 0.01`.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Reading the constants</b>: Hint 1</summary>

Everything the equations need is an attribute of `drug`: `drug.k10`, `drug.ke0`, and so on.

</details>
<details>
<summary><b>Reading the constants</b>: Hint 2 (nearly the answer)</summary>

```python
dA1 = rate - (drug.k10 + drug.k12 + drug.k13) * A1 + drug.k21 * A2 + drug.k31 * A3
# dA2, dA3 and dCe follow the same pattern
return dA1, dA2, dA3, dCe
```

</details>


### Things to consider

- The return order is a silent contract. `solve_ivp` (next week) matches positions, not names. If you return `(dA1, dA3, dA2, dCe)`, nothing crashes and every result is quietly wrong. That's exactly why this function gets its own test.
- Why does a function take a `t` it never uses? Because `solve_ivp` always calls `deriv(t, y, ...)`. You have to accept the arguments a library hands you.

### Checkpoint

`deriv(0, [100, 0, 0, 0], marsh_70kg, 0)` → **(−27.290, 11.200, 4.190, 1.629)**

**References:** Marsh B et al. *Br J Anaesth* 1991;67:41–8 · Sheiner LB, Stanski DR, Vozeh S, et al. Simultaneous modeling of pharmacokinetics and pharmacodynamics: application to d-tubocurarine. *Clin Pharmacol Ther* 1979;25:358–71 (the effect-site compartment)

---

## Week 3 — The `Simulation` class

**Goal:** schedule boluses and infusions, run 60 minutes, and get `t`, `cp` and `ce` arrays back.

**New concepts (Python):** a class with state built up over several method calls; a list of tuples as an event schedule; NumPy arrays; reading a library's result object (`solve_ivp`).

**Read first:** [NumPy: the absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html) · [SciPy `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)

### Starter code — `engine.py` (add below `deriv`)

```python
import numpy as np
from scipy.integrate import solve_ivp


class Simulation:
    def __init__(self, drug, t_end=60.0, steps_per_min=6):
        self.drug = drug
        self.t_end = t_end
        self.steps_per_min = steps_per_min
        self.schedule = []          # list of (time_min, kind, value)

    def bolus(self, at, dose):
        # TODO: record this event in self.schedule
        ...

    def rate(self, at, dose_per_min):
        # TODO: record this event too, so run() can tell the two kinds apart
        ...

    def _index(self, minute):
        """Convert a time in minutes to a grid index."""
        return round(minute * self.steps_per_min)

    def run(self):
        n = int(self.t_end * self.steps_per_min) + 1
        t = np.linspace(0, self.t_end, n)
        y = [0.0, 0.0, 0.0, 0.0]
        rate = 0.0
        cp = np.zeros(n)
        ce = np.zeros(n)

        for i in range(n):
            # 1. apply any events scheduled at this grid point
            for at, kind, value in self.schedule:
                if self._index(at) == i:
                    # TODO: a bolus is an instant jump in A1; a rate event
                    #       changes the infusion from this moment on
                    ...

            # 2. record output at this grid point
            # TODO: store this grid point's Cp (= A1/V1) and Ce

            # 3. advance to the next grid point (unless this is the last one)
            if i < n - 1:
                sol = solve_ivp(deriv, (t[i], t[i + 1]), y, args=(self.drug, rate))
                # TODO: update y to the state at the END of this short solve
                ...

        self.t, self.cp, self.ce = t, cp, ce
        return self

    def ce_at(self, minute):
        # TODO: return Ce at that minute
        ...
```

### Your tasks

1. Fill in `bolus` and `rate`. Print `sim.schedule` to see what you stored.
2. Before writing the loop, print `len(t)`, `t[0]` and `t[-1]` for the default settings.
3. Fill in the three `TODO` blocks in `run()`.
4. Run the checkpoint schedule below and print `ce_at()` for each minute.
5. Add `test_simulation_checkpoint` to `test_engine.py` (tolerance 0.05).
6. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>bolus</code> / <code>rate</code></b>: Hint 1</summary>

`self.schedule` is a list. Each event is one tuple of three values.

</details>
<details>
<summary><b><code>bolus</code> / <code>rate</code></b>: Hint 2 (nearly the answer)</summary>

```python
self.schedule.append((at, "bolus", dose))
```

</details>

<details>
<summary><b>Applying events</b>: Hint 1</summary>

Check `kind` with an `if`/`else`. A bolus changes the state `y`; a rate event changes the local variable `rate`.

</details>
<details>
<summary><b>Applying events</b>: Hint 2 (nearly the answer)</summary>

```python
if kind == "bolus":
    y[0] += value
else:
    rate = value
```

</details>

<details>
<summary><b>Recording output</b>: Hint 1</summary>

Cp needs the amount in compartment 1 and the drug's V1. Ce is already one of the four state values.

</details>
<details>
<summary><b>Recording output</b>: Hint 2 (nearly the answer)</summary>

```python
cp[i] = y[0] / self.drug.V1
ce[i] = y[3]
```

</details>

<details>
<summary><b>Reading <code>sol.y</code></b>: Hint 1</summary>

Print `sol.y.shape`. Rows are your four variables; columns are time points inside this one short call. You want the last column.

</details>
<details>
<summary><b>Reading <code>sol.y</code></b>: Hint 2 (nearly the answer)</summary>

```python
y = sol.y[:, -1].tolist()
```

</details>

<details>
<summary><b><code>ce_at</code></b>: Hint 1</summary>

Reuse `_index()` to turn minutes into a position in the array.

</details>
<details>
<summary><b><code>ce_at</code></b>: Hint 2 (nearly the answer)</summary>

```python
return self.ce[self._index(minute)]
```

</details>


### Things to consider

- `sol.y` is a 2-D array: rows are your four variables and columns are time points *within that short call*. `sol.y[:, -1]` means "all rows, last column". Print `sol.y.shape` once to see it.
- Why call `solve_ivp` once per grid step instead of once for the whole hour? Because the solver doesn't know a bolus is coming at minute 30. You stop it, apply the event, and restart it.
- `run()` ends with `return self`. That lets you write `sim = Simulation(drug).run()` in one line. That habit is called *method chaining*.
- **Bigger-project habit:** this is the biggest function so far. If it misbehaves, put `print(i, t[i], y, rate)` inside the loop and run only `t_end=2`.

### Checkpoint

80 kg Marsh: bolus 160 mg at 0, rate 13 mg/min from 0, rate 8 from 12, bolus 40 at 30, rate 0 from 45. Default `steps_per_min=6`.

| minute | 1 | 12 | 30 | 45 | 60 |
|---|---|---|---|---|---|
| Ce (µg/mL) | 1.83 | 3.82 | 2.73 | 3.02 | 1.28 |

Also check that `len(t)` is 361 for `t_end=60, steps_per_min=6`.

---

## Week 4 — Plotting, and plugging in your Roberts regimen

**Goal:** a reusable plot function, and a translator that turns `roberts_schedule()` into `Simulation` events.

**New concepts (Python):** matplotlib's `fig, ax` style; default and optional arguments (`None`); writing an *adapter* between two pieces of code whose data have different shapes.

**Read first:** [Matplotlib Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

### Starter code — `plotting.py`

```python
import matplotlib.pyplot as plt

def plot_concentrations(t, cp, ce=None, t_end=None, title=None,
                        conc_unit="µg/mL", save_path=None):
    """Knows nothing about drugs or patients. Only arrays in, picture out."""
    fig, ax = plt.subplots()
    ax.plot(t, cp, label="Cp")
    # TODO: plot Ce as well, but only if it was given
    # TODO: axis labels, legend, optional title, optional x-limit
    # TODO: save to save_path if one was given, otherwise show the window
    return fig, ax
```

### Starter code — `dosing.py`

```python
from roberts import roberts_schedule

def apply_roberts(sim, weight, start=0.0):
    """roberts_schedule() returns RELATIVE durations: [(10, r1), (10, r2), (40, r3)].
    Simulation wants ABSOLUTE start times. Walk a clock forward."""
    bolus_mg, schedule = roberts_schedule(weight)
    current_time = start
    # TODO: give the loading dose at the start time
    # TODO: walk through the segments: start each rate at current_time,
    #       then move current_time forward by that segment's duration
    return sim
```

### Your tasks

1. Write `plot_concentrations`. Feed it the Week 3 checkpoint run and look at the Ce/Cp lag.
2. Print `roberts_schedule(70)` and look at the shape before writing `apply_roberts`.
3. Write `apply_roberts`, run it through a 70 kg Marsh simulation and plot it.
4. Add a test for the Roberts checkpoint.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Plot calls</b>: Hint 1</summary>

Each line is one `ax.plot(x, y, label=...)`. Labels and limits are `ax.set_xlabel`, `ax.set_ylabel`, `ax.set_title`, `ax.set_xlim`, then `ax.legend()`.

</details>
<details>
<summary><b>Plot calls</b>: Hint 2 (nearly the answer)</summary>

```python
if ce is not None:
    ax.plot(t, ce, label="Ce")
...
if save_path:
    fig.savefig(save_path)
else:
    plt.show()
```

</details>

<details>
<summary><b><code>apply_roberts</code> loop</b>: Hint 1</summary>

Unpack each `(duration, rate)` tuple directly in the `for` line. Inside the loop: schedule, *then* advance.

</details>
<details>
<summary><b><code>apply_roberts</code> loop</b>: Hint 2 (nearly the answer)</summary>

```python
sim.bolus(current_time, bolus_mg)
for duration, rate in schedule:
    sim.rate(current_time, rate)
    current_time += duration
```

</details>


### Things to consider

- `if ce is not None:`, not `if ce:`. A NumPy array in an `if` raises an error ("truth value of an array is ambiguous"). Try it once so you recognize the message.
- In `apply_roberts`, does the order "record the rate, then advance the clock" matter? Swap the two lines and see what changes.
- Keep `plotting.py` free of `import patient` or any drug names. In Part 4 you'll swap the picture for a web chart, and the less this file knows, the easier that is.

### Checkpoint

Roberts (1 mg/kg, then 10 → 8 → 6 mg/kg/h) through 70 kg Marsh:

| t (min) | 1 | 10 | 20 | 40 | 60 |
|---|---|---|---|---|---|
| Cp | 3.99 | 3.22 | 2.98 | 2.66 | 2.75 |
| Ce | 0.95 | 3.05 | 2.98 | 2.64 | 2.74 |

**References:** Roberts FL, Dixon J, Lewis GT, Tackley RM, Prys-Roberts C. Induction and maintenance of propofol anaesthesia: a manual infusion scheme. *Anaesthesia* 1988;43 Suppl:14–17

---

## Week 5 — More drugs: Schnider, Minto, Eleveld

**Goal:** three new model functions, and a comparison script that shows why the choice of model matters.

**New concepts (Python):** translating multi-term published formulas safely; a dictionary as a *registry* (`{"Marsh": marsh_drug, ...}`); functions stored in variables; `.max()` and `.argmax()`.

### Starter code — add to `pk_models.py`

```python
def schnider_drug(patient):
    """Schnider TW et al. Anesthesiology 1998;88:1170-82 / 1999;90:1502-16."""
    age, wt, ht, lbm = patient.age, patient.weight, patient.height, patient.lbm
    V1, V3, Cl3 = 4.27, 238.0, 0.836                # fixed
    V2  = 18.9 - 0.391 * (age - 53)
    Cl2 = 1.29 - 0.024 * (age - 53)
    # Build Cl1 from NAMED terms. Long one-liners hide typos.
    weight_term = 0.0456 * (wt - 77)
    lbm_term    = 0.0681 * (lbm - 59)
    height_term = 0.0264 * (ht - 177)
    # TODO: Cl1 = 1.89 + weight_term - lbm_term + height_term
    # TODO: convert to a Drug with your Week 1 helper (Schnider ke0 = 0.456 /min)
    ...


def minto_drug(patient):
    """Minto CF et al. Anesthesiology 1997;86:10-23. Remifentanil: µg in, ng/mL out."""
    age_d = patient.age - 40
    lbm_d = patient.lbm - 55
    # Minto covariate model:
    #   V1  = 5.1   − 0.0201·age_d + 0.072·lbm_d      V3  = 5.42 (fixed)
    #   V2  = 9.82  − 0.0811·age_d + 0.108·lbm_d
    #   Cl1 = 2.6   − 0.0162·age_d + 0.0191·lbm_d
    #   Cl2 = 2.05  − 0.0301·age_d
    #   Cl3 = 0.076 − 0.00113·age_d
    #   ke0 = 0.595 − 0.007·age_d
    # TODO: compute all seven, then convert to a Drug.
    #       Remifentanil doses are µg and concentrations ng/mL, so set the unit labels.
    ...


def eleveld_drug_reference():
    """Eleveld DJ et al. Br J Anaesth 2018;120:942-959, reference individual ONLY
    (35 yo, 70 kg, 170 cm, male, no opioids). Read Table 2 of the paper before
    extending to other patients: it has ~30 covariate constants."""
    # Reference values: V1 6.28, V2 25.5, V3 273 (L); CL 1.79, Q2 1.75, Q3 1.11 (L/min); ke0 0.146 /min
    # (Q2 and Q3 are Eleveld's names for Cl2 and Cl3.)
    # TODO: return a Drug built from these
    ...


MODELS = {
    "Propofol": {"Marsh": marsh_drug, "Schnider": schnider_drug},
    "Remifentanil": {"Minto": minto_drug},
}
```

### Your tasks

1. Write `schnider_drug`. Before returning, print the three Cl1 terms for the reference patient. They should all be about zero except the LBM term.
2. Write `minto_drug` and `eleveld_drug_reference`, each with a test.
3. Write `compare.py` (a script, not a module). Run the *same* dose (150 mg bolus + 10 mg/min, dropping to 6 mg/min at minute 20) through Marsh and Schnider for Patient A. Print the peak Ce and time-to-peak for each, and overlay both Ce curves on one `ax`.
4. Write a small helper `peak_and_time(t, ce)` that returns `(ce.max(), t[ce.argmax()])`.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Finishing <code>schnider_drug</code></b>: Hint 1</summary>

The last line hands six numbers and a ke0 to `drug_from_clearances`, in the order its signature lists them.

</details>
<details>
<summary><b>Finishing <code>schnider_drug</code></b>: Hint 2 (nearly the answer)</summary>

```python
Cl1 = 1.89 + weight_term - lbm_term + height_term
return drug_from_clearances("Propofol (Schnider)", V1, V2, V3, Cl1, Cl2, Cl3, ke0=0.456)
```

</details>

<details>
<summary><b>Minto units</b>: Hint 1</summary>

Keyword arguments after the numbers go into `**units`.

</details>
<details>
<summary><b>Minto units</b>: Hint 2 (nearly the answer)</summary>

```python
return drug_from_clearances("Remifentanil (Minto)", V1, V2, V3, Cl1, Cl2, Cl3, ke0,
                            dose_unit="µg", conc_unit="ng/mL")
```

</details>

<details>
<summary><b><code>peak_and_time</code></b>: Hint 1</summary>

`.max()` gives the biggest value; `.argmax()` gives *where* it is, an index you can use on `t`.

</details>
<details>
<summary><b><code>peak_and_time</code></b>: Hint 2 (nearly the answer)</summary>

```python
return ce.max(), t[ce.argmax()]
```

</details>

<details>
<summary><b>Overlay</b>: Hint 1</summary>

Create one `fig, ax` and call `ax.plot` once per model, each with its own `label`. Don't call `plot_concentrations` twice, because that makes two figures.

</details>


### Things to consider

- Did `engine.py` need any changes for the new drugs? It shouldn't. If you had to edit it, something Marsh-specific leaked in.
- The registry lets later code do `MODELS["Propofol"]["Schnider"](patient)`. You're storing *functions* in a dict, without calling them. Notice there are no parentheses until you use them.
- The James LBM formula (which Schnider uses) behaves badly in obesity: past a certain BMI, LBM goes *down* as weight goes up. Try `Patient(40, 150, 165, "F").lbm`. This is a well-known Schnider limitation, and one reason Eleveld exists.
- For the overlay, use `steps_per_min=60` so the time-to-peak isn't rounded to the nearest 10 seconds.

### Checkpoint

| | value |
|---|---|
| Schnider k10, reference body (53 yo, 77 kg, 177 cm, M) | **0.419 /min** |
| Schnider k10, Patient A | **0.384 /min** |
| Minto, 40 yo M 65 kg 170 cm (LBM 52.79) | V1 4.94 L, Cl1 2.56, k10 0.518, ke0 0.595 |
| Eleveld reference | k10 0.2850, k12 0.2787, k21 0.0686, k13 0.1768, k31 0.00407 |
| Marsh vs Schnider peak Ce (Patient A, `steps_per_min=60`) | **4.24 at 5.5 min** vs **9.32 at 1.7 min** |

That last row is the lesson of the week. Schnider's fixed 4.27 L central volume is much smaller than Marsh's ~16 L, so the same bolus gives a peak twice as high and much sooner.

**References:** Schnider TW et al. The influence of method of administration and covariates on the pharmacokinetics of propofol in adult volunteers. *Anesthesiology* 1998;88:1170–82 · Schnider TW et al. The influence of age on propofol pharmacodynamics. *Anesthesiology* 1999;90:1502–16 · Minto CF et al. Influence of age and gender on the pharmacokinetics and pharmacodynamics of remifentanil. I. Model development. *Anesthesiology* 1997;86:10–23 · Eleveld DJ, Colin P, Absalom AR, Struys MMRF. Pharmacokinetic–pharmacodynamic model for propofol for broad application in anaesthesia and sedation. *Br J Anaesth* 2018;120:942–59

---

## Week 6 — Pharmacodynamics: probability of no response

**Goal:** turn Ce curves into "probability this patient tolerates laryngoscopy".

**New concepts (Python):** *vectorization*: a function written with plain `+ - * / **` works on whole NumPy arrays with no loop.

### Starter code — `pd_endpoints.py`

```python
def p_single(ce, c50, gamma):
    """Hill curve: probability of the drug effect at concentration ce.
        P = Ce^γ / (C50^γ + Ce^γ)
    """
    # TODO: translate the formula (Python writes 'to the power' as **)
    ...

def p_event(ce_p, ce_r, c50_p, c50_r, alpha, gamma):
    """Greco interaction surface for propofol + remifentanil.
    alpha > 0 synergy, alpha = 0 additive, alpha < 0 antagonism."""
    up = ce_p / c50_p
    ur = ce_r / c50_r
    # Greco:  U = UP + UR + α·UP·UR        P = U^γ / (1 + U^γ)
    # TODO: combine the two drugs into U, then return P
    ...
```

### Your tasks

1. Write both functions and test them with plain numbers (checkpoint below).
2. Run a propofol `Simulation` (Schnider) and a remifentanil `Simulation` (Minto) with the **same** `t_end` and `steps_per_min`.
3. Call `p_event(sim_p.ce, sim_r.ce, 3.0, 3.0, 3.0, 4.0)` **once**, passing whole arrays, and plot probability against time.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Hill and Greco in Python</b>: Hint 1</summary>

`^` is `**` in Python. Parentheses matter: `c50**gamma + ce**gamma` is all one denominator.

</details>
<details>
<summary><b>Hill and Greco in Python</b>: Hint 2 (nearly the answer)</summary>

```python
return ce**gamma / (c50**gamma + ce**gamma)
# Greco:
u = up + ur + alpha * up * ur
return u**gamma / (1 + u**gamma)
```

</details>

<details>
<summary><b>Arrays in, array out</b>: Hint 1</summary>

Don't write a loop. Pass `sim_p.ce` and `sim_r.ce` straight in. NumPy does the arithmetic element by element.

</details>


### Things to consider

- Why must both simulations share `t_end` and `steps_per_min`? Index 47 of one array has to mean the same moment as index 47 of the other. What error do you get if they're different lengths?
- These C50/γ/α values are illustrative teaching anchors. Published surfaces (Bouillon 2004, Kern 2004, Johnson 2008) differ. Put that sentence in your docstring.

### Checkpoint

- `p_single(2.0, 2.8, 1.5)` ≈ **0.38**, and `p_single(3.5, 2.8, 1.5)` ≈ **0.58**
- `p_event(1.5, 1.5, 3, 3, 3, 4)` ≈ **0.90**. With `alpha=0`, it's **0.50**.
- `p_event(3, 0, 3, 3, 3, 4)` = **0.50**. Either drug alone at its C50 gives 50%; half of each, with synergy, gives 90%.

**References:** Bouillon TW et al. Pharmacodynamic interaction between propofol and remifentanil regarding hypnosis, tolerance of laryngoscopy, bispectral index, and electroencephalographic approximate entropy. *Anesthesiology* 2004;100:1353–72 · Kern SE, Xie G, White JL, Egan TD. Opioid–hypnotic synergy: a response surface analysis of propofol–remifentanil pharmacodynamic interaction in volunteers. *Anesthesiology* 2004;100:1373–81 · Johnson KB, Syroid ND, et al. An evaluation of remifentanil–propofol response surfaces for loss of responsiveness, loss of response to surrogates of painful stimuli and laryngoscopy. *Anesth Analg* 2008;106:471–9 · Greco WR, Bravo G, Parsons JC. The search for synergy: a critical review from a response surface perspective. *Pharmacol Rev* 1995;47:331–85

---

## Week 7 — Wake-up prediction, and saving results to JSON

**Goal:** predict minutes-to-wake after an infusion stops, and save any simulation to a file a web page can read later.

**New concepts (Python):** returning `None` as a meaningful answer; replaying data onto a new object; the `json` module; why NumPy arrays need `.tolist()`.

**Read first:** [Python `json` module](https://docs.python.org/3/library/json.html) · [`pathlib`](https://docs.python.org/3/library/pathlib.html)

### Starter code — `wake.py`

```python
from engine import Simulation

def time_to_wake(old_sim, stop_time, wake_threshold, extra_minutes=180):
    """Replay old_sim's schedule, switch everything off at stop_time,
    and return minutes from stop until Ce < threshold (or None)."""
    new_sim = Simulation(old_sim.drug, t_end=stop_time + extra_minutes,
                         steps_per_min=old_sim.steps_per_min)
    for at, kind, value in old_sim.schedule:
        # TODO: re-add each event with the matching method
        ...
    # TODO: switch every infusion off at stop_time, then run the new simulation
    # TODO: find the first moment AFTER stop_time when Ce drops below the threshold,
    #       and return how many minutes after stopping that was
    return None   # never woke inside the window
```

### Starter code — `export.py`

```python
import json
from pathlib import Path

def save_sim_json(sim, path, label=""):
    data = {
        "label": label,
        "drug": sim.drug.name,
        "conc_unit": sim.drug.conc_unit,
        # TODO: "t": ..., "cp": ..., "ce": ...   (json can't save numpy arrays directly)
    }
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    # TODO: write `data` to the file as JSON
```

### Your tasks

1. Write `time_to_wake` and run the context-sensitivity experiment below.
2. Write `save_sim_json`. Save the Roberts run to `web/data/roberts_70kg.json`, then open the file in your editor and look at it. That plain text is what JavaScript will read in Week 24.
3. Commit, then write a `DEVLOG.md` entry summarizing all of Part 1.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Replaying events</b>: Hint 1</summary>

Read `kind` and call the matching method.

</details>
<details>
<summary><b>Replaying events</b>: Hint 2 (nearly the answer)</summary>

```python
if kind == "bolus":
    new_sim.bolus(at, value)
else:
    new_sim.rate(at, value)
```

</details>

<details>
<summary><b>Scanning for the crossing</b>: Hint 1</summary>

Convert `stop_time` to an index (you did this in Week 3), then walk forward with `range(start, len(new_sim.t))`. `return` inside the loop stops at the first hit.

</details>
<details>
<summary><b>Scanning for the crossing</b>: Hint 2 (nearly the answer)</summary>

```python
new_sim.rate(stop_time, 0.0)
new_sim.run()
start = new_sim._index(stop_time)
for i in range(start, len(new_sim.t)):
    if new_sim.ce[i] < wake_threshold:
        return new_sim.t[i] - stop_time
```

</details>

<details>
<summary><b>Writing JSON</b>: Hint 1</summary>

NumPy arrays need `.tolist()` first. Open the file with `with` so it closes itself.

</details>
<details>
<summary><b>Writing JSON</b>: Hint 2 (nearly the answer)</summary>

```python
"t": sim.t.tolist(), "cp": sim.cp.tolist(), "ce": sim.ce.tolist(),
...
with open(path, "w") as f:
    json.dump(data, f, indent=2)
```

</details>


### Things to consider

- Why not keep running the *old* simulation further? `run()` always rebuilds from t=0 with a fixed `t_end`. Replaying events onto a new object is cleaner than making `run()` resumable.
- `None` means "won't wake in the simulated window". Make sure the caller handles it. `print(f"{result:.1f}")` crashes on `None`.
- Try `json.dump({"x": np.array([1, 2])}, f)` once on purpose, so you recognize the error.

### Checkpoint

70 kg Marsh, 100 mg bolus + 10 mg/min, wake threshold Ce = 1.2 µg/mL:

| infusion length | minutes to wake after stopping |
|---|---|
| 5 min | **≈ 10.7** |
| 120 min | **≈ 30.8** |

Same drug, same rate, same threshold: only the duration changed. That's context sensitivity, and no half-life formula appears anywhere in your code.

**References:** Hughes MA, Glass PSA, Jacobs JR. Context-sensitive half-time in multicompartment pharmacokinetic models for intravenous anesthetic drugs. *Anesthesiology* 1992;76:334–41 · Bailey JM. Context-sensitive half-times: what are they and how valuable are they in anaesthesiology? *Clin Pharmacokinet* 2002;41:793–9

---

# PART 2 — ANESTHESIA MACHINE (Python)

Same habits as Part 1, with a new idea: a **time-stepping** model. Part 1 handed the math to `solve_ivp`. Here you write the stepping yourself (simple Euler steps), which makes every equation visible.

All concentrations are in **%** (volume percent, i.e. partial pressure). Time is in **minutes**, and `dt = 0.1/60` is a 0.1-second step.

---

## Week 8 — `Agent` and `Compartment`

**Goal:** an agent library, and one tissue compartment that exchanges gas with blood.

**New concepts (Python):** `@dataclass` (a class that's mostly data); a regular class for something with changing state; a dict of objects as a lookup table.

**Read first:** [Python `dataclasses`](https://docs.python.org/3/library/dataclasses.html)

### Starter code — `agents.py`

```python
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    mac: float              # %, young adult
    blood_gas: float        # λ blood:gas
    brain_blood: float      # λ VRG:blood
    muscle_blood: float
    fat_blood: float

    def mac_multiple(self, partial_pressure: float) -> float:
        # TODO: how many MACs is this partial pressure? (don't divide by zero)
        ...

AGENTS = {
    "sevoflurane":   Agent("Sevoflurane",   2.0,  0.65, 1.7, 3.1, 48),
    "isoflurane":    Agent("Isoflurane",    1.15, 1.46, 1.6, 2.9, 45),
    # TODO: desflurane    6.0, 0.42, 1.3, 2.0, 27
    # TODO: nitrous_oxide 104, 0.47, 1.1, 1.2, 2.3
}
```

### Starter code — `compartment.py`

```python
class Compartment:
    """dC/dt = (Q/V) * (C_arterial - C/λ)
    C is TISSUE concentration. C/λ is the tissue's partial pressure,
    the number you can compare with alveolar %."""

    def __init__(self, name, volume_L, blood_flow_Lmin):
        self.name = name
        self.volume = volume_L
        self.blood_flow = blood_flow_Lmin
        self.concentration = 0.0

    def partial_pressure(self, lam):
        # TODO
        ...

    def rate_of_change(self, c_arterial, lam):
        # TODO
        ...

    def update(self, c_arterial, lam, dt):
        # TODO: Euler step, then clamp at >= 0
        ...

    def reset(self):
        self.concentration = 0.0


def create_compartments():
    return {
        "VRG":    Compartment("Vessel-rich group", 6.0, 4.2),
        "muscle": Compartment("Muscle",           33.0, 0.9),
        "fat":    Compartment("Fat",              14.5, 0.35),
    }
```

### Your tasks

1. Finish both files. Notice that `@dataclass` writes `__init__` and `__repr__` for you: `print(AGENTS["sevoflurane"])`.
2. Write `test_compartment.py` using the checkpoint below.
3. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>mac_multiple</code></b>: Hint 1</summary>

Two lines: an `if` that returns 0 for `mac == 0`, then the division.

</details>

<details>
<summary><b><code>Compartment</code> methods</b>: Hint 1</summary>

`partial_pressure` is concentration ÷ λ. `rate_of_change` is (Q/V) × (arterial − partial pressure). `update` multiplies the rate by `dt`, adds it, and clamps with `max(0, ...)`.

</details>
<details>
<summary><b><code>Compartment</code> methods</b>: Hint 2 (nearly the answer)</summary>

```python
def rate_of_change(self, c_arterial, lam):
    return (self.blood_flow / self.volume) * (c_arterial - self.partial_pressure(lam))
```

</details>


### Things to consider

- Why doesn't `Compartment` store which agent it holds? Because the same compartment object works for any agent if λ is passed in. Less stored state means fewer ways to get out of sync.
- **Units trap (a bug in the old workbook):** a VRG *tissue* concentration of 3.4 at equilibrium with 2% alveolar doesn't mean the brain is at 1.7 MAC. Divide by λ first: 3.4 / 1.7 = 2.0% partial pressure = 1.0 MAC. That's why `partial_pressure()` exists.

### Checkpoint

- VRG, sevo (λ 1.7), arterial 2.0%, empty tissue: `rate_of_change` = **1.4 %/min**
- VRG at concentration 3.4: rate ≈ **0**, and `partial_pressure(1.7)` = **2.0**
- `AGENTS["sevoflurane"].mac_multiple(2.6)` = **1.3**

**References:** Eger EI, Saidman LJ, Brandstater B. Minimum alveolar anesthetic concentration: a standard of anesthetic potency. *Anesthesiology* 1965;26:756–63 · Yasuda N, Lockhart SH, Eger EI II, et al. Comparison of kinetics of sevoflurane and isoflurane in humans. *Anesth Analg* 1991;72:316–24 · Philip JH. Gas Man: an example of goal-oriented computer-assisted teaching which results in learning. *Int J Clin Monit Comput* 1986;3:165–73

---

## Week 9 — The gas-exchange engine: `step()`

**Goal:** a `VolatilePKModel` that advances the whole body by one time step.

**New concepts (Python):** `@property` (a value computed when you read it, so it can never be stale); breaking a long method into small private helper methods, which is *the* key skill for bigger projects.

**Read first:** [Python `property`](https://docs.python.org/3/library/functions.html#property)

### The five equations, in order (each needs the one before it)

1. Mixed venous: `Cv = Σ(Qᵢ · Cᵢ/λᵢ) / Q_total`
2. Inspired: if FGF ≥ MV, `FI = dial`. Otherwise `FI = (FGF·dial + (MV−FGF)·circuit) / MV`
3. Uptake: `U = CO · λ_blood:gas · (FA − Cv)`
4. Alveolar: `dFA/dt = (VA·(FI − FA) − U) / FRC`
5. Tissues: each compartment's `update(FA, λ, dt)`, using the **new** FA

### Starter code — `volatile.py`

```python
from compartment import create_compartments

class VolatilePKModel:
    def __init__(self, agent):
        self.agent = agent
        self.compartments = create_compartments()
        self.alveolar = 0.0
        self.circuit = 0.0
        self.dial = 0.0
        self.fresh_gas_flow = 6.0       # becomes a property in Week 11
        self.resp_rate = 14
        self.tidal_volume = 0.5
        self.FRC = 2.5
        self.dead_space_fraction = 0.3
        self.time = 0.0
        self.last_uptake = 0.0
        self.extra_alveolar_rate = 0.0  # hook for the second gas effect (Week 10)

    # ---- derived values: computed on read, never stored ----
    @property
    def minute_ventilation(self):
        return self.resp_rate * self.tidal_volume

    @property
    def cardiac_output(self):
        # Sum of tissue flows, so CO and the compartments can never disagree
        # (the old workbook used 5.0 while the flows summed to 5.45).
        # TODO
        ...

    def _lambda_for(self, name):
        # TODO: "VRG" -> brain_blood, "muscle" -> muscle_blood, "fat" -> fat_blood
        ...

    # ---- one helper per equation keeps step() readable ----
    def _mixed_venous(self):
        # TODO: equation 1
        ...

    def _inspired(self):
        # TODO: equation 2
        ...

    def step(self, dt):
        VA = self.minute_ventilation * (1 - self.dead_space_fraction)
        cv = self._mixed_venous()
        fi = self._inspired()
        # TODO: equation 3 -> self.last_uptake
        # TODO: equation 4 (add self.extra_alveolar_rate inside dFA/dt), clamp >= 0
        # TODO: equation 5, loop over compartments
        self.circuit = self.alveolar        # simplification: rebreathed gas = alveolar
        self.time += dt

    def brain_partial_pressure(self):
        # TODO: VRG concentration / brain λ
        ...

    def get_mac_values(self):
        # TODO: {"alveolar": ..., "brain": ...} as MAC multiples (use partial pressures!)
        ...

    def reset(self):
        # TODO
        ...
```

### Your tasks

1. Write the two properties and `_lambda_for`. Check that `cardiac_output` is 5.45.
2. Write `_mixed_venous` and `_inspired`. Test each on its own with hand-picked compartment values before writing `step()`.
3. Finish `step()`.
4. Write `run_washin.py`: sevo at 2%, FGF 8, run 5 minutes printing every minute, then dial 0 for 5 more minutes.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>cardiac_output</code></b>: Hint 1</summary>

Loop over `self.compartments.values()` and add up `blood_flow`. A generator inside `sum()` does it in one line.

</details>
<details>
<summary><b><code>cardiac_output</code></b>: Hint 2 (nearly the answer)</summary>

```python
return sum(c.blood_flow for c in self.compartments.values())
```

</details>

<details>
<summary><b><code>_mixed_venous</code></b>: Hint 1</summary>

For each `name, comp` in `self.compartments.items()`: flow × partial pressure, with λ from `self._lambda_for(name)`. Then divide by the total flow.

</details>
<details>
<summary><b><code>_mixed_venous</code></b>: Hint 2 (nearly the answer)</summary>

```python
total = 0.0
for name, comp in self.compartments.items():
    total += comp.blood_flow * comp.partial_pressure(self._lambda_for(name))
return total / self.cardiac_output
```

</details>

<details>
<summary><b><code>_inspired</code></b>: Hint 1</summary>

An `if`/`else` on `self.fresh_gas_flow >= self.minute_ventilation`. The `else` branch is the rebreathing formula (equation 2).

</details>

<details>
<summary><b><code>step()</code> equations 3–5</b>: Hint 1</summary>

Equation 4 has two parts inside the brackets, plus `self.extra_alveolar_rate` added to dFA/dt. Use the *new* `self.alveolar` when you update the tissues.

</details>
<details>
<summary><b><code>step()</code> equations 3–5</b>: Hint 2 (nearly the answer)</summary>

```python
self.last_uptake = self.cardiac_output * self.agent.blood_gas * (self.alveolar - cv)
dFA = (VA * (fi - self.alveolar) - self.last_uptake) / self.FRC + self.extra_alveolar_rate
self.alveolar = max(0.0, self.alveolar + dFA * dt)
for name, comp in self.compartments.items():
    comp.update(self.alveolar, self._lambda_for(name), dt)
```

</details>

<details>
<summary><b><code>get_mac_values</code></b>: Hint 1</summary>

Both entries go through `self.agent.mac_multiple(...)`. The brain one uses `self.brain_partial_pressure()`, not the raw VRG concentration.

</details>


### Things to consider

- Reorder equations 3 and 4, or update tissues before the alveolus, and the code still runs. It just gives subtly wrong curves. The helper-method layout makes the order easy to see.
- A 1-minute run is `int(1 / dt)` = 600 steps. Write a small `run_minutes(model, minutes, dt)` helper so you never type that loop again.
- To model low cardiac output (shock), would you change `cardiac_output`? You can't, because it's a read-only property. You'd scale every compartment's `blood_flow`. Think about why that's more honest.

### Checkpoint

Sevo 2%, FGF 8 L/min, RR 14, TV 0.5 (MV 7), `dt = 0.1/60`. Tissue columns are *tissue* concentrations.

| min | FA | VRG | muscle | fat |
|---|---|---|---|---|
| 1 | 1.186 | 0.509 | 0.023 | 0.021 |
| 3 | 1.425 | 1.503 | 0.094 | 0.085 |
| 5 | 1.549 | 2.091 | 0.174 | 0.156 |
| *dial → 0* | | | | |
| 6 | 0.404 | 1.778 | 0.191 | 0.174 |
| 10 | 0.133 | 0.621 | 0.210 | 0.196 |

Look at the behavior during washout: VRG falls more slowly than FA, while muscle and fat are **still rising**. At 5 minutes, brain partial pressure = 2.091 / 1.7 ≈ **1.23%** ≈ 0.62 MAC. Low flow matters too: the same run at FGF 1 L/min gives FA ≈ **0.562** at 5 minutes instead of 1.549.

**References:** Philip JH. *Gas Man: Understanding Anesthesia Uptake and Distribution*. Med Man Simulations (gasmanweb.com) · Eger EI II. The effect of inspired anesthetic concentration on the rate of rise of alveolar concentration. *Anesthesiology* 1963;24:153–7 · Eger EI II. *Anesthetic Uptake and Action*. Williams & Wilkins; 1974

---

## Week 10 — Two agents: MAC additivity and a correct second gas effect

**Goal:** sevo + N₂O running together, total MAC, and a second gas effect that behaves sensibly.

**New concepts (Python):** *composition* (one object holding two others); why any "per-step" adjustment must scale with `dt`.

### Starter code — `dual.py`

```python
from agents import AGENTS
from volatile import VolatilePKModel

class DualAgentModel:
    def __init__(self, volatile_agent, use_second_gas=True):
        self.volatile = VolatilePKModel(volatile_agent)
        self.n2o = VolatilePKModel(AGENTS["nitrous_oxide"])
        self.use_second_gas = use_second_gas

    def set_dials(self, volatile_pct, n2o_pct):
        # TODO
        ...

    def step(self, dt):
        self.n2o.step(dt)
        if self.use_second_gas:
            # N2O leaving the alveoli shrinks alveolar gas volume and concentrates
            # what's left. last_uptake is in %·L/min, so /100 gives L/min of gas.
            n2o_L_per_min = max(0.0, self.n2o.last_uptake) / 100
            # Concentrating rate (%/min) = FA_volatile × U_N2O (L/min) / FRC
            # TODO: store it where the volatile model's step() will pick it up
            ...
        else:
            self.volatile.extra_alveolar_rate = 0.0
        self.volatile.step(dt)

    def total_mac(self):
        # TODO: alveolar MAC of volatile + alveolar MAC of N2O
        ...
```

### Your tasks

1. Finish `dual.py`. Run sevo 1% + N₂O 50% for 10 minutes, once with the second gas effect on and once with it off.
2. Plot volatile FA for both runs on one axis.
3. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Second gas effect line</b>: Hint 1</summary>

The volatile model already adds `extra_alveolar_rate` inside its dFA/dt (Week 9). You only need to set that attribute.

</details>
<details>
<summary><b>Second gas effect line</b>: Hint 2 (nearly the answer)</summary>

```python
self.volatile.extra_alveolar_rate = self.volatile.alveolar * n2o_L_per_min / self.volatile.FRC
```

</details>

<details>
<summary><b><code>total_mac</code></b>: Hint 1</summary>

Call `get_mac_values()` on each sub-model and add the two `"alveolar"` entries.

</details>


### Things to consider

- **Why the old version exploded:** it did `alveolar *= 1 + uptake*0.01` every 0.1 s. With N₂O uptake around 40, that's ×1.4 six hundred times a minute, and sevo went to infinity within 3 minutes. Anything that happens "per step" must be a *rate* multiplied by `dt`, or changing `dt` changes the physics. Here the rate goes into dFA/dt, and `step()` multiplies by `dt` for you.
- This is still a teaching simplification. Modern work (Korman & Mapleson 1997; Hendrickx 2006) suggests the alveolar second gas effect is smaller than the classic diagram implies. Say so in a docstring.
- MAC additivity only applies to *inhaled* agents. Remember this for Week 25.

### Checkpoint

Sevo 1% + N₂O 50%, FGF 8:

| min | sevo FA, no SGE | sevo FA, with SGE | total MAC (with SGE) |
|---|---|---|---|
| 1 | 0.593 | 0.633 | 0.635 |
| 3 | 0.713 | 0.761 | 0.770 |
| 10 | 0.841 | 0.878 | 0.873 |

The second gas effect is visible but modest, and it **stays finite**.

**References:** Epstein RM, Rackow H, Salanitre E, Wolf GL. Influence of the concentration effect on the uptake of anesthetic mixtures: the second gas effect. *Anesthesiology* 1964;25:364–71 · Stoelting RK, Eger EI II. An additional explanation for the second gas effect: a concentrating effect. *Anesthesiology* 1969;30:273–7 · Taheri S, Eger EI II. A demonstration of the concentration and second gas effects in humans anesthetized with nitrous oxide and desflurane. *Anesth Analg* 1999;89:774–80 · Korman B, Mapleson WW. Concentration and second gas effects: can the accepted explanation be improved? *Br J Anaesth* 1997;78:618–25 · Hendrickx JFA, Carette R, Lemmens HJM, De Wolf AM. Large volume N₂O uptake alone does not explain the second gas effect of N₂O on sevoflurane during constant inspired ventilation. *Br J Anaesth* 2006;96:391–5

---

## Week 11 — Oxygen, FiO₂ and the hypoxic guard

**Goal:** fresh gas made of O₂ + air + N₂O flows; delivered vs inspired FiO₂; low-flow O₂ sag; alarms.

**New concepts (Python):** module-level functions and constants; replacing a stored attribute with a `@property` *without breaking older code*. `fresh_gas_flow` becomes derived, and Week 9's `_inspired()` keeps working unchanged.

### Starter code — `oxygen.py`

```python
O2_FRACTION = {"o2": 1.00, "air": 0.21, "n2o": 0.00}

def fresh_gas_fio2(o2_flow, air_flow, n2o_flow):
    """FiO2 = (Q_O2·1.00 + Q_air·0.21 + Q_N2O·0.00) / (Q_O2 + Q_air + Q_N2O)"""
    total = o2_flow + air_flow + n2o_flow
    if total <= 0:
        return 0.0
    # TODO: flow-weighted O2 fraction (O2_FRACTION has the three numbers)
    ...

def flows_for_target_fio2(target, total_flow):
    """Return (o2_flow, air_flow, feasible). Below 0.21 is impossible with O2+air.
        Q_O2 = Q_total·(target − 0.21) / (1.00 − 0.21)      Q_air = Q_total − Q_O2
    """
    # TODO: handle the impossible case first (all air, feasible = False)
    # TODO: otherwise compute both flows and return all three values
    ...

def fresh_gas_hypoxic(o2_flow, air_flow, n2o_flow, min_fio2=0.25):
    # TODO
    ...

def inspired_hypoxic(circuit_fio2, min_fio2=0.25):
    # TODO
    ...
```

### Changes to `volatile.py`

```python
# in __init__: delete self.fresh_gas_flow = 6.0 and add
self.o2_flow, self.air_flow, self.n2o_flow = 2.0, 0.0, 0.0
self.circuit_fio2 = 0.95       # after preoxygenation
self.V_system = 7.0            # circuit + FRC, treated as one well-mixed volume
self.vo2 = 0.25                # L/min O2 consumption
self.use_o2_consumption = True

@property
def fresh_gas_flow(self):
    # TODO: sum of the three flows
    ...

def _update_fio2(self, dt):
    # d(FiO2)/dt = [Q·(FiO2_freshgas − FiO2_circuit) − VO2] / V_system
    # TODO: compute, Euler-step, clamp to [0, 1]
    ...
# and call self._update_fio2(dt) at the end of step()
```

### Your tasks

1. Write `oxygen.py` with tests for every function.
2. Convert `fresh_gas_flow` to a property and rerun **all** your Week 9–10 tests. Any test that does `model.fresh_gas_flow = 8` will now fail with `AttributeError: property ... has no setter`. Good: the tests just told you exactly what broke. Fix it one of two ways: change those tests to set `o2_flow = 8`, or add a `@fresh_gas_flow.setter` that puts the whole value into `o2_flow`. Look up "python property setter". Then rerun until everything passes. That's the payoff of having tests.
3. Write `run_fio2.py`: start at 95%, set the flows for a 30% target at 2 L/min, run 30 minutes with consumption on and off, and plot both.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>fresh_gas_fio2</code></b>: Hint 1</summary>

Multiply each flow by its entry in `O2_FRACTION`, add the three products, and divide by `total`.

</details>

<details>
<summary><b><code>flows_for_target_fio2</code></b>: Hint 1</summary>

Return a tuple of three things in both branches, so callers can always unpack `o2, air, ok = ...`.

</details>
<details>
<summary><b><code>flows_for_target_fio2</code></b>: Hint 2 (nearly the answer)</summary>

```python
if target < 0.21:
    return 0.0, total_flow, False
o2 = total_flow * (target - 0.21) / (1 - 0.21)
return o2, total_flow - o2, True
```

</details>

<details>
<summary><b><code>_update_fio2</code></b>: Hint 1</summary>

Same shape as a compartment update: rate × `dt`, add, clamp. The clamp to [0, 1] is `min(1.0, max(0.0, x))`.

</details>


### Things to consider

- Who else uses `fresh_gas_flow`? `DualAgentModel` gives the N₂O sub-model its own flows. Should the N₂O model read the same machine? Decide whether both sub-models should share one "machine" object. That's a real design decision, and either answer is fine if you write it down in `DEVLOG.md`.
- The O₂ balance is a simplification (it ignores the small change in circuit volume when O₂ is consumed). It's still good enough to show the danger.
- Steady state with consumption is `FiO2_fresh − VO2/Q`. At 30% and 1 L/min that's about 5%, which is lethal. This is why low-flow O₂ needs watching.

### Checkpoint

- `fresh_gas_fio2(1, 1, 0)` = **0.605**, and `fresh_gas_fio2(1, 1, 2)` = **0.3025**
- `flows_for_target_fio2(0.30, 2.0)` → O₂ **0.228**, air **1.772**
- Circuit FiO₂ starting at 0.95, with fresh gas set to 30%:

| total flow | VO₂ | 1 min | 5 min | 10 min | 30 min |
|---|---|---|---|---|---|
| 2 L/min | off | 0.788 | 0.456 | 0.337 | 0.300 |
| 2 L/min | on | 0.757 | 0.361 | 0.219 ⚠ | 0.175 ⚠ |
| 10 L/min | on | 0.436 | 0.276 | 0.275 | 0.275 |

**References:** Baum JA. *Low Flow Anaesthesia: The Theory and Practice of Low Flow, Minimal Flow and Closed System Anaesthesia*. 2nd ed. Butterworth-Heinemann; 2001 · Mapleson WW. The concept of the time constant applied to breathing systems and to the body · Hendrickx JFA, De Wolf AM. The anaesthesia workstation: quo vadis? *Anesth Analg* 2018;127:671–5 · ISO 80601-2-13 (anaesthetic workstation safety; O₂:N₂O hypoxic guard, delivered O₂ ≈ ≥25%) · Resting adult O₂ consumption ≈ 250 mL/min (standard physiology)

---

## Week 12 — Decrement times, case scripts, and wrapping up Part 2

**Goal:** context-sensitive decrement times, and a few preset "cases" you can run from the terminal.

**New concepts (Python):** `copy.deepcopy` (simulate a "what if" without touching the real model); measuring *elapsed* time instead of absolute time; `if __name__ == "__main__":`.

**Read first:** [Python `copy` (shallow vs deep)](https://docs.python.org/3/library/copy.html)

### Starter code — `decrement.py`

```python
import copy

def decrement_times(model, targets=(50, 80, 90), max_minutes=60, dt=0.1/60):
    """Minutes for brain (VRG) concentration to fall by each % after the
    vaporizer is switched off, high-flow washout, starting from model's CURRENT state."""
    sim = copy.deepcopy(model)
    start_conc = sim.compartments["VRG"].concentration
    if start_conc < 0.01:
        return {}
    sim.dial = 0.0
    # TODO: high flow, e.g. sim.o2_flow = 10, others 0
    t0 = sim.time                  # remember when washout STARTED
    results = {}
    # TODO: step the copy forward until every target is found, or until
    #       max_minutes of WASHOUT time have passed.
    #       A target of 80 means "fallen to 20% of the starting concentration".
    #       Record elapsed washout minutes, not sim.time.
    return results
```

### Your tasks

1. Write `decrement_times`, run 10-, 60- and 180-minute sevo cases, and compare.
2. Write `cases.py` with a dict of presets, such as `"1.3 MAC sevo": dict(agent="sevoflurane", dial=2.6, n2o=0)`, `"Balanced": sevo 1.2 + N₂O 60`, and `"Low-flow trap": sevo 2%, O₂ 0.5 L/min`. Give it a `run_case(name, minutes)` that plots alveolar, brain and FiO₂.
3. Put the demo code under `if __name__ == "__main__":` so importing the module doesn't run it.
4. Commit, write a `DEVLOG.md` entry, and celebrate: two projects done.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Decrement loop condition</b>: Hint 1</summary>

Two conditions joined with `and`: elapsed washout time is under the cap, *and* you haven't found every target yet (`len(results) < len(targets)`).

</details>

<details>
<summary><b>Decrement loop body</b>: Hint 1</summary>

After each step, compute the fraction remaining, then check every target that isn't in `results` yet.

</details>
<details>
<summary><b>Decrement loop body</b>: Hint 2 (nearly the answer)</summary>

```python
while (sim.time - t0) < max_minutes and len(results) < len(targets):
    sim.step(dt)
    fraction = sim.compartments["VRG"].concentration / start_conc
    for target in targets:
        if target not in results and fraction <= 1 - target / 100:
            results[target] = sim.time - t0
```

</details>


### Things to consider

- **The two bugs this replaces:** the old loop stopped at `sim.time < 60/60` (that's 1 minute, not 60), and compared the case clock rather than elapsed washout time. After a 30-minute case it never ran at all. `t0` fixes both.
- `deepcopy` copies the whole tree of objects (the model and every compartment). A plain `copy.copy` would share the compartments, and your "what if" would wreck the real model. Try it once and watch it happen.

### Checkpoint

Sevo 2%, FGF 8 case, then washout at 10 L/min O₂ (minutes to reach each decrement):

| case length | d50 | d80 | d90 |
|---|---|---|---|
| 10 min | 2.9 | 6.5 | 9.2 |
| 60 min | 3.1 | 7.0 | 10.7 |
| 180 min | 3.2 | 7.9 | 14.2 |

d50 barely changes, but d90 grows by about 50% as the muscle and fat fill. This is the same lesson as Week 7, now for inhaled agents.

**References:** Hughes MA, Glass PSA, Jacobs JR. *Anesthesiology* 1992;76:334–41 · Bailey JM. *Clin Pharmacokinet* 2002;41:793–9 · Eger EI II. *Anesthetic Uptake and Action*, 1974 (1.0 and 1.3 MAC depth conventions)

---

# PART 3 — BEDSIDE MONITOR (JavaScript, from zero)

JavaScript is the language web browsers run. You'll write it in `.js` files, load them from an `.html` page, and see the results in the browser. There's nothing to install except a browser. To serve the files you'll use Python (one command), which is a nice bridge between your two languages.

### Learning JavaScript alongside this workbook

This workbook teaches JavaScript *through* the project, but it isn't a full JS course. Pair it with one of these free tutorials. Each week's **Read first** line points to the right chapter.

- **[javascript.info](https://javascript.info/)**, *The Modern JavaScript Tutorial*. This is the main one: clear, in order, with small exercises. Part 1 (the language) and Part 2 (the browser and DOM) cover everything here.
- **[MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)**: the reference you'll keep coming back to. Search "MDN" plus whatever you're stuck on.
- **[MDN Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development)**: beginner HTML/CSS/JS lessons, if the page side feels unfamiliar.
- **[MDN Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)**: drawing and animation, for Weeks 15–16.

A good rhythm: before Week 13, spend 3–4 hours on javascript.info chapters 2.1–2.15. Then follow the Read-first links week by week.

One idea runs underneath all of Part 3: **a waveform is a list of numbers, one every 4 ms (250 Hz).** Every week only changes *which numbers* get generated. The plumbing that turns numbers into a moving trace is built once, in Weeks 15–16.

---

## Week 13 — JavaScript basics by translating Python you already wrote

**Goal:** a page that runs your JS, a test page, and three small functions ported from Python.

**New concepts (JS):** `<script type="module">`; the browser console; `const`/`let`; functions; arrays and `for` loops; objects; classes; `===`; `export`/`import`.

**Read first:** [javascript.info: JavaScript Fundamentals](https://javascript.info/first-steps), chapters 2.1–2.15 (about 3–4 hours; do the small tasks at the end of each chapter) · [javascript.info: Developer console](https://javascript.info/devtools) · [MDN: JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)

### Running JS

```bash
cd anesthesia-sim/web
python -m http.server 8000
# open http://localhost:8000  in Chrome or Firefox
```

Open the **DevTools console** with F12 (or Cmd+Opt+J on a Mac). This is your terminal for JS: `console.log()` output and error messages show up here. Keep it open, always.

> You need the server because browsers block `import` between files opened straight from disk (`file://`). That's a security rule, not a bug.

### Starter code — `web/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Monitor</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Monitor</h1>
  <script type="module" src="js/main.js"></script>
</body>
</html>
```

### Starter code — `web/js/main.js`

```js
console.log("hello from main.js");
```

### Python → JavaScript cheat sheet (keep this open)

| Python | JavaScript |
|---|---|
| `x = 5` | `const x = 5;` (can't reassign) or `let x = 5;` (can reassign) |
| `def f(a, b=2): return a + b` | `function f(a, b = 2) { return a + b; }` |
| `lambda x: x * 2` | `x => x * 2` |
| `[1, 2, 3]`, `len(a)` | `[1, 2, 3]`, `a.length` |
| `a.append(4)` | `a.push(4)` |
| `for i in range(n):` | `for (let i = 0; i < n; i++) { ... }` |
| `for v in values:` | `for (const v of values) { ... }` |
| `{"hr": 72}`, `d["hr"]` | `{ hr: 72 }`, `d.hr` or `d["hr"]` |
| `None` | `null` (or `undefined`, which means "never set") |
| `==` | `===` (always use three; `==` does surprising conversions) |
| `and`, `or`, `not` | `&&`, `\|\|`, `!` |
| `x ** 2`, `math.exp(x)` | `x ** 2`, `Math.exp(x)` |
| `f"HR {hr}"` | `` `HR ${hr}` `` (backticks) |
| `print(x)` | `console.log(x)` |
| `class A:` / `def __init__(self, n):` / `self.n = n` | `class A {` / `constructor(n) {` / `this.n = n; }` |
| `from m import f` | `import { f } from "./m.js";` (the file must say `export function f...`) |
| indentation defines blocks | `{ }` define blocks. Indent anyway, for humans. |

### Starter code — `web/js/math.js`

```js
// Port of ideas you know. Every function is exported so other files can import it.

export function linspace(n) {
  // n evenly spaced values from 0 to 1 inclusive, e.g. linspace(3) -> [0, 0.5, 1]
  const out = [];
  for (let i = 0; i < n; i++) {
    // TODO: push the i-th evenly spaced value (careful: what if n === 1?)
  }
  return out;
}

export function gaussian(x, amp, center, width) {
  // TODO: amp * e^(-(x - center)^2 / (2 * width^2))
}

// Translation drill: your Python Compartment from Week 8, in JS
export class Compartment {
  constructor(name, volumeL, flowLmin) {
    this.name = name;
    // TODO: volume, flow, concentration = 0
  }
  rateOfChange(cArterial, lam) {
    // TODO: same equation as your Python version
  }
  update(cArterial, lam, dt) {
    // TODO: Euler step and clamp >= 0 (Math.max)
  }
}
```

### Starter code — `web/tests.html` and `web/js/tests.js`

```html
<!doctype html>
<html><head><meta charset="utf-8"><title>Tests</title></head>
<body><h1>Open the console</h1><script type="module" src="js/tests.js"></script></body></html>
```

```js
import { linspace, gaussian, Compartment } from "./math.js";

let failures = 0;
function check(name, actual, expected, tol = 1e-6) {
  const ok = Math.abs(actual - expected) <= tol;
  if (!ok) failures++;
  console.log(`${ok ? "PASS" : "FAIL"}  ${name}: got ${actual}, expected ${expected}`);
}

check("linspace length", linspace(5).length, 5);
check("gaussian peak", gaussian(0.4, 1, 0.4, 0.04), 1.0);
// TODO: gaussian(0.5, 1, 0.4, 0.04) ≈ 0.0439
// TODO: new Compartment("VRG", 6, 4.2).rateOfChange(2.0, 1.7) ≈ 1.4

console.log(failures === 0 ? "ALL PASS" : `${failures} FAILED`);
```

### Your tasks

1. Get "hello from main.js" into the console.
2. Fill in `math.js` and load `tests.html` until everything passes.
3. In the console, break something on purpose (call `gaussian()` with no arguments) and look at the result. JS returns `NaN` instead of crashing. That's different from Python, and it's why the `check()` helper matters.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>linspace</code> edge case</b>: Hint 1</summary>

Dividing by `n - 1` when `n === 1` gives `0/0 = NaN`. A ternary picks between two values: `condition ? a : b`.

</details>
<details>
<summary><b><code>linspace</code> edge case</b>: Hint 2 (nearly the answer)</summary>

```js
out.push(n > 1 ? i / (n - 1) : 0);
```

</details>

<details>
<summary><b><code>gaussian</code></b>: Hint 1</summary>

`Math.exp(x)` is eˣ. `**` squares, just like Python.

</details>
<details>
<summary><b><code>gaussian</code></b>: Hint 2 (nearly the answer)</summary>

```js
return amp * Math.exp(-((x - center) ** 2) / (2 * width ** 2));
```

</details>

<details>
<summary><b><code>Compartment</code> in JS</b>: Hint 1</summary>

Same as Python with `self.` changed to `this.`. Clamp with `Math.max(0, ...)`.

</details>


### Things to consider

- `const` arrays can still be changed (`out.push(...)` works). `const` only stops you assigning a *different* array to that name.
- A function that forgets `return` gives back `undefined`. No error is shown, so watch for it.
- Inside a class, you must write `this.` every time, the same way you write `self.` in Python.

### Checkpoint

`tests.html` shows `ALL PASS`, and `gaussian(0.5, 1, 0.4, 0.04)` ≈ **0.0439**.

---

## Week 14 — HTML, the DOM and events

**Goal:** a heart-rate slider that live-updates text showing the R-R interval and samples per beat.

**New concepts (JS):** HTML elements; the DOM (the page as JS objects); `document.getElementById`; `addEventListener`; `.textContent`; `parseFloat`.

**Read first:** [javascript.info: Document (the DOM)](https://javascript.info/document), first five chapters · [javascript.info: Introduction to browser events](https://javascript.info/events) · [MDN: Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development) (HTML basics, if the markup feels unfamiliar)

### Starter code — add to `index.html` (above the `<script>`)

```html
<section class="controls">
  <label>Heart rate <input id="hr" type="range" min="30" max="200" value="75"></label>
  <span id="hr-out">75</span> bpm
  <p>R-R interval: <span id="rr-out">?</span> ms &nbsp;·&nbsp; samples/beat: <span id="n-out">?</span></p>
</section>
```

### Starter code — `main.js`

```js
const SAMPLE_RATE = 250;

const hrSlider = document.getElementById("hr");
const hrOut = document.getElementById("hr-out");
// TODO: grab rr-out and n-out the same way

function rrMs(hr) {
  // TODO: R-R interval in milliseconds from heart rate
}

function render() {
  const hr = parseFloat(hrSlider.value);   // slider values are STRINGS
  hrOut.textContent = hr;
  // TODO: write rrMs(hr) (rounded) and samples per beat into the page
}

hrSlider.addEventListener("input", render);  // runs every time the slider moves
render();                                    // and once at start
```

### Your tasks

1. Wire it up. Drag the slider and watch the numbers.
2. Add a second control: a `<select id="rhythm">` with options NSR, AFIB, VTACH, VFIB and CHB. Log the choice when it changes (use the `"change"` event).
3. Add a small `style.css` with a dark background and green text, like a monitor. Use classes, not inline styles.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Writing into the page</b>: Hint 1</summary>

Set `.textContent` on the element. `Math.round()` keeps it tidy.

</details>
<details>
<summary><b>Writing into the page</b>: Hint 2 (nearly the answer)</summary>

```js
rrOut.textContent = Math.round(rrMs(hr));
nOut.textContent = Math.round(rrMs(hr) * SAMPLE_RATE / 1000);
```

</details>


### Things to consider

- Without `parseFloat`, `"75" + 5` is `"755"`. JS joins strings when one side is a string. This bug will bite you at least once.
- `addEventListener("input", render)` passes the function itself, with no `()`. Writing `render()` there would call it once immediately and hand over its return value (`undefined`). It's the same idea as storing functions in your Python registry.

### Checkpoint

HR 75 → R-R **800 ms**, **200** samples/beat. HR 150 → **400 ms**, **100** samples.

---

## Week 15 — One heartbeat on a canvas

**Goal:** draw a single normal-sinus beat as a static picture.

**New concepts (JS):** `<canvas>` and its 2-D drawing context; mapping values to pixels; splitting code into modules.

**Read first:** [MDN Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial): *Basic usage* and *Drawing shapes* · [javascript.info: Array methods](https://javascript.info/array-methods) (`map`, `forEach`) · [javascript.info: Destructuring](https://javascript.info/destructuring-assignment)

### Starter code — `web/js/ecg.js`

```js
import { linspace, gaussian } from "./math.js";

export const SAMPLE_RATE = 250;
export const samplesFor = ms => Math.max(1, Math.round(ms * SAMPLE_RATE / 1000));

export function pWave(n, amp = 0.15) {
  return linspace(n).map(x => gaussian(x, amp, 0.5, 0.15));   // .map = list comprehension
}

export function qrsComplex(n, q = -0.1, r = 1.0, s = -0.2) {
  // Shape: Q, R and S are three narrow gaussians (width 0.04) at x = 0.2, 0.4, 0.6,
  //        with amplitudes q, r, s, added together.
  // TODO: return an array of n values
}

export function tWave(n, amp = 0.3) {
  // A width-0.25 gaussian is still 13% high at its edges, which leaves a small
  // step in the trace. Fix: subtract the edge value, then rescale so the peak stays `amp`.
  const edge = Math.exp(-(0.5 ** 2) / (2 * 0.25 ** 2));
  // TODO: return n values that are 0 at both edges and `amp` at the peak
}

function place(buf, start, wave) {
  for (let i = 0; i < wave.length; i++) {
    const j = start + i;
    if (j >= 0 && j < buf.length) buf[j] = wave[i];
  }
}

export function nsrBeat(rrMs) {
  const total = samplesFor(rrMs);
  const beat = new Array(total).fill(0);
  const pS = samplesFor(80), gap = samplesFor(40), qS = samplesFor(100), stS = samplesFor(100), tS = samplesFor(160);
  const pStart = Math.floor(0.05 * total);
  // TODO: qrsStart and tStart (order: P, PR gap, QRS, ST segment, T)
  // TODO: place the three waves
  // TODO: return an OBJECT with samples, rOffset (index of the R peak, 40% into the QRS) and rrMs
}
```

### Starter code — `web/js/draw.js`

```js
export function valueToY(v, min, max, height) {
  // Canvas y = 0 is the TOP. Flip.
  // TODO: min should land at the bottom (height) and max at the top (0)
}

export function drawStatic(canvas, values, { min = -0.5, max = 1.5, color = "#0f0" } = {}) {
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = color;
  ctx.beginPath();
  values.forEach((v, i) => {
    const x = (i / (values.length - 1)) * canvas.width;
    const y = valueToY(v, min, max, canvas.height);
    // TODO: moveTo for the first point, lineTo for the rest
  });
  ctx.stroke();
}
```

### Your tasks

1. Add `<canvas id="ecg" width="900" height="200"></canvas>` to the page.
2. Finish `ecg.js` and `draw.js`, then draw `nsrBeat(800).samples`.
3. Hook it to the Week 14 slider, so changing HR redraws the beat.
4. Add `ecg.js` checks to `tests.js`.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>qrsComplex</code></b>: Hint 1</summary>

`.map()` turns every x into a value. Inside the arrow function, add three `gaussian()` calls.

</details>
<details>
<summary><b><code>qrsComplex</code></b>: Hint 2 (nearly the answer)</summary>

```js
return linspace(n).map(x => gaussian(x, q, 0.2, 0.04) + gaussian(x, r, 0.4, 0.04) + gaussian(x, s, 0.6, 0.04));
```

</details>

<details>
<summary><b>Edge-corrected T wave</b>: Hint 1</summary>

Subtract `edge` from a unit-height gaussian so the edges hit 0, then divide by `(1 - edge)` so the peak is back to 1, then multiply by `amp`.

</details>
<details>
<summary><b>Edge-corrected T wave</b>: Hint 2 (nearly the answer)</summary>

```js
return linspace(n).map(x => amp * (gaussian(x, 1, 0.5, 0.25) - edge) / (1 - edge));
```

</details>

<details>
<summary><b>Returning an object</b>: Hint 1</summary>

JS object literal: `{ key: value }`. If a variable already has the right name, `{ rrMs }` is shorthand for `{ rrMs: rrMs }`.

</details>
<details>
<summary><b>Returning an object</b>: Hint 2 (nearly the answer)</summary>

```js
return { samples: beat, rOffset: qrsStart + Math.round(0.4 * qS), rrMs };
```

</details>

<details>
<summary><b><code>valueToY</code></b>: Hint 1</summary>

First turn `v` into 0..1 (0 at `min`, 1 at `max`), then flip, because canvas y grows downward.

</details>
<details>
<summary><b><code>valueToY</code></b>: Hint 2 (nearly the answer)</summary>

```js
const normalized = (v - min) / (max - min);
return height * (1 - normalized);
```

</details>

<details>
<summary><b>First point vs the rest</b>: Hint 1</summary>

`forEach` gives you the index `i`. Use `i === 0` to choose `ctx.moveTo(x, y)` over `ctx.lineTo(x, y)`.

</details>


### Things to consider

- `{ min = -0.5, max = 1.5 } = {}` in a parameter list is *destructuring with defaults*, JS's version of keyword arguments. Call it as `drawStatic(c, v, { max: 2 })`.
- At HR 150 the components need 120 samples, but the beat has only 100. What does `place` do with the T wave? (Real QT intervals shorten with rate. Your stretch could model that.)

### Checkpoint

`nsrBeat(800)`: **200** samples, pStart **10**, qrsStart **40**, tStart **90**, rOffset **50**. QRS peak ≈ **1.0**, and the T wave starts and ends at exactly **0**.

**References:** *Project 3: Medical Waveform Training Platform* textbook, Ex 1.1 and 1.3 (Gaussian ECG components, NSR timing)

---

## Week 16 — Animation: the sweeping trace

**Goal:** a continuous ECG sweeping left to right at the right speed, with HR displayed.

**New concepts (JS):** `requestAnimationFrame` (the browser calls your function about 60 times a second); a *ring buffer* (index wraps with `%`); `Float32Array`; *callbacks*, where one object tells others "an R-wave just happened".

**Read first:** [MDN: Canvas basic animations](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations) · [MDN: `requestAnimationFrame`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame) · [javascript.info: Classes](https://javascript.info/classes)

### Starter code — `web/js/sweep.js`

```js
export class Sweep {
  constructor(canvas, { color = "#0f0", min = -0.5, max = 1.5, seconds = 6,
                        sampleRate = 250, mode = "extreme", baseline = 0 } = {}) {
    this.ctx = canvas.getContext("2d");
    this.w = canvas.width;
    this.h = canvas.height;
    Object.assign(this, { color, min, max, mode, baseline });
    this.samplesPerColumn = (seconds * sampleRate) / this.w;   // 1500 / 900 ≈ 1.67
    this.columns = new Float32Array(this.w).fill(NaN);         // NaN = blank
    this.cursor = 0;
    this.acc = 0;            // fractional sample counter
    this.pending = [];       // samples waiting to become one column
  }

  push(v) {
    this.pending.push(v);
    this.acc += 1;
    if (this.acc >= this.samplesPerColumn) {
      this.acc -= this.samplesPerColumn;
      this.columns[this.cursor] = this._combine(this.pending);
      this.pending = [];
      this.cursor = (this.cursor + 1) % this.w;
      // TODO: blank a small gap ahead of the cursor (e.g. 12 columns) by setting them to NaN
    }
  }

  _combine(samples) {
    if (this.mode === "last") return samples[samples.length - 1];
    // "extreme": keep the sample farthest from baseline, so the QRS spike survives
    // TODO: return that sample
  }

  draw() {
    const c = this.ctx;
    c.fillStyle = "#000";
    c.fillRect(0, 0, this.w, this.h);
    c.strokeStyle = this.color;
    c.lineWidth = 1.7;
    c.beginPath();
    let penDown = false;
    for (let x = 0; x < this.w; x++) {
      const v = this.columns[x];
      if (Number.isNaN(v)) { penDown = false; continue; }   // lift the pen over the gap
      // TODO: draw to this column; start a new line segment after a gap
    }
    c.stroke();
  }
}
```

### Starter code — `web/js/cardiac.js`

```js
import { nsrBeat } from "./ecg.js";

export class CardiacSource {
  constructor(getRR) {
    this.getRR = getRR;          // a FUNCTION that returns the current R-R in ms
    this.beatFn = nsrBeat;       // swapped when the rhythm changes (Week 17)
    this.buffer = [];
    this.index = 0;
    this.current = null;
    this.listeners = [];
  }

  onR(fn) { this.listeners.push(fn); }   // "call fn every time there's an R-wave"

  next() {
    if (this.index >= this.buffer.length) {
      // TODO: fetch a fresh beat and start reading its samples from the beginning
    }
    if (this.index === this.current.rOffset) {
      // TODO: tell every listener about this beat
    }
    return this.buffer[this.index++];
  }
}
```

### Starter code — the loop, in `main.js`

```js
import { Sweep } from "./sweep.js";
import { CardiacSource } from "./cardiac.js";
import { SAMPLE_RATE } from "./ecg.js";

const ecgSweep = new Sweep(document.getElementById("ecg"));
const heart = new CardiacSource(() => 60000 / parseFloat(hrSlider.value));

let carry = 0;
let lastT = performance.now();

function loop(now) {
  requestAnimationFrame(loop);
  const dt = Math.min(0.1, (now - lastT) / 1000);   // cap: tab-switch pauses can make dt huge
  lastT = now;
  carry += dt * SAMPLE_RATE;                         // samples "owed" since last frame
  while (carry >= 1) {
    carry -= 1;
    ecgSweep.push(heart.next());
  }
  ecgSweep.draw();
}
requestAnimationFrame(loop);
```

### Your tasks

1. Finish `Sweep` and `CardiacSource`, and watch it sweep.
2. Time one full sweep with a stopwatch. It should take 6 seconds.
3. Use `heart.onR(beat => ...)` to flash a heart symbol or beep-dot on every R-wave. This is your first callback.
4. Show the HR as a big number next to the trace.
5. Commit, and write a `DEVLOG.md` entry.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>_combine</code> extreme</b>: Hint 1</summary>

Loop over `samples`, track the one with the largest `Math.abs(v - this.baseline)`, and return it.

</details>

<details>
<summary><b><code>draw()</code> column</b>: Hint 1</summary>

Compute `const y = this.y(v)` (you need a `y(v)` method: copy your Week 15 `valueToY`). Then `penDown ? c.lineTo(x, y) : c.moveTo(x, y); penDown = true;`.

</details>

<details>
<summary><b>Refilling the buffer</b>: Hint 1</summary>

Three assignments: the new beat object, its samples array, and the index back to 0.

</details>
<details>
<summary><b>Refilling the buffer</b>: Hint 2 (nearly the answer)</summary>

```js
this.current = this.beatFn(this.getRR());
this.buffer = this.current.samples;
this.index = 0;
```

</details>

<details>
<summary><b>Calling listeners</b>: Hint 1</summary>

`this.listeners` is an array of functions. Call each one, passing the beat.

</details>
<details>
<summary><b>Calling listeners</b>: Hint 2 (nearly the answer)</summary>

```js
this.listeners.forEach(fn => fn(this.current));
```

</details>


### Things to consider

- Why the `acc` counter instead of "every 2 samples"? 1500 samples across 900 pixels is 1.67 samples per column. Rounding to 2 would make each sweep take 7.2 seconds.
- Why "extreme" instead of averaging? Averaging a QRS spike with its near-zero neighbours shrinks it. Try `mode: "last"` on the ECG to see the R-waves get chopped.
- `onR` is the architectural heart of Part 3. The arterial line, the pleth and the IABP will all *listen* for R-waves instead of knowing anything about the ECG. Python has the same pattern (any list of functions you call), and JS uses it everywhere.

### Checkpoint

A smooth green sweep, 6 seconds per screen, a crisp QRS, and the heart symbol flashing in step with the R-waves.

**References:** *Project 3* textbook, Ex 1.6 (canvas display)

---

## Week 17 — Patient state, controls and smooth transitions

**Goal:** one object holding the patient's vitals, controls that change it, and an HR that ramps instead of jumping.

**New concepts (JS):** a shared state object exported from a module; writing one function to bind many sliders; `switch`.

**Read first:** [javascript.info: Objects](https://javascript.info/object) · [javascript.info: `switch`](https://javascript.info/switch)

### Starter code — `web/js/patient.js`

```js
export const P = {
  hr: 75, targetHr: 75,
  sbp: 120, dbp: 80,
  spo2: 98, rr: 14, etco2: 38,
  rhythm: "NSR",
  nativeCO: 4.5,          // L/min. Make it LOW for cardiogenic-shock scenarios (Week 21)
};

export function nextEffectiveHR(step = 5) {
  // Called once per beat: move P.hr toward P.targetHr by at most `step`.
  // TODO (Math.min / Math.max keep it from overshooting)
  return P.hr;
}

export function map() {
  // TODO: (sbp + 2*dbp) / 3, rounded
}
```

### Starter code — `web/js/controls.js`

```js
import { P } from "./patient.js";

export function bindSlider(id, key, { onChange } = {}) {
  const el = document.getElementById(id);
  const out = document.getElementById(`${id}-out`);
  const update = () => {
    const v = parseFloat(el.value);
    P[key] = v;                         // P["targetHr"] is the same as P.targetHr
    if (out) out.textContent = v;
    if (onChange) onChange(v);
  };
  el.addEventListener("input", update);
  update();
}
// usage: bindSlider("hr", "targetHr"); bindSlider("sbp", "sbp"); ...
```

### Your tasks

1. Move HR into `P` and bind sliders for HR (target), SBP, DBP, SpO₂, RR and EtCO₂.
2. Make `CardiacSource` use `nextEffectiveHR()` once per beat, so HR changes ramp.
3. Wire the rhythm `<select>` to `P.rhythm`, and in `CardiacSource` pick `beatFn` with a `switch (P.rhythm)`. Only NSR exists for now. Make the others fall back to NSR.
4. Add a vitals panel showing HR, BP (MAP), SpO₂, RR and EtCO₂, refreshed in `loop()`.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>nextEffectiveHR</code></b>: Hint 1</summary>

If `P.hr` is below the target, add `step` but don't pass the target (`Math.min`). If above, subtract (`Math.max`).

</details>

<details>
<summary><b>Safe place to change rhythm</b>: Hint 1</summary>

Right where `CardiacSource` fetches a fresh beat: a `switch (P.rhythm)` there picks `this.beatFn` before calling it.

</details>


### Things to consider

- Rhythm changes should take effect at the **next beat**, not in the middle of one. Where in `CardiacSource.next()` is the safe place to check `P.rhythm`?
- `P` is imported by many files, and they all share the *same* object. Changing `P.sbp` anywhere is seen everywhere. That's convenient, but it's also how big projects get confusing, so only `controls.js` (and later, scenarios) should *write* to `P`.

### Checkpoint

Target HR 75 → 130 with step 5: **11 beats** to arrive. MAP for 120/80 = **93**, 90/60 = **70**, 180/100 = **127**.

**References:** *Project 3* textbook, Ex 1.4 (patient state, transitions) · Deranged Physiology, *Normal arterial line waveforms* (the ⅓ MAP formula is an estimate; monitors integrate the area under the curve). derangedphysiology.com

---

## Week 18 — Atrial fibrillation and the ectopy overlay

**Goal:** irregular AFib with a fibrillatory baseline, plus PVCs that can be injected into *any* rhythm.

**New concepts (JS):** `Math.random()`; a *wrapper* that takes a beat function and returns a modified beat; carrying extra data along on an object (`ampMod`).

**Read first:** [javascript.info: Object methods and `this`](https://javascript.info/object-methods)

### Starter code — add to `ecg.js`

```js
export function randn() {                    // standard-normal noise (Box–Muller)
  let u = 0, v = 0;
  while (!u) u = Math.random();
  while (!v) v = Math.random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

export function afibBeat(baseRrMs, irregularity = 0.3) {
  const r = (Math.random() * 2 - 1) * irregularity;
  const actual = Math.max(300, Math.min(1500, Math.round(baseRrMs * (1 + r))));
  const total = samplesFor(actual);
  // TODO: baseline = a few small sines (5.8, 7.3, 9.1, 6.5 Hz, random phases) + tiny randn() noise
  // TODO: ADD (not place) a QRS at 25% of the beat, then a T wave
  // TODO: fill = clamp(actual / baseRrMs, 0.5, 1.15)  -> a shorter beat fills less, so the pulse is weaker
  // return { samples, rOffset, rrMs: actual, ampMod: fill };
}

export function pvcComplex(n, amp = 1.5) {
  // wide main deflection + shoulder + T wave in the OPPOSITE direction
  // TODO: gaussian(x, amp, 0.30, 0.10) + gaussian(x, amp*0.5, 0.45, 0.08) + gaussian(x, -amp*0.4, 0.75, 0.12)
}
```

### Starter code — `web/js/ectopy.js`

```js
import { samplesFor, pvcComplex } from "./ecg.js";

export const Ectopy = {
  enabled: false,
  pattern: "random",    // "random" | "bigeminy" | "trigeminy"
  freq: 0.1,
  count: 0,
  lastWasPVC: false,

  shouldFire() {
    if (!this.enabled || this.lastWasPVC) return false;    // never two in a row
    // TODO: bigeminy = every 2nd beat, trigeminy = every 3rd beat,
    //       otherwise fire at random with probability `freq`
  },

  next(baseBeatFn, rrMs) {
    const fire = this.shouldFire();
    const afterPVC = this.lastWasPVC;
    this.lastWasPVC = fire;
    this.count++;
    if (fire) {
      // TODO: coupling = rrMs * (0.6..0.8); buffer length = 2*rrMs (compensatory pause)
      // TODO: place pvcComplex(samplesFor(160), 1.6) at the coupling point
      // return { samples, rOffset, rrMs: coupling, ampMod: 0.2 };   // weak ejection
    }
    const beat = baseBeatFn(rrMs);
    // TODO: post-PVC beat is stronger: multiply beat.ampMod (default 1) by 1.3 if afterPVC
    return beat;
  },
};
```

### Your tasks

1. AFib first: add it to your rhythm `switch` and check that there are no P waves, a wobbly baseline and uneven spacing.
2. Ectopy: in `CardiacSource`, call `Ectopy.next(this.beatFn, rr)` instead of `this.beatFn(rr)`. Add a checkbox and a pattern `<select>`.
3. Turn on PVCs over NSR, then over AFib, without changing `afibBeat`. That's the overlay doing its job.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>AFib baseline</b>: Hint 1</summary>

Start with `new Array(total).fill(0)`. For each frequency, pick `const phase = Math.random() * 2 * Math.PI` once, then add a small sine to every sample. The time of sample `i` is `i / SAMPLE_RATE` seconds.

</details>

<details>
<summary><b><code>shouldFire</code> patterns</b>: Hint 1</summary>

`%` is remainder, the same as in Python. Return the comparison itself; it's already `true` or `false`.

</details>
<details>
<summary><b><code>shouldFire</code> patterns</b>: Hint 2 (nearly the answer)</summary>

```js
if (this.pattern === "bigeminy") return this.count % 2 === 1;
if (this.pattern === "trigeminy") return this.count % 3 === 2;
return Math.random() < this.freq;
```

</details>

<details>
<summary><b>Post-PVC beat</b>: Hint 1</summary>

`beat.ampMod` may be missing on NSR beats. `(beat.ampMod ?? 1) * 1.3` handles both cases.

</details>


### Things to consider

- **Place vs add:** NSR's baseline is zeros, so overwriting is fine. AFib's baseline is the fibrillation squiggle, so you must *add* the QRS on top or you'll erase it.
- Why an overlay instead of separate NSR, NSR+PVC, AFib and AFib+PVC rhythms? Count how many rhythms you'd need for 5 rhythms × 3 ectopy types.
- In AFib there's no sinus node to "reset", so a true compensatory pause doesn't really apply. Your overlay always adds one. Is that worth fixing? (Stretch.)

### Checkpoint

- AFib at base 800 ms, irregularity 0.3: every R-R falls in **560–1040 ms**.
- Bigeminy for beats 0–5: normal, **PVC**, normal, **PVC**, normal, **PVC**. The ampMods are 1, **0.2**, **1.3**, 0.2, 1.3, ...

**References:** *Project 3* textbook, Ex 4.1 (atrial fibrillation) and Ex 4.2 (ectopy overlay, PVCs, compensatory pause, post-extrasystolic potentiation)

---

## Week 19 — Arterial line and pleth, triggered by the R-wave

**Goal:** an arterial pressure trace that rises 150 ms after each R-wave, with a realistic shape at *any* heart rate. Then a pleth built from the same class.

**New concepts (JS):** a per-sample *state machine*; a queue of delayed events (`push`/`shift`); reusing one class with different options.

### Why this is a new design (the old one "looked funny")

The old arterial pulse was a fixed 350 ms shape followed by a flat line. That gave a flat plateau at slow heart rates, a 3 mmHg step at the end of every beat, and a dicrotic notch far too early. It also broke at fast rates. The new design never "ends" a pulse:

- On each upstroke, rise from **wherever the pressure is now** to systolic, over about 100 ms (using `smoothstep`).
- After the peak, decay toward diastolic continuously: `dia + pp · exp(−t/τ)`, with τ ≈ 250 ms.
- Add a small notch at about 300 ms after the upstroke starts (end of ejection) and a small dicrotic bump just after it.
- The next beat starts from the current value, so there's never a jump. As a bonus, end-diastolic pressure *rises* at fast heart rates (less time to run off), which is physiologically right.

### Starter code — `web/js/pulse.js`

```js
import { samplesFor, SAMPLE_RATE } from "./ecg.js";

const smoothstep = u => u * u * (3 - 2 * u);
const bump = (t, c, w) => Math.exp(-((t - c) ** 2) / (2 * w * w));

export class PulsePump {
  constructor({ delayMs = 150, riseMs = 100, tauMs = 250, notchMs = 300,
                notchDepth = 0.08, bumpSize = 0.05, start = 80 } = {}) {
    Object.assign(this, { riseMs, tauMs, notchMs, notchDepth, bumpSize });
    this.delay = samplesFor(delayMs);
    this.value = start;
    this.pending = [];      // [{ left, sys, dia, sharp }]
    this.beat = null;       // the beat currently being drawn
    this.t = 0;             // samples since this beat's upstroke began
  }

  trigger(sys, dia, sharp = 1) {          // call this from heart.onR(...)
    this.pending.push({ left: this.delay, sys, dia, sharp });
  }

  next() {
    for (const p of this.pending) p.left--;
    if (this.pending.length && this.pending[0].left <= 0) {
      const p = this.pending.shift();
      // TODO: start a new beat: remember the pressure it starts from (base),
      //       its targets (sys, dia, sharp), and reset the beat clock
    }
    if (!this.beat) return this.value;

    const ms = (this.t * 1000) / SAMPLE_RATE;
    const b = this.beat;
    const pp = b.sys - b.dia;
    let v;
    if (ms < this.riseMs) {
      // TODO: upstroke: smoothstep from base up to sys over riseMs
    } else {
      // TODO: runoff: exponential decay from sys toward dia (time constant tauMs),
      //       minus a small notch at notchMs, plus a small dicrotic bump just after it.
      //       Both features scale with pp and `sharp`.
    }
    this.t++;
    this.value = v;
    return v;
  }
}
```

### Wiring (in `main.js`)

```js
const art = new PulsePump();                          // arterial: mmHg
heart.onR(beat => {
  const amp = beat.ampMod ?? 1;                       // ?? = "use 1 if ampMod is missing"
  // TODO: shrink or grow the pulse pressure by amp, then trigger the pump
});
// in the loop, next to the ECG push:  artSweep.push(art.next());
```

For the **pleth**, make a second `PulsePump` with `delayMs: 250`, `start: 0` and a slightly longer `riseMs`. Trigger it with `sys = 0.7 * amp` and `dia = 0`. Its height means **perfusion**, *not* the SpO₂ number, and it stays that way when the devices arrive in Week 21.

### Your tasks

1. Finish `PulsePump`. Add an arterial canvas (red, range 40–160) and a pleth canvas (cyan, range −0.1 to 1). Use `mode: "last"` for both.
2. Check the timing by eye: QRS → about 150 ms → arterial upstroke → about 100 ms later → pleth upstroke.
3. Turn on PVCs and AFib and watch the beat-to-beat pulse changes.
4. Add a few lines to `tests.js` that drive a `PulsePump` without any canvas: trigger every N samples and record the min and max. That's the checkpoint below.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Starting a beat</b>: Hint 1</summary>

Store an object on `this.beat`. The `sys` guard stops a weak beat from pointing the upstroke downward.

</details>
<details>
<summary><b>Starting a beat</b>: Hint 2 (nearly the answer)</summary>

```js
this.beat = { base: this.value, sys: Math.max(p.sys, this.value + 2), dia: p.dia, sharp: p.sharp };
this.t = 0;
```

</details>

<details>
<summary><b>Pulse shape formulas</b>: Hint 1</summary>

Upstroke: base + (sys − base)·smoothstep(ms / riseMs). Runoff: dia + pp·e^(−(ms − riseMs)/tauMs) − notchDepth·pp·sharp·bump(ms, notchMs, 15) + bumpSize·pp·sharp·bump(ms, notchMs + 40, 25).

</details>
<details>
<summary><b>Pulse shape formulas</b>: Hint 2 (nearly the answer)</summary>

```js
v = b.base + (b.sys - b.base) * smoothstep(ms / this.riseMs);
// ...
v = b.dia + pp * Math.exp(-(ms - this.riseMs) / this.tauMs)
    - this.notchDepth * pp * b.sharp * bump(ms, this.notchMs, 15)
    + this.bumpSize   * pp * b.sharp * bump(ms, this.notchMs + 40, 25);
```

</details>

<details>
<summary><b>Wiring the trigger</b>: Hint 1</summary>

Pulse pressure × amp, added to diastolic.

</details>
<details>
<summary><b>Wiring the trigger</b>: Hint 2 (nearly the answer)</summary>

```js
const sys = P.dbp + (P.sbp - P.dbp) * amp;
art.trigger(sys, P.dbp);
```

</details>


### Things to consider

- What should happen when a weak PVC beat's "systolic" target is *lower* than the pressure the line is already at? Try it without any guard and watch the upstroke go the wrong way, then add one.
- The notch sits at a fixed ~300 ms because ejection time changes much less than diastole as HR changes. Real ejection does shorten somewhat at high HR. That's a possible stretch.
- Both traces use the *same class*. If you find yourself copying `PulsePump` to make `PlethPump`, stop and add an option instead.

### Checkpoint

Trigger 120/80 every R-R in a test loop (no ECG needed) and record a few beats once it's steady:

| HR | peak | end-diastolic (just before upstroke) |
|---|---|---|
| 60 | 120.0 | **81.1** |
| 75 | 120.0 | **82.5** |
| 150 | 120.0 | **92.4** |

Triggering every 800 ms with ampMods 1, 1, 0.2, 1.3, 1 (so `sys = 80 + 40 × ampMod`) gives peaks **120, 120, 88, 132, 120**.

**References:** Stouffer GA. Arterial pressure (ch. 4). thoracickey.com/4-arterial-pressure/ · Deranged Physiology, *Normal arterial line waveforms*. derangedphysiology.com · *Arterial Lines*. anaestheasier.com/arterial-lines/ · *Broader applications of arterial pressure waveform analysis*. *BJA Education* 2017 (dicrotic notch about ⅓ down the descending limb). bjaed.org · *Capnography and Pulse Oximetry*, StatPearls NBK539754 (pleth height reflects perfusion, not saturation) · *Project 3* textbook, Ex 4.3 and 5.1

---

## Week 20 — Capnography, lethal rhythms and alarms

**Goal:** a CO₂ trace on the *breathing* clock, VTach, VFib and complete heart block, and visible alarms.

**New concepts (JS):** a second, independent clock; returning "no R-wave" from a beat; toggling CSS classes with `classList`.

**Read first:** [MDN: `classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) · [MDN: Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)

### Starter code — `web/js/capno.js`

```js
import { SAMPLE_RATE } from "./ecg.js";
import { P } from "./patient.js";

export const Capno = {
  phase: 0,          // 0 -> 1 across one breath
  next() {
    const period = 60 / Math.max(1, P.rr);           // seconds per breath
    this.phase += (1 / SAMPLE_RATE) / period;
    if (this.phase >= 1) this.phase -= 1;
    const f = this.phase, e = P.etco2;
    // TODO:
    // f < 0.40          -> 0                                  (baseline: inspiration + dead space)
    // 0.40 <= f < 0.50  -> rise 0 -> e, linear                (expiratory upstroke)
    // 0.50 <= f < 0.85  -> e (small upward slope is a nice touch)   (alveolar plateau)
    // 0.85 <= f < 1.00  -> fall e -> 0, linear                (inspiratory downstroke)
  },
};
```

### Starter code — lethal rhythms (add to `ecg.js`)

```js
export function vtachBeat(rrMs) {
  const actual = Math.max(240, Math.min(400, rrMs));    // forces 150–250 bpm
  // TODO: wide pvcComplex (~200 ms), no P wave; return { ..., ampMod: 0.35 }
}

export function vfibChunk(ms = 500) {
  // TODO: chaotic sum of a few sines (4–8 Hz) + randn() noise
  // return { samples, rOffset: -1, rrMs: ms };   // rOffset -1: NO R-wave, so no pulse
}

// Complete heart block: TWO independent clocks writing into one buffer.
export const CHB = {
  atrialPhaseMs: 0,               // persists between beats, which is the whole point
  beat(rrMsIgnored, atrialRate = 80, ventricularRate = 40) {
    // TODO: build a ventricular-rate beat (wide-ish QRS, no fixed PR)
    // TODO: walk atrialPhaseMs through this beat's duration; drop a P wave each
    //       time it passes a multiple of 60000/atrialRate, then carry the remainder over
  },
};
```

### Your tasks

1. Add a capno canvas (yellow, 0–50 mmHg) driven by `Capno.next()` in the same loop.
2. Add the three rhythms to your `switch`. Check that VFib makes the arterial line and pleth decay flat, because nothing triggers them.
3. Alarms: add CSS `.alarm { color: red; animation: blink 1s infinite; }` and toggle it on the HR box with `el.classList.toggle("alarm", condition)` for VTach, VFib, MAP < 65 and SpO₂ < 90.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Capno phases</b>: Hint 1</summary>

An `if` / `else if` chain on `f`. For the linear rise, how far through phase II are you? `(f - 0.40) / 0.10` goes 0 → 1.

</details>

<details>
<summary><b>CHB carry-over</b>: Hint 1</summary>

Keep `atrialPhaseMs` between calls. Each beat adds its duration; whenever it passes the P–P interval, place a P wave at that offset and subtract the interval. The remainder carries into the next beat.

</details>

<details>
<summary><b>VFib with no pulse</b>: Hint 1</summary>

`CardiacSource` only fires listeners when `index === rOffset`. Since `-1` never matches, nothing triggers the pumps.

</details>


### Things to consider

- Change HR and the CO₂ trace shouldn't change at all. That's a quick way to prove your two clocks are independent.
- Naming varies between books: some call the inspiratory downstroke "phase 0" and reserve "phase IV" for an end-plateau upswing. Write a one-line comment about which convention you're using.
- VFib and asystole are cardiac-arrest rhythms. The "flat arterial line" is the point of the lesson: no effective circulation.

### Checkpoint

- RR 14 → **4.29 s** per breath, **1071** samples per breath.
- With EtCO₂ 38: phase 0.20 → **0**, 0.45 → **19**, 0.70 → **38**, 0.92 → **≈20.3**.

**References:** *Capnography and Pulse Oximetry*, StatPearls NBK539754 (four phases; normal EtCO₂ 35–45 mmHg) · *Components of a time capnogram*, capnography.com · LITFL, *Capnography Waveform Interpretation* · NUEM Blog / EMS1 (EtCO₂ falls with low cardiac output, PE, arrest) · *Project 3* textbook, Ex 5.2 and 5.3

---

## Week 21 — Mechanical circulatory support: Impella and ECMO

**Goal:** devices that flatten the arterial pulse as flow rises, raise MAP on VA-ECMO, and change SpO₂ correctly for VV vs VA.

**New concepts (JS):** objects with methods that read each other through `this`; a device "manager" that combines several devices into one effect.

### Starter code — `web/js/devices.js`

```js
import { P } from "./patient.js";

export const devices = {
  impella: {
    on: false, level: 0,
    flowTable: [0, 1.0, 1.5, 2.0, 2.5, 2.8, 3.2, 3.5, 4.0, 4.3],   // Impella CP, P0–P9 (L/min)
    flow() { return this.on ? this.flowTable[this.level] : 0; },
  },
  ecmo: {
    on: false, mode: "VA", flow: 3.0,
    arterialFlow() { return this.on && this.mode === "VA" ? this.flow : 0; },  // VV adds no circulation
  },

  pulsatility() {
    const deviceFlow = this.impella.flow() + this.ecmo.arterialFlow();
    const linear = P.nativeCO / (P.nativeCO + deviceFlow);
    // Squared: a TUNING choice so high flow flattens the a-line hard, as seen clinically.
    // pulsatility = max(0.08, linear²)
    // TODO
  },

  mapOffset() {
    // TODO: VA-ECMO raises mean pressure: about 2.2 mmHg per L/min of arterial flow
  },

  spo2(nativeSpo2) {
    const e = this.ecmo;
    if (!e.on || e.flow === 0) return nativeSpo2;
    if (e.mode === "VV") {
      // VV: ECMO is IN SERIES. A fraction of venous return (flow / CO) is fully
      // oxygenated before it reaches the lungs. Recirculation is ignored.
      // Saturation = frac·100 + (1 − frac)·native, with frac = flow / CO (at most 1)
      // TODO
    }
    // VA: oxygenated blood joins the arterial side IN PARALLEL with native output
    // TODO: flow-weighted mix of nativeCO @ nativeSpo2 and e.flow @ 100
  },

  lvRisk() {
    // VA-ECMO adds afterload; an Impella unloads the LV ("ECPELLA")
    if (!this.ecmo.on || this.ecmo.mode !== "VA") return 0;
    // risk = ECMO load (0.2 × ECMO flow) − Impella unloading (0.25 × Impella flow), never below 0
    // TODO
  },
};
```

### Applying it (in your `heart.onR` handler)

```js
const puls = devices.pulsatility();
const m = map() + devices.mapOffset();
const pp = (P.sbp - P.dbp) * puls * amp;
// keep the MEAN where it belongs, then shrink the swing around it:
// TODO: centre the swing on the MAP (2/3 of pp above it, 1/3 below), then
//       trigger with puls as `sharp`, so the notch fades as support rises
// pleth: plethPump.trigger(0.7 * amp * Math.max(0.12, puls), 0, puls)
```

### Your tasks

1. Build a device panel: Impella on/off plus a P-level slider (0–9); ECMO on/off, a VA/VV select and a flow slider.
2. Display pulse pressure, MAP, a "LV distension risk" readout and the device-adjusted SpO₂.
3. Make `P.nativeCO` a slider too. Lower it to 2.0 (cardiogenic shock) and watch the same Impella level flatten the line much more.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>VA mix</b>: Hint 1</summary>

Same idea as the fresh-gas FiO₂ formula: (Q_native·SpO₂_native + Q_ECMO·100) / (Q_native + Q_ECMO).

</details>

<details>
<summary><b>Centring on MAP</b>: Hint 1</summary>

Two-thirds of the pulse pressure sits above MAP and one-third below. That's where the MAP ≈ DBP + PP/3 rule comes from.

</details>
<details>
<summary><b>Centring on MAP</b>: Hint 2 (nearly the answer)</summary>

```js
const sys = m + 2 * pp / 3;
const dia = m - pp / 3;
art.trigger(sys, dia, puls);
```

</details>


### Things to consider

- **The bug this replaces:** the old workbook mixed VV-ECMO in parallel, giving 92% for native 85%, CO 4.5 and flow 4.0. In series it's about 98%. Which model fits VA-ECMO's "differential hypoxia" (good O₂ to the legs, poor O₂ to the right hand)? Your simple VA mix ignores *where* the probe is. Note that as a limitation.
- A pulse pressure **> 10 mmHg** is commonly used as a sign that the LV is still ejecting on VA-ECMO. Find the flow at which your model crosses it.
- Why is `pulsatility()` on `devices` rather than computed in `main.js`? Because then the arterial line, the pleth and the readouts all ask one place.

### Checkpoint

Native CO 4.5, 120/80 (PP 40):

| device flow (L/min) | 0 | 2.0 | 3.2 | 4.3 | 6.0 |
|---|---|---|---|---|---|
| pulsatility | 1.00 | 0.479 | 0.342 | 0.261 | 0.184 |
| displayed PP (mmHg) | 40 | 19.2 | 13.7 | 10.5 | 7.3 |

VV-ECMO at 4.0 L/min, native SpO₂ 85, CO 4.5 → **≈98%**.

**References:** *Unloading the Left Ventricle in Venoarterial ECMO*. *Circulation* 2022. doi:10.1161/CIRCULATIONAHA.122.062371 · *LV distension and venting strategies on VA-ECMO*, PMC6531683 (pulse pressure > 10 mmHg suggests the LV is still ejecting) · *Flow Optimization… Prevention of LV Distention during VA-ECMO*, IntechOpen 2018 (ECPELLA) · *Project 3* textbook, Ex 6.1, 6.3–6.5

---

## Week 22 — IABP: counterpulsation timed off the ECG

**Goal:** a balloon that **inflates at the dicrotic notch** and **deflates on the R-wave**, giving the classic assisted waveform at 1:1 or 1:2.

**New concepts (JS):** adding behavior to an existing class through hooks, without rewriting it; event-driven timing (the R-wave *is* the deflation trigger, just as on a real console).

### The design

Add an `iabp` term that `PulsePump.next()` adds to its output:

- **Inflate:** once `ms` passes the notch (about 290 ms), the term rises over about 40 ms to roughly 35 mmHg and then sags slowly, giving diastolic augmentation.
- **Deflate:** the next R-wave arrives about 150 ms *before* the next upstroke. On that R-wave, ramp the term from wherever it is down to about **−18 mmHg** over 120 ms. The next upstroke then starts from this lower pressure, which is the "assisted end-diastolic pressure".
- **Assisted systole:** on assisted beats, aim systole about 5 mmHg lower (less afterload).
- **Ratio:** assist every beat (1:1) or every other beat (1:2) using a beat counter.

### Starter code — additions to `PulsePump`

```js
// in the constructor
this.iabp = { enabled: false, ratio: 1, count: 0, assisting: false, term: 0, deflating: null };

// public hook: call from heart.onR(...) BEFORE trigger()
deflate() {
  const b = this.iabp;
  if (!b.enabled || !b.assisting) return;
  b.deflating = { k: 0, from: b.term };         // start the ramp down from the current term
}

// in next(), when a new upstroke begins:
//   TODO: count the beat and decide whether this one is assisted (ratio)
//   TODO: reset the balloon term; on assisted beats aim systole 5 mmHg lower

// in next(), after computing v:
//   TODO: if deflating, ramp the term from its starting value down to −18 over ~120 ms
//   TODO: otherwise, on assisted beats past ~290 ms, inflate: rise to ~35 over ~40 ms, then sag slowly
//   TODO: add the term to v
```

### Your tasks

1. Add the hooks, a toggle and a 1:1 / 1:2 select.
2. Use 1:2 to compare assisted and unassisted beats side by side, and label them.
3. Look at what happens at HR 150. (Hint: when does the next R-wave arrive compared with the notch?)
4. Commit, and write a `DEVLOG.md` entry. The monitor is complete.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Deciding assisted beats</b>: Hint 1</summary>

Same `%` trick as bigeminy: with a counter, `count % ratio === 0` is true every `ratio`-th beat.

</details>

<details>
<summary><b>Balloon term code</b>: Hint 1</summary>

Deflation is a ramp from `from` to −18 using `smoothstep(Math.min(1, k / samplesFor(120)))`. Inflation is `35 * smoothstep(...)` over 40 ms, multiplied by a slow `Math.exp(-(ms - 330) / 600)` sag.

</details>
<details>
<summary><b>Balloon term code</b>: Hint 2 (nearly the answer)</summary>

```js
// on a new upstroke:
b.count++; b.assisting = b.enabled && (b.count % b.ratio === 0);
b.term = 0; b.deflating = null;
if (b.assisting) sys -= 5;

// after computing v:
if (b.deflating) {
  b.deflating.k++;
  const u = smoothstep(Math.min(1, b.deflating.k / samplesFor(120)));
  b.term = b.deflating.from + (-18 - b.deflating.from) * u;
} else if (b.assisting && ms >= 290) {
  b.term = 35 * smoothstep(Math.min(1, (ms - 290) / 40)) * Math.exp(-Math.max(0, ms - 330) / 600);
}
v += b.term;
```

</details>


### Things to consider

- At HR 150 the augmentation disappears: the R-wave (deflate) comes about 250 ms after the upstroke, *before* the notch (inflate). Real consoles shorten timing at fast rates, and clinicians often switch to 1:2. Your model just showed you why.
- Stretch: add timing-error modes. *Early inflation* moves the inflation point before the notch, so systole and augmentation merge and the V disappears. *Late deflation* delays the ramp past the upstroke. Each one is a single number changed.
- Why was the old IABP's end-diastolic dip "wrong" at normal heart rates? Its fixed-length pulse deflated about 650 ms before the next beat at HR 60, which is the *early deflation* error pattern.

### Checkpoint

120/80, IABP 1:1, steady state:

| HR | assisted systole | augmentation peak | assisted end-diastolic |
|---|---|---|---|
| 60 | 115 | **≈130** | **≈63** |
| 75 | 115 | **≈130** | **≈64** |
| 150 | 115 | *(no augmentation)* | ≈73 |

These match the textbook targets: augmentation above unassisted systole, assisted end-diastolic pressure 15–20 mmHg lower, and assisted systole about 5 mmHg lower.

**References:** *The Intra-aortic Balloon Pump: A Focused Review*, 2024, PMC11307388 (augmentation exceeds unassisted systole; assisted EDP 15–20 mmHg lower; assisted systole about 5 mmHg lower) · EMCrit IBCC, *Intra-aortic balloon pump*. emcrit.org/ibcc/iabp/ · LITFL, *IABP Trouble-shooting* (timing-error waveforms) · NCBI Bookshelf NBK543576 (inflation at the dicrotic notch) · *Project 3* textbook, Ex 6.2

---

# PART 4 — OPTIONAL CAPSTONE: one page, three simulators

You have three working projects. These three weeks put them on one web page. All of it is optional, and each week is useful on its own.

Final layout of `index.html`:

```
┌────────────────────────── Monitor (Part 3) ─────────────────────────┐
│ ECG / ART / PLETH / CO2 sweeps                        HR BP SpO2 EtCO2 │
├──────────── Machine (Week 23) ───────────┬──── TCI (Week 24) ─────────┤
│ agent · dial · O2/air/N2O · MAC · FiO2   │ Cp/Ce chart from JSON      │
└──────────────────────────────────────────┴────────────────────────────┘
```

---

## Week 23 — Port the anesthesia machine to JavaScript

**Goal:** `machine.js`, a JS translation of your Part 2 Python, running live in the page.

**New concepts (JS):** class getters (`get cardiacOutput()`, JS's version of `@property`); objects as dictionaries (`Object.entries`); checking that two languages give identical numbers.

**Read first:** [javascript.info: Getters and setters](https://javascript.info/property-accessors) · [javascript.info: Object.keys, values, entries](https://javascript.info/keys-values-entries)

### Starter code — `web/js/machine.js`

```js
import { Compartment } from "./math.js";     // you already ported this in Week 13

export const AGENTS = {
  sevoflurane: { name: "Sevoflurane", mac: 2.0, bloodGas: 0.65, lam: { VRG: 1.7, muscle: 3.1, fat: 48 } },
  // TODO: isoflurane, desflurane, nitrous_oxide
};

export class VolatileModel {
  constructor(agent) {
    this.agent = agent;
    this.comps = {
      VRG: new Compartment("VRG", 6.0, 4.2),
      muscle: new Compartment("Muscle", 33.0, 0.9),
      fat: new Compartment("Fat", 14.5, 0.35),
    };
    this.alveolar = 0; this.circuit = 0; this.dial = 0;
    this.o2Flow = 8; this.airFlow = 0; this.n2oFlow = 0;
    this.rr = 14; this.tv = 0.5; this.FRC = 2.5; this.deadSpace = 0.3;
    this.time = 0; this.lastUptake = 0; this.extraRate = 0;
  }
  get freshGasFlow() { return this.o2Flow + this.airFlow + this.n2oFlow; }
  get cardiacOutput() {
    // TODO: sum of the compartment flows
  }
  step(dt) {
    // TODO: the same five equations, in the same order, as your Python step()
  }
}
```

### Your tasks

1. Translate `step()` line by line from your Python. Keep the two files open side by side.
2. In `tests.js`, run sevo 2% for 5 simulated minutes (`3000` steps of `0.1/60`) and check against the Week 9 table: FA **1.549**, VRG **2.091**. The two languages should agree to 3 decimals.
3. Build the machine panel: agent buttons, a dial slider, O₂/air/N₂O flows, a big color-coded MAC number (< 0.5 red, < 1.0 orange, < 1.3 yellow, ≥ 1.3 green), and inspired FiO₂ with the hypoxic alarm.
4. Advance the machine in `loop()` with a speed multiplier, for example 10 × real time. Large `dt` values make Euler steps unstable, so take many small steps per frame rather than one big one.
5. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Summing in JS</b>: Hint 1</summary>

`Object.values(obj)` gives an array of the values. `.reduce((sum, c) => sum + c.flow, 0)` adds them up, starting from 0.

</details>

<details>
<summary><b>Translation order</b>: Hint 1</summary>

Translate one Python helper at a time (`_mixedVenous`, `_inspired`) and test each against a hand-picked input before writing `step()`. That's the same order you used in Week 9.

</details>


### Things to consider

- If JS and Python disagree, the bug is almost always equation order, a `=` that should be `+=`, or a missing `this.`.
- At 10× speed and 60 frames per second, how many `0.1/60` steps do you need per frame? Does that run fast enough? Open DevTools → Performance if it stutters.

**References:** Same as Weeks 8–11

---

## Week 24 — The TCI panel: Python writes JSON, JavaScript reads it

**Goal:** show the Part 1 simulations in the page, without rewriting them in JS.

**New concepts (JS):** `fetch`; `async`/`await` (waiting for a file without freezing the page); using a library from a CDN.

**Read first:** [javascript.info: Promises, async/await](https://javascript.info/async) (chapters on Promise basics and async/await) · [MDN: Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) · [Chart.js docs](https://www.chartjs.org/docs/latest/)

### Starter code — `web/js/tci_panel.js`

```js
export async function loadRun(path) {
  const res = await fetch(path);                  // wait for the file to arrive
  if (!res.ok) throw new Error(`Couldn't load ${path}: ${res.status}`);
  return await res.json();                        // text -> JS object, the same shape you saved
}

export async function showRun(canvas, path) {
  const run = await loadRun(path);
  // Option A: your own drawStatic() from Week 15 (Cp and Ce as two calls)
  // Option B: Chart.js. Add to index.html:
  //   <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  //   new Chart(canvas, { type: "line", data: { labels: run.t, datasets: [...] } })
  // TODO
}
```

### Your tasks

1. In Python, write a script that exports several runs: Roberts 70 kg, Marsh vs Schnider, and a 5 vs 120 min infusion. Also write `web/data/index.json` listing the file names.
2. In JS, load `index.json`, fill a `<select>` with it, and plot whichever run is chosen.
3. Show peak Ce and time-to-peak beside the chart. Should you compute them in JS, or have Python include them in the JSON? Decide, and note why in `DEVLOG.md`.
4. Commit.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b>Filling a <code><select></code></b>: Hint 1</summary>

For each file name, `const opt = document.createElement("option"); opt.value = opt.textContent = name; sel.append(opt);`.

</details>

<details>
<summary><b>Chart.js datasets</b>: Hint 1</summary>

One dataset per line: `{ label: "Ce", data: run.ce, pointRadius: 0 }`. `labels` is the time array.

</details>


### Things to consider

- `fetch` only works through the `http.server`. Opening `index.html` by double-clicking will fail, the same as Week 13.
- If you forget `await`, `run` is a *Promise* (a "value arriving later"), and `run.t` is `undefined`. This is the most common async bug.
- This "Python computes, JS displays" split is how many real tools work. A later step could run Python live in the browser (Pyodide), but you don't need that now.

**References:** Same as Weeks 1–7

---

## Week 25 — The bridge: opioid MAC-sparing, then deploy

**Goal:** connect the TCI and machine panels clinically, and put the whole page online.

**Read first:** [GitHub Pages: creating a site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

### The clinical link (the most important point of this capstone)

Two *inhaled* agents add by MAC (Week 10). **IV drugs have no MAC.** Remifentanil doesn't add MAC. It **reduces how much volatile you need** (Lang et al. 1996: about 50% isoflurane MAC reduction at about 1.37 ng/mL, with a ceiling of about 90%).

```js
export function macReduction(remiCe, emax = 0.9, ec50 = 1.096) {
  // Saturating Emax curve fitted so macReduction(1.37) = 0.5:
  //   reduction = Emax·Ce / (EC50 + Ce)
  // TODO
}
// effective required MAC = baseline × (1 − macReduction(remiCe))
// show: "volatile 0.8 MAC + remi 1.4 ng/mL → equivalent to ≈1.6 MAC"
```

### Your tasks

1. Load a remifentanil run (Minto) exported from Python. Let the user pick a minute, and read remi Ce at that time.
2. In the machine panel, show *effective* MAC = volatile MAC ÷ (1 − reduction), with the same color scale. Raising remi should move the patient from "light" toward "surgical" **without touching the dial**.
3. Deploy: push `web/` to GitHub, then go to Settings → Pages → deploy from your branch. You get a live URL to share, and everything runs in the browser.
4. Final `DEVLOG.md` entry: what you'd build next.

### Hints (open only when stuck)

Try each TODO for 15–20 minutes before opening a hint. Open Hint 1 first.

<details>
<summary><b><code>macReduction</code></b>: Hint 1</summary>

One line of arithmetic, straight from the formula in the comment.

</details>

<details>
<summary><b>Effective MAC</b>: Hint 1</summary>

Divide the volatile MAC by `(1 - macReduction(remiCe))`. Check it against the checkpoint: 0.8 ÷ 0.5 = 1.6.

</details>


### Checkpoint

`macReduction(1.37)` = **0.50**. With 0.8 MAC of volatile and remi at 1.37 ng/mL, the effective MAC is **1.6**.

> Label it on screen: "Model of opioid MAC-sparing (Lang 1996). Fitted to published points, not a per-patient prediction."

**References:** Lang E, Kapila A, Shlugman D, Hoke JF, Sebel PS, Glass PSA. Reduction of isoflurane minimum alveolar concentration by remifentanil. *Anesthesiology* 1996;85:721–8 · McEwan AI, Smith C, Dyar O, Goodman D, Glass PSA. Isoflurane MAC reduction by fentanyl. *Anesthesiology* 1993;78:864–9

---

# Appendices

## A. When you're stuck: a debugging checklist

1. **Read the whole error.** In Python, read the *last* line first, then the line in *your* file. In JS, click the file:line link in the console.
2. **Shrink it.** Copy the failing function into a scratch file and give it one fixed input.
3. **Print every intermediate.** `print(f"{A1=} {Cp=}")` in Python (the `=` prints the name too). `console.log({ A1, Cp })` in JS.
4. **Check units.** Minutes vs seconds, % vs fraction, mg vs µg. This is about a third of all bugs in this workbook.
5. **Check order.** Equations that depend on each other, and "record, then advance" vs "advance, then record".
6. **Check the test, too.** Occasionally the expected number is wrong. Every number here came from a reference run, but your settings (`dt`, `steps_per_min`) have to match.
7. **Walk away for 10 minutes.** Seriously.

## B. JavaScript traps that Python programmers hit

| Trap | What happens | Fix |
|---|---|---|
| `"75" + 5` | `"755"` | `parseFloat()` everything from the page |
| `==` | `0 == ""` is `true` | always use `===` |
| forgot `return` | function gives `undefined` | check every function returns |
| forgot `this.` in a class | `ReferenceError` or a silent global | always `this.` |
| forgot `await` | you get a Promise, not data | `await` inside an `async` function |
| math on `undefined` | `NaN` spreads silently | `console.log` inputs, use `check()` tests |
| opening `index.html` directly | imports and fetch fail | `python -m http.server` |

## C. What changed from the earlier workbooks

| Old | Problem | Now |
|---|---|---|
| Second gas: `alveolar *= 1 + uptake*0.01` per step | Timestep-dependent; sevo went to infinity in 3 min | A rate term `FA·U/FRC` inside dFA/dt (Week 10) |
| Decrement loop `sim.time < 60/60` | 1-minute cap, absolute clock; never ran after 30 min | Elapsed time from `t0`, true 60-minute cap (Week 12) |
| CO 5.0 while tissue flows sum to 5.45 | Inconsistent mass balance | `cardiac_output` is a property: the sum of flows (Week 9) |
| VRG MAC = tissue conc / MAC | Ignored λ; showed brain at 1.7 MAC when alveolar was 1 MAC | Partial pressure = C/λ first (Weeks 8–9) |
| Fixed 350 ms arterial pulse + flat hold | Flat diastole, 3 mmHg step, early notch, broke at high HR | Continuous `PulsePump` decay from the current pressure (Week 19) |
| IABP on the fixed-length pulse | EDP only ~7 mmHg lower; drew *early deflation* | Inflate at notch, deflate on R-wave (Week 22) |
| VV-ECMO SpO₂ mixed in parallel | 92% where ~98% is expected | VV in series, VA in parallel (Week 21) |
| T wave width 0.25 | 0.04 step at its edges | Edge-subtracted, rescaled T (Week 15) |
| Native CO fixed at 4.5 | Shock scenarios unrealistic | `P.nativeCO` is a control (Week 21) |

## D. Full reference list

These are the references from your original workbooks (the TCI roadmap, the volatile curriculum, the waveform program and the FiO₂ module) and the citations in your `patient.py` docstrings, grouped by project.

### Body size (your `Patient` class)
1. James WPT. *Research on Obesity: A Report of the DHSS/MRC Group*. London: HMSO; 1976. (James lean-body-mass formula, used by Schnider)
2. Lemmens HJM, Brodsky JB, Bernstein DP. Estimating ideal body weight: a new formula. *Obes Surg* 2005;15:1082–1083.
3. Al-Sallami HS, Goulding A, Grant A, et al. Prediction of fat-free mass in children. *Clin Pharmacokinet* 2015;54:1169–1178. (Fat-free mass for Eleveld)
4. Servin F, Farinotti R, Haberer JP, Desmonts JM. Propofol infusion for maintenance of anesthesia in morbidly obese patients receiving nitrous oxide. *Anesthesiology* 1993;78:657–665. (Adjusted body weight)

### Part 1: TCI pharmacokinetics and pharmacodynamics
5. Marsh B, White M, Morton N, Kenny GN. Pharmacokinetic model driven infusion of propofol in children. *Br J Anaesth* 1991;67:41–48.
6. Schnider TW, Minto CF, Gambus PL, et al. The influence of method of administration and covariates on the pharmacokinetics of propofol in adult volunteers. *Anesthesiology* 1998;88:1170–1182.
7. Schnider TW, Minto CF, Shafer SL, et al. The influence of age on propofol pharmacodynamics. *Anesthesiology* 1999;90:1502–1516.
8. Minto CF, Schnider TW, Egan TD, et al. Influence of age and gender on the pharmacokinetics and pharmacodynamics of remifentanil. I. Model development. *Anesthesiology* 1997;86:10–23.
9. Eleveld DJ, Colin P, Absalom AR, Struys MMRF. Pharmacokinetic–pharmacodynamic model for propofol for broad application in anaesthesia and sedation. *Br J Anaesth* 2018;120:942–959. (Read Table 2 before extending beyond the reference individual.)
10. Roberts FL, Dixon J, Lewis GT, Tackley RM, Prys-Roberts C. Induction and maintenance of propofol anaesthesia: a manual infusion scheme. *Anaesthesia* 1988;43(Suppl):14–17.
11. Sheiner LB, Stanski DR, Vozeh S, Miller RD, Ham J. Simultaneous modeling of pharmacokinetics and pharmacodynamics: application to d-tubocurarine. *Clin Pharmacol Ther* 1979;25:358–371.
12. Bouillon TW, Bruhn J, Radulescu L, et al. Pharmacodynamic interaction between propofol and remifentanil regarding hypnosis, tolerance of laryngoscopy, bispectral index, and electroencephalographic approximate entropy. *Anesthesiology* 2004;100:1353–1372.
13. Kern SE, Xie G, White JL, Egan TD. Opioid–hypnotic synergy: a response surface analysis of propofol–remifentanil pharmacodynamic interaction in volunteers. *Anesthesiology* 2004;100:1373–1381.
14. Johnson KB, Syroid ND, Gupta DK, et al. An evaluation of remifentanil–propofol response surfaces for loss of responsiveness, loss of response to surrogates of painful stimuli and laryngoscopy in patients undergoing elective surgery. *Anesth Analg* 2008;106:471–479.
15. Greco WR, Bravo G, Parsons JC. The search for synergy: a critical review from a response surface perspective. *Pharmacol Rev* 1995;47:331–385.
16. Hughes MA, Glass PSA, Jacobs JR. Context-sensitive half-time in multicompartment pharmacokinetic models for intravenous anesthetic drugs. *Anesthesiology* 1992;76:334–341.
17. Bailey JM. Context-sensitive half-times: what are they and how valuable are they in anaesthesiology? *Clin Pharmacokinet* 2002;41:793–799.

### Part 2: Anesthesia machine and volatile agents
18. Eger EI, Saidman LJ, Brandstater B. Minimum alveolar anesthetic concentration: a standard of anesthetic potency. *Anesthesiology* 1965;26:756–763.
19. Eger EI II. The effect of inspired anesthetic concentration on the rate of rise of alveolar concentration. *Anesthesiology* 1963;24:153–157.
20. Eger EI II. *Anesthetic Uptake and Action*. Baltimore: Williams & Wilkins; 1974.
21. Epstein RM, Rackow H, Salanitre E, Wolf GL. Influence of the concentration effect on the uptake of anesthetic mixtures: the second gas effect. *Anesthesiology* 1964;25:364–371.
22. Stoelting RK, Eger EI II. An additional explanation for the second gas effect: a concentrating effect. *Anesthesiology* 1969;30:273–277.
23. Taheri S, Eger EI II. A demonstration of the concentration and second gas effects in humans anesthetized with nitrous oxide and desflurane. *Anesth Analg* 1999;89:774–780.
24. Korman B, Mapleson WW. Concentration and second gas effects: can the accepted explanation be improved? *Br J Anaesth* 1997;78:618–625.
25. Hendrickx JFA, Carette R, Lemmens HJM, De Wolf AM. Large volume N₂O uptake alone does not explain the second gas effect of N₂O on sevoflurane during constant inspired ventilation. *Br J Anaesth* 2006;96:391–395.
26. Yasuda N, Lockhart SH, Eger EI II, et al. Comparison of kinetics of sevoflurane and isoflurane in humans. *Anesth Analg* 1991;72:316–324.
27. Philip JH. Gas Man: an example of goal-oriented computer-assisted teaching which results in learning. *Int J Clin Monit Comput* 1986;3:165–173.
28. Philip JH. *Gas Man: Understanding Anesthesia Uptake and Distribution*. Med Man Simulations Inc. (gasmanweb.com).
29. Baum JA. *Low Flow Anaesthesia: The Theory and Practice of Low Flow, Minimal Flow and Closed System Anaesthesia*. 2nd ed. Butterworth-Heinemann; 2001.
30. Mapleson WW. The concept of the time constant applied to breathing systems and to the body.
31. Hendrickx JFA, De Wolf AM. The anaesthesia workstation: quo vadis? *Anesth Analg* 2018;127:671–675.
32. ISO 80601-2-13: Particular requirements for the basic safety and essential performance of an anaesthetic workstation (O₂:N₂O hypoxic guard).
33. Lang E, Kapila A, Shlugman D, Hoke JF, Sebel PS, Glass PSA. Reduction of isoflurane minimum alveolar concentration by remifentanil. *Anesthesiology* 1996;85:721–728.
34. McEwan AI, Smith C, Dyar O, Goodman D, Glass PSA. Isoflurane MAC reduction by fentanyl. *Anesthesiology* 1993;78:864–869.

### Part 3: Monitor waveforms and mechanical circulatory support
35. *Project 3: Medical Waveform Training Platform* textbook (`Project3_Waveform_Platform_Textbook.docx`). Exercise numbers are cited per week.
36. Stouffer GA. Arterial pressure (ch. 4). thoracickey.com/4-arterial-pressure/ (anacrotic limb, dicrotic notch at aortic valve closure, dicrotic wave from arterial recoil).
37. Deranged Physiology. *Normal arterial line waveforms*. derangedphysiology.com (MAP from the area under the curve is more accurate than the ⅓ estimate).
38. *Arterial Lines*. anaestheasier.com/arterial-lines/ (three components; incisura vs dicrotic notch).
39. *Broader applications of arterial pressure waveform analysis*. *BJA Education* 2017. bjaed.org (dicrotic notch about ⅓ down the descending limb).
40. *Unloading the Left Ventricle in Venoarterial ECMO*. *Circulation* 2022. doi:10.1161/CIRCULATIONAHA.122.062371.
41. *Left ventricular distension and venting strategies during VA-ECMO*. PMC6531683 (pulse pressure > 10 mmHg suggests the LV is still ejecting).
42. *Flow Optimization, Management, and Prevention of LV Distention during VA-ECMO*. IntechOpen; 2018 (ECPELLA pathophysiology).
43. *The Intra-aortic Balloon Pump: A Focused Review*. 2024. PMC11307388 (augmentation exceeds unassisted systole; assisted EDP 15–20 mmHg lower; assisted systole about 5 mmHg lower; sharp V at the notch).
44. EMCrit IBCC. *Intra-aortic balloon pump*. emcrit.org/ibcc/iabp/
45. LITFL. *IABP Trouble-shooting* (early and late inflation/deflation waveforms).
46. NCBI Bookshelf NBK543576 (figure: inflation at the dicrotic notch; augmentation above unassisted systole).
47. *Capnography and Pulse Oximetry*. StatPearls, NCBI Bookshelf NBK539754 (four capnogram phases; normal EtCO₂ 35–45 mmHg; SpO₂ from the red/infrared ratio, not trace height).
48. *Components of a time capnogram*. capnography.com (phase III up-slope, phase IV down-stroke).
49. LITFL. *Capnography Waveform Interpretation*.
50. NUEM Blog / EMS1: EtCO₂ falls with low cardiac output, pulmonary embolism and arrest.
51. NursingCE: pulse oximetry and the plethysmograph (amplitude reflects perfusion).

## E. Learning resources

**Python**
- [The Python Tutorial](https://docs.python.org/3/tutorial/), especially §9 Classes
- [pytest: Get started](https://docs.pytest.org/en/stable/getting-started.html)
- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Matplotlib Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)
- [SciPy `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [Pro Git, chapter 2: Git basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

**JavaScript and the web**
- [javascript.info: The Modern JavaScript Tutorial](https://javascript.info/) (start with [Fundamentals](https://javascript.info/first-steps), then [Document](https://javascript.info/document) and [Events](https://javascript.info/events))
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [MDN Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development)
- [MDN JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [MDN Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial) and [Basic animations](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations)
- [MDN `requestAnimationFrame`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame)
- [MDN Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Chart.js documentation](https://www.chartjs.org/docs/latest/)
- [GitHub Pages: creating a site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

*A teaching simulator. Not a medical device, and not for clinical decisions.*
