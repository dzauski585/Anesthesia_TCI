Two reference patients recur through every step below:
- **Patient A** — 40yo M, 70 kg, 170 cm (round numbers, easy to also
  check by hand on a calculator)
- **Patient B** — 53yo, 77 kg, 177 cm, run once as M and once as F (the
  classic Schnider-paper reference body, useful later too)


## Step 2 — Validation

**Practicing:** raising exceptions on purpose (`TypeError` vs.
`ValueError` — different exception for "wrong kind of thing" vs. "right
kind of thing, bad value"), `isinstance()`, writing an f-string error
message that shows the bad value back to the caller.

**Spec:** before storing anything, check each argument and raise if it
fails:
- `age` — must be `int` (`TypeError` if not), must be `> 0`
  (`ValueError` if not)
- `weight`, `height` — must be `int` or `float` (`TypeError`), must be
  `> 0` (`ValueError`)
- `sex` — must be `str` (`TypeError`), must be exactly `"M"` or `"F"`
  (`ValueError`)

Check type before value for each one — comparing a non-number to `0`
isn't meaningful, so there's nothing to check until you know it's a
number.

**Checkpoint:** this is exactly what `test_invalid_age_raises_error` in
`test_patient.py` already checks — rerun it, it should pass again. Also
try `Patient(age=40.5, weight=70, height=170, sex="M")` by hand in a
scratch script: it should raise `TypeError`, not silently round `40.5`
down.

---

## Step 3 — BMI

**Practicing:** a "private" helper method (leading underscore signals
"implementation detail, not part of the public interface"), calling it
from `__init__`, storing the result as `self.bmi`.

**Spec:** `_calculate_bmi(self) -> float`.
BMI = weight_kg / (height_m)², where height_m = height / 100.

**Checkpoint:**

| Patient | BMI |
|---|---|
| A (70 kg, 170 cm) | 24.22 |
| B (77 kg, 177 cm) | 24.58 |

BMI is the same for the M and F versions of Patient B — it doesn't
depend on sex, so that's also a sanity check that you didn't
accidentally branch on sex here.

Fill in `test_bmi_known_value` in `test_patient.py` now — you have the
number.

---

## Step 4 — LBM (James formula)

**Practicing:** an `if`/`else` inside a helper method, branching on
another attribute (`self.sex`) you already validated and stored.

**Spec:** `_calculate_lbm(self) -> float`. James formula, cited for use
with the Schnider model:
- Male: `1.1 * weight - 128 * (weight / height) ** 2`
- Female: `1.07 * weight - 148 * (weight / height) ** 2`

Note the units switch from Step 3: here `height` is used in **cm**
directly, not converted to meters. Worth a comment in your own code —
this is exactly the kind of inconsistency-between-formulas that causes
real bugs if you copy-paste a pattern without rereading it.

**Checkpoint:**

| Patient | LBM |
|---|---|
| A (M) | 55.30 |
| B, M | 60.48 |
| B, F | 54.38 |

B-as-M and B-as-F must differ — if they come out equal, the branch
isn't firing. Fill in `test_lbm_differs_by_sex` now.

---

## Step 5 — IBW (Lemmens formula)

**Practicing:** the simplest of the remaining formulas — one input
only. Good, quick confidence-builder right after Step 4's branching.

**Spec:** `_calculate_ibw(self) -> float`. IBW = 22 × (height_m)².

**Checkpoint:**

| Patient | IBW |
|---|---|
| A (170 cm) | 63.58 |
| B (177 cm) | 68.92 |

Same value for B-as-M and B-as-F — height-only, so sex shouldn't move
this number at all.

---

## Step 6 — FFM (Al-Sallami formula)

**Practicing:** carefully transcribing a more complex published
formula (a sigmoid "maturation" term) without rushing it. This one also
*depends on* `self.bmi` from Step 3 — first real case in this class
where computation order inside `__init__` actually matters.

**Spec:** `_calculate_ffm(self) -> float`, sex-dependent:
- Male: `maturation = 0.88 + (1 - 0.88) / (1 + (age / 13.4) ** -12.7)`,
  then `ffm = maturation * (9270 * weight / (6680 + 216 * bmi))`
- Female: `maturation = 1.11 + (1 - 1.11) / (1 + (age / 7.1) ** -1.1)`,
  then `ffm = maturation * (9270 * weight / (8780 + 244 * bmi))`

`bmi` here means `self.bmi` — make sure `_calculate_bmi()` has already
run and been stored before this one is called.

**Checkpoint:**

| Patient | FFM |
|---|---|
| A (M) | 54.48 |
| B, M | 59.54 |
| B, F | 48.83 |

---

## Step 7 — Adjusted body weight

**Practicing:** a derived value built from two *already-computed*
attributes (`self.ibw`, `self.weight`) rather than a fresh formula —
this is the step that really tests whether `__init__` computes things
in the right order.

**Spec:** not a private helper this time — a single expression in
`__init__` itself:
`adjusted_weight = ibw + 0.4 * (weight - ibw)`
(Servin et al., *Anesthesiology* 1993 — obesity dosing adjustment;
cite it same as your reference file does.)

**Checkpoint:**

| Patient | adjusted_weight |
|---|---|
| A | 66.15 |
| B (M or F) | 72.15 |

---

## Step 8 — The rest: `post_menstrual_age_weeks`, `summary`, `__repr__`

**Practicing:** regular public methods (no underscore — callable after
construction), f-string formatting for human-readable output, and
`__repr__`, the special method Python calls when you `print()` an
object or inspect it in a debugger.

**Why bother with both — what's actually at stake:**

`__repr__` is a dunder method: Python calls it *automatically*,
without you asking, anywhere it needs to display your object and
nothing more specific has been defined — the interactive prompt, a
debugger watch, a logging call, and, easy to miss, **inside
containers**: `print([p1, p2])` calls `repr()` on each element, not
`summary()`. Skip `__repr__` entirely and you get Python's built-in
default instead: something like
`<patient.Patient object at 0x7f8a1c0d5490>` — a memory address, no
help at all for telling two patients apart mid-debug. That's the whole
case for writing it: a handful of lines now buys readable output
everywhere, forever, for free.

`summary()` is a different kind of thing wearing a similar hat — a
plain public method, *not* a dunder, so nothing calls it automatically.
`print(p)` will **not** show your nice one-line summary; it falls back
to `__repr__`, because Python only reaches for `__str__` (which this
class never defines) or, failing that, `__repr__`. You have to call
`p.summary()` yourself.

That split is a real design choice worth knowing the alternative to:
you could define `__str__(self) -> str` instead of `summary()`, with
the same content, and then plain `print(p)` would show it automatically
— no explicit call needed anywhere. The trade-off is implicit-and-
convenient (`__str__`) vs. explicit-and-visible-at-the-call-site
(`summary()`); neither is more "correct," codebases genuinely differ on
which they prefer. Worth trying both ways in scratch code, since the
point here is internalizing the pattern, not reproducing the original
file exactly.

One more consequence, since better OOP is the goal: right now
`Patient(40,70,170,'M') == Patient(40,70,170,'M')` evaluates to
`False`. Python's default `==` compares *identity* (same object in
memory), not whether the field values match, and nothing here
overrides that. Fixing it means writing `__eq__` by hand, field by
field — which is exactly what `@dataclass` auto-generates for you,
alongside `__repr__`. You're not missing anything by leaving it out
now; you're doing by hand, once, the thing `dataclass` would otherwise
hide from you, which is a good reason to skip it deliberately rather
than by accident.

**Spec:**
- `post_menstrual_age_weeks(self) -> float` — your original formula is
  `(age * 52) + 40`, a placeholder until real gestational age is
  available for pediatric use. When you write it fresh: decide for
  yourself whether to keep the formula as-is, or add a sharper comment
  flagging it as a stand-in. Either is fine — this is a judgment call
  you're making now, not a right answer to look up.
- `summary(self) -> str` — one formatted line with age, sex, weight,
  height, BMI, LBM.
- `__repr__(self) -> str` — shorter, shows the four constructor
  arguments back. This is what you'll see if you type a `Patient`
  object into the debugger watch panel or just `print(p)`.

**Checkpoint:** for Patient A, `print(p)` → `Patient (age=40, weight=70, height=170, sex=M)`,
and `p.summary()` → `Patient: 40yoM, 70kg, 170cm, BMI = 24.2, LBM = 55.30kg`.

---

## Step 9 — Full validation

Run `python test_patient.py`. If `All tests passed!` prints, and every
checkpoint above matched, your rebuild is functionally identical to
`patient_reference.py` — which is the actual goal here, not
line-for-line sameness.

Optional, once it passes: open both files side by side. You're not
copying anything at this point — you're looking for places your
approach to structuring validation or docstrings diverged from the
original, and deciding which version you actually prefer now that
you've written both.

## Milestone 1 — Patient class + first real tests

**Files:** `patient.py` (already written, carried over unmodified),
`test_patient.py` (started for you — you finish it)

Your `patient.py` is genuinely solid — validation, docstrings, correct
derived formulas. This milestone isn't about rewriting it, it's about
building the habit you'll lean on for every model after this:
**write down a number you trust, then assert your code matches it.**

Two small things worth a look on your own time, not blockers:
- `_calculate_lbm`'s docstring says "For Schneider" — should be Schnider.
- `post_menstrual_age_weeks()` is a placeholder formula that only makes
  real sense once there's a pediatric model in the picture. Fine to
  leave as-is for now; just don't forget it's a stub.

**Done when:** `python test_patient.py` prints `All tests passed!`

---

## Milestone 2 — One drug, as *parameters only*: Marsh

**File:** `pk_models.py` (repurposed — see below)

This is the step that breaks the old pattern. Your current
`pk_models.py` has `MarshModel` doing two jobs at once: computing Marsh's
volumes/clearances from weight, *and* running its own hand-written
integration loop. We're splitting those — this milestone is only the
first job. If you're ever unsure whether something belongs here or in
`engine.py`, ask: "does this number change per drug, or does the math
stay the same for every drug?" Numbers here, math in `engine.py`.

**A correction before you start — not a nitpick.** While pulling the
reference numbers below I checked your old `MarshModel` against Marsh's
actual published model, and against Week 5 of your own course notes,
and it's computing the wrong numbers. It treats all five rate constants
as if they scale with weight (`Cl1 = 0.119 * weight`, later
`k10 = Cl1 / V1`). Since `V1` also scales with weight, the weight
cancels out algebraically — but what's left (`k10 ≈ 0.119/0.228 ≈
0.52/min`) isn't the real Marsh `k10`. The actual, published Marsh
(1991) model defines the five rate constants as **fixed population
values that don't scale with weight at all** — only `V1` does.
`claudeengineaugust.py` already has this right (`k10=0.119` hardcoded,
not derived), and it's what your own Week 5 notes show too. This
milestone uses the correct version:

| | Marsh (1991), correct |
|---|---|
| V1 | 0.228 L/kg × weight |
| k10 | 0.119 /min (fixed) |
| k12 | 0.112 /min (fixed) |
| k13 | 0.0419 /min (fixed) |
| k21 | 0.055 /min (fixed) |
| k31 | 0.0033 /min (fixed) |

### Step 1 — Recognize the pattern before you touch the keyboard

**Practicing:** noticing that "a drug's parameters for one patient" is
structurally the *same problem* you already solved in the Patient
roadmap — you're not learning anything new about Python here, you're
reusing a shape you already built. That recognition is the actual
skill; the code is almost incidental.

**Concept, spelled out:** a class bundles some values together and
gives you a name for the bundle. `Patient` bundles age/weight/height/
sex plus derived numbers under the name "one patient." `MarshDrug` will
bundle six numbers under the name "Marsh's parameters for one patient."
Same three ingredients both times: a `class` statement, an `__init__`
that takes some inputs and computes/stores values onto `self`, and
nothing else needed to make it usable. If any of `class`, `__init__`,
or `self` feel shaky, that's worth a quick re-read of Patient roadmap
Step 1 before continuing — everything below assumes that part is solid
so it can focus on what's actually new (the physiology, not the class
mechanics).

### Step 2 — Decide the constructor's shape

**Spec:** `MarshDrug`, with `__init__(self, patient)`. Yes, the whole
`Patient` object, even though Marsh only ever reads `.weight` from it.
Every drug's parameter class in this project will take a full
`Patient` and use whatever slice of it that particular drug's formula
needs — Schnider will need age/weight/height/LBM in Milestone 5, Marsh
needs only weight — but the *interface* (what arguments you call it
with) stays identical across every drug. That consistency is what lets
the engine, and later the app, treat every drug the same way without
special-casing which one it's holding. (If this still feels abstract:
imagine the alternative, where `MarshDrug(weight)` and later
`SchniderDrug(age, weight, height, lbm)` had different argument lists —
any code that runs "whichever drug the user picked" would need an
`if`/`elif` per drug just to know what to pass in. One shared shape
avoids that entirely.)

### Step 3 — `V1`: the one number that actually depends on the patient

**Spec:** inside `__init__`, compute `self.V1` from `patient.weight`
using the coefficient in the table above (0.228 L/kg). This is the
only one of the six numbers that's *derived* — everything else in
Step 4 is a literal you type in directly, not computed from anything.

**Checkpoint (just this one number):** 70 kg → `V1 = 15.96`. Print it
and check before moving on — small checkpoints like this one catch a
typo (like swapping 0.228 for 0.288) immediately, rather than three
formulas later when it's harder to tell which line is wrong.

### Step 4 — The five fixed rate constants

**Concept:** these five don't get computed from anything — they're the
same number for every patient, every time. That might feel strange
right after Step 3 (where you *did* compute something), but it's
correct: Marsh's rate constants are population averages baked into the
model itself, not something derived per-patient. In code terms, this
just means five plain assignment lines, each a literal number from the
table — no arithmetic, no reference to `patient` at all.

**Spec:** store `self.k10`, `self.k12`, `self.k13`, `self.k21`,
`self.k31` as the five fixed values from the table. Add a class
docstring citing Marsh B, White M, Morton N, Kenny GN. *Br J Anaesth.*
1991;67(1):41-48 — the same reference your course notes already used.

**Full checkpoint** — 70 kg patient (Patient A, from the Patient
roadmap):

| | value |
|---|---|
| V1 | 15.96 L |
| k10 | 0.1190 |
| k12 | 0.1120 |
| k13 | 0.0419 |
| k21 | 0.0550 |
| k31 | 0.0033 |

Now change only the weight to 90 kg and rerun: `V1` should move (to
20.52), and **nothing else should**. If any rate constant changes too,
weight has snuck into a formula it shouldn't be in — the exact mistake
the old file made. This one experiment (change one input, see what
moves and what doesn't) is worth doing on every model you build from
here forward, not just this one.

### Step 5 — `__repr__`, same reasoning as Patient

**Spec:** one line, same idea as the Patient roadmap's Step 8 — show
the constructor inputs back, so a stray `print(drug)` mid-debug later
tells you something useful instead of a memory address. You don't need
`summary()`/`__str__` here — this class has no natural "one nice
sentence" the way a patient does, `__repr__` alone is enough.

### Step 6 — Text test, following the same recipe as `test_patient.py`

**Spec:** new file, `test_pk_models.py`. Structure it exactly like
`test_patient.py` did: one fully-worked-by-you test first (construct a
70 kg `MarshDrug`, assert `V1` rounds to 15.96 — you already have this
number from Step 3's checkpoint), then a second test for the "only V1
moves" check from Step 4 (construct both a 70 kg and a 90 kg
`MarshDrug`, assert their `k10` values are equal to each other, assert
their `V1` values are *not* equal). Same `main()` runner pattern as
before — no new test infrastructure to learn here, just more tests
using the pattern you already have.

**Done when:** `python test_pk_models.py` prints `All tests passed!`
and both checks above are encoded as real asserts, not something you
eyeballed once and moved on from.

---

## Milestone 3 — The engine, rebuilt from scratch, with guidance

**File:** `engine.py`

This is the one you specifically want to rebuild yourself rather than
inherit — good instinct, this is the file worth understanding cold, and
it's also the most abstract milestone in the whole project, so it gets
the most steps. We build it together in chat; `claudeengineaugust.py`
is the answer key to check against once you're done, not the starting
point. Two pieces, built and tested separately before they're joined:
first `deriv()` (the physics, Steps 2–4), then `Simulation` (the thing
that calls `deriv()` on a schedule, Steps 6–10). Don't skip testing
`deriv()` alone — it's much easier to debug four lines of math in
isolation than to debug them for the first time buried inside a loop.

### Step 1 — Generalize the container: `Drug`

**Practicing:** the same plain-class pattern again, one more field.

**Spec:** `Drug` needs everything `MarshDrug` already has (`V1`, `k10`,
`k12`, `k13`, `k21`, `k31`) plus `ke0` — the effect-site rate constant
from Week 6 of your own notes. Add `name`, and optionally
`dose_unit`/`conc_unit` strings purely as axis labels for later — the
math never reads them. Decide whether Milestone 2's `MarshDrug` *becomes*
this class directly, or gets converted into one here; either is fine,
but don't keep two nearly-identical classes around — that duplication
is exactly the kind of thing that causes bugs when you fix one and
forget the other.

**Spec, continued — the clearance doorway:** Marsh publishes rate
constants directly, but Schnider/Minto/Eleveld (Milestone 5) publish
*volumes and clearances* instead. Rather than making every future model
hand-divide clearance by volume — error-prone, see Milestone 2's
correction — write one small helper next to the `Drug` class:
`drug_from_clearances(name, V1, V2, V3, Cl1, Cl2, Cl3, ke0, ...)`, doing
the division once (`k10=Cl1/V1`, `k12=Cl2/V1`, `k21=Cl2/V2`,
`k13=Cl3/V1`, `k31=Cl3/V3`) and returning a `Drug`. Notice this isn't a
method on any object — it's a plain function that *builds and returns*
one. That pattern (a function whose whole job is constructing an
object) is common enough to have a name, a "factory function" — you'll
write three more of these in Milestone 5. You won't need it until then,
but write it now while `Drug`'s shape is fresh in your head.

**Checkpoint:** rebuild Milestone 2's six Marsh numbers as a `Drug`,
adding `ke0=0.26`.

### Step 2 — Unpacking `y`: a Python mechanic you'll lean on

**Practicing:** sequence unpacking — a language feature, not part of
the physics, but you can't write `deriv()` without it.

**Concept:** Python lets you pull several variables out of one
list/tuple in a single line. If `y = [10, 20, 30, 40]`, then
`a, b, c, d = y` sets `a=10, b=20, c=30, d=40` — one name per position,
matched left to right. `deriv()` will receive `y` as a single 4-number
sequence `[A1, A2, A3, Ce]` (that specific order, by the convention you
choose and then stick to everywhere), and the very first thing it does
is unpack it into those four named variables so the rest of the
function can read like the equations you already know, instead of
`y[0]`, `y[1]`, `y[2]`, `y[3]` everywhere.

**Spec:** start `deriv(t, y, drug, rate)` by unpacking `y` into
`A1, A2, A3, Ce` in one line.

### Step 3 — The physics, now that the names exist

**Concept, not new to you** — you already derived these four equations
by hand in Week 5/6 of your own notes:
```
Cp = A1 / V1
dA1/dt = rate − (k10+k12+k13)·A1 + k21·A2 + k31·A3
dA2/dt = k12·A1 − k21·A2
dA3/dt = k13·A1 − k31·A3
dCe/dt = ke0·(Cp − Ce)
```
`V1`, `k10`, etc. come off the `drug` argument (`drug.V1`, `drug.k10`,
...) — this is the entire reason `deriv()` takes `drug` as a parameter,
so the same function works for Marsh, Schnider, or anything else,
purely by being handed a different `Drug` object.

**Spec:** compute `Cp` first (you need it for the fourth line), then
the four derivatives, each as its own named variable
(`dA1`, `dA2`, `dA3`, `dCe`) — don't try to cram this into one
tangled expression; five short lines, each matching one equation above,
is far easier to check against your own notes than one long one.

### Step 4 — Return them, and test this function completely alone

**Spec:** `return` the four derivatives as a tuple, in the *same order*
you unpacked `y` in Step 2 — `(dA1, dA2, dA3, dCe)`. This ordering
match is not optional: `solve_ivp` has no idea these represent A1/A2/
A3/Ce, it just matches position to position, so a mismatched order
here silently corrupts every simulation you ever run with this
function. That's exactly why you test it now, standalone, before it's
buried inside a loop where a mistake is much harder to spot.

**Checkpoint — call `deriv()` directly, no `Simulation` involved yet.**
For a 70 kg Marsh `Drug`, call `deriv(0, [100, 0, 0, 0], drug, 0)` —
i.e. 100 mg just bolused into A1, everything else empty, no infusion
running. I computed the exact expected return value:

| | value |
|---|---:|
| dA1 | -27.290 |
| dA2 | 11.200 |
| dA3 | 4.190 |
| dCe | 1.629 |

These aren't independently invented numbers — they're the same
quantities your own Week 5 by-hand section computed for this exact
scenario (a 100 mg bolus, 70 kg, before any Euler step is taken).
Write a small throwaway script that calls `deriv()` with these inputs
and prints the result; if it doesn't match, the bug is in Step 3's five
lines and you'll find it far faster here than inside `Simulation`.

**Done with this half when:** that checkpoint matches. Only then move
on to `Simulation`.

### Step 5 — Boluses are jumps, infusions are rates

**Concept, from your own Week 7 notes:** a bolus is not part of the
differential equation at all — it's an instantaneous jump in `A1`,
applied *before* integration resumes, never inside `deriv()`. An
infusion, by contrast, is exactly the `rate` argument `deriv()` already
expects; it just needs to be the right number at the right time.

**Spec:** give `Simulation` (from Step 6 on) somewhere to record *when*
each kind of event happens: `.bolus(at, dose)` appends
`(at, "bolus", dose)` to a list; `.rate(at, dose_per_min)` appends
`(at, "rate", dose_per_min)` to the same list. A "list of tuples" here
just means: each scheduled event is one small group of three related
values, and you're collecting many of those groups in order. Pure
bookkeeping, no math in this step — you're not computing anything yet,
just writing down what should happen and when.

### Step 6 — `Simulation.__init__` and the time grid

**Practicing:** setting up state that later methods will use — this is
what `__init__` is for on *any* class, not just `Patient`.

**Spec:** `__init__(self, drug, t_end=60.0, steps_per_min=6)` stores
`drug`, `t_end`, `steps_per_min`, and an empty list for events (Step 5
appends into this). Separately, `run(self)` starts by building a time
array from `0` to `t_end`, spaced so there are exactly `steps_per_min`
points per minute (`numpy.arange` or an equivalent — you choose). This
resolution is what makes "an event at minute 12" land exactly on a
grid point, which is why event times and `steps_per_min` need to agree
— an event at minute 12.5 needs `steps_per_min` fine enough to actually
have a grid point there.

**Checkpoint:** for `t_end=60, steps_per_min=6`, your time array should
have 361 points (60×6 + 1, since it includes both endpoints), starting
at `0.0` and ending at `60.0`. Print `len(t)`, `t[0]`, `t[-1]` and
check before continuing — same small-checkpoint habit as Milestone 2
Step 3.

### Step 7 — Starting state and the output arrays

**Spec:** still inside `run()`: start `y = [0, 0, 0, 0]` (nothing in
any compartment yet) and `rate = 0.0` (nothing infusing yet). Also
create two empty output arrays the same length as your time array —
one for `Cp`, one for `Ce` — that you'll fill in as you go (either
pre-sized with `numpy.zeros(n)` and filled by index, or built up with
`.append()` on a plain list; both work, pre-sizing is slightly more
common once you know the length upfront).

### Step 8 — Recognizing "did an event happen right now"

**Practicing:** converting a time (in minutes) into a position (a grid
index) — a small piece of arithmetic that trips people up the first
time.

**Concept:** your loop will walk through the time grid one point at a
time, using an index `i` (`0, 1, 2, ...`). Each event you scheduled in
Step 5 has an `at` time in *minutes*, not an index. Since your grid has
exactly `steps_per_min` points per minute, minute `at` corresponds to
index `at * steps_per_min` — provided that multiplication comes out to
a whole number, which is exactly Step 6's resolution requirement made
concrete. So: for each grid point `i`, and for each scheduled event,
check `i == at * steps_per_min`.

**Spec:** inside the loop over grid points, loop over `self.schedule`
(or whatever you named Step 5's list) and compare each event's
converted index to the current `i`.

### Step 9 — Applying the event

**Spec:** when Step 8 finds a match: if the event was a `"bolus"`, add
its dose directly into `y[0]` (`y[0] = y[0] + dose`) — this is the
"jump" from Step 5, a direct mutation of the state, nothing to do with
`deriv()`. If it was a `"rate"`, reassign the loop's `rate` variable to
the new value — from this point in the loop onward, that's the number
`deriv()` will be called with, until another rate event changes it
again.

### Step 10 — Recording output and advancing time

**Practicing:** reading a `solve_ivp` result back out — the one piece
of `scipy`-specific plumbing in this whole engine.

**Spec:**
1. Record this grid point's output: `Cp = y[0] / drug.V1`,
   `Ce = y[3]`, store both into the arrays from Step 7 at index `i`.
2. If `i` isn't the last grid point, advance: call
   `solve_ivp(deriv, (t[i], t[i+1]), y, args=(drug, rate))`. This runs
   your Step 2–4 function forward from the current instant to the next
   grid point, using whatever `rate` currently is.
3. `solve_ivp` returns a result object; the state you want is its
   `.y` attribute, a 2D array where each *row* is one of your four
   state variables over time and each *column* is one time point
   within this short call. You want the *last column* — `sol.y[:, -1]`
   reads as "every row, last column," i.e. the state at `t[i+1]`.
   Convert it back to a plain list and that becomes your new `y` for
   the next loop iteration.
4. After the loop finishes, store the filled `Cp`/`Ce` arrays (and the
   time array) onto `self`, so other code can read `sim.t`, `sim.cp`,
   `sim.ce` after `run()` returns.

**Why re-call `solve_ivp` fresh for every small grid step**, rather
than once for the whole run: that's exactly Steps 8–9's event
handling. `solve_ivp` has no idea a bolus or rate change happens at
minute 12; you have to stop it there, apply the event, and resume —
which means one call per grid step, not one call total.

**Checkpoint — the real one, joining everything above.** Build an
80 kg Marsh `Drug` and run this schedule (bolus 160 mg at t=0, rate
13 mg/min from t=0, rate 8 mg/min from t=12, bolus 40 mg at t=30, rate
0 from t=45) — generated by actually running `claudeengineaugust.py`:

| minute | Ce (µg/mL) |
|-------:|-----------:|
|      1 |       1.83 |
|     12 |       3.82 |
|     30 |       2.73 |
|     45 |       3.02 |
|     60 |       1.28 |

### Step 11 — Convenience accessor

**Spec:** `ce_at(self, minute)` — index into `self.ce` using
`minute * self.steps_per_min` (the exact conversion from Step 8,
reused). Small, but Milestones 7 and 9 lean on this repeatedly.

**Done when:** the checkpoint table in Step 10 reproduces (within a
couple hundredths) from your own `engine.py`, driven by a Marsh `Drug`,
and `test_engine.py` (new, same pattern as before) encodes both the
Step 4 `deriv()` checkpoint and the Step 10 `Simulation` checkpoint as
asserts with a tolerance — e.g. `abs(sim.ce_at(12) - 3.82) < 0.05` —
not an eyeball comparison.

---

## Milestone 4 — Plotting

**File:** `plotting.py`

### Step 1 — One function, no state

**Practicing:** recognizing when a function is enough and a class would
be overkill. This file has no data to hold between calls, so it
doesn't need `__init__`/`self` at all — just an ordinary function.

**Spec:** decide the signature:
`plot_concentrations(t, cp, ce=None, t_end=120, title=None)`. Four of
these are the inputs the function actually needs (`t`, `cp`, `ce`); the
other two (`t_end`, `title`) are display options with sensible
defaults, which is exactly what a default value in a function signature
is for — call the function with just `t` and `cp` and it still works,
using `t_end=120` unless you say otherwise.

### Step 2 — The matplotlib mechanics, explicitly

**Concept, if this is your first plotting function rather than a
one-off script:** the pattern you want is `fig, ax = plt.subplots()`,
then call `ax.plot(...)` once per line you want drawn, then
`ax.set_xlabel(...)`, `ax.set_ylabel(...)`, `ax.set_xlim(0, t_end)`,
`ax.legend()` to label which line is which, and finally either
`plt.show()` (a window pops up) or `fig.savefig("some_name.png")` (a
file gets written) — decide which one your function does, or accept a
`save_path=None` argument and do whichever the caller asked for.
Working through `ax.` rather than the shortcut `plt.` versions of these
calls is the more common style once you're inside a function rather
than a quick script, and it's what lets Milestone 10 embed the same
figure inside a Streamlit page later without changes.

### Step 3 — Plotting `ce` only if it was actually given

**Concept:** `ce=None` in the signature means "this argument is
optional, and if the caller doesn't pass one, `ce` will literally be
the value `None` inside the function." You need an `if` that checks for
that before trying to plot it — `if ce is not None:` (use `is not`,
not `!=`, when comparing against `None`; it's the idiomatic way and
avoids some subtle edge cases with numpy arrays that `!=` can trip on).
Everything inside that `if` block — the `ax.plot(t, ce, ...)` call and
its label — only runs when `ce` was actually supplied.

**Spec, put together:** always `ax.plot(t, cp, label="Cp")`;
conditionally, inside the `if`, `ax.plot(t, ce, label="Ce")`. X-axis
labeled "Time (min)", limited to `(0, t_end)`. Y-axis labeled with a
concentration unit if you want to pass one in, or just "Concentration"
if not.

### Step 4 — Keep it dumb, on purpose

**Why:** this file should never `import patient` or know what a `Drug`
is — it only ever sees arrays of numbers and an optional label. That's
what lets Milestone 10's Streamlit app call this exact same function
later with zero changes; the UI is a different *source* of the same
arrays, never a reason to rewrite the plot.

**Checkpoint:** feed it the Milestone 3 Step 10 checkpoint arrays (the
80 kg Marsh run). You should see Cp rise sharply at the bolus, Ce lag
behind and peak later and lower, both decline through the rest of the
window — the same shape your Week 6 notes called "the Ce/Cp lag."

**Done when:** a small script produces a saved or displayed chart with
that shape, and changing `t_end` moves the x-axis without touching the
underlying simulation at all.

---

## Milestone 5 — More drugs

**File:** `pk_models.py` (add to it)

### Step 1 — A technique for transcribing a multi-term formula safely

**Why this step exists:** Schnider's `Cl1` below has four terms added
together, each with its own coefficient and its own reference value.
Typing that as one long line invites exactly the kind of small
transcription error that's brutal to spot later (a `+` that should be
a `−`, a `77` that should be `59`). A safer habit: compute each term as
its own named variable first, then add the named pieces together on
the last line. For `Cl1`, that might look like naming
`weight_term`, `lbm_term`, `height_term` as three separate lines, then
`Cl1 = 1.89 + weight_term - lbm_term + height_term` as the fourth. This
also makes it trivial to print each term individually while debugging
— "which one of these four is wrong" becomes answerable in seconds
instead of requiring you to mentally re-derive the whole expression.
Use this technique for every multi-term formula in this milestone.

### Step 2 — Schnider propofol: where `drug_from_clearances` earns its keep

**Practicing:** reading a covariate-dependent published formula and
translating it faithfully — same skill as the Patient roadmap's FFM
step, just with more terms, using Step 1's technique to stay safe.

**Spec:** `schnider_drug(patient)`, same interface shape as your Marsh
constructor. Reads `patient.age`, `patient.weight`, `patient.height`,
`patient.lbm` — already sitting on your `Patient` object since
Milestone 1, which is the actual payoff of having built it early.
Published as volumes + clearances:

| | Schnider (1998/1999) |
|---|---|
| V1 | 4.27 L (fixed) |
| V2 | 18.9 − 0.391·(age − 53) |
| V3 | 238 L (fixed) |
| Cl1 | 1.89 + 0.0456·(weight−77) − 0.0681·(LBM−59) + 0.0264·(height−177) |
| Cl2 | 1.29 − 0.024·(age − 53) |
| Cl3 | 0.836 (fixed) |
| ke0 | 0.456 /min |

**Build it in this order, checking as you go, rather than all six at once:**
1. The three fixed values (`V1`, `V3`, `Cl3`) — no formula, just type
   the literals. Nothing to get wrong here.
2. `V2` — one covariate term, the simplest formula in the table. Good
   warm-up before `Cl1`.
3. `Cl2` — also one term, same shape as `V2`.
4. `Cl1` — the four-term one. Use Step 1's named-term technique here
   specifically; this is the line most worth slowing down for.
5. Feed all six into `drug_from_clearances` from Milestone 3 Step 1 —
   this is exactly the case it was built for.

**Checkpoint:** at the reference individual (53 yo, 77 kg, 177 cm, M —
every `(x − ref)` term is zero), `V1=4.27`, `Cl2=1.29`, and (using LBM
from your own `Patient`, ≈60.48 for this individual) `Cl1 ≈ 1.79`,
giving **k10 = Cl1/V1 ≈ 0.419/min** — I confirmed this by running it.
For Patient A instead (40 yo, 70 kg, 170 cm), `k10` comes out to
≈0.384/min — different, because the covariate terms are no longer zero.
If your reference-individual number doesn't land on 0.419, check `Cl1`
first — it's the term most likely to have a transcription slip.

**Worth remembering for Milestone 7:** Schnider's `V1` is *fixed* at
4.27 L, completely unrelated to weight — much smaller than Marsh's
weight-scaled `V1` (≈16 L at 70 kg). Same bolus, very different central
compartment, very different predicted peak.

### Step 3 — Minto remifentanil

**Spec:** same shape again, `minto_drug(patient)`, reading only
`patient.age` and `patient.lbm`:

| | Minto (1997) |
|---|---|
| V1 | 5.1 − 0.0201·(age−40) + 0.072·(LBM−55) |
| V2 | 9.82 − 0.0811·(age−40) + 0.108·(LBM−55) |
| V3 | 5.42 (fixed) |
| Cl1 | 2.6 − 0.0162·(age−40) + 0.0191·(LBM−55) |
| Cl2 | 2.05 − 0.0301·(age−40) |
| Cl3 | 0.076 − 0.00113·(age−40) |
| ke0 | 0.595 − 0.007·(age−40) |

Every row here has at most two covariate terms — more manageable than
Schnider's `Cl1`, but still worth naming each term separately (Step 1)
rather than writing one long line per row.

Remifentanil is an opioid — natural dose unit micrograms, not
milligrams; concentration reads in ng/mL, not µg/mL. If your `Drug`
carries unit-label fields (Milestone 3 Step 1), set them here.

**Checkpoint:** at the reference point (age=40, LBM=55) every covariate
term is exactly zero by construction, so every number in the table
above *is* its own checkpoint — no arithmetic required. Construct a
`Patient` whose age and LBM land close to 40/55 (LBM depends on
weight/height too, so you may not hit exactly 55 — close is fine for
sanity-checking) and confirm your six numbers are close to the table.
If your code doesn't reproduce the table at that point, the bug is in
how the terms combine, not in the constants themselves.

### Step 4 — Eleveld propofol, carefully

**Why this one's different:** Eleveld (2018) is the most general
propofol model — spans neonates to the elderly to the obese — but has
roughly thirty covariate constants and several helper functions. Your
own course notes flag this honestly as the single most error-prone
thing to hand-transcribe in the whole project, for anyone. So: don't
try to reproduce the full covariate model from a formula list. Instead:

**Spec:** implement Eleveld only for the reference individual for now
— 35 yo, 170 cm, 70 kg, male, no co-administered anesthetics. At that
specific patient the model collapses to fixed, well-verified numbers:

| | Eleveld reference individual |
|---|---|
| V1 | 6.28 L |
| V2 | 25.5 L |
| V3 | 273 L |
| CL | 1.79 L/min |
| Q2 | 1.75 L/min |
| Q3 | 1.11 L/min |
| ke0 | 0.146 /min |

Write `eleveld_drug_reference()` — deliberately no `patient` argument
yet — returning a `Drug` built from exactly these six numbers via
`drug_from_clearances`, plus a self-test asserting your `Drug` matches
this table. That self-test *is* the milestone for now — there's no
formula to transcribe at all in this step, only six literals and an
assert, precisely because a formula list for the full model would be
the least trustworthy thing in this entire project.

**Before extending this to arbitrary patients:** read the covariate
formulas directly from Eleveld DJ et al., *Br J Anaesth* 2018;
120:942-959, Table 2 — not from memory, not from a course summary, the
primary table. This is the one model in the whole project worth
reading the actual paper for before trusting it outside a ~70 kg adult.

### Step 5 — Confirm the architecture actually pays off

**Done when:** `engine.py` and `plotting.py` run Schnider and Minto
(and Eleveld-at-reference) with **zero changes** to either file — only
new functions in `pk_models.py`. If you find yourself editing
`engine.py` to make a new drug work, that's a sign Milestone 3 baked in
a Marsh-specific assumption worth revisiting before drug #4. Add each
new drug's checkpoint numbers to `test_pk_models.py` as you go, same
pattern as Marsh.

---

## Milestone 6 — Roberts regimen, wired in

**File:** `roberts.py` (adapt), maybe a new `dosing.py`

### Step 1 — The shape mismatch

**Concept:** `roberts_schedule(weight)` already returns correct
numbers — a bolus and a list of `(duration_min, rate_mg_min)` segments,
each relative to the segment before it. Your engine's
`.rate(at, dose_per_min)` wants an *absolute* clock time, not a
duration. Neither shape is wrong — they're organized differently, and
you need a translator between them.

### Step 2 — Look at the actual shape before writing anything

**Spec:** before writing the translator, call
`bolus_mg, schedule = roberts_schedule(70)` and `print(bolus_mg)`,
`print(schedule)`. You should see a single number for `bolus_mg`, and
`schedule` as a list of three tuples, each `(duration, rate)` — e.g.
something like `[(10, 11.67), (10, 9.33), (40, 7.0)]`. Seeing the real
shape on screen before you write a loop over it removes any guessing
about what you're iterating over.

### Step 3 — The running clock

**Concept:** "unroll relative durations into absolute times" means:
keep one variable — call it `current_time` — that starts at your
regimen's start time (usually `0.0`), and after processing each
segment, add that segment's duration to it before moving to the next.
This is the same idea as a physical clock: you don't need to know "what
absolute time does segment 3 start at" in advance — you just track
"what time is it now" and update it as you go.

**Spec:**
1. `current_time = start` (`start` defaults to `0.0`).
2. `sim.bolus(current_time, bolus_mg)` — the loading dose always goes
   in at the regimen's start time.
3. Loop over `schedule` with a `for duration, rate in schedule:` — this
   is tuple unpacking again (Milestone 3 Step 2's lesson), now applied
   to each `(duration, rate)` pair as the loop visits it in order.
4. Inside the loop: `sim.rate(current_time, rate)` — this segment's
   rate starts at whatever `current_time` currently is.
5. Still inside the loop, on the next line: `current_time = current_time + duration`
   — advance the clock by this segment's length, so the *next* loop
   iteration's `sim.rate(...)` call uses the right start time.

Notice steps 4 and 5 have to happen in that order — record the rate at
the *current* time, then advance the clock — not the reverse.

**Checkpoint** — Roberts' regimen (1 mg/kg bolus, 10→8→6 mg/kg/hr)
through a 70 kg Marsh `Drug`, run through your own engine:

| t (min) | Cp | Ce |
|--------:|---:|---:|
| 1 | 3.99 | 0.95 |
| 10 | 3.22 | 3.05 |
| 20 | 2.98 | 2.98 |
| 40 | 2.66 | 2.64 |
| 60 | 2.75 | 2.74 |

Notice Cp and Ce nearly converge by minute 20 and stay close — that's
the near-steady-state behavior a step-down regimen like Roberts is
designed to produce, unlike a single bolus's sharp rise-and-fall.

**Done when:** your translator reproduces this table (small
differences from your own engine's exact `steps_per_min` are fine) for
a 70 kg patient.

---

## Milestone 7 — Comparison mode

**File:** a script that reuses everything above — no new core files

### Step 1 — Same drug, different models, same dose

**Spec:** for one patient (Patient A, 70 kg, is fine), build both a
Marsh and a Schnider `Drug`, run the *identical* dosing plan through
each (same bolus, same rate schedule — don't tune the dose per model,
that defeats the point).

### Step 2 — Actually overlaying two curves on one plot

**Concept:** `plot_concentrations` from Milestone 4 was built for one
simulation's `cp`/`ce` at a time — it doesn't know how to take two.
You have two reasonable options, and either is fine: (a) call
`ax.plot(...)` twice yourself in this comparison script, once per
model, each with its own `label`, on the *same* `fig, ax` pair, instead
of routing through `plot_concentrations` at all; or (b) go back and
generalize `plot_concentrations` to accept a list of
`(label, t, ce)` tuples and loop over them internally, plotting one
line per entry. Option (a) is faster right now; option (b) is more
reusable if you know you'll want overlays again (you will — Milestone
8's probability curves and Milestone 10's app both want this). Pick
one; if you pick (b), this is a good moment to update `test_patient.py`-
style tests for `plotting.py` too, if you wrote any.

### Step 3 — A small helper worth writing once

**Concept:** `.max()` on a numpy array returns its largest value;
`.argmax()` returns the *index* of that largest value, which is exactly
what you need to look up the corresponding time —
`t[ce.argmax()]` reads as "the time at the index where `ce` was
biggest." You'll want both peak value and time-to-peak repeatedly from
here on, so wrap them once: `peak_and_time(t, ce)` returning
`(ce.max(), t[ce.argmax()])`. Small, but it's the same "don't repeat
yourself" instinct as `ce_at()` in Milestone 3 — write the lookup once,
call it everywhere.

**Checkpoint, and the actual lesson** — 150 mg bolus + 10 mg/min (then
6 mg/min at minute 20), same 70 kg patient, through both models:

| model | peak Ce | time to peak |
|---|---:|---:|
| Marsh | 4.24 µg/mL | 5.5 min |
| Schnider | 9.32 µg/mL | 1.7 min |

That's not a bug in either model — it's real. Schnider's central volume
(`V1 = 4.27 L`, fixed) is much smaller than Marsh's (`V1 = 0.228 ×
weight`, ≈16 L at 70 kg), so the identical bolus lands in a much
smaller "tank" and produces a much higher, much faster peak. This is
exactly why commercial TCI pumps lock the model once an infusion
starts — silently re-solving for the same target under a different
model can produce a real dose discontinuity. Seeing it fall out of your
own two models, side by side, is worth more than reading it in a manual.

### Step 4 — "Smart" scheme vs. what you actually do at the pump

**Spec:** a second comparison, same overlay technique as Step 2 — the
Roberts regimen (Milestone 6) against a genuinely naive baseline: one
constant mg/kg/hr rate, no bolus, no step-down, the kind of number you
might dial in by feel. Run both through the same model, overlay Cp or
Ce, and print `peak_and_time` for each.

**Done when:** one script produces the overlay plot plus printed
peak/time-to-peak for each scenario, for both comparisons above.

---

## Milestone 8 — Tolerance to laryngoscopy / incision

**New file**, likely `pd_endpoints.py`

### Step 1 — Concentration isn't a clinical answer

**Concept:** "Ce = 3 µg/mL" means little on its own; "92% probability
this patient won't respond to laryngoscopy" does. The bridge is a
sigmoid (Hill) curve mapping concentration to probability.

### Step 2 — Single drug, single endpoint

**Spec:** `p_single(ce, c50, gamma)` →
`ce**gamma / (c50**gamma + ce**gamma)`. Same shape as a BIS Hill curve
— a probability instead of a BIS number is just a different scaling of
the same equation. `**` is Python's exponent operator — `ce**gamma`
means "ce to the power of gamma," same as `ce ** 1.5` for a fractional
power, which is exactly what this formula needs.

**Checkpoint** (propofol, loss of responsiveness, C50=2.8 µg/mL,
γ=1.5 — from your own course notes' by-hand work):
- Ce = 2.0 → P ≈ 0.38
- Ce = 3.5 → P ≈ 0.58

### Step 3 — Two drugs, one endpoint: the Greco surface

**Concept:** propofol and remifentanil together are strongly
*synergistic* for tolerating stimulation — neither drug alone reaches a
safe intubating probability at reasonable doses, but together they do.
That's the actual pharmacological reason to give an opioid before
laryngoscopy, not just a rule you memorized.

**Spec:** `p_event(ceP, ceR, c50P, c50R, alpha, gamma)`:
```
UP = ceP / c50P
UR = ceR / c50R
U  = UP + UR + alpha * UP * UR
P  = U**gamma / (1 + U**gamma)
```
`alpha > 0` synergy, `alpha = 0` plain additivity (no bonus from
combining), `alpha < 0` antagonism.

**Checkpoint** (illustrative laryngoscopy constants — C50P=3.0,
C50R=3.0, γ=4, α=3, Bouillon-2004-style surface):
- CeP=1.5, CeR=1.5 → P ≈ 0.90
- Same point with α=0 (no synergy) → P ≈ 0.50
- CeP=3.0 alone (CeR=0) → P = 0.50; CeR=3.0 alone (CeP=0) → P = 0.50

That last line is the clinical argument in three numbers: either drug
alone at its own C50 gets you to 50%; split evenly between the two with
real synergy gets you to 90%. That's dose-sparing — the actual reason
induction is propofol *and* an opioid, not just a bigger propofol dose.

**Honesty note, matching your own course material:** the C50/γ/α
numbers above are illustrative and differ between published surfaces
(Bouillon 2004, Kern 2004, Johnson/Syroid 2008) and between
populations. Treat them as anchors to get your code right, not as
numbers to trust clinically without checking the specific paper for the
endpoint and drug pair you're modeling.

### Step 4 — Two simulations that actually line up

**Concept, easy to trip on:** to compare propofol's `ce` array against
remifentanil's `ce` array point by point, index 47 of one array has to
represent the *same moment in time* as index 47 of the other. That only
happens if both `Simulation` objects were built with the same `t_end`
and the same `steps_per_min` — different resolutions produce
different-length arrays that don't line up at all. Build both
simulations with matching settings before anything else in this step.

**Spec:** run a propofol `Simulation` and a remifentanil `Simulation`
over the same `t_end`/`steps_per_min`, giving you `sim_prop.ce` and
`sim_remi.ce` as two arrays of equal length, index-aligned in time.

### Step 5 — Calling `p_event` across a whole array at once

**Concept, worth knowing explicitly:** `p_single`/`p_event` were
written using plain arithmetic (`/`, `*`, `**`) — no loop. If you call
them with two full numpy arrays instead of two single numbers, numpy
applies the arithmetic *element-wise* automatically: `ceP / c50P`
divides every element of `ceP` by `c50P` in one call, producing a whole
new array, no `for` loop needed anywhere in `p_event` itself. This is
called vectorization, and it's the reason `p_event(sim_prop.ce,
sim_remi.ce, 3.0, 3.0, 3.0, 4.0)` — called *once*, with two full arrays
— returns a full probability-vs-time array directly, rather than
needing you to loop over every time point by hand.

**Spec:** call `p_event` once, passing `sim_prop.ce` and `sim_remi.ce`
directly (not element-by-element), producing your probability curve —
one array, same length as `sim_prop.t`, ready to hand to a plot.

**Done when:** the probability curve is near zero early, rises as both
Ce traces climb, falls again as the drugs clear, and your two
checkpoint numbers from Step 3 reproduce exactly when you call
`p_event`/`p_single` with plain numbers instead of arrays.

---

## Milestone 9 — Wake-up time predictor

**New file**, likely `wake_predictor.py`

### Step 1 — Why this isn't a formula

**Concept, from your own course notes:** "context-sensitive half-time"
tempts you toward a lookup-table answer, but the real answer depends on
how full the peripheral compartments are *right now* — a 5-minute case
and a 5-hour case at the identical Ce wake very differently, because in
the long case the full peripheral tanks keep back-feeding the central
compartment after you stop. Your three-compartment engine already
reproduces this automatically; the predictor's job is just to keep
running the simulation forward with the infusion off and watch where Ce
lands.

### Step 2 — Replaying an existing schedule onto a new `Simulation`

**Concept:** you can't just keep running the *same* `Simulation` object
further, because `run()` always rebuilds from t=0 with a fixed `t_end`
(that's a deliberate choice from Milestone 3, not a limitation to work
around) — so predicting a wake time means building a *new* `Simulation`
with a longer `t_end`, that replays every event the original had, plus
one extra "stop everything" event at the end.

**Spec:** recall each entry in `self.schedule` (Milestone 3 Step 5) is
a tuple `(at, kind, dose)`, where `kind` is the string `"bolus"` or
`"rate"`. To replay them onto a new `Simulation`:
```
for at, kind, dose in old_sim.schedule:
    if kind == "bolus":
        new_sim.bolus(at, dose)
    else:
        new_sim.rate(at, dose)
```
This is the same tuple-unpacking pattern from Step 5 of Milestone 3,
now with an `if`/`else` reading the `kind` field to decide which method
to call — the exact reason you stored `kind` as a string in the first
place back then.

### Step 3 — Adding the stop event and running longer

**Spec:** after replaying the old events, add one more:
`new_sim.rate(stop_time, 0.0)` — every infusion off from `stop_time`
onward (a bolus doesn't need a matching "off" event; it was already a
one-time jump). Build `new_sim` with a `t_end` well beyond `stop_time`
— long enough that Ce has a real chance to fall below your wake
threshold — then call `new_sim.run()`.

### Step 4 — Scanning for the crossing

**Concept:** you already know how to convert a time in minutes to a
grid index (Milestone 3 Step 8: `index = time * steps_per_min`). Use
that here to find where `stop_time` sits in the array, then walk
forward from there.

**Spec:**
```
stop_index = int(stop_time * new_sim.steps_per_min)
for i in range(stop_index, len(new_sim.t)):
    if new_sim.ce[i] < wake_threshold:
        return new_sim.t[i] - stop_time   # minutes after stopping
return None   # never crossed within t_end — the "won't wake in window" case
```
`range(stop_index, len(new_sim.t))` walks every index from the stop
point to the end of the array, in order — exactly "scan forward from
when we stopped." The first `i` where `ce[i]` drops below threshold is
your answer; subtract `stop_time` so the result reads as "minutes after
stopping," not "minutes since the whole simulation began." Returning
`None` when the loop finishes without finding a crossing is
deliberate, not an oversight — it's how your code represents "this
patient will not wake within the window you simulated," which is a
real, useful answer for a long-acting drug like methadone.

(Your own course notes describe a fancier version using `solve_ivp`'s
built-in `events` parameter, which finds the crossing precisely instead
of at your grid resolution. Worth knowing that exists — `events` lets
you tell the solver "stop integrating exactly when this quantity
crosses zero" — but the scan-and-search version above is simpler to
build first, and accurate enough at `steps_per_min=6` to make the same
clinical point. Upgrade to it later if you want more precision than the
grid gives you.)

**Checkpoint** — 70 kg Marsh, 100 mg bolus + 10 mg/min, wake threshold
Ce = 1.2 µg/mL, time measured *from when the infusion stops*:

| infusion duration | time to wake after stopping |
|---|---:|
| 5 min | ≈10.7 min |
| 120 min | ≈30.8 min |

Same drug, same rate, same wake threshold — the only thing that changed
is how long the infusion ran, and the wake time nearly triples. That's
context sensitivity, produced by your engine with no half-time formula
anywhere in the code — exactly the point your own course notes make.

**Done when:** your predictor reproduces roughly this pattern (exact
numbers will shift slightly with your own engine's `ke0`/`steps_per_min`
choices — the *direction and rough size* of the difference is the
thing to match, not the decimal places).

---

## Milestone 10 — Streamlit wrap

**New file**, `app.py`

### Step 1 — What's actually left to build

By this point almost everything the UI needs already exists as a
tested function: `Patient`, the `*_drug(patient)` functions,
`Simulation`, `plot_concentrations`, `p_event`/`p_single`, the wake
predictor. This milestone is composition and wiring, not new logic —
the actual payoff of doing Milestones 1–9 first. It also introduces a
handful of genuinely new concepts (Streamlit's widgets, its rerun
model, caching) that Milestones 1–9 had no reason to cover — those get
their own explanation below as they come up, same as `solve_ivp` got
one in Milestone 3.

**Spec, the one rule to hold onto for every step below:** if you catch
yourself computing a concentration, a probability, or a formula
*inside* `app.py`, stop — that logic belongs in one of the files from
Milestones 1–9. `app.py`'s job is reading widget values, calling your
functions, and drawing what comes back.

### Step 2 — The one thing about Streamlit worth understanding before you write any of it

**Concept:** a Streamlit script isn't like a normal Python script that
runs once. Every time the person using the app changes a widget (moves
a slider, edits the dosing table), Streamlit **reruns your entire
`app.py` file from top to bottom**. Widgets remember their own values
between reruns, but plain Python variables don't — which is why the
guide's patient-slider helper stashes values in `st.session_state`
(a dictionary-like object Streamlit keeps alive across reruns) instead
of a normal variable. You don't need to memorize the mechanism yet,
just the one consequence: anything expensive (like running a full PK
simulation) should be wrapped so it doesn't recompute on every single
rerun if its inputs haven't changed — that's what `@st.cache_data`
(Step 7) is for.

### Step 3 — App skeleton and layout

**Spec:** following the guide's Step 1, set up the page structure
first, before any real widgets: a page title, and a two-column main
layout (dosing controls on the left, plots/readouts on the right) using
`st.columns`. Get this rendering with placeholder text in each column
before wiring anything real in — confirming the skeleton works makes
every later step easier to debug in isolation.

### Step 4 — Patient panel

**Spec:** following the guide's Step 2, build the sidebar: age,
weight, height (each a slider — the paired slider+typed-number-box
trick from the guide is a nice-to-have, not required for a first
pass), and a sex selector. Collect these into a `Patient` the moment
they're read — this is the one place `Patient` gets constructed in the
whole app, from live widget values instead of hardcoded numbers.

### Step 5 — The drug + model registry

**Spec:** following the guide's Step 3, one dictionary mapping each
drug name to the list of models you've built for it, e.g.
`{"Propofol": ["Marsh", "Schnider"], "Remifentanil": ["Minto"]}`. This
is what powers every drug/model dropdown from here on — add to this
dictionary, not to scattered `if` statements, whenever you add a model.

### Step 6 — The editable dosing table

**Spec:** following the guide's Step 4, `st.data_editor` renders a
pandas DataFrame as an editable spreadsheet-like grid right in the
page — rows for time, drug, bolus-or-infusion, dose, and (for
infusions) an end time. `num_rows="dynamic"` lets the user add/delete
rows. This grid **is** the schedule your `Simulation` objects (Step 7)
will be built from — one row per event, in the same shape as the
`(at, kind, dose)` events you've been building programmatically since
Milestone 3, just entered by a person instead of by you in code.

### Step 7 — Running the simulation, and why caching matters here

**Concept:** re-read Step 2's rerun behavior — without caching, editing
one cell in the dosing table would re-run every `Simulation` from
scratch on every keystroke. `@st.cache_data` above a function tells
Streamlit "remember this function's return value for a given set of
arguments, and only actually re-run the function if the arguments
change." Put your "build all the `Simulation` objects for the current
patient/events/models" logic inside one such function.

**Spec:** following the guide's Step 6, write the function that reads
the current patient, dosing table, and chosen models, builds one
`Simulation` per drug in use (Milestones 2–5's `*_drug()` functions
feed straight into Milestone 3's `Simulation`), runs each, and returns
the results in a shape the plotting/readout steps can use. Decorate it
with `@st.cache_data`.

### Step 8 — Plots and readouts

**Spec:** following the guide's Steps 7–8, call `plot_concentrations`
(Milestone 4) — or your Step 2-of-Milestone-7 overlay variant, if
several drugs are running at once — inside the results column, and add
a small set of `st.metric` readouts (peak Ce, wake-up time,
P(no response to laryngoscopy)) driven by the `peak_and_time` helper
(Milestone 7), the wake predictor (Milestone 9), and `p_event`
(Milestone 8) respectively. Every number displayed here should trace
back to a function you already built and already tested — if you find
yourself writing a new formula to produce a readout, that formula
belongs in Milestone 8 or 9's file, not here.

### Step 9 — Polish, and stopping here on purpose

**Spec:** following the guide's Step 10 — a reset button
(`st.session_state.clear()` plus `st.rerun()`), a persistent "not for
clinical use" caption near the plot. The guide's optional Step 9 (a TCI
target-concentration solver, entering a target Ce and having the app
back-solve a dosing regimen) is real, useful, and a legitimately harder
problem than anything above — it's deliberately out of scope for this
roadmap. Worth returning to once everything here is solid, not before.

**Done when:** `streamlit run app.py` gives you an interactive version
of everything in Milestones 1–9 — patient entry, dosing table, model
selection, plots, and clinical readouts — with no PK or PD math living
in `app.py` itself.

---

## Quick reference — module map

| File               | Owns                                              |
|---------------------|---------------------------------------------------|
| `patient.py`         | demographics + derived body-size values           |
| `pk_models.py`       | per-drug parameter functions (numbers only)        |
| `engine.py`          | the integrator — same math for every drug          |
| `plotting.py`        | matplotlib charts, knows nothing about drug names   |
| `roberts.py`/`dosing.py` | regimen → event schedule adapters              |
| `pd_endpoints.py`    | probability-of-response models                     |
| `wake_predictor.py`  | post-infusion wake time                             |
| `app.py`             | Streamlit UI, thin layer over everything above      |
