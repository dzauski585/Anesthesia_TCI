# Anesthesia Simulator Workbook: Hand-Typed Edition
### One workbook, three projects: learn Python and JavaScript by building a TCI pump, an anesthesia machine and a bedside monitor

| Part | Project | Language | Lessons |
|---|---|---|---|
| Warm-up | Errors, functions, lists, loops, dictionaries and classes | Python | P1–P2 |
| 1 | **TCI simulator, StanpumpR-style.** Manual dose tables, 7 drugs, model comparison, propofol–opioid interaction, a pump that re-decides every 10 seconds, schedules to Excel, a Streamlit app | Python | 0–12 |
| 2 | **Anesthesia machine.** Volatile uptake, MAC, N₂O, FiO₂, and a Streamlit machine with flowmeters, vaporizer and a time-warp | Python | 13–18 |
| 3 | **Bedside monitor.** ECG, arterial line, SpO₂, capnography, MCS devices | JavaScript, from zero | 19–28 |
| 4 | **Optional capstone.** All three on one web page | JS + Python | 29–31 |

Every block of code in this workbook has been run, including the hidden answers, and the numbers in each checkpoint are what the finished code produced.

---

## How the hand-typed edition works

There is no starter code in this edition. No skeleton files, no `TODO`s to fill in, and nothing to paste. Every file starts empty, and you type every line of it, including the checks.

1. **Type everything.** That includes answers you open from a hidden section. Pasting teaches you nothing.
2. **Run often.** If you've typed about five lines without running them, run them.
3. **Mistyping is part of the course.** Finding your own typos is the skill you're here to build.
4. **Turn off code suggestions.** Switch off any AI assistant for this folder. In VS Code, also set `editor.inlineSuggest.enabled` to `false`.

### The main rule: learn in a scratch file, build in the project

Each new idea is first taught with an example that has nothing to do with anesthesia: dogs, bank accounts, snacks. You type that example along with the book, line by line, in a throwaway scratch file. Then you use the idea yourself in the real project.

The anesthesia code is never handed to you line by line. You write it, and you've already practiced the idea it needs.

| Level | Where it's used | What you get | What you do |
|---|---|---|---|
| 🟢 **Type along** | Scratch files, and your first page in a new language | Every line, explained | Type it, run it, change it, break it |
| 🟡 **Finish the pattern** | Project code, the first time you use an idea | A rule or formula, part of the code, and the output to expect | Write the rest |
| 🔴 **From the spec** | Project code, once you've used the idea before | A plain description, the formula and the checks | Write all of it |

Yellow and red tasks have hidden sections. Try for 15–20 minutes, then open the **Hint**, which is a nudge. The **Answer** comes last, and you still type it.

### How it changes as you go

It gets harder on purpose. Your project code moves steadily toward red, and the scratch files keep coming for every new idea.

| Lessons | Scratch files | Your project code |
|---|---|---|
| P1–P2 | All of it | None yet |
| 0–2 | Every new idea | Mostly 🟡, some 🔴 |
| 3–12 | Every new idea (solver, plotting, CSV, Streamlit) | Mostly 🔴, with 🟡 for the hardest new pieces |
| 13–18 | Every new idea (`@property`, session state) | Nearly all 🔴 |
| 19–22 | Every new idea | Back to 🟡, because the language is new |
| 23–28 | New ideas only | Mostly 🔴 |
| 29–31 | Rarely | All 🔴. You're translating your own Python |

### What each lesson contains

- **Goal** and **New ideas:** what works by the end, and what it teaches.
- **The science:** the pharmacology or physiology behind the lesson, and the papers it came from.
- **The big picture:** how this file fits with the others.
- **Learn it 🟢:** each new idea with an unrelated example, in a scratch file.
- **Build it 🟡🔴:** the real project code, written by you.
- **Check it:** checks you type into your own project. They print `OK` or `XX`.
- **Break it on purpose:** small mistakes to make deliberately, so you've met each error before it happens by accident.
- **If something goes wrong, Things to consider, Checkpoint.**

A lesson takes about 4–6 focused hours. Taking two weeks over one is normal.

> **Not for clinical use.** Everything here is a simplified teaching model.

### When you get stuck

Appendix A has a debugging checklist. In short: one file has one job. Make it run, then make it right, then make it nice. Commit every time something works. Write three lines in `DEVLOG.md` at the end of each session. If you're stuck for more than 30 minutes, shrink the problem into a tiny scratch file.

---

## The roadmap

Week numbers from the original workbook stay the same, so every "see Week 13" still makes sense. A big week becomes lettered parts.

| Original | Topic | New lessons |
|---|---|---|
| New | **Python warm-up:** errors, functions, lists, loops and dicts, then classes | P1, P2 |
| 0 | Setup, Git, your own `check()`, how imports work | 0 |
| 1 | `Drug` class and the Marsh model | 1 |
| 2 | `deriv()` | 2 |
| 3 | `Simulation`: the event schedule, then the time loop | 3A, 3B |
| 4 | Plotting, then the Roberts regimen | 4A, 4B |
| 5 | Reading a CSV file, then dose tables | 5A, 5B |
| 6 | Comparing models, then the full Eleveld model | 6A, 6B |
| 7 | Drug library: scaling, then the parameter table | 7A, 7B |
| 8 | Whole case: many drugs, then long cases | 8A, 8B |
| 9 | Drug interactions | 9 |
| 10 | Wake-up prediction and JSON | 10 |
| 11 | TCI: the decision rule, the matrix step, the schedule | 11A, 11B, 11C |
| 12 | TCI app: Streamlit basics, then the full app | 12A, 12B |
| 13 | `Agent` and `Compartment` | 13 |
| 14 | Gas exchange: one tissue, then the whole body | 14A, 14B |
| 15 | Two agents | 15 |
| 16 | Oxygen, then the hypoxic guard | 16A, 16B |
| 17 | Decrement times | 17 |
| 18 | Machine app: controls, session state, time-warp | 18A, 18B, 18C |
| 19 | **JavaScript from zero:** page and console; functions and modules; arrays and loops; objects and classes | 19A, 19B, 19C, 19D |
| 20 | HTML, then the DOM and events | 20A, 20B |
| 21 | Canvas drawing, then one heartbeat | 21A, 21B |
| 22 | Animation loop, ring buffer, sweeping trace | 22A, 22B, 22C |
| 23 | Patient state and controls | 23 |
| 24 | Atrial fibrillation, then ectopy | 24A, 24B |
| 25 | Arterial line, then pleth | 25A, 25B |
| 26 | Capnography, then lethal rhythms and alarms | 26A, 26B |
| 27 | Impella, then ECMO | 27A, 27B |
| 28 | IABP | 28 |
| 29 | Port the machine to JavaScript | 29A, 29B |
| 30 | TCI panel with JSON | 30 |
| 31 | Opioid MAC-sparing, then deploy | 31A, 31B |

That's **60 lessons** instead of 32, or a little over a year at one lesson a week.

---

## Week P1 — Python warm-up: errors, functions, lists, loops and dictionaries

**Goal:** be comfortable reading an error, writing a function, and looping over a list or dictionary, because every lesson after this assumes them.

**New ideas:** variables; `print`; numbers and strings; `if`; functions and `return`; lists; `for`; tuples; dictionaries; reading a traceback.

**Read first:** [Python tutorial: An informal introduction](https://docs.python.org/3/tutorial/introduction.html), then [More control flow tools](https://docs.python.org/3/tutorial/controlflow.html), up to section 4.8

### The big picture

You've already written `patient.py` and `roberts.py`, so much of this may be review. Go quickly through whatever feels familiar, but do type it. This lesson has no anesthesia in it, and nothing here is part of the project. Make a folder called `practice`, and work there. On a Mac, type `python3` wherever this book says `python`.

### Values and variables 🟢

Create `practice/basics.py`:

```python
name = "Biscuit"
legs = 4
weight = 12.5

print(name)
print(legs * 2)
print(weight / 2)
print(7 // 2, 7 % 2, 2 ** 3)
print(f"{name} has {legs} legs and weighs {weight} kg")
print(type(name), type(legs), type(weight))
```

Run it from inside `practice/`:

```bash
python basics.py
```

```text
Biscuit
8
6.25
3 1 8
Biscuit has 4 legs and weighs 12.5 kg
<class 'str'> <class 'int'> <class 'float'>
```

- `=` stores a value under a name. It doesn't mean "equals", as it does in math.
- `//` divides and drops the remainder, `%` gives the remainder, and `**` is "to the power of".
- `f"..."` is an *f-string*. Anything inside `{ }` gets filled in.
- `str`, `int` and `float` are text, whole numbers and decimals.

### Reading an error 🟢

Errors aren't a sign of failure. They're Python telling you exactly what it couldn't do, and you'll read thousands. Add this to the bottom of `basics.py`, and run it:

```python

print(nmae)
```

The output ends like this (your folder path will differ):

```text
Traceback (most recent call last):
  File ".../practice/basics.py", line 12, in <module>
    print(nmae)
          ^^^^
NameError: name 'nmae' is not defined. Did you mean: 'name'?
```

**Read errors from the bottom up.** The last line says what went wrong. The lines above say where: the file, the line number, and the code on that line. Older versions of Python show less, without the arrows and the suggestion. Now delete that last line.

| Error | What it usually means |
|---|---|
| `SyntaxError` | Python can't read the line. Look for a missing `:`, `)` or quote, sometimes on the line above |
| `IndentationError` | The spaces at the start of a line are wrong |
| `NameError` | You used a name that doesn't exist yet, often a typo |
| `TypeError` | The right names but the wrong kinds of thing, such as `"5" + 5`, or too few inputs to a function |
| `IndexError` | You asked a list for a position past its end |
| `KeyError` | You asked a dictionary for a key it doesn't have |
| `AttributeError` | You asked an object for something it doesn't have, such as `rex.colour` |
| `ValueError` | The right kind of thing but an impossible value, such as `float("banana")` |
| `ModuleNotFoundError` | An `import` couldn't find that file or package |

### Decisions 🟢

Create `practice/decide.py`:

```python
temperature = 31

if temperature > 30:
    print("hot")
elif temperature < 10:
    print("cold")
else:
    print("mild")

print(temperature == 31, temperature != 31)
print(temperature > 20 and temperature < 40)
print(not temperature > 20)
```

```text
hot
True False
True
False
```

The colon starts a block, and the four-space indent marks what's inside it. `==` asks "are these equal?", and `!=` asks "are they different?". `and`, `or` and `not` combine conditions.

### Functions 🟢

A function is a named piece of work. It takes inputs and gives back an output. Create `practice/functions.py`:

```python
def area(width, height):
    return width * height


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


def shout(text):
    print(text.upper())


a = area(3, 4)
print(a)
print(area(height=2, width=5))
print(greet("Ana"))
print(greet("Ana", greeting="Welcome"))

result = shout("hi")
print(result)
```

```text
12
10
Hello, Ana
Welcome, Ana
HI
None
```

- `return` sends a value back to whoever called the function, and ends the function.
- `greeting="Hello"` is a *default*, used when you leave that input out.
- `area(height=2, width=5)` passes inputs by name, so their order doesn't matter.
- **`print` and `return` are different.** `shout` prints something but returns nothing, so `result` is `None`, Python's word for "no value". Mixing these up is a common beginner bug.

### Lists and loops 🟢

Create `practice/lists.py`:

```python
scores = [70, 85, 92]

print(scores[0], scores[-1])
print(len(scores))
scores.append(60)
print(scores)
print(scores[1:3])

for s in scores:
    print("score", s)

for i in range(3):
    print("i is", i)

total = 0
for s in scores:
    total = total + s
print(total / len(scores))

doubled = []
for s in scores:
    doubled.append(s * 2)
print(doubled)

print(sum(scores), max(scores), min(scores))
```

```text
70 92
3
[70, 85, 92, 60]
[85, 92]
score 70
score 85
score 92
score 60
i is 0
i is 1
i is 2
76.75
[140, 170, 184, 120]
307 92 60
```

- Positions start at 0, and `-1` means the last item.
- `scores[1:3]` gives positions 1 and 2. The end isn't included.
- `range(3)` gives 0, 1, 2. It stops before 3.
- Two patterns will come up constantly: *keep a running total*, and *make an empty list, loop, append*.

### Tuples and dictionaries 🟢

A **tuple** is a small fixed group of values, written with round brackets. A **dictionary** looks up a value by its name instead of its position. Create `practice/dicts.py`:

```python
point = (3, 4)
x, y = point
print(x, y)

events = [(0, "wake"), (8, "work"), (17, "home")]
for hour, what in events:
    print(hour, what)

ages = {"Rex": 3, "Fido": 7}
print(ages["Rex"])
ages["Spot"] = 1
print(len(ages), "Fido" in ages, "Tom" in ages)
print(ages.get("Tom", "unknown"))

for name, age in ages.items():
    print(name, age)

print(list(ages))
```

```text
3 4
0 wake
8 work
17 home
3
3 True False
unknown
Rex 3
Fido 7
Spot 1
['Rex', 'Fido', 'Spot']
```

`x, y = point` is called *unpacking*, and it works directly in a `for` line. The dose schedule in Week 3 is a list of tuples, and the drug registry in Week 6 is a dictionary, so you'll use both of these for real.

### Your turn: a shopping total 🟡

In `practice/shop.py`, write `total_cost(items)`, where `items` is a list of `(name, price, quantity)` tuples, and it returns the total. Then write `most_expensive(items)`, which returns the name of the item with the highest price. Test them on this list:

```python
basket = [("apple", 0.5, 6), ("bread", 3.0, 1), ("cheese", 7.25, 2)]
print(total_cost(basket))
print(most_expensive(basket))
```

```text
20.5
cheese
```

<details>
<summary><b>Hint</b></summary>

Both start with a loop that unpacks each tuple: `for name, price, quantity in items:`. The first keeps a running total. The second remembers the best price so far and the name that went with it.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def total_cost(items):
    total = 0
    for name, price, quantity in items:
        total += price * quantity
    return total


def most_expensive(items):
    best_name = None
    best_price = 0
    for name, price, quantity in items:
        if price > best_price:
            best_price = price
            best_name = name
    return best_name


basket = [("apple", 0.5, 6), ("bread", 3.0, 1), ("cheese", 7.25, 2)]
print(total_cost(basket))
print(most_expensive(basket))
```

</details>

### Your turn: counting words 🔴

In `practice/count.py`, write `count_words(text)`, which returns a dictionary giving the number of times each word appears. `"the cat and the dog".split()` turns text into a list of words. Test it on `"the cat and the dog and the fish"`, and print the result:

```text
{'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'fish': 1}
```

<details>
<summary><b>Hint</b></summary>

Start with an empty dictionary. For each word, if it's already a key, add one to its value. Otherwise, set it to 1.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def count_words(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(count_words("the cat and the dog and the fish"))
```

</details>

### Checkpoint

You can explain the difference between `print` and `return`, read a traceback from the bottom up, and write a loop over a list of tuples without looking anything up.

---

## Week P2 — Classes and objects, from the beginning

**Goal:** understand what a class is, what `self` means and why object-oriented programming (OOP) exists, well enough to write a class with no help.

**New ideas:** classes and objects; attributes; `__init__`; `self`; methods; `__repr__`; objects that hold other objects; factory functions.

**Read first:** [Python tutorial: Classes](https://docs.python.org/3/tutorial/classes.html) (sections 9.3.1–9.3.5)

### The big picture

The whole project is made of a few classes: `Patient`, `Drug`, `Simulation`, `Case`, `Compartment`, and later `Sweep` and `PulsePump` in JavaScript. Nearly everything they do uses only what's in this lesson. The one addition, `@property`, gets its own scratch file in Week 14.

This lesson has no anesthesia in it. It's all about dogs. Make a folder called `practice` and work there.

### The problem classes solve 🟢

Say you're tracking dogs with what you already know. Type this into `practice/dogs_no_class.py`:

```python
rex_name = "Rex"
rex_age = 3
fido_name = "Fido"
fido_age = 7


def birthday(age):
    return age + 1


rex_age = birthday(rex_age)
print(rex_name, rex_age)
print(fido_name, fido_age)
```

```text
Rex 4
Fido 7
```

It works, but nothing connects `rex_name` to `rex_age` except the way you named them. A hundred dogs would need two hundred variables. A dog with ten facts would need ten arguments for every function.

Now imagine a patient with an age, weight, height, sex, BMI and lean body mass, then seven drugs for that patient, each with eight numbers. Keeping that in loose variables is hopeless.

A **class** bundles related data together, along with the functions that work on it. That's the core of OOP.

### Your first class 🟢

Create `practice/dogs.py`:

```python
class Dog:
    pass


rex = Dog()
fido = Dog()

rex.name = "Rex"
fido.name = "Fido"

print(rex.name)
print(fido.name)
print(type(rex))
```

- `class Dog:` defines a new kind of thing. `pass` means "nothing inside yet".
- `Dog()` **makes one dog**. The brackets are what make it happen. It's like calling a function that hands you a new object.
- `rex.name = "Rex"` stores a value *on that object*. A value stored on an object is called an **attribute**.
- `rex` and `fido` are separate objects. Each holds its own `name`.

```text
Rex
Fido
<class '__main__.Dog'>
```

The vocabulary, which you'll see everywhere:

| Word | Meaning | Here |
|---|---|---|
| **Class** | The blueprint: what a dog is | `Dog` |
| **Object** (or *instance*) | One actual thing built from the blueprint | `rex`, `fido` |
| **Attribute** | A value stored on an object | `rex.name` |
| **Method** | A function that belongs to a class | coming next |

In project terms, `Patient` is the blueprint for a patient, and `Patient(40, 70, 170, "M")` is one particular man.

### `__init__`: setting up a new object 🟢

Setting attributes by hand after making each object is clumsy, and you could forget one. `__init__` is a special method that Python runs **automatically** whenever an object is made. Replace everything in `dogs.py` with this:

```python
class Dog:
    def __init__(self, name, age):
        print("__init__ is running for", name)
        self.name = name
        self.age = age


rex = Dog("Rex", 3)
fido = Dog("Fido", 7)

print(rex.name, rex.age)
print(fido.name, fido.age)
```

```text
__init__ is running for Rex
__init__ is running for Fido
Rex 3
Fido 7
```

The name has two underscores on each side. Notice that you never called `__init__` yourself. Writing `Dog("Rex", 3)` makes Python do three things:

1. Create a new, empty dog.
2. Call `__init__`, passing the new dog as `self`, then `"Rex"` and `3`.
3. Hand you back the finished dog, which gets stored in `rex`.

**What is `self`?** It's the particular object being worked on. When `__init__` runs for Rex, `self` *is* Rex, so `self.name = name` means "store this on Rex". When it runs for Fido, `self` is Fido. That's how one blueprint can serve any number of dogs.

**Why `self.name = name`?** These are two different things. The right-hand `name` is an ordinary input, which disappears when `__init__` ends. The left-hand `self.name` is stored on the object, so it stays. This line is how a value survives.

Now delete the `print` line inside `__init__`. It was only there to show you when `__init__` runs.

### Methods: what an object can do 🟢

A **method** is a function defined inside a class. Its first input is always `self`. Add these two methods inside the class, lined up with `def __init__`, and change the code at the bottom:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says woof"

    def birthday(self):
        self.age = self.age + 1


rex = Dog("Rex", 3)
fido = Dog("Fido", 7)

print(rex.speak())
print(fido.speak())

rex.birthday()
print(rex.age)
print(fido.age)

print(Dog.speak(rex))
```

```text
Rex says woof
Fido says woof
4
7
Rex says woof
```

Look at these three things:

- **Only Rex got older.** `birthday` changed `self.age`, and `self` was Rex. Fido has his own age.
- **`birthday` returns nothing.** It changes the object instead. An object remembers things between method calls, which a plain function can't do. Your `Simulation` depends on this: `bolus()` stores a dose, and `run()` uses it later.
- **The last line reveals the trick.** `rex.speak()` is shorthand for `Dog.speak(rex)`. Python takes the object before the dot and passes it in as `self`. That's why you define `speak(self)` with one input but call `rex.speak()` with none.

### `__repr__`: making an object printable 🟢

Add this line to the bottom of the file, and run it:

```python

print(rex)
```

You'll see something like `<__main__.Dog object at 0x10f3a2b50>`, which tells you nothing. `__repr__` is another special method that Python calls by itself, and it decides what an object looks like when printed. Inside the class, add this:

```python
    def __repr__(self):
        return f"Dog({self.name!r}, age={self.age})"
```

```text
Dog('Rex', age=4)
```

It must **return** text, not print it. The `!r` puts quotes around the name. Writing one takes 30 seconds, and it pays off every time you debug.

### Refusing bad data, and default values 🟢

Your `Patient` refuses `sex="X"`. Here's how that works. Create `practice/dogs2.py`:

```python
class Dog:
    def __init__(self, name, age, species="dog"):
        if age < 0:
            raise ValueError("age can't be negative")
        self.name = name
        self.age = age
        self.species = species


a = Dog("Rex", 3)
b = Dog("Tom", 5, species="cat")
print(a.species, b.species)

c = Dog("Ghost", -1)
print("this line never runs")
```

- `species="dog"` is a default, so you can leave it out.
- `raise ValueError(...)` stops the program with an error. No bad dog ever gets created.

```text
dog cat
ValueError: age can't be negative
```

### Objects that hold other objects 🟢

Real projects are made of objects inside objects. A `Case` will hold several `Simulation`s, one per drug. Here's the same shape. Create `practice/kennel.py`:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Kennel:
    def __init__(self):
        self.dogs = []

    def add(self, dog):
        self.dogs.append(dog)

    def oldest(self):
        best = self.dogs[0]
        for dog in self.dogs:
            if dog.age > best.age:
                best = dog
        return best


north = Kennel()
south = Kennel()

north.add(Dog("Rex", 3))
north.add(Dog("Fido", 7))
south.add(Dog("Spot", 1))

print(north.oldest().name)
print(len(north.dogs), len(south.dogs))
```

```text
Fido
2 1
```

`self.dogs = []` runs once per kennel, so each kennel gets its own list. Your `Simulation` keeps its dose schedule the same way.

`north.oldest().name` reads left to right: ask `north` for its oldest dog, then read that dog's name.

### Functions that build objects 🟢

A function can make an object and return it. This is called a *factory function*, and it's how every drug model works in this project. Add this to the bottom of `kennel.py`:

```python


def puppy(name):
    return Dog(name, 0)


def describe(dog):
    return f"{dog.name} is {dog.age}"


print(describe(puppy("Biscuit")))
print(describe(Dog("Rex", 3)))
```

```text
Biscuit is 0
Rex is 3
```

`describe` doesn't care how a dog was made. That's the payoff of OOP in this project. The engine will accept any `Drug`, whichever model built it, so adding a seventh drug means no changes to the engine.

### Break it on purpose 🟢

Each of these is a mistake everyone makes. In `dogs.py`, make the change, run it, read the message, and undo it.

| Change | What you'll see | What it means |
|---|---|---|
| `def speak(self):` → `def speak():` | `TypeError: Dog.speak() takes 0 positional arguments but 1 was given` | Python passes the object in as `self` even if you forgot to accept it |
| `self.name` in `speak` → `name` | `NameError: name 'name' is not defined. Did you mean: 'self.name'?` | Inside a method, you must always say `self.` |
| Delete `self.age = age` | `AttributeError: 'Dog' object has no attribute 'age'` | The value was never stored |
| `__init__` → `__init` | `TypeError: Dog() takes no arguments` | Python only recognizes the exact special name |
| `print(rex.speak())` → `print(rex.speak)` | `<bound method Dog.speak of Dog('Rex', age=3)>` | Without brackets, you got the method but didn't call it |
| `Dog("Rex", 3)` → `Dog("Rex")` | `TypeError: Dog.__init__() missing 1 required positional argument: 'age'` | You passed too few values |
| `rex = Dog("Rex", 3)` → `rex = Dog` | `TypeError: Dog.speak() missing 1 required positional argument: 'self'` | Without brackets, `rex` is the blueprint, not a dog |

### Your turn: a `Book` 🟡

In `practice/book.py`, write a class named `Book`:

- `Book(title, pages)` stores both values, plus `pages_read`, which starts at `0`.
- A method `read(n)` adds `n` to `pages_read`.
- A method `percent()` returns the percentage read.
- `__repr__` shows something like `Book('Dune', 25%)`.

Then make a book with 400 pages, read 60 pages and then 40, and print it. Expected:

```text
Book('Dune', 25%)
```

<details>
<summary><b>Hint</b></summary>

`pages_read` isn't an input. Just set `self.pages_read = 0` inside `__init__`. `__repr__` can call another method: `self.percent()`. `:.0f` shows no decimals.

</details>
<details>
<summary><b>Answer</b></summary>

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.pages_read = 0

    def read(self, n):
        self.pages_read += n

    def percent(self):
        return 100 * self.pages_read / self.pages

    def __repr__(self):
        return f"Book({self.title!r}, {self.percent():.0f}%)"


b = Book("Dune", 400)
b.read(60)
b.read(40)
print(b)
```

</details>

### Your turn: a bank account 🔴

Write `practice/bank.py`, with no help this time. An `Account` has an owner and a balance, which starts at 0. It can `deposit(amount)` and `withdraw(amount)`. Withdrawing more than the balance must raise a `ValueError`. Show `Account('Ana', 50)` when printed.

Test it: deposit 100, withdraw 50, print it, then try to withdraw 500. The last two lines of your output should be:

```text
Account('Ana', 50)
ValueError: not enough money
```

<details>
<summary><b>Hint</b></summary>

`withdraw` needs an `if` before it changes anything, the same way the `Dog` refused a negative age.

</details>
<details>
<summary><b>Answer</b></summary>

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("not enough money")
        self.balance -= amount

    def __repr__(self):
        return f"Account({self.owner!r}, {self.balance})"


a = Account("Ana")
a.deposit(100)
a.withdraw(50)
print(a)
a.withdraw(500)
```

</details>

### Things to consider

- **Not everything should be a class.** If you just need to turn inputs into an output, write a function. `deriv()` in Week 2 is a function, because it remembers nothing. `Simulation` is a class, because it has to remember its doses. Ask yourself: "does this thing need to remember anything?"
- **Inheritance** is a feature where one class is built from another. You'll see it mentioned in every OOP tutorial, but this project doesn't use it, so you can skip it for now.
- **A leading underscore** on a method, like `_index`, is a convention meaning "for use inside this class".

### Checkpoint

Without looking, explain these out loud: the difference between a class and an object; what `self` is; why `self.age = age` is needed; and why `rex.speak()` works when `speak` is defined with one input. Then write a class from memory for anything you like, such as a `Car` or a `Playlist`.

---

## Week 0 — Setup, your own checker, and how imports work

**Goal:** a project folder, Git, a `check()` function you wrote yourself, and a clear idea of how Python files share code.

**New ideas:** virtual environments; `git commit`; `abs()`; default arguments; f-strings; `try`/`except`; `if __name__ == "__main__":`; imports.

**Read first:** [Git: the basics (Pro Git, ch. 2)](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) · [Python tutorial: Modules](https://docs.python.org/3/tutorial/modules.html)

### The science: which "weight" do you mean?

Your `Patient` class calculates several versions of body size, because no single number predicts how drugs behave. Each one tries to fix a problem with using plain weight.

| Measure | What it tries to capture | Where it's used here |
|---|---|---|
| **Total body weight** | The number on the scale | Marsh (Week 1) |
| **BMI** | Weight relative to height | Showing how obese a patient is |
| **Ideal body weight** | What a person "should" weigh for their height (Lemmens 2005) | Dosing in obesity |
| **Adjusted body weight** | Ideal weight plus a fraction of the excess (Servin 1993) | Propofol maintenance in obesity |
| **Lean body mass** | Weight minus fat, estimated by the James equation | Schnider (Week 6) |
| **Fat-free mass** | A newer estimate of the same idea (Al-Sallami 2015) | Eleveld (Week 6), and the drug library (Week 7) |

Al-Sallami's paper is about children, despite being used here for adults too. It built a model on 1,011 people aged 3 to 29, whose curve levels off at an established adult equation. That's why one formula can span childhood and adulthood.

Fat receives relatively little of the blood flow, so a patient who doubles their weight by adding fat doesn't double their circulating volume. That's the problem running through Part 1, and you'll see exactly how it breaks a model in Week 1.

**References:** James WPT. *Research on Obesity*. London: HMSO; 1976 · Lemmens HJM, Brodsky JB, Bernstein DP. *Obes Surg* 2005;15:1082–3 · [Al-Sallami HS et al. *Clin Pharmacokinet* 2015;54:1169–78](https://link.springer.com/doi/10.1007/s40262-015-0277-z) · Servin F et al. *Anesthesiology* 1993;78:657–65

### The big picture

Every number in this workbook was produced by a reference program. So instead of wondering whether your code is right, you can have it compare itself to those numbers and print `OK` or `XX`. This week you build the tool that does that.

```
your code ──► a number ──► check("Marsh V1", number, 15.96) ──► OK or XX
```

### Set up the project

These are setup commands rather than code, so just type them. In your terminal (on Mac, type `python3` wherever this says `python`):

```bash
mkdir anesthesia-sim
cd anesthesia-sim
mkdir tci
python -m venv .venv
```

The last line creates a *virtual environment*: a private copy of Python for this project, so its packages can't clash with anything else on your computer. Now turn it on:

```bash
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

Your prompt now starts with `(.venv)`. You'll repeat this activate line every time you open a new terminal. Then install the packages and start Git:

```bash
pip install numpy scipy matplotlib pandas openpyxl "streamlit>=1.37"
git init
```

In your editor, create a file named `.gitignore` in `anesthesia-sim/` containing these two lines, which tell Git what not to save:

```text
.venv/
__pycache__/
```

Copy your own `patient.py` and `roberts.py` into `tci/`, then `cd tci`. You keep these as they are, because you wrote them yourself. Later lessons read `age`, `weight`, `height`, `sex`, `bmi`, `lbm` and `ffm` from your `Patient`, and call `summary()`. `roberts_schedule(weight)` should return a bolus in mg and a list of `(duration_min, rate_mg_per_min)` tuples.

### Learn it: functions that decide 🟢

In `tci/scratch.py`, type this. You'll reuse this file for practice all course, emptying it each time:

```python
def is_big_enough(label, size, minimum):
    if size >= minimum:
        print("YES", label)
    else:
        print("NO", label)


is_big_enough("the suitcase", 20, 10)
is_big_enough("the backpack", 5, 10)
```

```bash
python scratch.py
```

```text
YES the suitcase
NO the backpack
```

`==` asks "are these equal?". A single `=` means "store this value".

### Build it: `check()`, version 1 🟡

Create `tci/checks.py`, and write a function `check(label, got, expected)`:

- If `got` equals `expected`, it prints `OK` and the label.
- Otherwise it prints `XX` and the label.

Below the function, with no indent, add these two lines:

```python
check("two plus two", 2 + 2, 4)
check("this one should fail", 2 + 2, 5)
```

You should get:

```text
OK two plus two
XX this one should fail
```

<details>
<summary><b>Hint</b></summary>

It's the scratch function with small changes: the condition, and the two words printed.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def check(label, got, expected):
    if got == expected:
        print("OK", label)
    else:
        print("XX", label)
```

</details>

### Learn it: close enough, and printing nicely 🟢

Empty `scratch.py` and type this:

```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(abs(5 - 8))


def price(item, cost, tax=0.08):
    total = cost * (1 + tax)
    print(f"{item} costs {total:.2f}")


price("coffee", 4)
price("book", 10, tax=0)
```

```text
0.30000000000000004
False
3
coffee costs 4.32
book costs 10.00
```

- Computers store decimals with tiny rounding errors, so testing decimals for exact equality fails on numbers that are effectively the same.
- `abs()` gives the size of a difference, ignoring its sign. So "are these two close?" becomes `abs(a - b) <= something_small`.
- `tax=0.08` is a *default argument*, used when you leave it out.
- `f"..."` is an *f-string*. Anything inside `{ }` gets filled in, and `:.2f` means "2 decimal places".

### Build it: `check()`, version 2 🟡

Rewrite `check` in `checks.py`, with these changes:

- It takes a fourth input, `tol`, which defaults to `0.01`.
- It passes if `got` and `expected` differ by no more than `tol`.
- It prints the label, the value it got (with 4 decimals) and the expected value.

Replace the test lines at the bottom with these:

```python
check("rounding noise", 0.1 + 0.2, 0.3)
check("too far apart", 15.96, 16.5)
check("a count must be exact", 360, 361, tol=0)
```

Your output should match this, including the two spaces after `OK` and `XX`:

```text
OK  rounding noise: got 0.3000, expected 0.3
XX  too far apart: got 15.9600, expected 16.5
XX  a count must be exact: got 360.0000, expected 361
```

<details>
<summary><b>Hint</b></summary>

The condition is `abs(got - expected) <= tol`. Inside the f-string, write `{got:.4f}`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def check(label, got, expected, tol=0.01):
    if abs(got - expected) <= tol:
        print(f"OK  {label}: got {got:.4f}, expected {expected}")
    else:
        print(f"XX  {label}: got {got:.4f}, expected {expected}")
```

</details>

### Learn it: surviving an error with `try`/`except` 🟢

Later you'll check words as well as numbers, and you can't subtract words. Empty `scratch.py` and type this:

```python
def to_number(text):
    try:
        return float(text)
    except ValueError:
        return "that isn't a number"


print(to_number("3.5"))
print(to_number("banana"))
print(repr("banana"))
print(float(7))

ok = 2 + 2 == 4
print(ok)
```

```text
3.5
that isn't a number
'banana'
7.0
True
```

- `try` means "attempt this". `except ValueError` means "if that exact kind of error happens, do this instead of crashing".
- You can list several error types: `except (TypeError, ValueError):`. `float("banana")` raises a `ValueError`, and `float(None)` raises a `TypeError`.
- `repr()` shows a value as code would write it, so words appear in quotes.
- `ok = 2 + 2 == 4` stores the answer to the question, which is `True` or `False`.

**Read errors from the bottom up.** The last line says what went wrong, and the lines above say where. That habit will save you hours.

### Build it: `check()`, final version 🔴

Rewrite `check` one last time, keeping the same four inputs:

- **Try** treating both values as numbers using `float()`. Passing means they're within `tol`. Show `got` with 4 decimals.
- **If that raises a `TypeError` or `ValueError`,** they aren't numbers. Passing means they're simply equal. Show `got` using `repr()`.
- Print one line in the same format as before, then **return** `True` or `False`.

Test it with these lines at the bottom:

```python
check("numbers within tolerance", 0.1 + 0.2, 0.3)
check("matching words", "bolus", "bolus")
check("this one SHOULD say XX", "bolus", "rate")
```

You should see:

```text
OK  numbers within tolerance: got 0.3000, expected 0.3
OK  matching words: got 'bolus', expected bolus
XX  this one SHOULD say XX: got 'bolus', expected rate
```

<details>
<summary><b>Hint</b></summary>

Inside `try`, set two variables: `ok` (the comparison) and `shown` (the text to display). Set the same two in `except`. Then use them after the whole `try`/`except`, so you only need one `print`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def check(label, got, expected, tol=0.01):
    """Print OK or XX for one checkpoint, and return True or False."""
    try:
        ok = abs(float(got) - float(expected)) <= tol
        shown = f"{float(got):.4f}"
    except (TypeError, ValueError):
        ok = got == expected
        shown = repr(got)

    if ok:
        mark = "OK"
    else:
        mark = "XX"

    print(f"{mark}  {label}: got {shown}, expected {expected}")
    return ok
```

The triple-quoted line is a *docstring*, a note saying what the function does.

</details>

### Learn it: how imports work 🟢

A project this size can't live in one file. Imports let one file use what another file has defined. This is a section you'll come back to.

Make a new folder, `practice/kitchen/`, and create `recipes.py` in it:

```python
print("recipes.py is being read")

CUPS_PER_LITER = 4.2


def double(x):
    return x * 2


def triple(x):
    return x * 3


class Oven:
    def __init__(self, temp):
        self.temp = temp
```

It holds three kinds of thing: a constant, two functions and a class. There are several ways to get at them from another file in the same folder. Create `dinner.py` next to it and type this:

```python
# Style 1: bring in one function by name
from recipes import double
print(double(5))

# Style 2: bring in several things. A class imports the same way as a function
from recipes import triple, Oven, CUPS_PER_LITER
print(triple(5))
print(Oven(180).temp)
print(CUPS_PER_LITER)

# Style 3: bring in the whole file, then use its name with a dot
import recipes
print(recipes.double(10))
print(recipes.Oven(200).temp)

# Style 4: bring it in under a shorter or clearer name
import recipes as r
from recipes import double as twice
print(r.triple(10))
print(twice(10))
```

Run it from inside `kitchen/`:

```bash
python dinner.py
```

```text
recipes.py is being read
10
15
180
4.2
20
200
30
20
```

What to notice:

- **No `.py`.** The file is `recipes.py`, and you import `recipes`. So a file name has to work as a Python name: `dose_table.py` is fine, but `dose-table.py` can't be imported this way.
- **Importing runs the file.** That's what the first line of the output shows. It also only happened once, even with several imports.

| Style | Example | Use it when |
|---|---|---|
| `from file import thing` | `from engine import Simulation` | You need a few things. This is what the project uses most |
| `import file` | `import recipes` | You need many things, or want it obvious where each came from |
| `import file as name` | `import numpy as np` | The name is long, or there's a standard short form |
| `from file import thing as other` | `double as twice` | Two files use the same name |

**How does Python find the file?** It looks in the folder of the file you're running, then in the standard library, then in installed packages such as NumPy. Three rules follow from this:

1. **Files in the same folder can import each other directly.** All of `tci/` works this way.
2. **Files in different folders can't, by default.** That's why `machine/` gets its own copy of `checks.py` in Part 2.
3. **Never name your file after something you import.** A file of your own called `math.py` or `random.py` hides the real one. You'll try this below.

One more trap: if `a.py` imports from `b.py` and `b.py` imports from `a.py`, you can get a confusing error about a "circular import". Have code flow in one direction, like this:

```
checks.py, patient.py ──► pk_models.py ──► engine.py ──► everything else
```

### Learn it: `if __name__ == "__main__":` 🟢

Since importing a file runs it, any test code at the bottom of a file runs on every import too. In a big project, that would mean a pile of tests going off constantly.

Python gives every file a hidden variable called `__name__`. In the file you run directly, it holds `"__main__"`. In a file being imported, it holds the file's own name. Add this to the bottom of `recipes.py`:

```python


print("my name is", __name__)

if __name__ == "__main__":
    print("I was run directly, so here are my tests")
    print(double(2) == 4)
```

Now run each file and compare:

```bash
python recipes.py
```

```text
recipes.py is being read
my name is __main__
I was run directly, so here are my tests
True
```

```bash
python dinner.py
```

```text
recipes.py is being read
my name is recipes
10
```

The tests only run when you run that file itself. That's the pattern for the whole course: code at the top of a file, and its checks in this block at the bottom.

### Build it: finish `checks.py` 🟡

In `checks.py`, put your three test lines inside an `if __name__ == "__main__":` block. The output should be unchanged. Then prove that it works: in `tci/scratch.py`, import `check` and call it once with a label of `"borrowed function"`. You should see only one line:

```text
OK  borrowed function: got 4.0000, expected 4
```

<details>
<summary><b>Answer</b></summary>

At the bottom of `checks.py`:

```python
if __name__ == "__main__":
    check("numbers within tolerance", 0.1 + 0.2, 0.3)
    check("matching words", "bolus", "bolus")
    check("this one SHOULD say XX", "bolus", "rate")
```

And in `scratch.py`:

```python
from checks import check

check("borrowed function", 2 + 2, 4)
```

</details>

### Check it: your `Patient` 🟡

At the bottom of your `patient.py`, write a check block that does the following:

1. Imports `check`.
2. Makes patient `a`, who is 40 years old, 70 kg, 170 cm and male. Prints `a.summary()`, and checks that `a.bmi` is `24.22`.
3. Makes patient `ref`, who is 53, 77 kg, 177 cm and male. Checks that `ref.lbm` is `60.48`.
4. Tries to make a patient with `sex="X"`. If that succeeds, it prints `XX  sex 'X' was accepted`. If it raises a `ValueError`, it prints `OK  sex 'X' was rejected`.

You should see your patient's summary, followed by this:

```text
OK  Patient A BMI: got 24.2215, expected 24.22
OK  Schnider reference LBM: got 60.4761, expected 60.48
OK  sex 'X' was rejected
```

<details>
<summary><b>Hint</b></summary>

For step 4, put the `Patient(...)` line and the `XX` print together in the `try`. If the patient is refused, Python jumps straight to `except` and skips the `XX` line.

</details>
<details>
<summary><b>Answer</b></summary>

```python
if __name__ == "__main__":
    from checks import check

    a = Patient(age=40, weight=70, height=170, sex="M")
    print(a.summary())
    check("Patient A BMI", a.bmi, 24.22)

    ref = Patient(age=53, weight=77, height=177, sex="M")
    check("Schnider reference LBM", ref.lbm, 60.48)

    try:
        Patient(age=40, weight=70, height=170, sex="X")
        print("XX  sex 'X' was accepted")
    except ValueError:
        print("OK  sex 'X' was rejected")
```

</details>

Fix the **first** `XX` before anything else. Later ones often disappear with it. Then save your work:

```bash
cd ..
git add .
git commit -m "week 0: checker and patient checks"
cd tci
```

### Break it on purpose

1. In `checks.py`, delete the colon after `def check(...)`. The error points at the line and says `expected ':'`.
2. Remove the indent from the `if ok:` line. You'll get `IndentationError: unindent does not match any outer indentation level`.
3. In `patient.py`, change `from checks import check` to `from check import check`. You'll get `ModuleNotFoundError: No module named 'check'`.
4. In `practice/kitchen/`, create a file called `random.py` containing one line, `print("oops")`. In `dinner.py`, add `import random` and then `print(random.randint(1, 6))`. Your `random.py` runs instead of the real one, and you get `AttributeError: module 'random' has no attribute 'randint'`. Newer versions of Python go on to suggest that your file may be hiding the real module. Delete `random.py`.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ModuleNotFoundError: No module named 'checks'` | Python looks for imported files in the same folder as the file you're running. Make sure `checks.py` is next to `patient.py`, and spelled exactly that way. |
| `ImportError: cannot import name 'check' from 'checks'` | The file was found, but it has nothing called that. Check the spelling, and make sure you saved. |
| `ModuleNotFoundError: No module named 'numpy'` | Your virtual environment isn't active. Run the activate line again. |
| `FileNotFoundError` when opening a data file (from Week 5 on) | Paths like `cases/x.csv` are relative to the folder your *terminal* is in. `cd` into `tci/` first. |
| Nothing prints at all | The `if __name__ == "__main__":` line is misspelled (two underscores on each side), or it's indented. |
| `XX  Patient A BMI` | Your BMI calculation. Height must go from cm to m before squaring. |
| `IndentationError` | Lines inside a block must be indented by exactly 4 more spaces. Don't mix tabs and spaces. |

### Things to consider

- Your `Patient` refuses a non-integer age. In Part 4 a web form might hand you `40.0`, and you'll have to choose between converting it with `int()` and loosening the check.
- `check()` returns `ok`, but nothing uses that yet. It costs nothing to keep, and a later script can count failures with it.

### Checkpoint

`python checks.py` prints three lines, ending in the deliberate `XX`. `python patient.py` prints all `OK`. You can name the four import styles, and `git log` shows your commit.

---

# PART 1 — TCI SIMULATOR (Python)

The rule for all of Part 1: **numbers that change per drug live in `pk_models.py`. Math that's the same for every drug lives in `engine.py`.** When you're unsure where something goes, ask: "does this change if I switch drugs?"

### The story of propofol models

You'll build these models in roughly the order they were developed, and each one exists because of a problem with an earlier one.

| Year | Model | What it added | Its weakness |
|---|---|---|---|
| 1979 | **Sheiner** (d-tubocurarine, not propofol) | The effect-site compartment: a way to explain why effect lags behind plasma concentration | |
| 1987 | **Gepts** | An early three-compartment propofol model, from three groups of six patients on constant infusions (3, 6 or 9 mg/kg/h) | Apparently few elderly or obese patients, and the full details weren't published |
| 1991 | **Marsh** | Became the basis of the first commercial TCI systems | Scales by total weight and ignores age |
| 1998–99 | **Schnider** | Age and lean body mass, from a combined PK and PD study in volunteers | Fixed V1 needs effect-site mode, and the James equation misbehaves in severe obesity |
| 2018 | **Eleveld** | A single model for a very wide range of patients | Complex. You'll build it in Week 6B |

The usual summary is "Marsh came first, failed in obesity, and Schnider fixed it." The truth is a bit more interesting:

- **Marsh wasn't first.** It was adapted from Gepts.
- **Marsh is a children's paper,** though the adult numbers associated with it became what we now call the "Marsh model."
- **Schnider didn't fix obesity.** It addressed different problems (age, and the time course of effect), and its lean body mass equation creates a new failure in severe obesity.
- **Neither failure is simple.** In one study of morbidly obese patients, entering an *adjusted* weight into Marsh or Schnider made them markedly more accurate.

**Schnider 1998, in brief** (you'll build this model in Week 6). 24 healthy volunteers aged 26 to 81 each received a bolus and, an hour later, a 60-minute infusion at 25, 50, 100 or 200 µg/kg/min. Parameters estimated from infusion data alone underpredicted the concentrations seen after a bolus, so the way a drug is given matters. Age affected V2 and Cl2, while weight, height and lean body mass affected metabolic clearance. V1 is fixed at 4.27 L for everyone, so in plasma-targeting mode the initial bolus doesn't change with weight, which is why Absalom's review says Schnider should always be used in effect-site mode.

**Why this matters at the bedside.** The BJA Education review by Al-Rifai and Mulvey makes the point that poor understanding of these models has contributed to accidental awareness, as documented in the NAP5 report. A TCI number on a screen is only as good as your understanding of what the model assumes.

**Eleveld 2018, in brief.** Rather than a new study, this pooled 30 previously published studies: 15,433 concentrations and 28,639 BIS observations from 1,033 people, aged from 27 weeks post-menstrual to 88 years and weighing 0.68 to 160 kg. The goal was a single model for all of them, in both anesthesia and sedation. It uses age, post-menstrual age, weight, height, sex, and whether other anesthetic drugs are present.

**References:** [Schnider TW et al. *Anesthesiology* 1998;88:1170–82](https://scilit.com/publications/d01854b67fa6fdeb01a22b8de7e9238c) · Schnider TW et al. *Anesthesiology* 1999;90:1502–16 · [Eleveld DJ et al. *Br J Anaesth* 2018;120:942–59](https://doi.org/10.1016/j.bja.2018.01.018), corrigendum 121:519 · Al-Rifai Z, Mulvey D. *BJA Education* 2016;16:92–7 · [Engbers F, Boveri H. From Schnider to Eleveld. TIVA Trainer blog, 2024](https://blog.tivatrainer.com/from-schnider-to-eleveld/)

**Where Part 1 ends up:** a simple Python version of [StanpumpR](https://stanpumpr.io). You enter a patient and a dose table the way you dose in the OR, and see each drug's effect-site concentration, compare models, see the combined propofol–opioid effect, and run a simulated TCI pump that re-decides every 10 seconds.

---

## Week 1 — A `Drug` class and the Marsh model

**Goal:** `marsh_drug(patient)` returns a `Drug` holding V1, five rate constants and `ke0`.

**New ideas:** using a class purely to hold data; applying a factory function to a real problem; `**kwargs`.

### The science: the Marsh model

**Where it came from.** Marsh is an adaptation of the Gepts model, not a fresh study. It matches Gepts except for a larger central volume, 0.228 L/kg, and no rationale for that change was ever published (Absalom 2009).

**The 1991 paper, in brief.** Marsh and colleagues used an automated pump running an adult model to give propofol to 20 children having minor surgery. Blood samples showed the pump consistently overestimated the children's levels. So they derived new rate constants from their data, and those matched better in 10 further children. The point of the paper was that *adult models don't work in children.* The irony is that the name now mostly refers to the adult parameter set. It's the one you're about to use, and it's the one the Diprifusor system used.

**How it scales.** Volumes and clearances are proportional to total body weight, and the rate constants never change. This is simple, and it has consequences:

- **Obesity.** V1 sets the size of the induction dose, and Marsh's V1 keeps growing with weight. But V1 hasn't been shown to be significantly larger in obesity, so severely obese patients can get a very large induction dose. Induction needs seem to follow lean mass more closely, while maintenance needs follow total mass.
- **Age.** There's no age term at all, and Marsh has been shown to under-predict plasma concentrations in the elderly.

**Its ke0.** The 0.26 /min you'll use came from first-generation pumps, and the data behind it were never published in a peer-reviewed journal. Struys and colleagues later found that 1.2 /min predicted the time course of clinical effect better. That pair is often called the "modified Marsh". Early Diprifusor pumps could only target plasma concentration, and showed effect-site concentration only for information.

**Marsh in obesity, measured.** Cortínez and colleagues (2014) tested propofol models in 20 morbidly obese patients. All the models tended to underestimate concentrations. Entering an adjusted weight, instead of total weight, into Marsh and Schnider gave the lowest errors of all (median performance error under 10%, median absolute error under 25%).

**References:** [Marsh B et al. *Br J Anaesth* 1991;67:41–8](https://scilit.com/publications/4b744948e94af9a237cc748dec3fc33c) · [Gepts E et al. *Anesth Analg* 1987;66:1256–63](https://scilit.com/publications/4eb6c555dcc148eec453e1fcc6d611bd) · [Absalom AR et al. *Br J Anaesth* 2009;103:26–37](https://doi.org/10.1093/bja/aep143) (the best place to read this history) · [Cortínez LI et al. *Anesth Analg* 2014;119:302–10](https://read.qxmd.com/read/24977639/performance-of-propofol-target-controlled-infusion-models-in-the-obese-pharmacokinetic-and-pharmacodynamic-analysis)

### The big picture

`patient.py` describes a *person*. This week's file describes a *drug in that person*: a labeled box of numbers. Nothing moves over time yet. That starts in Weeks 2 and 3.

```
patient.py  ──(patient.weight)──►  pk_models.py: marsh_drug(patient) ──► a Drug (just numbers)
```

Every model you ever add will have this shape: a function that takes a `Patient` and returns a `Drug`.

You practiced all the class skills you need in Week P2 with `Dog` and `Book`. If you want a refresher, reread that lesson first.

### Build it: the `Drug` class 🟡

Create `tci/pk_models.py`. Write a class named `Drug`, whose `__init__` takes these inputs, in exactly this order:

```
name, V1, k10, k12, k13, k21, k31, ke0, dose_unit, conc_unit
```

- `dose_unit` defaults to `"mg"`, and `conc_unit` defaults to `"µg/mL"`.
- Every input gets stored on the object under the same name.
- Add a `__repr__` that displays as `Drug('test', V1=15.00, k10=0.100)`.
- A docstring is a good habit: "Rate constants for a 3-compartment model with an effect site. The engine reads these. It never needs to know which drug this is."

To test it, add this at the bottom:

```python
if __name__ == "__main__":
    d = Drug("test", 15, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6)
    print(d.name, d.V1, d.ke0, d.dose_unit)
    print(d)
```

You should see:

```text
test 15 0.6 mg
Drug('test', V1=15.00, k10=0.100)
```

<details>
<summary><b>Hint</b></summary>

It's `Dog` with more attributes, plus defaults like `species="dog"`. A long list of inputs can continue onto a second line, because Python knows the bracket is still open. For the `__repr__`, `:.2f` shows two decimals and `:.3f` shows three.

</details>
<details>
<summary><b>Answer</b></summary>

```python
class Drug:
    """Rate constants for a 3-compartment model with an effect site.
    The engine reads these. It never needs to know which drug this is."""

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
        return f"Drug({self.name!r}, V1={self.V1:.2f}, k10={self.k10:.3f})"


if __name__ == "__main__":
    d = Drug("test", 15, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6)
    print(d.name, d.V1, d.ke0, d.dose_unit)
    print(d)
```

</details>

### Build it: `marsh_drug` 🔴

Write a factory function, like `puppy()` in Week P2. `marsh_drug(patient)` takes a `Patient` and returns a `Drug` named `"Propofol (Marsh)"`, using these values:

| Parameter | Value |
|---|---|
| V1 | 0.228 L/kg × weight |
| k10, k12, k13 | 0.119, 0.112, 0.0419 /min |
| k21, k31 | 0.055, 0.0033 /min |
| ke0 | 0.26 /min |

It goes above the `if __name__` line, with no indent. Watch out: if you pass the numbers by position and swap two, nothing crashes and every result is quietly wrong.

<details>
<summary><b>Hint</b></summary>

Only one line does any arithmetic. Then call `Drug(...)` with the values in the order `__init__` expects. You can pass the last one by name: `ke0=0.26`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def marsh_drug(patient):
    """Marsh B et al. Br J Anaesth 1991;67:41-48.
    Only V1 scales with weight. The rate constants are FIXED."""
    V1 = 0.228 * patient.weight
    return Drug("Propofol (Marsh)", V1, 0.119, 0.112, 0.0419, 0.055, 0.0033, ke0=0.26)
```

</details>

### Learn it: `**extras`, in a scratch file 🟢

The next function uses a piece of syntax you haven't seen. Empty `scratch.py` and type this:

```python
def order(food, **extras):
    print(food, extras)


order("pizza")
order("pizza", size="large")
order("pizza", size="large", crust="thin")

options = {"size": "small", "crust": "thick"}
order("pasta", **options)
```

```text
pizza {}
pizza {'size': 'large'}
pizza {'size': 'large', 'crust': 'thin'}
pasta {'size': 'small', 'crust': 'thick'}
```

In a function's *definition*, `**extras` collects any extra keyword arguments into a dictionary. In a *call*, `**options` does the reverse and unpacks a dictionary back into keyword arguments. Together they let a function pass labels along without knowing what they are.

### Build it: `drug_from_clearances` 🔴

Marsh publishes rate constants, but most papers publish volumes and clearances. Write a function that converts them, once, so no other code has to.

Its inputs are `name, V1, V2, V3, Cl1, Cl2, Cl3, ke0, **units`.

```
k10 = Cl1 / V1      k12 = Cl2 / V1      k13 = Cl3 / V1
k21 = Cl2 / V2      k31 = Cl3 / V3
```

It returns a `Drug`, passing `**units` along so that unit labels get through. You won't use this function until Week 6, but it belongs here while the idea is fresh.

<details>
<summary><b>Answer</b></summary>

```python
def drug_from_clearances(name, V1, V2, V3, Cl1, Cl2, Cl3, ke0, **units):
    """Many papers publish volumes + clearances, not rate constants.
    Convert once, here, so no other code ever has to."""
    k10 = Cl1 / V1
    k12 = Cl2 / V1
    k13 = Cl3 / V1
    k21 = Cl2 / V2
    k31 = Cl3 / V3
    return Drug(name, V1, k10, k12, k13, k21, k31, ke0, **units)
```

</details>

### Check it 🟡

Replace everything inside the `if __name__` block with checks. Here's the start:

```python
if __name__ == "__main__":
    from patient import Patient
    from checks import check

    # --- Week 1: Marsh ---
    p70 = Patient(40, 70, 170, "M")
    d70 = marsh_drug(p70)
    print(d70)
    check("Marsh V1, 70 kg (L)", d70.V1, 15.96)
```

Add these yourself:

- The same patient at 90 kg: V1 should be `20.52`.
- k10 must be identical at 70 and 90 kg. Compare the two with `tol=1e-12`.
- `drug_from_clearances("test", V1=2, V2=4, V3=8, Cl1=1, Cl2=2, Cl3=4, ke0=0.5)`, with one check for each of its five rate constants. The values are 0.5, 1.0, 2.0, 0.5 and 0.5. They're made-up numbers, chosen so that using the wrong volume can't pass by accident.

<details>
<summary><b>Answer</b></summary>

```python
if __name__ == "__main__":
    from patient import Patient
    from checks import check

    # --- Week 1: Marsh ---
    p70 = Patient(40, 70, 170, "M")
    p90 = Patient(40, 90, 170, "M")
    d70 = marsh_drug(p70)
    d90 = marsh_drug(p90)
    print(d70)
    check("Marsh V1, 70 kg (L)", d70.V1, 15.96)
    check("Marsh V1, 90 kg (L)", d90.V1, 20.52)
    check("k10 is the same at 70 and 90 kg", d90.k10, d70.k10, tol=1e-12)

    # --- Week 1: drug_from_clearances ---
    test = drug_from_clearances("test", V1=2, V2=4, V3=8, Cl1=1, Cl2=2, Cl3=4, ke0=0.5)
    check("k10 = Cl1/V1", test.k10, 0.5)
    check("k12 = Cl2/V1", test.k12, 1.0)
    check("k13 = Cl3/V1", test.k13, 2.0)
    check("k21 = Cl2/V2", test.k21, 0.5)
    check("k31 = Cl3/V3", test.k31, 0.5)
```

</details>

You should see:

```text
Drug('Propofol (Marsh)', V1=15.96, k10=0.119)
OK  Marsh V1, 70 kg (L): got 15.9600, expected 15.96
OK  Marsh V1, 90 kg (L): got 20.5200, expected 20.52
OK  k10 is the same at 70 and 90 kg: got 0.1190, expected 0.119
OK  k10 = Cl1/V1: got 0.5000, expected 0.5
OK  k12 = Cl2/V1: got 1.0000, expected 1.0
OK  k13 = Cl3/V1: got 2.0000, expected 2.0
OK  k21 = Cl2/V2: got 0.5000, expected 0.5
OK  k31 = Cl3/V3: got 0.5000, expected 0.5
```

Commit.

### Explore it: see the obesity problems for yourself 🔴

This is where the code meets the science. In `scratch.py`, write a loop over these weights for a 40-year-old man who is 170 cm tall: 70, 100, 124, 150 and 200 kg. For each one, print the weight, the BMI, Marsh's V1 and the James lean body mass, in this format. Your `Patient` must calculate `lbm` with the James equation for these to match.

```text
70 kg  BMI 24  Marsh V1 16.0 L  LBM 55.3 kg
100 kg  BMI 35  Marsh V1 22.8 L  LBM 65.7 kg
124 kg  BMI 43  Marsh V1 28.3 L  LBM 68.3 kg
150 kg  BMI 52  Marsh V1 34.2 L  LBM 65.3 kg
200 kg  BMI 69  Marsh V1 45.6 L  LBM 42.8 kg
```

Read down the columns. Marsh's V1 keeps climbing, which is the induction problem. Then look at lean body mass: it peaks near a BMI of 43, then **falls**, until the 200 kg man is calculated to have less lean mass than the 70 kg man. That can't be true, and it's a property of the equation's shape: the second term grows with weight squared, so it eventually overtakes the first.

If you work it out with calculus, the peak is at a BMI of about 43 for men and about 36 for women, close to the roughly 42 and 37 that Absalom's review reports. Devices handle this by capping lean body mass at its peak for a given height. You'll meet this again in Week 6.

<details>
<summary><b>Answer</b></summary>

```python
from patient import Patient
from pk_models import marsh_drug

for weight in [70, 100, 124, 150, 200]:
    p = Patient(40, weight, 170, "M")
    print(f"{weight} kg  BMI {p.bmi:.0f}  Marsh V1 {marsh_drug(p).V1:.1f} L  LBM {p.lbm:.1f} kg")
```

</details>

### Break it on purpose

1. Delete the `self.k10 = k10` line. You'll get `AttributeError: 'Drug' object has no attribute 'k10'. Did you mean: 'k12'?` Python is guessing at a typo, and here the guess is wrong, because the attribute isn't misspelled. It's missing.
2. In `marsh_drug`, remove `ke0=0.26`. You'll get `TypeError: Drug.__init__() missing 1 required positional argument: 'ke0'`.
3. Change `0.228 * patient.weight` to `0.228 * patient.height`. There's no crash at all, only `XX` lines. This is the most important one, because it's why the checks exist.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `AttributeError: 'Drug' object has no attribute 'k10'` | `__init__`: a `self.k10 = k10` line is missing or misspelled. |
| `TypeError: Drug.__init__() missing 1 required positional argument` | The `Drug(...)` call passes fewer values than `__init__` lists. Count them. |
| `XX  Marsh V1, 70 kg` | The coefficient in `marsh_drug` (0.228). |
| `XX  k10 is the same at 70 and 90 kg` | Weight has crept into a rate constant. Only V1 may use `patient.weight`. |
| `XX  k21 = Cl2/V2` (or another k) | A division in `drug_from_clearances` uses the wrong volume. |
| `print(d70)` shows `<...Drug object at 0x...>` | `__repr__` is missing, or isn't indented inside the class. |

### Things to consider

- Why does `marsh_drug` take the whole `Patient` when it only reads `.weight`? Because every model will take a `Patient`, so later code can call `model_fn(patient)` without caring which model it holds.
- `Drug` has no methods beyond `__repr__`, because a `Drug` only remembers numbers. All the time-based work goes in the engine.

### Checkpoint

| 70 kg Marsh | value |
|---|---|
| V1 | 15.96 L |
| k10 / k12 / k13 | 0.119 / 0.112 / 0.0419 |
| k21 / k31 | 0.055 / 0.0033 |
| 90 kg V1 | 20.52 L (everything else unchanged) |

---

## Week 2 — The physics: `deriv()`

**Goal:** one function that, given the current state, returns how fast each compartment is changing.

**New ideas:** tuple unpacking; returning several values; testing one function on its own before it's buried in a loop.

### The science: compartments and the effect site

**What a compartment is.** A compartment is a mathematical convenience, not an organ. V1 isn't the blood volume, and Marsh's 16 L for a 70 kg patient is far more than that. The model says only that measured concentrations behave *as if* the drug were moving between three tanks. The fast and slow peripheral compartments are often described as well-perfused tissue and fat, but that's an interpretation and not what was measured.

**The problem of hysteresis.** After a bolus, plasma concentration peaks almost at once, yet the clinical effect takes minutes to peak. So one plasma concentration can correspond to two different effects, one on the way up and one on the way down. A plot of effect against concentration makes a loop instead of a line.

**Sheiner 1979, in brief.** Sheiner and colleagues wanted a model that would work in this early, non-equilibrium period. They studied d-tubocurarine, relating plasma concentration to paralysis in 7 normal subjects. Their solution was to add a hypothetical compartment connected to plasma by a first-order process, without changing the drug's mass balance in the body. The concentration in that compartment then links to effect through a sigmoid curve (the Hill equation). For d-tubocurarine they found an equilibration rate constant of about 0.13 /min.

That hypothetical compartment is your `Ce`, and its rate constant is your `ke0`. It's the idea behind effect-site targeting.

**What ke0 means at the bedside.** Effect-site concentration closes half of the gap to plasma every `ln(2) / ke0` minutes: about 2.7 minutes with Marsh's 0.26, and 1.5 minutes with Schnider's 0.456. That's a large difference for what's nominally the same drug, and it's one reason a ke0 shouldn't simply be moved from one model to another.

**References:** [Sheiner LB et al. *Clin Pharmacol Ther* 1979;25:358–71](https://scilit.net/publications/0811ea632d03667f15fd3d16c5397fee) · [Absalom AR et al. *Br J Anaesth* 2009;103:26–37](https://doi.org/10.1093/bja/aep143)

### The big picture

`engine.py` is where time will start to matter, but this week you write only its heart. `deriv()` answers one question: **right now, how fast is each compartment changing?** It doesn't move time forward. That's next week.

```
a Drug (numbers) ──────────┐
state y = [A1, A2, A3, Ce] ┼──► deriv() ──► (dA1, dA2, dA3, dCe)
infusion rate ─────────────┘
```

A1, A2 and A3 are *amounts* of drug (mg) in the central, fast-peripheral and slow-peripheral compartments. Ce is the effect-site *concentration*.

### Learn it: unpacking, in a scratch file 🟢

Empty `scratch.py` and type this:

```python
colors = ["red", "green", "blue"]
first, second, third = colors
print(first)
print(third)


def smallest_and_largest(a, b):
    return min(a, b), max(a, b)


low, high = smallest_and_largest(9, 3)
print(low, high)
```

```text
red
blue
3 9
```

`first, second, third = colors` hands out the list's values by position, one per name. A function can also return several values separated by commas, and you catch them the same way. Your `deriv` will do both.

### Work it on paper first

The model is four equations:

```
dA1/dt = rate − (k10 + k12 + k13)·A1 + k21·A2 + k31·A3
dA2/dt = k12·A1 − k21·A2
dA3/dt = k13·A1 − k31·A3
dCe/dt = ke0·(Cp − Ce)        where Cp = A1 / V1
```

In words:

- **dA1:** the pump adds `rate`. Drug leaves by elimination (k10) and by moving out to the peripheral compartments (k12, k13). Drug returns from them (k21, k31).
- **dA2, dA3:** each gains what flows in from the centre and loses what flows back.
- **dCe:** the effect site chases the plasma concentration, at a speed set by ke0.

Take a 70 kg Marsh patient who has just received 100 mg, with nothing anywhere else: A1 = 100 and A2 = A3 = Ce = 0. With a calculator or by hand:

- dA2 = 0.112 × 100 − 0 = **11.2** mg/min
- dA3 = 0.0419 × 100 − 0 = **4.19** mg/min
- Now work out dA1, and dCe (V1 is 15.96). You should get **−27.29** and about **1.629**.

If you know the answer before the code gives it, you can tell whether the code is right. Do this whenever you can.

### Build it: `deriv` 🔴

Create `tci/engine.py`, and write this function from the equations above:

```python
def deriv(t, y, drug, rate):
    """Rates of change for [A1, A2, A3, Ce].
    t    : time (min). solve_ivp passes it in, even though we don't use it
    y    : [A1, A2, A3, Ce]  amounts in mg (A) and effect-site conc (Ce)
    drug : a Drug
    rate : current infusion rate into A1 (mg/min)
    """
    # your code here
```

Use one short line per equation, not one giant expression. Return all four values, in the same order as `y`.

<details>
<summary><b>Hint</b></summary>

Start by unpacking `y`, as in the scratch file, then calculate `Cp`. Each constant lives on `drug`, so the first equation begins `dA1 = rate - (drug.k10 + ...`. It reads almost like the math.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def deriv(t, y, drug, rate):
    """Rates of change for [A1, A2, A3, Ce].
    t    : time (min). solve_ivp passes it in, even though we don't use it
    y    : [A1, A2, A3, Ce]  amounts in mg (A) and effect-site conc (Ce)
    drug : a Drug
    rate : current infusion rate into A1 (mg/min)
    """
    A1, A2, A3, Ce = y
    Cp = A1 / drug.V1

    dA1 = rate - (drug.k10 + drug.k12 + drug.k13) * A1 + drug.k21 * A2 + drug.k31 * A3
    dA2 = drug.k12 * A1 - drug.k21 * A2
    dA3 = drug.k13 * A1 - drug.k31 * A3
    dCe = drug.ke0 * (Cp - Ce)
    return dA1, dA2, dA3, dCe
```

</details>

### Check it 🔴

Write the check block at the bottom of `engine.py`, with no help on its structure this time. Make `drug` from a 40-year-old, 70 kg, 170 cm man, call `deriv(0, [100, 0, 0, 0], drug, 0)`, and check the four results against the numbers you worked out on paper. Your labels should produce this:

```text
OK  dA1/dt: got -27.2900, expected -27.29
OK  dA2/dt: got 11.2000, expected 11.2
OK  dA3/dt: got 4.1900, expected 4.19
OK  dCe/dt: got 1.6291, expected 1.629
```

<details>
<summary><b>Hint</b></summary>

You'll need three imports at the top of the block: `Patient`, `marsh_drug` and `check`. Your Week 1 block is a good model.

</details>
<details>
<summary><b>Answer</b></summary>

```python


if __name__ == "__main__":
    from patient import Patient
    from pk_models import marsh_drug
    from checks import check

    # --- Week 2: deriv, 100 mg just bolused, 70 kg Marsh ---
    drug = marsh_drug(Patient(40, 70, 170, "M"))
    dA1, dA2, dA3, dCe = deriv(0, [100, 0, 0, 0], drug, 0)
    check("dA1/dt", dA1, -27.290)
    check("dA2/dt", dA2, 11.200)
    check("dA3/dt", dA3, 4.190)
    check("dCe/dt", dCe, 1.629)
```

</details>

### Write your own check 🔴

The checks so far compare your code to numbers from the book. Here's a stronger kind: a check based on physiology.

Drug can only leave the body through k10. Moving between compartments shuffles it around but doesn't create or destroy any. So at any moment:

```
dA1 + dA2 + dA3  =  rate − k10·A1
```

Add a check to your block that tests this for the same bolus, with a label of `"mass balance"`. The expected value is the right-hand side, which you can calculate in code from `drug.k10`.

<details>
<summary><b>Answer</b></summary>

```python
    check("mass balance", dA1 + dA2 + dA3, 0 - drug.k10 * 100)
```

</details>

```text
OK  mass balance: got -11.9000, expected -11.899999999999999
```

If your `expected` prints as a long decimal like that, it's the rounding noise from Week 0, and this is why `check()` has a tolerance.

Commit.

### Break it on purpose

1. Remove the `return` line. You'll get `TypeError: cannot unpack non-iterable NoneType object`. A function with no `return` gives back `None`.
2. Pass `[100, 0, 0]` as the state. You'll get `ValueError: not enough values to unpack (expected 4, got 3)`.
3. Return `dA1, dA3, dA2, dCe`. There's no crash. Only the `dA2` and `dA3` lines turn `XX`, and the mass balance still passes, because it adds them up. A check can only catch what it tests, so one kind of check isn't enough.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ValueError: not enough values to unpack (expected 4, got 3)` | The `y` passed in has 3 numbers. It needs 4. |
| `TypeError: cannot unpack non-iterable NoneType object` | `deriv` has no `return` line. |
| Only `XX  dA1/dt` | The signs in the dA1 line: three things leave (minus) and two return (plus). |
| Only `XX  dCe/dt` | Ce must chase **Cp** (A1 ÷ V1), not A1 itself. |
| Only dA2 and dA3 are `XX`, with each other's numbers | They're swapped in the `return`. |
| `XX  mass balance`, but the other four are `OK` | The `expected` side of your check. It should use k10 and A1 only. |

### Things to consider

- The return order is a silent contract. Next week `solve_ivp` matches values by position, not by name, so a wrong order would give wrong results and no error.
- Why take a `t` the function never uses? Because `solve_ivp` always calls `deriv(t, y, ...)`. You have to accept the arguments a library hands you.

### Checkpoint

`deriv(0, [100, 0, 0, 0], marsh_70kg, 0)` → **(−27.290, 11.200, 4.190, 1.629)**, and the mass balance check says `OK`.

---

## Week 3A — `Simulation`: the event schedule

**Goal:** a `Simulation` class that writes down boluses and infusion rates, ready to run next lesson.

**New ideas:** a class whose state builds up across several method calls; a list of tuples as an event schedule; NumPy arrays and `np.linspace`.

**Read first:** [NumPy: the absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html)

### The science: a bolus and an infusion are different mathematics

`deriv()` has a `rate` input, so an infusion fits directly into the equations: it's a steady inflow to A1. A bolus doesn't. It's modeled as an instant jump in A1, because the whole dose arrives in far less time than anything else in the model takes to happen.

That's a simplification, and Schnider's 1998 study shows it has a cost. Parameters estimated from infusion data alone underpredicted the concentrations seen after a bolus. Early concentrations after a fast injection are the least accurate part of these models. Eleveld's diagnostic plots show the same kind of early bias, which the authors attribute to the model not capturing "front-end kinetics". So be a little skeptical of any model's prediction for the first minute or two.

### The big picture

`deriv()` knows *how fast* things change. `Simulation` is the **clock**. It holds a to-do list of doses, then walks time forward. This lesson builds the to-do list, and next lesson builds the walking.

```
sim.bolus(at, dose) / sim.rate(at, value)  ──► add an event to sim.schedule  (nothing runs yet)
```

### Learn it: a class that collects things 🟢

In Week P2, a `Kennel` kept a list that grew as you called `add()`. Here's the same pattern with a to-do list, plus a way to tell kinds of item apart. Empty `tci/scratch.py` and type this:

```python
class Diary:
    def __init__(self, days=7):
        self.days = days
        self.entries = []

    def meeting(self, day, who):
        self.entries.append((day, "meeting", who))

    def holiday(self, day, place):
        self.entries.append((day, "holiday", place))

    def on_day(self, day):
        found = []
        for when, kind, detail in self.entries:
            if when == day:
                found.append(f"{kind}: {detail}")
        return found


d = Diary()
d.holiday(5, "beach")
d.meeting(2, "Ana")
d.meeting(5, "Sam")
print(d.entries)
print(d.on_day(5))
print(d.on_day(1))
```

```text
[(5, 'holiday', 'beach'), (2, 'meeting', 'Ana'), (5, 'meeting', 'Sam')]
['holiday: beach', 'meeting: Sam']
[]
```

Notice that the holiday was added first, even though it's later in the week. Writing a schedule first and acting on it afterward means entries can come in any order.

### Learn it: NumPy arrays 🟢

A NumPy array is like a list of numbers, except math works on the whole thing at once, and it's much faster. Empty `scratch.py` again:

```python
import numpy as np

grid = np.linspace(0, 1, 5)
print(grid)
print(len(grid), grid[0], grid[-1])

filled = np.zeros(3)
filled[1] = 7.5
print(filled)

print(grid * 10)

table = np.array([[1, 2, 3], [4, 5, 6]])
print(table.shape)
print(table[:, -1])
print(table[:, -1].tolist())
```

```text
[0.   0.25 0.5  0.75 1.  ]
5 0.0 1.0
[0.  7.5 0. ]
[ 0.   2.5  5.   7.5 10. ]
(2, 3)
[3 6]
[3, 6]
```

- `np.linspace(0, 1, 5)` gives 5 evenly spaced values, **including both ends**. So a 60-minute grid at 6 steps per minute needs `60 * 6 + 1` = 361 points.
- `np.zeros(3)` makes an array to fill in later.
- `table[:, -1]` means "all rows, last column". That exact expression appears next lesson.

### Build it: the start of `Simulation` 🟡

At the top of `engine.py`, add these imports. Imports always go at the top of a file:

```python
import numpy as np
from scipy.integrate import solve_ivp


```

Below `deriv`, above the `if __name__` block, write `class Simulation`:

- `__init__(self, drug, t_end=60.0, steps_per_min=6)` stores all three inputs, and makes an empty list called `self.schedule`.
- `bolus(self, at, dose)` adds the tuple `(at, "bolus", dose)` to the schedule.
- `rate(self, at, dose_per_min)` adds the tuple `(at, "rate", dose_per_min)`.
- `_index(self, minute)` converts a time in minutes to a position on the grid: `round(minute * self.steps_per_min)`. With 6 steps per minute, minute 12 is position 72.

In your `if __name__` block, add a quick look at it:

```python
    sim = Simulation(drug)
    sim.bolus(0, 160)
    sim.rate(12, 8)
    print(sim.schedule)
    print(sim._index(12))
```

```text
[(0, 'bolus', 160), (12, 'rate', 8)]
72
```

The leading underscore on `_index` means it's for use inside the class.

<details>
<summary><b>Hint</b></summary>

`bolus` and `rate` each have one line, and they look just like `meeting` and `holiday` in the `Diary`. The string has to be spelled the same way every time, because next lesson's code compares it.

</details>
<details>
<summary><b>Answer</b></summary>

```python
class Simulation:
    def __init__(self, drug, t_end=60.0, steps_per_min=6):
        self.drug = drug
        self.t_end = t_end
        self.steps_per_min = steps_per_min
        self.schedule = []          # list of (time_min, kind, value)

    def bolus(self, at, dose):
        self.schedule.append((at, "bolus", dose))

    def rate(self, at, dose_per_min):
        self.schedule.append((at, "rate", dose_per_min))

    def _index(self, minute):
        """Convert a time in minutes to a grid index."""
        return round(minute * self.steps_per_min)


```

And in the check block:

```python

    sim = Simulation(drug)
    sim.bolus(0, 160)
    sim.rate(12, 8)
    print(sim.schedule)
    print(sim._index(12))
```

</details>

Delete those last five lines from the check block when you're done. Next lesson's checks replace them. Then commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ModuleNotFoundError: No module named 'numpy'` | Your virtual environment isn't active. Run the activate line from Week 0. |
| `AttributeError: 'Simulation' object has no attribute 'schedule'` | `self.schedule = []` is missing from `__init__`. |
| All your simulations share the same doses | You wrote `schedule = []` at class level or as a default argument. It has to be set inside `__init__`. |
| `TypeError: Simulation.bolus() takes 2 positional arguments but 3 were given` | `self` is missing from the method's definition. |

### Checkpoint

`sim.schedule` shows your events as tuples, in the order you added them, and `sim._index(12)` is 72.

---

## Week 3B — `Simulation`: the time loop

**Goal:** schedule boluses and infusions, run 60 minutes, and get `t`, `cp` and `ce` arrays back.

**New ideas:** numerically solving an equation with `solve_ivp`; reading a library's result object; a loop that applies events, records, then advances; method chaining.

**Read first:** [SciPy `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)

### The science: turning rates into a curve

`deriv()` gives you slopes. To get a curve, you take many small steps along those slopes, which is called *numerical integration*. The simplest method is Euler's: new value = old value + slope × time step. It's what you'll use by hand for the anesthesia machine in Part 2. SciPy's `solve_ivp` uses a more accurate method, but the idea is the same.

The solver doesn't know a bolus is coming. So the simulation stops at each grid point, applies any events, then restarts the solver for the next short stretch. That's why it runs once per grid step rather than once for the whole hour.

### The big picture

```
Simulation.run():
    for each grid point i:
        1. any events due at i?   bolus → add to A1 instantly;  rate → change the pump
        2. record cp[i] and ce[i]
        3. solve_ivp(deriv, t[i] → t[i+1])  → the new state y
```

After `run()`, the results live on the object: `sim.t`, `sim.cp`, `sim.ce`.

### Learn it: `solve_ivp` on a cooling cup of coffee 🟢

Newton's law of cooling says a cup's temperature falls in proportion to how far it is above room temperature. It has the same shape as your `dCe` equation: something chasing a target. Empty `scratch.py` and type this:

```python
from scipy.integrate import solve_ivp


def cooling(t, y, k, room):
    temp = y[0]
    return [k * (room - temp)]


sol = solve_ivp(cooling, (0, 10), [90.0], args=(0.2, 20.0))

print(sol.y.shape)
print(sol.t[0], sol.t[-1])
print(round(sol.y[0, 0], 1), round(sol.y[0, -1], 1))
print(round(sol.y[:, -1].tolist()[0], 1))
```

```text
0.0 10.0
90.0 29.5
29.5
```

The first line also prints a shape such as `(1, 12)`. Yours may differ slightly, and that's fine. Here's how each part works:

- `solve_ivp(function, (start, end), starting_values, args=(...))` is the call. `args` holds any extra inputs your function needs, after `t` and `y`.
- The function must take `t` first, then `y`, whether or not it uses `t`. That's why `deriv` has a `t`.
- The result's `.y` is a 2-D array. Rows are your variables, and columns are the time points the solver chose.
- **`sol.y[:, -1]` is "all rows, last column"**, or the state at the end. `.tolist()` makes it a plain list.

### Learn it: apply, record, advance 🟢

The loop order matters. Here's a bank account that earns interest monthly and gets deposits on certain months. Empty `scratch.py`:

```python
import numpy as np

deposits = [(0, 100), (2, 50)]
months = 4
balance = 0.0
record = np.zeros(months + 1)

for i in range(months + 1):
    for when, amount in deposits:
        if when == i:
            balance += amount

    record[i] = balance

    if i < months:
        balance = balance * 1.10

print(record.round(2))
```

```text
[100.   110.   171.   188.1  206.91]
```

Each month: **apply** anything due, **record** the balance, then **advance** to next month. The `if i < months` stops the very last pass from advancing past the end. Your `run()` has exactly this shape.

### Build it: `run()` and `ce_at()` 🔴

Add two methods to `Simulation`.

**`run(self)`:**

1. `n` = number of grid points = `int(t_end * steps_per_min) + 1`. `t` = `np.linspace(0, t_end, n)`.
2. Start with `y = [0.0, 0.0, 0.0, 0.0]` (an empty patient), `rate = 0.0` (pump off), and `cp` and `ce` as `np.zeros(n)`.
3. For each grid point `i`:
   - **Apply:** for each `(at, kind, value)` in the schedule, if `self._index(at) == i`: a bolus does `y[0] += value`, and a rate event sets `rate = value`.
   - **Record:** `cp[i] = y[0] / V1`, and `ce[i] = y[3]`.
   - **Advance,** unless it's the last point: `sol = solve_ivp(deriv, (t[i], t[i + 1]), y, args=(self.drug, rate))`, then set `y` to the last column of `sol.y`, as a list.
4. Store `self.t`, `self.cp` and `self.ce`, then `return self`.

**`ce_at(self, minute)`** returns Ce at that minute, using `_index`.

<details>
<summary><b>Hint</b></summary>

Use the bank account loop as your model. A bolus adds with `+=`, because a second bolus lands on top of whatever's already there. `y` has to be a list you can change, which is why it needs `.tolist()`.

</details>
<details>
<summary><b>Answer</b></summary>

```python


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
                    if kind == "bolus":
                        y[0] += value
                    else:
                        rate = value

            # 2. record output at this grid point
            cp[i] = y[0] / self.drug.V1
            ce[i] = y[3]

            # 3. advance to the next grid point (unless this is the last one)
            if i < n - 1:
                sol = solve_ivp(deriv, (t[i], t[i + 1]), y, args=(self.drug, rate))
                y = sol.y[:, -1].tolist()

        self.t, self.cp, self.ce = t, cp, ce
        return self

    def ce_at(self, minute):
        return self.ce[self._index(minute)]
```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`__init__`** only stores settings and makes an empty `schedule` list. No calculating happens here.
- **`bolus()` and `rate()`** only *write down* an event as a tuple `(time, kind, value)`. Writing the schedule first and running it later means you can add doses in any order.
- **`_index(minute)`** converts a time in minutes into a position in the arrays. With 6 steps per minute, minute 12 is position 72. The leading underscore means "used inside the class, not meant for outside code".
- **`run()`**, block by block:
  - `n`, `t`: the time grid. `np.linspace(0, 60, 361)` gives 361 evenly spaced times, 10 seconds apart.
  - `y`, `rate`, `cp`, `ce`: the starting state (empty patient, pump off) and two empty arrays to fill.
  - **Step 1** loops over the schedule and applies anything due at this grid point.
  - **Step 2** records what the patient looks like *now*.
  - **Step 3** asks SciPy to move the state forward one step. `sol.y` holds the answer; you want its last column.
  - `return self` lets you write `sim = Simulation(drug).run()` in one line.
- **`ce_at(minute)`** is a convenience: Ce at a time given in minutes.

</details>

### Check it

Replace the last five lines in your check block (the `sim = Simulation(drug)` lines from last lesson) with these. Your Week 2 checks stay, and they run every time, so you'll see straight away if anything older broke.

```python
    # --- Week 3: Simulation, 80 kg Marsh ---
    sim = Simulation(marsh_drug(Patient(40, 80, 170, "M")))
    sim.bolus(0, 160)
    sim.rate(0, 13)
    sim.rate(12, 8)
    sim.bolus(30, 40)
    sim.rate(45, 0)
    sim.run()
    check("number of grid points", len(sim.t), 361, tol=0)
    for minute, expected in [(1, 1.83), (12, 3.82), (30, 2.73), (45, 3.02), (60, 1.28)]:
        check(f"Ce at {minute} min", sim.ce_at(minute), expected, tol=0.05)
```


`return self` lets you write `sim = Simulation(drug).run()` in one line, which is called *method chaining*.

Commit.

### Break it on purpose

1. Change `y[0] += value` to `y[0] = value`. Ce at minute 30 goes wrong, because the second bolus has replaced what was there.
2. Take out the `+ 1` in `n`. `number of grid points` goes to `XX`, at 360.
3. In `rate()`, misspell `"rate"` as `"rat"`. With this `if`/`else` the misspelling doesn't matter, because anything that isn't a bolus counts as a rate. In the opposite version of this code it would silently break. Consider which is safer.

### If something goes wrong

| What you see | Where to look |
|---|---|
| Ce is 0 everywhere | Step 1 never matches. Print `self._index(at), i` inside the loop for a short run (`t_end=2`). Or Step 3 isn't saving the new `y`. |
| `XX  number of grid points` (360 or 362) | The `+ 1` in `n`. A 60-minute grid with both endpoints has 361 points. |
| Ce right at first, wrong after minute 30 | The second bolus is replacing A1 (`=`) instead of adding to it (`+=`). |
| An infusion never stops | The rate event at 45 isn't reaching Step 1. Check that `rate()` stores `"rate"` spelled the same way Step 1 compares it. |
| `IndexError` from `ce_at` | You asked for a minute past `t_end`. |
| Everything is very slow | `steps_per_min` is set high. 6 is plenty for checking. |

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

## Week 4A — Plotting

**Goal:** a reusable function that draws Cp and Ce.

**New ideas:** matplotlib's `fig, ax` style; optional arguments with `None`; `if x is not None`.

**Read first:** [Matplotlib Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

### The science: seeing the hysteresis

This is the first time you'll see Week 2's effect-site lag. After a bolus, Cp spikes immediately while Ce rises slowly, and the two lines cross at Ce's peak. At that moment, Cp and Ce are equal, so dCe/dt is zero. That crossing isn't a coincidence. It's what the equation says has to happen.

### The big picture

```
plotting.py   arrays in ──► picture out          (knows nothing about drugs or patients)
```

Keep this file free of `import patient` and any drug names. In Part 4 you'll swap the picture for a web chart, and the less this file knows, the easier that is.

### Learn it: matplotlib 🟢

Empty `scratch.py` and type this. Plotting has a lot of small commands, and they're easiest to learn with made-up data:

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [3, 5, 4, 6, 8]
costs = [2, 2, 3, 3, 3]

fig, ax = plt.subplots()
ax.plot(days, sales, label="Sales")
ax.plot(days, costs, label="Costs")
ax.set_xlabel("Day")
ax.set_ylabel("Dollars")
ax.set_title("A small shop")
ax.set_xlim(1, 4)
ax.legend()
fig.savefig("shop.png")
plt.show()
print("the window was closed")
```

```text
the window was closed
```

- `fig, ax = plt.subplots()` makes a *figure* (the whole picture) and an *axes* (the graph inside it).
- Each `ax.plot(x, y, label=...)` adds one line. `label` is what `ax.legend()` displays.
- `fig.savefig(...)` writes a file. Open `shop.png` to see it.
- **`plt.show()` opens a window, and your program waits there until you close it.** That's why the print comes last. If a program seems to hang, look for a plot window.

### Learn it: optional inputs 🟢

Sometimes a function's input is optional. `None` is the standard way to say "not given". Empty `scratch.py`:

```python
import numpy as np


def describe(values, extra=None):
    print("values", values)
    if extra is not None:
        print("extra", extra)


describe([1, 2])
describe([1, 2], extra=[3, 4])
describe([1, 2], extra=np.array([3, 4]))
describe([1, 2], extra=0)
```

```text
values [1, 2]
values [1, 2]
extra [3, 4]
values [1, 2]
extra [3 4]
values [1, 2]
extra 0
```

Always write `if extra is not None:`, not `if extra:`. The short form fails in two ways. A zero counts as false, so `extra=0` would be skipped. And a NumPy array in an `if` raises `ValueError: The truth value of an array with more than one element is ambiguous`. Try changing it to see that message, so you'll recognize it later.

### Build it: `plot_concentrations` 🔴

Create `tci/plotting.py`. Write:

```python
def plot_concentrations(t, cp, ce=None, t_end=None, title=None,
                        conc_unit="µg/mL", save_path=None):
```

- It plots `cp` against `t`, labeled `"Cp"`. If `ce` was given, it also plots that, labeled `"Ce"`.
- The x-axis label is `"Time (min)"`, and the y-axis label includes `conc_unit`.
- It adds a legend. It adds a title if one was given, and sets the x-limit from 0 to `t_end` if that was given.
- If `save_path` was given, it saves there. Otherwise, it shows the window.
- It returns `fig, ax`.

Test it by adding these lines to your `engine.py` check block, then look at the picture. Find where Cp and Ce cross:

```python
    from plotting import plot_concentrations
    plot_concentrations(sim.t, sim.cp, sim.ce, title="Week 3 checkpoint run")
```

<details>
<summary><b>Hint</b></summary>

It's all in your shop example. The new parts are each one `if`: `if ce is not None:`, `if title:`, `if t_end:` and `if save_path:`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
import matplotlib.pyplot as plt


def plot_concentrations(t, cp, ce=None, t_end=None, title=None,
                        conc_unit="µg/mL", save_path=None):
    """Knows nothing about drugs or patients. Only arrays in, picture out."""
    fig, ax = plt.subplots()
    ax.plot(t, cp, label="Cp")
    if ce is not None:
        ax.plot(t, ce, label="Ce")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel(f"Concentration ({conc_unit})")
    ax.legend()
    if title:
        ax.set_title(title)
    if t_end:
        ax.set_xlim(0, t_end)
    if save_path:
        fig.savefig(save_path)
    else:
        plt.show()
    return fig, ax
```

</details>


Commit. You can take the plotting lines back out of `engine.py`'s check block if the window gets annoying. A plotting function has no number to check, so looking at the picture is the check.

### Checkpoint

The window shows two lines. Cp starts high and falls, Ce starts at zero and rises, and each time a dose changes, Ce follows Cp with a delay.

---

## Week 4B — The Roberts regimen

**Goal:** a translator that turns `roberts_schedule()` into `Simulation` events.

**New ideas:** writing an *adapter* between two pieces of code whose data have different shapes; running a clock forward through durations.

### The science: the 10-8-6 scheme

Before TCI pumps, the standard way to run a propofol infusion was a manual recipe. Roberts and colleagues (1988) described one that's still taught: **1 mg/kg, then 10 mg/kg/h for 10 minutes, 8 mg/kg/h for 10 minutes, then 6 mg/kg/h.**

The stepped-down rates exist for a pharmacokinetic reason. Early on, the peripheral compartments are empty and drug moves into them quickly, so a higher rate is needed to hold the concentration. As they fill, less is needed. A single fixed rate either undershoots early or overshoots late. In effect, it's a manual approximation of what a TCI pump calculates continuously.

**Reference:** Roberts FL, Dixon J, Lewis GT, Tackley RM, Prys-Roberts C. Induction and maintenance of propofol anaesthesia: a manual infusion scheme. *Anaesthesia* 1988;43 Suppl:14–17

### The big picture

```
dosing.py     roberts_schedule() ──► sim.bolus / sim.rate events    (a translator)
```

Your `roberts_schedule()` gives *durations* ("10 minutes at this rate, then 10 at that"). `Simulation` wants *start times* ("at minute 0, at minute 10").

### Learn it: durations into start times 🟢

Here's a concert schedule, given as set lengths. To print the start time of each act, keep a clock and move it forward. Empty `scratch.py`:

```python
sets = [("Opening band", 30), ("Second band", 45), ("Headliner", 90)]

clock = 19 * 60
for name, minutes in sets:
    print(f"{clock // 60}:{clock % 60:02d} {name}")
    clock += minutes

print("Ends at", clock // 60, ":", clock % 60)
```

```text
19:00 Opening band
19:30 Second band
20:15 Headliner
Ends at 21 : 45
```

The order inside the loop is the whole trick: **use the clock, then advance it.** Swap those two lines to see every act start one slot too late.

### Build it: `apply_roberts` 🔴

First, look at your own function's output. In `scratch.py`:

```python
from roberts import roberts_schedule
print(roberts_schedule(70))
```

It returns a bolus in mg, and a list of `(duration_min, rate_mg_per_min)` tuples. Now create `tci/dosing.py`, and write `apply_roberts(sim, weight, start=0.0)`:

1. Get the bolus and schedule from `roberts_schedule(weight)`.
2. Start a clock at `start`, and give the bolus at that time.
3. For each segment, start that rate at the current clock time, then move the clock forward by that segment's duration.
4. Return `sim`.

<details>
<summary><b>Hint</b></summary>

Unpack in the `for` line: `for duration, rate in schedule:`. It's two lines inside the loop, in the same order as the concert.

</details>
<details>
<summary><b>Answer</b></summary>

```python
from roberts import roberts_schedule


def apply_roberts(sim, weight, start=0.0):
    """roberts_schedule() returns RELATIVE durations: [(10, r1), (10, r2), (40, r3)].
    Simulation wants ABSOLUTE start times. Walk a clock forward."""
    bolus_mg, schedule = roberts_schedule(weight)
    current_time = start
    sim.bolus(current_time, bolus_mg)
    for duration, rate in schedule:
        sim.rate(current_time, rate)
        current_time += duration
    return sim
```

</details>

### Check it

Add this at the bottom of `dosing.py`, then run `python dosing.py` from inside `tci/`. A plot window opens at the end. Close it to finish.

```python
if __name__ == "__main__":
    from patient import Patient
    from pk_models import marsh_drug
    from engine import Simulation
    from plotting import plot_concentrations
    from checks import check

    # --- Week 4: Roberts through 70 kg Marsh ---
    patient = Patient(40, 70, 170, "M")
    sim = Simulation(marsh_drug(patient))
    apply_roberts(sim, patient.weight)
    sim.run()
    for minute, cp, ce in [(1, 3.99, 0.95), (10, 3.22, 3.05), (20, 2.98, 2.98),
                           (40, 2.66, 2.64), (60, 2.75, 2.74)]:
        check(f"Roberts Cp at {minute} min", sim.cp[sim._index(minute)], cp, tol=0.05)
        check(f"Roberts Ce at {minute} min", sim.ce_at(minute), ce, tol=0.05)
    plot_concentrations(sim.t, sim.cp, sim.ce, title="Roberts, 70 kg, Marsh")   # close the window to continue
```


Every line should start with `OK`. Fix the **first** `XX` before anything else. Then commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ValueError: The truth value of an array ... is ambiguous` | You wrote `if ce:`. Use `if ce is not None:`. |
| The plot window is empty | No `ax.plot` ran, or you called `plt.subplots()` twice. |
| The program seems to hang | `plt.show()` waits until you close the window. Close it and the rest runs. |
| Every Roberts rate starts at minute 0 | `current_time` is never advanced. |
| Rates are shifted one segment late | You advanced the clock *before* scheduling the rate. |
| `XX  Roberts Cp at 1 min` but later minutes OK | The bolus: 1 mg/kg, scheduled at `start`. |

### Things to consider

- Does the order "record the rate, then advance the clock" matter? Swap the two lines and see what changes.

### Checkpoint

Roberts (1 mg/kg, then 10 → 8 → 6 mg/kg/h) through 70 kg Marsh:

| t (min) | 1 | 10 | 20 | 40 | 60 |
|---|---|---|---|---|---|
| Cp | 3.99 | 3.22 | 2.98 | 2.66 | 2.75 |
| Ce | 0.95 | 3.05 | 2.98 | 2.64 | 2.74 |

**References:** Roberts FL, Dixon J, Lewis GT, Tackley RM, Prys-Roberts C. Induction and maintenance of propofol anaesthesia: a manual infusion scheme. *Anaesthesia* 1988;43 Suppl:14–17

---

## Week 5A — Translating doses and reading a CSV file

**Goal:** turn an entry like "150 mcg/kg/min" into what the engine understands, and read a table of doses from a file.

**New ideas:** splitting strings; dictionaries as lookup tables; raising your own errors with a clear message; `with open(...)`; the `csv` module.

**Read first:** [Python: string methods](https://docs.python.org/3/library/stdtypes.html#str.split) · [Python `csv` module (`DictReader`)](https://docs.python.org/3/library/csv.html#csv.DictReader) · [Python tutorial: errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

### The science: the thousand-fold error

Fentanyl's model works in mcg and ng/mL, while propofol's works in mg and µg/mL. Mixing these up is one of the most dangerous errors in dosing, because the resulting number can still look plausible. This week's translator exists so that this conversion happens in one place, gets checked once, and can't be done wrongly anywhere else.

### The big picture

People think in "140 mg" and "150 mcg/kg/min". Your engine only understands two things: *a bolus in the drug's dose unit* and *a rate in that unit per minute*.

```
CSV file ──read_dose_table──► rows ──apply_rows──► sim.bolus(...) / sim.rate(...) ──run──► Ce
                                        │
                                        └── to_engine(amount, units, weight, dose_unit) on each row
```

This is the same convention StanpumpR uses. Each row of the dose table is **time, drug, amount, units**:

| units contain… | meaning | example |
|---|---|---|
| no time (`mg`, `mcg`, `mg/kg`, `mcg/kg`) | **bolus**, given instantly at that time | `0, propofol, 140, mg` |
| a time (`/min`, `/h`) | **infusion**, runs from that time until the next infusion row for the same drug | `10, propofol, 120, mcg/kg/min` |
| a time, amount 0 | **infusion off** | `52, propofol, 0, mcg/kg/min` |

Your engine only understands two things: a bolus in the drug's dose unit (mg or mcg), and a rate in that unit **per minute**. So the whole week comes down to one translator function.

### Learn it: splitting text, and lookup tables 🟢

Here's a tiny recipe converter. Empty `scratch.py`:

```python
TO_GRAMS = {"g": 1.0, "kg": 1000.0, "oz": 28.35}
PER_HOUR = {"h": 1.0, "day": 24.0}

text = "kg/person/day"
parts = text.split("/")
print(parts)
print(parts[0], parts[-1])
print("person" in parts, "dog" in parts)
print(TO_GRAMS["oz"] * 2)


def grams(amount, unit):
    if unit not in TO_GRAMS:
        raise ValueError(f"Unknown unit '{unit}'. Use one of {list(TO_GRAMS)}.")
    return amount * TO_GRAMS[unit]


print(grams(3, "kg"))

try:
    grams(3, "pounds")
except ValueError as err:
    print("Problem:", err)
```

```text
['kg', 'person', 'day']
kg day
True False
56.7
3000.0
Problem: Unknown unit 'pounds'. Use one of ['g', 'kg', 'oz'].
```

- `text.split("/")` cuts text into a list at each `/`.
- A dictionary of conversion factors replaces a long chain of `if`/`elif`. Adding a new unit means adding one entry.
- `raise ValueError("...")` stops the program with **your** message. "Unknown unit 'pounds'" is far more useful than a `KeyError` buried three files deep.
- `except ValueError as err:` catches it and gives you the message. In Week 12, that's what your app shows on screen.

### Learn it: reading a CSV file 🟢

A CSV file is a plain-text table. Create `tci/scratch_pets.csv` by typing this into your editor:

```text
name,age,kind
Rex,3,dog
Tom,5,cat
```

Then empty `scratch.py`, and type this:

```python
import csv

rows = []
with open("scratch_pets.csv", newline="") as f:
    for r in csv.DictReader(f):
        print(r)
        rows.append((r["name"], float(r["age"]), r["kind"].strip()))

print(rows)
print(rows[0][1] + 1)
```

```text
{'name': 'Rex', 'age': '3', 'kind': 'dog'}
{'name': 'Tom', 'age': '5', 'kind': 'cat'}
[('Rex', 3.0, 'dog'), ('Tom', 5.0, 'cat')]
4.0
```

- `with open(...) as f:` opens the file, and closes it for you when the block ends.
- `csv.DictReader` reads the first line as column names, then gives you each row as a dictionary.
- **Everything arrives as text.** `r["age"]` is the string `'3'`, so it needs `float()` before you can do math with it.
- `.strip()` removes stray spaces.
- The path is relative to the folder your terminal is in. That's why you always run from inside `tci/`.

Delete `scratch_pets.csv` when you're done.


### Build it: `to_engine` 🟡

Add these two tables and this function to `dosing.py`, above the `if __name__` block:

```python
MASS_TO_MG = {"mg": 1.0, "mcg": 0.001}     # how many mg is one of these?
TIME_TO_MIN = {"min": 1.0, "h": 60.0}       # how many minutes is one of these?


def to_engine(amount, units, weight_kg, dose_unit):
    """Translate one dose-table entry into what Simulation understands.

    amount    : the number typed in, e.g. 150
    units     : e.g. "mcg/kg/min", "mg/kg", "mcg", "mg/kg/h"
    weight_kg : patient weight (only used if units contain "/kg")
    dose_unit : the drug's own dose unit, "mg" or "mcg"

    Returns ("bolus", amount_in_dose_unit) or ("rate", dose_unit_per_minute).
    Example: to_engine(150, "mcg/kg/min", 70, "mg")  ->  ("rate", 10.5)
    """
    # your code here
```

Do it in steps, each on its own line:

1. Split `units`. The first piece is the mass unit. If it isn't in `MASS_TO_MG`, raise a `ValueError` with a helpful message.
2. Convert the amount to mg, then to the drug's `dose_unit`.
3. If `"kg"` is one of the pieces, multiply by the weight.
4. If the **last** piece is a time unit, it's a rate. Convert to per-minute, and return `("rate", value)`.
5. Otherwise, return `("bolus", value)`.

<details>
<summary><b>Hint</b></summary>

Step 2 in one line: `value = amount * MASS_TO_MG[mass] / MASS_TO_MG[dose_unit]`. Multiplying gets you to mg, and dividing gets you to the drug's unit. Step 4 divides by `TIME_TO_MIN[last]`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
MASS_TO_MG = {"mg": 1.0, "mcg": 0.001}     # how many mg is one of these?
TIME_TO_MIN = {"min": 1.0, "h": 60.0}       # how many minutes is one of these?


def to_engine(amount, units, weight_kg, dose_unit):
    """Translate one dose-table entry into what Simulation understands.

    amount    : the number typed in, e.g. 150
    units     : e.g. "mcg/kg/min", "mg/kg", "mcg", "mg/kg/h"
    weight_kg : patient weight (only used if units contain "/kg")
    dose_unit : the drug's own dose unit, "mg" or "mcg"

    Returns ("bolus", amount_in_dose_unit) or ("rate", dose_unit_per_minute).
    Example: to_engine(150, "mcg/kg/min", 70, "mg")  ->  ("rate", 10.5)
    """
    parts = units.split("/")          # "mcg/kg/min" -> ["mcg", "kg", "min"]
    mass = parts[0]
    if mass not in MASS_TO_MG:
        raise ValueError(f"Unknown dose unit '{mass}' in '{units}'. Use mg or mcg.")
    value = amount * MASS_TO_MG[mass] / MASS_TO_MG[dose_unit]
    if "kg" in parts:
        value *= weight_kg
    last = parts[-1]
    if last in TIME_TO_MIN:
        return "rate", value / TIME_TO_MIN[last]
    return "bolus", value


```

</details>

### Check it

Add these lines inside the `if __name__` block in `dosing.py`, below your earlier checks. `to_engine(*args)` unpacks a tuple into separate inputs, the same way `**` does for a dictionary.

```python

    # --- Week 5: unit conversions ---
    conversions = [
        ((2, "mg/kg", 70, "mg"),          ("bolus", 140.0)),
        ((150, "mcg/kg/min", 70, "mg"),   ("rate", 10.5)),
        ((10, "mg/kg/h", 70, "mg"),       ("rate", 11.667)),
        ((100, "mcg", 70, "mcg"),         ("bolus", 100.0)),
        ((0.5, "mcg/kg/h", 70, "mcg"),    ("rate", 0.5833)),
        ((1, "mg", 70, "mcg"),            ("bolus", 1000.0)),
    ]
    for args, (kind, amount) in conversions:
        got_kind, got_amount = to_engine(*args)
        check(f"{args} kind", got_kind, kind)
        check(f"{args} amount", got_amount, amount)
```


Commit.

### Things to consider

- Why convert to the drug's unit? If someone types "0.1 mg" of fentanyl, it must become 100 mcg. That's one line of your function, and it prevents the classic thousand-fold error.
- Your translator accepts any of these units, so the dose table can be written however the person entering it thinks: propofol boluses in mg and drips in mcg/kg/min, fentanyl in mcg, and rocuronium in mg/kg or plain mg.

### Checkpoint

| call | result |
|---|---|
| `(2, "mg/kg", 70, "mg")` | `("bolus", 140.0)` |
| `(150, "mcg/kg/min", 70, "mg")` | `("rate", 10.5)` |
| `(10, "mg/kg/h", 70, "mg")` | `("rate", 11.667)` |
| `(100, "mcg", 70, "mcg")` | `("bolus", 100.0)` |
| `(0.5, "mcg/kg/h", 70, "mcg")` | `("rate", 0.5833)` |
| `(1, "mg", 70, "mcg")` | `("bolus", 1000.0)` |

---

## Week 5B — Manual regimens: the dose table

**Goal:** type in a regimen the way you'd give it in the OR, simulate it, and compare it to Roberts on one plot.

**New ideas:** nothing new in the language. This lesson is about connecting pieces you've already built, which is what most programming turns out to be.

### The science: what your regimen costs

You're about to compare a typical clinical regimen with Roberts. This regimen runs higher throughout. It might feel safer, because a higher concentration gives more margin against awareness. But in Week 10, you'll see what it costs in wake-up time. Being able to put a number on that tradeoff is what the simulator is for.

### The big picture

```
cases/manual_propofol.csv ──read_dose_table──► rows ──apply_rows──► sim ──run──► Ce
```

### Build it: your first dose table 🟢

Make a folder, `tci/cases/`, and create `cases/manual_propofol.csv`:

```text
time,drug,amount,units
0,propofol,140,mg
0,propofol,150,mcg/kg/min
10,propofol,120,mcg/kg/min
52,propofol,0,mcg/kg/min
```

An infusion of `0` is a perfectly good row. It means "stop".

### Build it: `apply_rows` and `read_dose_table` 🔴

Add these to `dosing.py`, above the `if __name__` block:

**`apply_rows(sim, rows, patient)`.** `rows` is a list of `(time_min, drug_name, amount, units)` tuples for one drug. For each row, translate it with `to_engine`, using `patient.weight` and `sim.drug.dose_unit`, then call `sim.bolus` or `sim.rate` depending on the kind. Return `sim`.

**`read_dose_table(path)`.** It reads a CSV with the columns `time,drug,amount,units`, and returns a list of those tuples. `time` and `amount` need converting to `float`, and `.strip()` tidies the text columns.

`sim.drug.dose_unit` is why fentanyl rows will come out in mcg and propofol rows in mg automatically, once you have more drugs.

<details>
<summary><b>Hint</b></summary>

`kind, value = to_engine(amount, units, patient.weight, sim.drug.dose_unit)`, then an `if kind == "bolus":`. For the file, use your pets example, and put `import csv` at the top of `dosing.py`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
import csv

```

```python
def apply_rows(sim, rows, patient):
    """rows: a list of (time_min, drug_name, amount, units) for ONE drug."""
    for time_min, drug_name, amount, units in rows:
        kind, value = to_engine(amount, units, patient.weight, sim.drug.dose_unit)
        if kind == "bolus":
            sim.bolus(time_min, value)
        else:
            sim.rate(time_min, value)
    return sim


def read_dose_table(path):
    """Read a CSV with columns: time,drug,amount,units. Returns a list of tuples."""
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append((float(r["time"]), r["drug"].strip(),
                         float(r["amount"]), r["units"].strip()))
    return rows


```

</details>

### Check it

Add these lines inside the `if __name__` block, below your earlier checks:

```python

    # --- Week 5: your regimen from the CSV, and Roberts stopped at the same time ---
    manual = Simulation(marsh_drug(patient), t_end=90)
    apply_rows(manual, read_dose_table("cases/manual_propofol.csv"), patient)
    manual.run()
    roberts = Simulation(marsh_drug(patient), t_end=90)
    apply_roberts(roberts, patient.weight)
    roberts.rate(52, 0)                          # stop at 52, like the manual regimen
    roberts.run()
    for minute, m_ce, r_ce in [(1, 1.82, 0.95), (10, 3.80, 3.05), (30, 3.02, 2.67),
                               (52, 3.20, 2.70), (60, 2.00, 1.69), (70, 1.20, 1.02)]:
        check(f"manual Ce at {minute} min", manual.ce_at(minute), m_ce, tol=0.05)
        check(f"Roberts Ce at {minute} min", roberts.ce_at(minute), r_ce, tol=0.05)
```


Then overlay the two Ce curves on one plot, using `sim.t` and `sim.ce`. For a fair comparison Roberts stops at minute 52 too, which is why there's an extra `roberts.rate(52, 0)`. Don't change `apply_roberts` itself, because the Week 4 check needs it as it is. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `KeyError: 'mcg'` | A misspelled key in `MASS_TO_MG`, or the CSV has a typo in its units. |
| An amount 1000× too big or too small | `to_engine`'s mg ↔ mcg line: multiply by the mass factor, then *divide* by the drug's unit factor. |
| A rate 60× off | `"h"` should divide by 60 to get per-minute. |
| An infusion is treated as a bolus | The "is the last piece a time unit?" test. |
| `ValueError: could not convert string to float` | The CSV has a blank line, an extra header, or a stray character. Open it in a text editor. |
| The infusion never stops | A `0` amount was skipped somewhere, for example `if amount:` (zero counts as False). |
| `FileNotFoundError` | The path is relative to the folder you ran Python from. Run from `tci/`. |

### Checkpoint

Your example regimen, Marsh, Patient A, `steps_per_min=6`, compared with Roberts (also stopped at 52):

| minute | 1 | 10 | 30 | 52 | 60 | 70 |
|---|---|---|---|---|---|---|
| Ce, manual | 1.82 | 3.80 | 3.02 | 3.20 | 2.00 | 1.20 |
| Ce, Roberts | 0.95 | 3.05 | 2.67 | 2.70 | 1.69 | 1.02 |

Your regimen runs about 0.2–0.9 µg/mL higher than Roberts throughout.

**References:** Roberts FL et al. *Anaesthesia* 1988;43 Suppl:14–17 · Shafer SL. *stanpumpR* (stanpumpr.io; github.com/StevenLShafer/stanpumpR): the dose-table convention used here

---

## Week 6A — One regimen, several models

**Goal:** run the same dose table through Marsh, Schnider and Eleveld, and overlay the predictions. This is the "which model do I believe?" view.

**New ideas:** translating multi-term published formulas safely; a dictionary as a *registry* of functions; looping over a dictionary; a plot function that takes a list of runs.

**Read first:** [Python tutorial: looping techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)

### The science: why the same dose gives such different predictions

The story so far is at the start of Part 1. Here are the details that matter for this week's code.

**Schnider's central volume is fixed at 4.27 L for everyone, while Marsh's is about 16 L at 70 kg.** A bolus divided by a smaller volume gives a far higher predicted concentration. So in plasma-targeting mode, Schnider gives every patient the same small initial dose, whatever they weigh. In effect-site mode, the dose is calculated from ke0, and it's more sensible. Absalom's review works an example with a target of 4 µg/mL at 70 kg: effect-site mode gives about 172 mg with Marsh (ke0 0.26), and about 77 mg with Schnider.

**A practical clinical point.** The two models' effect-site concentrations can't be swapped. Engbers and Boveri's TIVA Trainer article gives Schnider's induction problem in numbers: for a standard patient, a Schnider target of 2.3 µg/mL gets there in 1.5 minutes using only 40 mg, which is not enough for induction. So users of Schnider typically induce at a much higher target, then drop down. They warn against carrying that habit over to Eleveld, whose effect-site predictions differ.

**What the Eleveld model's ke0 depends on.** Eleveld reports two: 0.146 /min for arterial samples, which is what this workbook uses, and 1.24 /min for venous samples. That's an eightfold difference caused by where the blood was drawn. It's another reason a ke0 only has meaning together with its own model.

**A correction worth noticing.** The original workbook used Q2 = 1.75 L/min for the Eleveld reference adult, the number in the abstract you can see in the paper. The journal later printed a corrigendum: the value for the reference individual should be **1.83 L/min**. Both numbers are in the paper, because 1.75 is the parameter Q5, and the reference individual's Q2 also includes a small maturation term. You'll calculate it yourself next lesson. This workbook uses 1.83.

**References:** [Schnider TW et al. *Anesthesiology* 1998;88:1170–82](https://scilit.com/publications/d01854b67fa6fdeb01a22b8de7e9238c) · Schnider TW et al. *Anesthesiology* 1999;90:1502–16 · Eleveld DJ, Colin P, Absalom AR, Struys MMRF. *Br J Anaesth* 2018;120:942–59, corrigendum *Br J Anaesth* 2018;121:519 · [Absalom AR et al. *Br J Anaesth* 2009;103:26–37](https://doi.org/10.1093/bja/aep143) · [Engbers F, Boveri H. From Schnider to Eleveld. TIVA Trainer blog, 2024](https://blog.tivatrainer.com/from-schnider-to-eleveld/) · Al-Rifai Z, Mulvey D. Principles of total intravenous anaesthesia: basic pharmacokinetics and model descriptions. *BJA Education* 2016;16:92–7

### The big picture

This week adds two more propofol models and a **registry**, a dictionary that lists every model for every drug:

```
DRUGS = {"propofol": {"Marsh": marsh_drug, "Schnider": schnider_drug, "Eleveld ...": eleveld_drug_reference}}
           drug name     model name → the function that builds that Drug
```

From now on, any code that needs "a propofol model" asks `DRUGS` instead of naming a function directly. That's what lets Weeks 8 and 12 build menus and run any model without new `if` statements.

### Learn it: functions stored in a dictionary 🟢

A function is a value like any other. You can store one in a dictionary without calling it, then call it later. Empty `scratch.py`:

```python
def add_tax_us(price):
    return price * 1.08


def add_tax_uk(price):
    return price * 1.20


TAX_RULES = {"US": add_tax_us, "UK": add_tax_uk}

print(TAX_RULES)
rule = TAX_RULES["UK"]
print(rule(100))
print(TAX_RULES["US"](100))

for country, rule in TAX_RULES.items():
    print(country, round(rule(50), 2))

print(list(TAX_RULES))
```

```text
120.0
108.0
US 54.0
UK 60.0
['US', 'UK']
```

The first line prints something like `<function add_tax_us at 0x...>`, because that's a function that hasn't been called. **No brackets means "the function itself". Brackets mean "call it".** That's why the dictionary holds `add_tax_us` and not `add_tax_us()`. To add a new country, you add one line, and all the loops keep working.

### Learn it: finding a peak with NumPy 🟢

Empty `scratch.py`:

```python
import numpy as np

hours = np.array([0, 1, 2, 3, 4])
temps = np.array([12.0, 18.0, 21.0, 19.0, 15.0])

where = temps.argmax()
print(where)
print(temps[where], hours[where])
print(temps.max())
```

```text
2
21.0 2
21.0
```

`argmax()` gives the *position* of the largest value, and you can use that position in any array of the same length.

### Build it: two more models 🔴

Add these to `pk_models.py`, above the `if __name__` block.

**`schnider_drug(patient)`:**

```
V1 = 4.27       V3 = 238       Cl3 = 0.836              (fixed)
V2  = 18.9 − 0.391·(age − 53)
Cl2 = 1.29 − 0.024·(age − 53)
Cl1 = 1.89 + 0.0456·(weight − 77) − 0.0681·(lbm − 59) + 0.0264·(height − 177)
ke0 = 0.456 /min
```

Build `Cl1` from **named terms**, such as `weight_term`, `lbm_term` and `height_term`. Long one-liners hide typos. Use your Week 1 `drug_from_clearances`, and name it `"Propofol (Schnider)"`.

**`eleveld_drug_reference(patient=None)`** returns the reference individual only (35 yo, 70 kg, 170 cm, male, no opioids): V1 6.28, V2 25.5, V3 273 L; CL 1.79, Q2 1.83, Q3 1.11 L/min; ke0 0.146 /min. Q2 and Q3 are Eleveld's names for Cl2 and Cl3. It ignores `patient`, but accepts one so that every model can be called the same way. Name it `"Propofol (Eleveld)"`.

Then create the registry:

```python
# Every model for every drug, in one place. Week 7 adds more drugs; Week 12's
# drop-down menus are built straight from this dict.
DRUGS = {
    "propofol": {
        "Marsh": marsh_drug,
        "Schnider": schnider_drug,
        "Eleveld (reference adult only)": eleveld_drug_reference,
    },
}
```

Print the three `Cl1` terms once for the Schnider reference patient (53 yo, 77 kg, 177 cm, M). All except the LBM term should be about zero, and the LBM term should be small too.

<details>
<summary><b>Hint</b></summary>

`age, wt, ht, lbm = patient.age, patient.weight, patient.height, patient.lbm` at the top saves a lot of typing. Check the sign on the LBM term: it's subtracted.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def schnider_drug(patient):
    """Schnider TW et al. Anesthesiology 1998;88:1170-82 / 1999;90:1502-16."""
    age, wt, ht, lbm = patient.age, patient.weight, patient.height, patient.lbm
    V1, V3, Cl3 = 4.27, 238.0, 0.836                # fixed
    V2 = 18.9 - 0.391 * (age - 53)
    Cl2 = 1.29 - 0.024 * (age - 53)
    # Build Cl1 from NAMED terms. Long one-liners hide typos.
    weight_term = 0.0456 * (wt - 77)
    lbm_term = 0.0681 * (lbm - 59)
    height_term = 0.0264 * (ht - 177)
    Cl1 = 1.89 + weight_term - lbm_term + height_term
    return drug_from_clearances("Propofol (Schnider)", V1, V2, V3, Cl1, Cl2, Cl3, ke0=0.456)


def eleveld_drug_reference(patient=None):
    """Eleveld DJ et al. Br J Anaesth 2018;120:942-959 (corrigendum 121:519),
    reference individual ONLY: 35 yo, 70 kg, 170 cm, male, no opioids."""
    return drug_from_clearances("Propofol (Eleveld)", 6.28, 25.5, 273.0,
                                1.79, 1.83, 1.11, ke0=0.146)


# Every model for every drug, in one place. Week 7 adds more drugs; Week 12's
# drop-down menus are built straight from this dict.
DRUGS = {
    "propofol": {
        "Marsh": marsh_drug,
        "Schnider": schnider_drug,
        "Eleveld (reference adult only)": eleveld_drug_reference,
    },
}


```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`schnider_drug`** is the first model with real covariates. Each term of Cl1 gets its own named variable (`weight_term`, `lbm_term`, `height_term`), so you can print them one at a time when something's off. At the reference body each term should be near zero.
- **`eleveld_drug_reference(patient=None)`** ignores the patient on purpose; it's only valid for one reference adult. It still *accepts* a patient so it can be called the same way as every other model.
- **`DRUGS`** stores the functions themselves, without parentheses. `DRUGS["propofol"]["Schnider"]` *is* `schnider_drug`; adding `(patient)` calls it.
- **`plot_runs`** takes a list of `(label, t, values)` and draws them all on one set of axes. It's the general version of `plot_concentrations`.

</details>

### Check it: the models

Add these lines inside the check block in `pk_models.py`:

```python

    # --- Week 6: Schnider ---
    check("Schnider k10, reference body", schnider_drug(Patient(53, 77, 177, "M")).k10, 0.419, tol=0.001)
    check("Schnider k10, Patient A", schnider_drug(p70).k10, 0.384, tol=0.001)
```


### Build it: `plot_runs` 🔴

Add `plot_runs(runs, ylabel="Ce", t_end=None, title=None, save_path=None)` to `plotting.py`. `runs` is a list of `(label, t, values)` tuples, and it draws one line per run on the same axes. The labels, legend, title, limits, and saving or showing all work the same way as `plot_concentrations`.

<details>
<summary><b>Answer</b></summary>

```python


def plot_runs(runs, ylabel="Ce", t_end=None, title=None, save_path=None):
    """runs: a list of (label, t, values). One line per run, all on the same axes."""
    fig, ax = plt.subplots()
    for label, t, values in runs:
        ax.plot(t, values, label=label)
    ax.set_xlabel("Time (min)")
    ax.set_ylabel(ylabel)
    ax.legend()
    if title:
        ax.set_title(title)
    if t_end:
        ax.set_xlim(0, t_end)
    if save_path:
        fig.savefig(save_path)
    else:
        plt.show()
    return fig, ax
```

</details>

### Build it: `compare_models.py` 🔴

Create `tci/compare_models.py`:

1. Write a helper `peak_and_time(t, ce)` that returns the peak value and the time it happens.
2. In an `if __name__ == "__main__":` block, make the Eleveld reference adult (35 yo, 70 kg, 170 cm, M), and read `cases/manual_propofol.csv`.
3. Loop over `DRUGS["propofol"].items()`. For each model, build the drug, make a `Simulation` with `t_end=90` and `steps_per_min=60`, apply the rows, run it, and append `(name, sim.t, sim.ce)` to a list called `runs`.
4. Print each model's peak, and overlay the curves with `plot_runs`.
5. Then add this check at the end of the block:

```python
    # --- Week 6: the comparison (put this after the loop that builds `runs`) ---
    from checks import check
    expected = {"Marsh": (4.08, 5.8),
                "Schnider": (8.62, 1.7),
                "Eleveld (reference adult only)": (3.63, 4.6)}
    for name, t, ce in runs:
        peak, when = peak_and_time(t, ce)
        check(f"{name} peak Ce", peak, expected[name][0], tol=0.05)
        check(f"{name} time to peak (min)", when, expected[name][1], tol=0.1)
```

<details>
<summary><b>Answer</b>: everything above the check</summary>

```python
from dosing import apply_rows, read_dose_table
from engine import Simulation
from patient import Patient
from pk_models import DRUGS
from plotting import plot_runs


def peak_and_time(t, ce):
    i = ce.argmax()
    return ce[i], t[i]


if __name__ == "__main__":
    patient = Patient(35, 70, 170, "M")
    rows = read_dose_table("cases/manual_propofol.csv")
    runs = []
    for name, model_fn in DRUGS["propofol"].items():
        sim = Simulation(model_fn(patient), t_end=90, steps_per_min=60)
        apply_rows(sim, rows, patient)
        sim.run()
        runs.append((name, sim.t, sim.ce))
        print(name, peak_and_time(sim.t, sim.ce))
    plot_runs(runs, title="Same doses, three models")
```

</details>


With 60 steps per minute this takes a little while to run. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  Schnider k10, reference body` (about 0.44 instead of 0.419) | The LBM term should be *subtracted*, and it uses `patient.lbm`, not weight. |
| `KeyError: 'Schnider'` | The key in `DRUGS` is spelled differently from the one you look up. Copy-paste one into the other. |
| `TypeError: eleveld_drug_reference() takes 0 positional arguments` | Add the `patient=None` parameter. |
| Three separate plot windows instead of one | `plt.subplots()` is being called inside your loop. Collect the runs first, then call `plot_runs` once. |
| Peak times off by about 0.1 min | Use `steps_per_min=60` for the comparison. |

### Things to consider

- Did `engine.py` need any changes for the new models? It shouldn't. If you had to edit it, something Marsh-specific leaked in.
- Why does `eleveld_drug_reference` accept a `patient` it ignores? So it fits the registry: every model function is called the same way, `model_fn(patient)`.
- The James LBM formula (which Schnider uses) behaves badly in obesity: past a certain BMI, LBM goes *down* as weight goes up. Try `Patient(40, 150, 165, "F").lbm`. This is a well-known Schnider limitation, and one reason Eleveld exists.
- Use `steps_per_min=60` for comparisons, so the peak time isn't rounded to the nearest 10 seconds.

### Checkpoint

- Schnider k10, reference body (53 yo, 77 kg, 177 cm, M): **0.419 /min**. Patient A: **0.384 /min**.
- Your manual regimen, Eleveld reference adult, `steps_per_min=60`:

| model | peak Ce | time to peak | Ce at 30 min | Ce at 52 min |
|---|---|---|---|---|
| Marsh | 4.08 | 5.8 min | 3.02 | 3.20 |
| Schnider | 8.62 | 1.7 min | 3.37 | 3.51 |
| Eleveld | 3.63 | 4.6 min | 2.96 | 3.05 |

The lesson: during the maintenance phase the three models agree within about 0.5 µg/mL, but right after the bolus Schnider predicts more than **twice** the peak. Its fixed 4.27 L central volume is much smaller than Marsh's ~16 L. This is why TCI pumps never let you switch models mid-case.

**References:** Schnider TW et al. *Anesthesiology* 1998;88:1170–82 and 1999;90:1502–16 · Eleveld DJ, Colin P, Absalom AR, Struys MMRF. *Br J Anaesth* 2018;120:942–59 · Marsh B et al. *Br J Anaesth* 1991;67:41–8

---

## Week 6B — The full Eleveld model

**Goal:** implement the Eleveld PK model for any patient from the paper's own equations, and see for yourself how it handles age, sex and obesity.

**New ideas:** reading equations out of a published paper; helper functions inside a larger calculation; dividing by a reference value so the reference patient comes out exactly right.

### The science: one model for everyone

**The paper, in brief.** Eleveld and colleagues pooled 30 previously published studies, giving 15,433 concentrations and 28,639 BIS observations from 1,033 people, aged from 27 weeks post-menstrual to 88 years and weighing 0.68 to 160 kg. They wanted one model that works across all of them, without separate models for children, the obese and the elderly. Its covariates are age, post-menstrual age, weight, height, sex and whether opioids are present.

**Why this answers the Marsh and Schnider problems:**

- **V1 doesn't keep growing with weight.** It follows an Emax curve, with half its maximum at 33.6 kg. This fits Absalom's point that V1 isn't significantly larger in obesity.
- **There's no James equation.** V3 scales with fat-free mass from Al-Sallami's model, which doesn't show the James paradox.
- **Age and opioids matter.** V2, V3 and clearance all shrink with age, and opioids make V3 and clearance fall faster with age.

**What it means for a clinician,** from Engbers and Boveri:

- Eleveld maintenance targets run about 5% above Schnider's in an average-sized patient, so 2.3 µg/mL on Schnider corresponds to about 2.4 on Eleveld.
- Don't use Schnider's higher induction targets, because Eleveld's effect-site predictions differ.
- Eleveld's Ce50, about 3 µg/mL for a 40-year-old, is the concentration for BIS 47, midway between awake BIS (93) and 0. It isn't the concentration for 50% loss of consciousness. They place loss of consciousness at BIS 60–65, or about 2.3 µg/mL in their example.
- A 140 kg patient isn't two 70 kg patients. Dose per kilogram falls as weight rises.

**The other side of the dose: hemodynamics.** Su and colleagues (2022) studied 36 healthy volunteers given stepped propofol by TCI, modeling mean arterial pressure, heart rate and pulse pressure. In their mechanistic model, propofol lowers both total peripheral resistance and stroke volume, with C50 values of 2.96 µg/mL for resistance and 0.34 µg/mL for stroke volume. So in healthy volunteers, the effect on stroke volume begins at a much lower concentration than the effect on resistance. This workbook doesn't simulate hemodynamics under propofol, but the stretch at the end of this lesson points to how you could.

> **A caution from the authors.** The corrigendum to the Eleveld paper warns that printed equations are easy to misread, and recommends the paper's supplementary NONMEM files as the source for any real implementation. Your version is for learning. It uses the arterial form of the model only.

**References:** [Eleveld DJ et al. *Br J Anaesth* 2018;120:942–59](https://doi.org/10.1016/j.bja.2018.01.018), corrigendum *Br J Anaesth* 2018;121:519 · [Engbers F, Boveri H. From Schnider to Eleveld. TIVA Trainer blog, 2024](https://blog.tivatrainer.com/from-schnider-to-eleveld/) · Su H, Eleveld DJ, Struys MMRF, Colin PJ. Mechanism-based pharmacodynamic model for propofol haemodynamic effects in healthy volunteers. *Br J Anaesth* 2022;128:806–16 · Al-Sallami HS et al. *Clin Pharmacokinet* 2015;54:1169–78

### The big picture

`eleveld_drug(patient)` is one more function with the same shape as all the others, so it goes in the registry and every later lesson can use it with no other changes.

### Learn it: a sigmoid, and scaling to a reference 🟢

Eleveld's equations use two building blocks over and over. The first is a *sigmoid*, a curve that rises from 0 toward 1, reaching one half at a value called E50. The second is dividing by the same calculation at a reference value, so that the reference person gets exactly the published number. Here they are in a toy example. Empty `scratch.py`:

```python
def sigmoid(x, e50, slope):
    return x ** slope / (x ** slope + e50 ** slope)


for x in [10, 50, 100, 200, 1000]:
    print(x, round(sigmoid(x, 50, 1), 3))


def plant_height(age_weeks):
    """Published: 80 cm at the reference age of 20 weeks."""
    return 80 * sigmoid(age_weeks, 8, 2) / sigmoid(20, 8, 2)


print(round(plant_height(20), 1))
print(round(plant_height(8), 1), round(plant_height(100), 1))
```

```text
10 0.167
50 0.5
100 0.667
200 0.8
1000 0.952
80.0
46.4 92.2
```

At x = E50, the sigmoid is exactly 0.5, as promised. And `plant_height(20)` is exactly the published 80 at the reference age, while other ages scale from there.

### Build it: `eleveld_drug` 🔴

These are the equations from the paper, for arterial sampling. The reference individual is 35 yr, 70 kg, 170 cm, male. **PMA** is post-menstrual age in weeks, which for this workbook is `age * 52 + 40`. **AGE in weeks** is `age * 52`.

```
sigmoid(x, E50, λ) = x^λ / (x^λ + E50^λ)        ageing(x) = exp(x · (AGE − 35))
central(w)   = sigmoid(w, 33.6, 1)
CLmat(pma)   = sigmoid(pma, 42.3, 9.06)
Q3mat(weeks) = sigmoid(weeks + 40, 68.3, 1)
opiates(x)   = 1 if no opioids, otherwise exp(x · AGE)

V1 = 6.28 · central(WGT) / central(70)
V2 = 25.5 · (WGT / 70) · ageing(−0.0156)
V3 = 273 · (FFM / FFMref) · opiates(−0.0138)
CL = (1.79 male, 2.10 female) · (WGT / 70)^0.75 · CLmat(PMA) / CLmat(PMAref) · opiates(−0.00286)
Q2 = 1.75 · (V2 / 25.5)^0.75 · (1 + 1.30 · (1 − Q3mat(AGEweeks)))
Q3 = 1.11 · (V3 / 273)^0.75 · Q3mat(AGEweeks) / Q3mat(AGEweeks at 35 yr)
ke0 = 0.146 · (WGT / 70)^−0.25
Ce50 = 3.08 · ageing(−0.00635)
```

In `pk_models.py`, above the `DRUGS` dictionary:

1. Add `FFM_REFERENCE = 54.48`, the FFM in kg of the reference man.
2. Write a small `sigmoid(x, e50, slope)` function.
3. Write `eleveld_drug(patient, opioids=False)`, returning a `Drug` named `"Propofol (Eleveld full)"` through `drug_from_clearances`.
4. Write `eleveld_ce50(age)`.
5. Add `"Eleveld (full)": eleveld_drug` to the registry.

<details>
<summary><b>Hint</b></summary>

Work line by line, with one named variable for each equation, in the order shown. Q2 uses your V2 and Q3 uses your V3, so those come first. `math.exp` needs `import math` at the top of the file. Run the check after each one if you can, because the reference individual should give the published value for every line.

</details>
<details>
<summary><b>Answer</b></summary>

```python
import math


```

```python
FFM_REFERENCE = 54.48   # kg: 35 yo, 70 kg, 170 cm man (Al-Sallami)


def sigmoid(x, e50, slope):
    return x ** slope / (x ** slope + e50 ** slope)


def eleveld_drug(patient, opioids=False):
    """Eleveld DJ et al. Br J Anaesth 2018;120:942-959, arterial PK model.
    A teaching implementation from the printed equations."""
    age, wgt = patient.age, patient.weight
    pma = age * 52 + 40
    age_weeks = age * 52

    def central(w):
        return sigmoid(w, 33.6, 1)

    def cl_maturation(p):
        return sigmoid(p, 42.3, 9.06)

    def q3_maturation(weeks):
        return sigmoid(weeks + 40, 68.3, 1)

    def opiates(x):
        return math.exp(x * age) if opioids else 1.0

    def ageing(x):
        return math.exp(x * (age - 35))

    V1 = 6.28 * central(wgt) / central(70)
    V2 = 25.5 * (wgt / 70) * ageing(-0.0156)
    V3 = 273 * (patient.ffm / FFM_REFERENCE) * opiates(-0.0138)

    cl_base = 1.79 if patient.sex == "M" else 2.10
    CL = (cl_base * (wgt / 70) ** 0.75
          * cl_maturation(pma) / cl_maturation(35 * 52 + 40) * opiates(-0.00286))
    Q2 = 1.75 * (V2 / 25.5) ** 0.75 * (1 + 1.30 * (1 - q3_maturation(age_weeks)))
    Q3 = 1.11 * (V3 / 273) ** 0.75 * q3_maturation(age_weeks) / q3_maturation(35 * 52)
    ke0 = 0.146 * (wgt / 70) ** -0.25
    return drug_from_clearances("Propofol (Eleveld full)", V1, V2, V3, CL, Q2, Q3, ke0=ke0)


def eleveld_ce50(age):
    """Ce for BIS 47 (midway between awake BIS 93 and 0). NOT the Ce for 50% LOC."""
    return 3.08 * math.exp(-0.00635 * (age - 35))


```

```python

        "Eleveld (full)": eleveld_drug,
```

</details>

### Check it

The reference individual must give back the published numbers. This is where you see the corrigendum for yourself: the calculated Q2 is 1.83, even though the input parameter is 1.75. Add these lines inside the check block in `pk_models.py`:

```python

    # --- Week 6B: full Eleveld must reproduce the reference individual ---
    ref = eleveld_drug(Patient(35, 70, 170, "M"))
    check("Eleveld V1", ref.V1, 6.28, tol=0.005)
    check("Eleveld V2", ref.k12 * ref.V1 / ref.k21, 25.5, tol=0.01)
    check("Eleveld V3", ref.k13 * ref.V1 / ref.k31, 273, tol=0.5)
    check("Eleveld CL", ref.k10 * ref.V1, 1.79, tol=0.005)
    check("Eleveld Q2 (the corrigendum value)", ref.k12 * ref.V1, 1.83, tol=0.005)
    check("Eleveld Q3", ref.k13 * ref.V1, 1.11, tol=0.005)
    check("Eleveld ke0", ref.ke0, 0.146, tol=0.0005)
    check("Eleveld Ce50, age 40", eleveld_ce50(40), 2.98, tol=0.01)

    # V1 flattens with weight: 140 kg is not two 70 kg patients
    check("Eleveld V1, 140 kg", eleveld_drug(Patient(35, 140, 170, "M")).V1, 7.50, tol=0.02)
    check("Marsh V1, 140 kg", marsh_drug(Patient(35, 140, 170, "M")).V1, 31.92, tol=0.02)
```


Because you added a model to the registry, `compare_models.py` now needs its numbers too. Add this line inside its `expected` dictionary. At the reference adult, the two Eleveld versions should give the same answer:

```python
,
                "Eleveld (full)": (3.63, 4.6)
```


### Explore it: three patients, three models 🔴

In `scratch.py`, print V1, and the clearance `k10 * V1`, from Marsh, Schnider and full Eleveld for each of these patients:

- A 35-year-old, 70 kg, 170 cm man
- An 80-year-old, 70 kg, 170 cm man
- A 35-year-old, 170 kg, 170 cm man

You should see Marsh's V1 ignore age completely and more than double with weight, Schnider's V1 never change, and Eleveld's V1 move only modestly. Now look at Schnider's clearance for the 170 kg man (BMI 59). It's well past the James peak, so its clearance comes out far too high.

```text
35 yo, 70 kg  Marsh: V1 15.96 L, CL 1.90 L/min
35 yo, 70 kg  Schnider: V1 4.27 L, CL 1.64 L/min
35 yo, 70 kg  Eleveld: V1 6.28 L, CL 1.79 L/min
80 yo, 70 kg  Marsh: V1 15.96 L, CL 1.90 L/min
80 yo, 70 kg  Schnider: V1 4.27 L, CL 1.64 L/min
80 yo, 70 kg  Eleveld: V1 6.28 L, CL 1.79 L/min
35 yo, 170 kg  Marsh: V1 38.76 L, CL 4.61 L/min
35 yo, 170 kg  Schnider: V1 4.27 L, CL 5.95 L/min
35 yo, 170 kg  Eleveld: V1 7.76 L, CL 3.48 L/min
```

Notice that without opioids, Eleveld's clearance doesn't change with age here. Pass `opioids=True` for the 80-year-old to see it fall.

<details>
<summary><b>Answer</b></summary>

```python
from patient import Patient
from pk_models import marsh_drug, schnider_drug, eleveld_drug

patients = [("35 yo, 70 kg", Patient(35, 70, 170, "M")),
            ("80 yo, 70 kg", Patient(80, 70, 170, "M")),
            ("35 yo, 170 kg", Patient(35, 170, 170, "M"))]
for label, p in patients:
    for name, model in [("Marsh", marsh_drug), ("Schnider", schnider_drug), ("Eleveld", eleveld_drug)]:
        d = model(p)
        print(f"{label}  {name}: V1 {d.V1:.2f} L, CL {d.k10 * d.V1:.2f} L/min")
```

</details>

Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  Eleveld Q2` showing 1.75 | The `(1 + 1.30 · (1 − Q3mat))` term is missing or uses the wrong age. |
| `XX  Eleveld V3` off by a small amount | Your `Patient.ffm` must give 54.48 for the reference man. Check it on its own first. |
| `XX  Eleveld CL` | The maturation ratio should be almost exactly 1 for any adult. Check the `PMA` calculation. |
| `XX  Eleveld V1, 140 kg` | `central()` is `w / (w + 33.6)`, divided by its value at 70 kg. |
| `compare_models.py` raises `KeyError: 'Eleveld (full)'` | Add that line to its `expected` dictionary. |

### Things to consider

- The paper reports its results with inter-individual variability on nearly every parameter: the coefficient of variation is large. Your function gives the *typical* patient only. A real patient can differ a lot, which is why you titrate to effect.
- Stretch: the mechanistic hemodynamic model in Su 2022 uses turnover equations with the same shape as your `dCe` equation. If you get through the course and want a project, the paper gives everything you'd need to add a blood-pressure panel.

### Checkpoint

The full Eleveld function reproduces the published reference values, including Q2 = **1.83**. V1 at 140 kg is **7.50 L**, against **31.92 L** for Marsh.

---

## Week 7A — The drug library: sizing patients and storing data

**Goal:** a table of reference parameters, and one function that scales any row of it to any patient.

**New ideas:** storing *data* in a dictionary instead of writing near-identical functions; `dict(...)`; adding optional attributes with defaults so old code keeps working; `lambda`.

**Read first:** [Python tutorial: default argument values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) · [Lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

### The science: allometric scaling

Bigger animals have larger volumes, but their metabolism doesn't rise in proportion. Across species, metabolic rate rises roughly with body mass to the power 0.75, called *allometric* scaling. That's why many modern PK models, including the ones in this lesson and Eleveld's own CL equation, scale volumes with size to the power 1 and clearances to the power 0.75.

Most of these models were published for a typical 70 kg adult. StanpumpR scales them by **fat-free mass**, which your `Patient` class already calculates (`patient.ffm`, Al-Sallami):

- volume factor = patient FFM ÷ 54.48 kg (the FFM of a 35 yo, 70 kg, 170 cm man)
- clearance factor = volume factor ^ 0.75

So a 70 kg, 170 cm man gets exactly the published numbers, and everyone else scales from there.

| drug | V1 | V2 | V3 | Cl1 | Cl2 | Cl3 | ke0 | doses in → conc. in | typical / MEAC |
|---|---|---|---|---|---|---|---|---|---|
| fentanyl | 12.1 | 35.7 | 224 | 0.632 | 2.8 | 1.55 | 0.221 | mcg → ng/mL | MEAC 0.6 ng/mL |
| dexmedetomidine | 8.057 | 12.75 | 177.69 | 0.4448 | 2.0788 | 1.9902 | 0.033 | mcg → ng/mL | 0.4–0.8 ng/mL |
| ketamine | 4.081 | 39.66 | 171.92 | 0.9223 | 2.6812 | 0.8407 | 0.088 | mg → µg/mL | 0.10–0.16 µg/mL |
| rocuronium | 3.920 | 16.06 | 0 | 0.6844 | 0.3935 | 0 | 0.186 | mg → µg/mL | 1.0–2.2 µg/mL |

Volumes in L, clearances in L/min, ke0 in /min. Rocuronium is a **two**-compartment model (no V3).

Two drugs are built differently:
- **Remifentanil:** Minto 1997, with its own age and LBM covariates (below). MEAC 1.0 ng/mL.
- **Methadone:** Inturrisi 1987. V1 = 0.18 L/kg × total weight; k10 0.00806, k12 0.408, k13 0.112, k21 0.06, k31 0.00114 /min (fixed); ke0 0.045 /min. Doses in mg, concentrations in µg/mL. MEAC 0.06 µg/mL (60 ng/mL).

> **Where these numbers come from.** These are the parameter sets StanpumpR uses, read from its source code (October 2026), with two simplifications so you can actually build them. StanpumpR's current methadone is a two-enantiomer model (Henthorn & Kharasch 2026) that's far beyond this workbook; Inturrisi 1987 is the classic model it replaced. StanpumpR also uses Eleveld 2017 for remifentanil; Minto is the long-standing standard. StanpumpR derives each ke0 from a published **time to peak effect** (Minto 2003). The ke0 column above is the result of that calculation, and your checkpoint is to confirm each drug peaks at the right time.

### The big picture

Six new drugs, but almost no new code. Most of them are *data*: one row each in `REFERENCE_PK`. One function, `scaled_drug`, turns any row plus a patient into a `Drug`:

```
REFERENCE_PK["fentanyl"] (70 kg reference numbers) ─┐
patient.ffm → size_factors() → (volume factor, clearance factor) ─┴─► scaled_drug() ─► Drug
```

Remifentanil (Minto) and methadone (Inturrisi) have their own published formulas, so they get their own small functions. Everything is then registered in `DRUGS`, and every later week can use all seven drugs.

### Learn it: data instead of code 🟢

Here's the same idea with phone plans. Rather than writing one function per plan, store each plan as a row, and write one function that reads any row. Empty `scratch.py`:

```python
PLANS = {
    "basic": dict(monthly=20, per_gb=5.0),
    "family": dict(monthly=60, per_gb=2.0, lines=(2, 5)),
}

print(PLANS["basic"]["monthly"])
print(PLANS["family"].get("lines"))
print(PLANS["basic"].get("lines"))


def bill(plan_name, gb):
    p = PLANS[plan_name]
    return p["monthly"] + p["per_gb"] * gb


print(bill("basic", 2), bill("family", 10))

CHOICES = {"cheap": lambda gb: bill("basic", gb), "big": lambda gb: bill("family", gb)}
print(CHOICES["cheap"](1))
first_key = next(iter(CHOICES))
print(first_key)
```

```text
20
(2, 5)
None
30.0 80.0
25.0
cheap
```

- `dict(monthly=20, per_gb=5.0)` is another way to write `{"monthly": 20, "per_gb": 5.0}`.
- `.get("lines")` gives `None` instead of a `KeyError` when a key is missing, which suits things only some rows have.
- `lambda gb: ...` is a small unnamed function, written inline.
- `next(iter(d))` gives a dictionary's first key. Dictionaries remember the order items were added.

### Learn it: adding an input without breaking old code 🟢

When you add an input with a default, every existing call keeps working. And `x if condition else y` picks one of two values in a single line. Empty `scratch.py`:

```python
def label(name, size="M", note=None):
    return f"{name} ({size}) {note}"


print(label("shirt"))
print(label("shirt", note="on sale"))

stock, sold = 0, 4
per_unit = sold / stock if stock else 0
print(per_unit)
```

```text
shirt (M) None
shirt (M) on sale
0
```

The last part avoids dividing by zero: when `stock` is 0, it counts as false, so the `else` value is used.

### Build it: update `Drug` and `drug_from_clearances` 🟡

Two small changes to Week 1 code:

- `Drug.__init__` gets two new keyword inputs with defaults, `meac=None` and `band=None`, stored on the object.
- `drug_from_clearances` must cope with **V3 = 0**, for rocuronium. Right now, `Cl3 / V3` would crash. If V3 is 0, `k31` should be 0.

Then rerun `python pk_models.py`, `python engine.py` and `python dosing.py`. Every earlier line should still say `OK`.

<details>
<summary><b>Answer</b></summary>

In `__init__`, the signature's last line and two new lines at the end:

```python
    def __init__(self, name, V1, k10, k12, k13, k21, k31, ke0,
                 dose_unit="mg", conc_unit="µg/mL", meac=None, band=None):
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
        self.meac = meac
        self.band = band

```

And in `drug_from_clearances`, the `k31` line:

```python
def drug_from_clearances(name, V1, V2, V3, Cl1, Cl2, Cl3, ke0, **units):
    """Many papers publish volumes + clearances, not rate constants.
    Convert once, here, so no other code ever has to."""
    k10 = Cl1 / V1
    k12 = Cl2 / V1
    k13 = Cl3 / V1
    k21 = Cl2 / V2
    k31 = Cl3 / V3 if V3 else 0.0     # rocuronium is 2-compartment: V3 = 0
    return Drug(name, V1, k10, k12, k13, k21, k31, ke0, **units)

```

</details>


### Build it: `size_factors`, `REFERENCE_PK` and `scaled_drug` 🔴

Add these to `pk_models.py`, above the `DRUGS` dictionary. `FFM_REFERENCE` is already there from Week 6B.

- **`size_factors(patient)`** returns `(volume_factor, clearance_factor)`, as defined above.
- **`REFERENCE_PK`** is a dictionary of the four drugs in the table. Fentanyl, for example, is `dict(V1=12.1, V2=35.7, V3=224, Cl1=0.632, Cl2=2.8, Cl3=1.55, ke0=0.221, dose_unit="mcg", conc_unit="ng/mL", meac=0.6)`. Use `band=(0.4, 0.8)` for dexmedetomidine, `band=(0.10, 0.16)` for ketamine, and `band=(1.0, 2.2)` for rocuronium.
- **`scaled_drug(name, patient)`** multiplies the three volumes by the volume factor and the three clearances by the clearance factor, and builds the drug with `drug_from_clearances`. Pass along `ke0`, the units, `meac` and `band`. Use `p.get("meac")`, because not every row has one.

<details>
<summary><b>Hint</b></summary>

`drug_from_clearances` passes `**units` straight to `Drug`, so `meac=...` and `band=...` go through it with no further changes. `name.capitalize()` makes a tidy display name.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def size_factors(patient):
    """Return (volume_factor, clearance_factor) relative to the 70 kg reference man."""
    fv = patient.ffm / FFM_REFERENCE
    return fv, fv ** 0.75


# Data, not code: adding a drug means adding a row here.
REFERENCE_PK = {
    "fentanyl": dict(V1=12.1, V2=35.7, V3=224, Cl1=0.632, Cl2=2.8, Cl3=1.55, ke0=0.221,
                     dose_unit="mcg", conc_unit="ng/mL", meac=0.6),
    "dexmedetomidine": dict(V1=8.057, V2=12.75, V3=177.69, Cl1=0.4448, Cl2=2.0788, Cl3=1.9902,
                            ke0=0.033, dose_unit="mcg", conc_unit="ng/mL", band=(0.4, 0.8)),
    "ketamine": dict(V1=4.081, V2=39.66, V3=171.92, Cl1=0.9223, Cl2=2.6812, Cl3=0.8407,
                     ke0=0.088, dose_unit="mg", conc_unit="µg/mL", band=(0.10, 0.16)),
    "rocuronium": dict(V1=3.920, V2=16.06, V3=0, Cl1=0.6844, Cl2=0.3935, Cl3=0,
                       ke0=0.186, dose_unit="mg", conc_unit="µg/mL", band=(1.0, 2.2)),
}


def scaled_drug(name, patient):
    """Build a Drug for any drug in REFERENCE_PK, scaled to this patient."""
    p = REFERENCE_PK[name]
    fv, fc = size_factors(patient)
    return drug_from_clearances(
        name.capitalize(),
        p["V1"] * fv, p["V2"] * fv, p["V3"] * fv,
        p["Cl1"] * fc, p["Cl2"] * fc, p["Cl3"] * fc,
        ke0=p["ke0"], dose_unit=p["dose_unit"], conc_unit=p["conc_unit"],
        meac=p.get("meac"), band=p.get("band"),
    )


```

</details>

### Check it

Add these lines inside the check block in `pk_models.py`:

```python

    # --- Week 7A: sizing ---
    pB = Patient(53, 77, 177, "F")
    fv, fc = size_factors(pB)
    check("Patient B FFM (kg)", pB.ffm, 48.83)
    check("volume factor", fv, 0.896, tol=0.001)
    check("clearance factor", fc, 0.921, tol=0.001)
    check("fentanyl V1, Patient B (L)", scaled_drug("fentanyl", pB).V1, 10.85)
    check("fentanyl k10, Patient B", scaled_drug("fentanyl", pB).k10, 0.0537, tol=0.0005)
    check("rocuronium k31 is zero", scaled_drug("rocuronium", pB).k31, 0, tol=0)
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ZeroDivisionError` when building rocuronium | The `V3 = 0` fix in `drug_from_clearances`. |
| `TypeError: Drug.__init__() got an unexpected keyword argument 'meac'` | Add `meac=None, band=None` to `Drug.__init__`. |
| `XX  Patient B FFM` | Your `Patient` class's female Al-Sallami formula. This uses sex `"F"`. |
| `KeyError: 'meac'` | Use `p.get("meac")`, not `p["meac"]`. |
| An old check turned `XX` after you changed `Drug` | You put `meac` or `band` before `dose_unit` in the signature, which shifted the order. New inputs go at the end. |

### Checkpoint

Patient B: FFM **48.83 kg**, volume factor **0.896**, clearance factor **0.921**. Fentanyl V1 **10.85 L**, k10 **0.0537**.

**References:** Al-Sallami HS et al. *Clin Pharmacokinet* 2015;54:1169–78 · Janmahasatian S et al. Quantification of lean bodyweight. *Clin Pharmacokinet* 2005;44:1051–65 · Fentanyl pooled set: McClain DA, Hug CC. *Clin Pharmacol Ther* 1980;28:106–14; Scott JC, Stanski DR. *J Pharmacol Exp Ther* 1987;240:159–66; Hudson RJ et al. *Anesthesiology* 1986;64:334–8; Varvel JR et al. *Anesthesiology* 1989;70:928–34; Shafer SL et al. *Anesthesiology* 1990;73:1091–102 · Dyck JB et al. *Anesthesiology* 1993;78:821–8 · Colin PJ et al. *Br J Anaesth* 2017;119:200–10 · Domino EF et al. *Clin Pharmacol Ther* 1984;36:645–53 · Mion G, Villevieille T. *CNS Neurosci Ther* 2013;19:370–80 · Plaud B et al. *Clin Pharmacol Ther* 1995;58:185–91 · Cortínez LI et al. *Br J Anaesth* 2007;99:679–85

---

## Week 7B — The drug library: remifentanil, methadone and the time-to-peak check

**Goal:** the last two drugs, every drug registered, and one check that tests a whole model at once.

**New ideas:** more practice turning published formulas into code; registering functions; a single behavioral check that covers many parameters.

### The science: covariates, and why ke0 comes from time to peak

**Remifentanil (Minto 1997).** Its strong age and lean-body-mass effects are why it has its own formula. It's also one of the models the Al-Rifai review highlights as widely used because it applies across adult ages. Remifentanil's organ-independent metabolism by esterases is what gives its short, predictable offset.

**Methadone (Inturrisi 1987).** It's unusual because its k31 is so small, giving a very slow return from the deep compartment. That's what you'll see in the time course: 61.9 ng/mL at 10 minutes after a 10 mg bolus, and still 6.0 ng/mL at 24 hours.

**Why a time-to-peak check works.** Minto and colleagues (2003) showed that it's better to carry a drug's ke0 across models by way of its **time to peak effect** after a bolus, rather than by copying the ke0 number. A ke0 means something only in combination with the PK model it came with, but time to peak is a clinical observation that any model can be asked to reproduce. So the time to peak depends on V1, all the rate constants and ke0 at once, which makes it one check that catches a mistake in any of them.

| drug | V1 | V2 | V3 | Cl1 | Cl2 | Cl3 | ke0 | doses in → conc. in | typical / MEAC |
|---|---|---|---|---|---|---|---|---|---|
| fentanyl | 12.1 | 35.7 | 224 | 0.632 | 2.8 | 1.55 | 0.221 | mcg → ng/mL | MEAC 0.6 ng/mL |
| dexmedetomidine | 8.057 | 12.75 | 177.69 | 0.4448 | 2.0788 | 1.9902 | 0.033 | mcg → ng/mL | 0.4–0.8 ng/mL |
| ketamine | 4.081 | 39.66 | 171.92 | 0.9223 | 2.6812 | 0.8407 | 0.088 | mg → µg/mL | 0.10–0.16 µg/mL |
| rocuronium | 3.920 | 16.06 | 0 | 0.6844 | 0.3935 | 0 | 0.186 | mg → µg/mL | 1.0–2.2 µg/mL |

Volumes in L, clearances in L/min, ke0 in /min. Rocuronium is a **two**-compartment model (no V3).

Two drugs are built differently:
- **Remifentanil:** Minto 1997, with its own age and LBM covariates (below). MEAC 1.0 ng/mL.
- **Methadone:** Inturrisi 1987. V1 = 0.18 L/kg × total weight; k10 0.00806, k12 0.408, k13 0.112, k21 0.06, k31 0.00114 /min (fixed); ke0 0.045 /min. Doses in mg, concentrations in µg/mL. MEAC 0.06 µg/mL (60 ng/mL).

> **Where these numbers come from.** These are the parameter sets StanpumpR uses, read from its source code (October 2026), with two simplifications so you can actually build them. StanpumpR's current methadone is a two-enantiomer model (Henthorn & Kharasch 2026) that's far beyond this workbook; Inturrisi 1987 is the classic model it replaced. StanpumpR also uses Eleveld 2017 for remifentanil; Minto is the long-standing standard. StanpumpR derives each ke0 from a published **time to peak effect** (Minto 2003). The ke0 column above is the result of that calculation, and your checkpoint is to confirm each drug peaks at the right time.

### The big picture

Remifentanil and methadone have their own published formulas, so they get their own small functions. Then everything goes in `DRUGS`, and every later lesson can use all seven drugs.

### Build it: `minto_drug` and `methadone_drug` 🔴

Add these to `pk_models.py`, above the `DRUGS` dictionary. Both follow the same shape you've written several times now.

**`minto_drug(patient)`.** Remifentanil: doses in mcg, concentrations in ng/mL, MEAC 1.0. With `age_d = age − 40` and `lbm_d = lbm − 55`:

```
V1  = 5.1   − 0.0201·age_d + 0.072·lbm_d      V3  = 5.42 (fixed)
V2  = 9.82  − 0.0811·age_d + 0.108·lbm_d
Cl1 = 2.6   − 0.0162·age_d + 0.0191·lbm_d
Cl2 = 2.05  − 0.0301·age_d
Cl3 = 0.076 − 0.00113·age_d
ke0 = 0.595 − 0.007·age_d
```

**`methadone_drug(patient)`.** V1 = 0.18 L/kg × weight. Fixed k10 0.00806, k12 0.408, k13 0.112, k21 0.06, k31 0.00114. ke0 0.045. Doses in mg, concentrations in µg/mL, MEAC 0.06.

Which helper does each one need? Look at whether the source gives clearances or rate constants.

<details>
<summary><b>Hint</b></summary>

Minto publishes clearances, so use `drug_from_clearances`. Inturrisi publishes rate constants, so call `Drug(...)` directly, like `marsh_drug`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def minto_drug(patient):
    """Minto CF et al. Anesthesiology 1997;86:10-23. Remifentanil: mcg in, ng/mL out."""
    age_d = patient.age - 40
    lbm_d = patient.lbm - 55
    V1 = 5.1 - 0.0201 * age_d + 0.072 * lbm_d
    V2 = 9.82 - 0.0811 * age_d + 0.108 * lbm_d
    V3 = 5.42
    Cl1 = 2.6 - 0.0162 * age_d + 0.0191 * lbm_d
    Cl2 = 2.05 - 0.0301 * age_d
    Cl3 = 0.076 - 0.00113 * age_d
    ke0 = 0.595 - 0.007 * age_d
    return drug_from_clearances("Remifentanil (Minto)", V1, V2, V3, Cl1, Cl2, Cl3, ke0=ke0,
                                dose_unit="mcg", conc_unit="ng/mL", meac=1.0)


def methadone_drug(patient):
    """Inturrisi CE et al. Clin Pharmacol Ther 1987;41:392-401 (simplified)."""
    V1 = 0.18 * patient.weight
    return Drug("Methadone (Inturrisi)", V1, 0.00806, 0.408, 0.112, 0.06, 0.00114, ke0=0.045,
                dose_unit="mg", conc_unit="µg/mL", meac=0.06)


```

</details>

### Build it: register everything 🟡

Below the `DRUGS` dictionary, add one `DRUGS.update({...})` call. Here's the first entry. A `lambda` is needed because `scaled_drug` takes two inputs and the registry wants functions of one input:

```python
DRUGS.update({
    "fentanyl":        {"StanpumpR (pooled)": lambda p: scaled_drug("fentanyl", p)},
    # your lines: remifentanil (Minto), methadone (Inturrisi), dexmedetomidine (Dyck),
    #             ketamine (Domino), rocuronium (Plaud)
})
```

<details>
<summary><b>Answer</b></summary>

```python
DRUGS.update({
    "fentanyl":        {"StanpumpR (pooled)": lambda p: scaled_drug("fentanyl", p)},
    "remifentanil":    {"Minto": minto_drug},
    "methadone":       {"Inturrisi": methadone_drug},
    "dexmedetomidine": {"Dyck": lambda p: scaled_drug("dexmedetomidine", p)},
    "ketamine":        {"Domino": lambda p: scaled_drug("ketamine", p)},
    "rocuronium":      {"Plaud": lambda p: scaled_drug("rocuronium", p)},
})


```

</details>

### Check it

Each drug gets one bolus and nothing else, and Ce should peak at the published time. It takes several seconds to run. Add these lines inside the check block:

```python

    # --- Week 7B: every drug through the registry ---
    for name, v1 in [("fentanyl", 10.85), ("dexmedetomidine", 7.22), ("ketamine", 3.66),
                     ("rocuronium", 3.51), ("methadone", 13.86)]:
        model_fn = next(iter(DRUGS[name].values()))      # the first model listed for that drug
        check(f"{name} V1, Patient B (L)", model_fn(pB).V1, v1)

    # --- Week 7B: time to peak. One bolus, nothing else, Patient A ---
    from engine import Simulation
    for name, t_peak in [("fentanyl", 3.6), ("remifentanil", 1.4), ("methadone", 10.0),
                         ("dexmedetomidine", 14.9), ("ketamine", 3.0), ("rocuronium", 4.5)]:
        model_fn = next(iter(DRUGS[name].values()))
        sim = Simulation(model_fn(p70), t_end=20, steps_per_min=60)
        sim.bolus(0, 1.0)
        sim.run()
        check(f"{name} time to peak (min)", sim.t[sim.ce.argmax()], t_peak, tol=0.1)
```


The import of `Simulation` is inside the check block on purpose. `engine.py` doesn't import `pk_models`, so there's no circular import problem, but keeping test-only imports here makes it clear that the rest of the file doesn't need them. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ZeroDivisionError` | `drug_from_clearances` dividing Cl3 by a V3 of 0 (rocuronium). |
| `TypeError: __init__() got an unexpected keyword argument 'meac'` | `Drug.__init__` doesn't have the new `meac` and `band` parameters yet. |
| `XX  ... time to peak` for one drug only | That drug's `ke0` (typo), or its V1 or clearances in `REFERENCE_PK`. |
| Concentrations 1000× off | The drug's `dose_unit`. Fentanyl and dexmedetomidine are `"mcg"`; ketamine, rocuronium and methadone are `"mg"`. |
| `KeyError: 'remifentanil'` | That drug isn't registered in `DRUGS` yet, or its name is spelled differently. |
| `XX  Patient B FFM` | Your `Patient` FFM uses the sex-specific formula. Check that `"F"` reaches the female branch. |
| Older checks now fail | Something in `Drug` or `drug_from_clearances` changed behavior. Run `python pk_models.py` and fix the first `XX` before going on. |

### Things to consider

- **Why put the numbers in a dict?** Four drugs share one builder. Writing four functions would mean four places for a typo. The dict is also something Week 12 can read to build menus.
- **Units are part of the drug.** Fentanyl's Ce comes out in ng/mL because doses are in mcg and volumes in L (mcg/L = ng/mL). Ketamine's doses in mg give µg/mL (mg/L = µg/mL). Write that rule in a comment. It explains every unit in this project.
- **The ketamine numbers** are StanpumpR's 2026 refit of Domino's 1984 measured concentrations, not the paper's own table, which turned out not to describe its data. That's a good reminder that published parameters aren't automatically right.
- Patient A (40 yo, 70 kg, 170 cm, M) has almost exactly the reference FFM, so their factors are about 1.0. Use Patient B to see scaling actually do something.

### Checkpoint

- Patient B: FFM **48.83 kg**, volume factor **0.896**, clearance factor **0.921**.
- Patient B, scaled: fentanyl V1 **10.85 L**, k10 **0.0537**; dexmedetomidine V1 **7.22 L**; ketamine V1 **3.66 L**; rocuronium V1 **3.51 L**; methadone V1 **13.86 L**.
- Time-to-peak check (single bolus, Patient A):

| drug | Ce peaks at | example bolus → peak Ce |
|---|---|---|
| fentanyl | **3.6 min** | 100 mcg → 2.25 ng/mL |
| remifentanil (Minto) | **1.4 min** | 1 mcg/kg → 4.09 ng/mL |
| methadone | **10 min** | 10 mg → 61.9 ng/mL at 10 min, 6.0 ng/mL at 24 h |
| dexmedetomidine | **14.9 min** | |
| ketamine | **3.0 min** | 0.5 mg/kg → 0.58 µg/mL |
| rocuronium | **4.5 min** | 0.6 mg/kg → 3.23 µg/mL |

- Dexmedetomidine 1 mcg/kg over 10 min (6 mcg/kg/h), then 0.5 mcg/kg/h: Ce **0.44** at 10 min, **0.62** at 30 min, **0.58** at 60 min, inside the 0.4–0.8 band.

**References:** Al-Sallami HS et al. *Clin Pharmacokinet* 2015;54:1169–78 · Janmahasatian S et al. Quantification of lean bodyweight. *Clin Pharmacokinet* 2005;44:1051–65 · Minto CF et al. *Anesthesiology* 1997;86:10–23 · Minto CF, Schnider TW, Gregg KM, Henthorn TK, Shafer SL. Using the time of maximum effect site concentration to combine pharmacokinetics and pharmacodynamics. *Anesthesiology* 2003;99:324–33 · Fentanyl pooled set: McClain DA, Hug CC. *Clin Pharmacol Ther* 1980;28:106–14; Scott JC, Stanski DR. *J Pharmacol Exp Ther* 1987;240:159–66; Hudson RJ et al. *Anesthesiology* 1986;64:334–8; Varvel JR et al. *Anesthesiology* 1989;70:928–34; Shafer SL et al. *Anesthesiology* 1990;73:1091–102 · Shafer SL, Varvel JR. Pharmacokinetics, pharmacodynamics, and rational opioid selection. *Anesthesiology* 1991;74:53–63 · Dyck JB et al. *Anesthesiology* 1993;78:821–8 · Colin PJ et al. *Br J Anaesth* 2017;119:200–10 · Domino EF et al. *Clin Pharmacol Ther* 1984;36:645–53 · Mion G, Villevieille T. *CNS Neurosci Ther* 2013;19:370–80 · Plaud B et al. *Clin Pharmacol Ther* 1995;58:185–91 · Cortínez LI et al. *Br J Anaesth* 2007;99:679–85 · Inturrisi CE et al. *Clin Pharmacol Ther* 1987;41:392–401 · Kharasch ED et al. *Clin Pharmacol Ther* 2004;76:250–69 · Henthorn TK, Kharasch ED. *Clin Pharmacol Ther* 2026;119:739–50 (StanpumpR's current methadone model)

---

## Week 8A — A whole case: many drugs at once

**Goal:** one dose table with five drugs mixed together, run as one case, with each drug kept separate.

**New ideas:** *grouping* a list by a key into a dictionary of lists; a class that owns several other objects; `dict.get` with a default.

### The science: why one table

Real cases don't happen one drug at a time. Hypnotic, opioid and relaxant are given together, and each has its own time course. StanpumpR's insight was to let you enter them the way an anesthetic record reads, as one list in time order, and have the software sort out which row belongs to which drug. Next lesson's redoses are where this pays off, and in Week 9 the drugs get combined into one clinical answer.

### The big picture

Until now, one `Simulation` meant one drug. A real case has several. `Case` is a manager: it takes the whole dose table, splits it by drug, and builds one `Simulation` per drug, all on the same time grid.

```
dose table (all drugs mixed) ──group_by_drug──► {"propofol": [rows], "fentanyl": [rows], ...}
                                                      │  for each drug:
                                                      │    DRUGS[drug][model] → Drug
                                                      │    Simulation + apply_rows + run
                                                      ▼
                                       case.sims = {"propofol": sim, "fentanyl": sim, ...}
plot_case(case) ──► one stacked panel per drug
```

There's no new pharmacology here. It's organizing code you've already written.

### Learn it: grouping 🟢

Grouping is one of the most common jobs in programming. Empty `scratch.py`:

```python
sales = [("Mon", "apple", 3), ("Mon", "pear", 1), ("Tue", "apple", 2), ("Wed", "plum", 5)]

groups = {}
for row in sales:
    fruit = row[1]
    if fruit not in groups:
        groups[fruit] = []
    groups[fruit].append(row)

print(list(groups))
print(groups["apple"])

for fruit, rows in groups.items():
    print(fruit, len(rows))
```

```text
['apple', 'pear', 'plum']
[('Mon', 'apple', 3), ('Tue', 'apple', 2)]
apple 2
pear 1
plum 1
```

The first time a key appears, create an empty list for it. Then always append.

### Learn it: a manager object 🟢

A class can build and hold other objects. Here's a `School` that takes a mixed list of students, and builds one `Classroom` for each subject. Empty `scratch.py`:

```python
class Classroom:
    def __init__(self, subject):
        self.subject = subject
        self.students = []


SUBJECTS = {"math": "Room 1", "art": "Room 2"}


class School:
    def __init__(self, roster, preferred=None):
        self.roster = roster
        self.preferred = preferred or {}
        self.rooms = {}

    def room_for(self, subject):
        if subject not in SUBJECTS:
            raise ValueError(f"Unknown subject '{subject}'. Known: {list(SUBJECTS)}")
        return self.preferred.get(subject, SUBJECTS[subject])

    def build(self):
        for name, subject in self.roster:
            if subject not in self.rooms:
                self.rooms[subject] = Classroom(subject)
            self.rooms[subject].students.append(name)
        return self


s = School([("Ana", "math"), ("Sam", "art"), ("Jo", "math")], preferred={"art": "Studio"}).build()
print(s.rooms["math"].students)
print(s.room_for("math"), s.room_for("art"))

try:
    s.room_for("music")
except ValueError as err:
    print(err)
```

```text
['Ana', 'Jo']
Room 1 Studio
Unknown subject 'music'. Known: ['math', 'art']
```

- `preferred or {}` means "use `preferred` if it was given, otherwise an empty dictionary".
- `.get(key, default)` gives a fallback when a key is missing.
- `.build()` returns `self`, so the object can be made and built in one line.

### Build it: `case.py` 🔴

The dose table goes in `cases/four_hour_case.csv`:

```text
time,drug,amount,units
0,propofol,140,mg
0,propofol,150,mcg/kg/min
0,fentanyl,100,mcg
0,rocuronium,0.6,mg/kg
0,ketamine,0.5,mg/kg
10,propofol,120,mcg/kg/min
45,fentanyl,50,mcg
45,rocuronium,10,mg
90,fentanyl,50,mcg
90,rocuronium,10,mg
120,propofol,100,mcg/kg/min
120,dexmedetomidine,0.4,mcg/kg/h
170,propofol,0,mcg/kg/min
170,dexmedetomidine,0,mcg/kg/h
```

Now create `tci/case.py`, importing `Simulation`, `apply_rows` and `DRUGS`:

**`group_by_drug(rows)`** turns `[(t, drug, amount, units), ...]` into `{drug: [rows for that drug], ...}`.

**`class Case`**, with `__init__(self, patient, rows, model_choice=None, t_end=240, steps_per_min=6)`, stores everything, and makes `self.sims = {}`.

**`model_name_for(self, drug)`:** if `drug` isn't in `DRUGS`, raises a `ValueError` listing the drugs you do know. Otherwise, it returns the name chosen in `model_choice`, or the first model listed for that drug.

**`run(self)`:** for each drug in the grouped rows, finds the model function, builds the `Drug` for this patient, makes a `Simulation` with this case's settings, applies the rows, runs it, and stores it in `self.sims[drug]`. It returns `self`.

Print `group_by_drug(...)` for the example case first. You should see five keys.

<details>
<summary><b>Hint</b></summary>

`next(iter(DRUGS[drug]))` gives the first model's name. Then `DRUGS[drug][name]` is the function, and `DRUGS[drug][name](self.patient)` calls it.

</details>
<details>
<summary><b>Answer</b></summary>

```python
from dosing import apply_rows
from engine import Simulation
from pk_models import DRUGS


def group_by_drug(rows):
    """[(t, drug, amount, units), ...]  ->  {drug: [rows for that drug], ...}"""
    groups = {}
    for row in rows:
        drug = row[1]
        if drug not in groups:
            groups[drug] = []
        groups[drug].append(row)
    return groups


class Case:
    def __init__(self, patient, rows, model_choice=None, t_end=240, steps_per_min=6):
        self.patient = patient
        self.rows = rows
        self.model_choice = model_choice or {}    # e.g. {"propofol": "Schnider"}
        self.t_end = t_end
        self.steps_per_min = steps_per_min
        self.sims = {}                            # drug name -> finished Simulation

    def model_name_for(self, drug):
        """The chosen model, or the first one listed in DRUGS for that drug."""
        if drug not in DRUGS:
            raise ValueError(f"Unknown drug '{drug}'. Known drugs: {', '.join(DRUGS)}")
        return self.model_choice.get(drug, next(iter(DRUGS[drug])))

    def run(self):
        for drug, drug_rows in group_by_drug(self.rows).items():
            name = self.model_name_for(drug)
            model_fn = DRUGS[drug][name]
            sim = Simulation(model_fn(self.patient), t_end=self.t_end,
                             steps_per_min=self.steps_per_min)
            apply_rows(sim, drug_rows, self.patient)
            sim.run()
            self.sims[drug] = sim
        return self
```

</details>
<details>
<summary><b>How the code works</b></summary>

- `run()` asks `model_name_for` first, so a misspelled drug gets your clear message rather than a `KeyError`.
- Each `Simulation` is the same class you built in Week 3. The `Case` adds no pharmacology at all. It only organizes.
- `self.sims` is a dictionary of finished simulations, so later code can write `case.sims["fentanyl"].ce_at(45)`.

</details>

### Check it

Add this at the bottom of `case.py`. It uses `plot_case`, which you'll write next lesson, so leave out the `from plotting ...` line and the final `plot_case(case)` line for now.

```python


if __name__ == "__main__":
    from patient import Patient
    from dosing import read_dose_table
    from checks import check

    case = Case(Patient(40, 70, 170, "M"), read_dose_table("cases/four_hour_case.csv")).run()
    expected = {
        "propofol":        [(5, 4.05), (45, 3.14), (170, 3.13), (200, 1.04)],
        "fentanyl":        [(5, 2.14), (45, 0.39), (50, 1.43), (90, 0.42), (95, 1.47)],
        "rocuronium":      [(5, 3.21), (45, 0.21), (50, 0.96)],
        "ketamine":        [(5, 0.56), (45, 0.17)],
        "dexmedetomidine": [(45, 0.0), (170, 0.16)],
    }
    for drug, points in expected.items():
        for minute, value in points:
            check(f"{drug} Ce at {minute} min", case.sims[drug].ce_at(minute), value, tol=0.02)

    try:
        Case(Patient(40, 70, 170, "M"), [(0, "fentanly", 100, "mcg")]).run()
        print("XX  a misspelled drug was accepted")
    except ValueError as err:
        print("OK  misspelled drug rejected:", err)
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `KeyError: 'fentanly'` instead of a friendly message | `run()` looks the drug up in `DRUGS` *before* calling `model_name_for`. Call `model_name_for` first. |
| A drug is missing from `case.sims` | Its name in the CSV doesn't match. Check for capitals and spaces (`"Fentanyl "` ≠ `"fentanyl"`). |
| One drug's curve looks like another's | The `zip(axes..., case.sims.items())` pairing in `plot_case`, or two drugs share one `Simulation` object. |
| No shaded band | That drug's `band` is `None`. Check `REFERENCE_PK`. |
| `XX` for propofol but other drugs OK | The default propofol model. The first key in `DRUGS["propofol"]` should be Marsh. |
| Slow | 7 drugs × 1,441 steps is a lot of `solve_ivp` calls. Try `steps_per_min=2` while developing. |

### Checkpoint

Every line says `OK`, including the rejected misspelling. Fentanyl Ce at 45 min is **0.39**, just before the redose, and **1.43** at 50 min, just after it.

---

## Week 8B — Long cases on screen

**Goal:** a stacked plot with one panel per drug and the typical ranges shaded, and a script that runs any case from a CSV file.

**New ideas:** subplots that share an x-axis; `zip`; `ax.axhspan` and `ax.axhline`; a script that takes a file name from the command line.

**Read first:** [Matplotlib: multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html) · [`ax.axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html)

### The science: accumulation

Look at the fentanyl troughs in this lesson's checkpoint: 0.42 ng/mL before the second redose, *higher* than the 0.39 before the first, even though the redose was half the size of the first dose. That's accumulation in the peripheral compartments. Fentanyl is short-acting after one bolus because it redistributes, not because it's eliminated quickly. As the peripheral compartments fill, redistribution slows, and each dose lasts longer than the one before.

### The big picture

```
cases/four_hour_case.csv ──► run_case.py ──► Case(...).run() ──► plot_case(case) ──► the picture
```

### Learn it: stacked panels 🟢

Empty `scratch.py`:

```python
import matplotlib.pyplot as plt

data = {"rain": [1, 3, 2], "wind": [5, 4, 6]}
days = [1, 2, 3]

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6, 4), squeeze=False)
print(axes.shape)

for ax, (name, values) in zip(axes[:, 0], data.items()):
    ax.plot(days, values)
    ax.set_ylabel(name)
    ax.axhspan(2, 4, alpha=0.2)
    ax.axhline(3, linestyle="--")

axes[-1, 0].set_xlabel("Day")
fig.tight_layout()
plt.show()

for letter, number in zip(["a", "b", "c"], [1, 2, 3]):
    print(letter, number)
```

```text
(2, 1)
a 1
b 2
c 3
```

- `plt.subplots(2, 1, sharex=True)` makes 2 rows and 1 column of panels with a shared time axis.
- `squeeze=False` always returns a 2-D array of axes, even for a single panel. Without it, a one-drug case would break your code.
- `zip` walks through two lists side by side.
- `ax.axhspan(low, high)` shades a band, and `ax.axhline(y)` draws a horizontal line.

### Learn it: a file name from the command line 🟢

`sys.argv` is the list of words you typed to run a script. Empty `scratch.py`:

```python
import sys

print(sys.argv)
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "nobody"
print("hello", name)
```

Run it twice: `python scratch.py`, then `python scratch.py Ana`.

```text
['scratch.py', 'Ana']
hello Ana
```

### Build it: `plot_case` 🔴

Add `plot_case(case, save_path=None)` to `plotting.py`. It makes one panel per drug in `case.sims`, stacked, with a figure size of `(8, 2.2 * n)`:

- Each panel plots `sim.t` and `sim.ce`, with a y-label of the drug name and `sim.drug.conc_unit`.
- If the drug has a `band`, shade it. If it has a `meac`, draw a dashed line there.
- The bottom panel gets the x-axis label `"Time (min)"`. Then call `tight_layout`, and save or show.
- It returns `fig, axes`.

<details>
<summary><b>Answer</b></summary>

```python


def plot_case(case, save_path=None):
    """One panel per drug, stacked, sharing the time axis."""
    n = len(case.sims)
    fig, axes = plt.subplots(n, 1, sharex=True, figsize=(8, 2.2 * n), squeeze=False)
    for ax, (name, sim) in zip(axes[:, 0], case.sims.items()):
        ax.plot(sim.t, sim.ce, label="Ce")
        ax.set_ylabel(f"{name}\n({sim.drug.conc_unit})")
        if sim.drug.band:
            low, high = sim.drug.band
            ax.axhspan(low, high, alpha=0.2)
        if sim.drug.meac:
            ax.axhline(sim.drug.meac, linestyle="--")
    axes[-1, 0].set_xlabel("Time (min)")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
    else:
        plt.show()
    return fig, axes
```

</details>

### Build it: `run_case.py` 🔴

Write `tci/run_case.py`. It takes a CSV path from the command line, defaulting to `cases/four_hour_case.csv`, builds a `Case` for Patient A (40 yo, 70 kg, 170 cm, M), prints each drug's peak Ce, and plots it. Then try `model_choice={"propofol": "Schnider"}`. Only one panel should change.

<details>
<summary><b>Answer</b></summary>

```python
import sys

from case import Case
from dosing import read_dose_table
from patient import Patient
from plotting import plot_case

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "cases/four_hour_case.csv"
    patient = Patient(40, 70, 170, "M")
    case = Case(patient, read_dose_table(path)).run()
    for name, sim in case.sims.items():
        print(f"{name}: peak Ce {sim.ce.max():.2f} {sim.drug.conc_unit}")
    plot_case(case)
```

</details>

```text
propofol: peak Ce 4.08 µg/mL
```

Add `plot_case` to the end of the check block in `case.py`, so that running the file shows you the picture:

```python

    from plotting import plot_case
    plot_case(case)
```


Commit.

### Things to consider

- **Speed.** Four hours at 6 steps/min is 1,441 `solve_ivp` calls per drug. That's fine for now. If a 12-hour methadone case feels slow, try `steps_per_min=2` and see how much the curve changes. (Stretch: StanpumpR is fast because it uses exact closed-form solutions between events instead of a numerical solver. Look up "three-compartment model closed form" if you're curious.)
- **Every drug on the same time grid** matters for Week 9, where you'll combine propofol and fentanyl point by point.
- **Rows don't have to be in order** in the CSV, since each simulation checks event times itself. Test that by shuffling the rows.
- What should happen if someone types a drug that's in `DRUGS` but gives units of the wrong kind, like `fentanyl, 2, mg/kg`? It would run, and give a thousand-fold dose. Real software warns about doses outside a typical range. Stretch: add a `max_bolus` to `REFERENCE_PK` and warn.

### Checkpoint

The example case, Patient A, propofol on Marsh, `t_end=240`, `steps_per_min=6`:

| minute | 5 | 45 | 50 | 90 | 95 | 170 | 200 |
|---|---|---|---|---|---|---|---|
| propofol (µg/mL) | 4.05 | 3.14 | 3.18 | 3.39 | 3.41 | 3.13 | 1.04 |
| fentanyl (ng/mL) | 2.14 | 0.39 | 1.43 | 0.42 | 1.47 | 0.38 | 0.34 |
| rocuronium (µg/mL) | 3.21 | 0.21 | 0.96 | 0.16 | 0.91 | 0.08 | 0.05 |
| ketamine (µg/mL) | 0.56 | 0.17 | 0.15 | 0.08 | 0.07 | 0.04 | 0.03 |
| dexmedetomidine (ng/mL) | 0 | 0 | 0 | 0 | 0 | 0.16 | 0.13 |

Each redose jumps the curve back up. Look at the fentanyl troughs: 0.42 ng/mL before the second redose, *higher* than the 0.39 before the first, even though the redose was half the size of the first dose. That's accumulation in the peripheral compartments. Notice also that a 0.4 mcg/kg/h dexmedetomidine infusion for 50 minutes with no load only reaches 0.16 ng/mL, well below its sedation band, because of its 15-minute time to peak and large distribution volume.

**References:** Shafer SL. *stanpumpR* (stanpumpr.io). The four-hour case is a teaching example, not a recommended regimen.

---

## Week 9 — Drug interactions: propofol plus all the opioids

**Goal:** combine every opioid on board into one number, and use the propofol–opioid interaction model StanpumpR uses to predict the probability of responding to laryngoscopy over the whole case.

**New ideas:** *vectorization* (arithmetic on whole NumPy arrays, no loops); summing arrays from a dictionary; `np.maximum` for safe math.

**Read first:** [NumPy: basic array operations](https://numpy.org/doc/stable/user/absolute_beginners.html#basic-array-operations)

### The science: synergy

Propofol alone is a poor analgesic, and it takes a high concentration on its own to stop a response to laryngoscopy. An opioid changes this dramatically: a small amount sharply reduces the propofol needed. Bouillon and colleagues (2004) modeled this as a hierarchy. The opioid first reduces how intense the stimulus feels, and propofol then has to suppress what's left.

Fentanyl 1 ng/mL and remifentanil 1 ng/mL are not the same amount of opioid. StanpumpR's answer: divide each opioid's Ce by **its own MEAC** (minimum effective analgesic concentration), then add. Fentanyl at 1.2 ng/mL is 2 × MEAC; remifentanil at 2 ng/mL is also 2 × MEAC; together they're 4 × MEAC, or **400% MEAC**.

To feed the interaction model, convert that total back into the drug the model was fitted with, remifentanil:

```text
remifentanil-equivalent Ce (ng/mL) = Σ (Ce_opioid / MEAC_opioid) × MEAC_remifentanil
```

Bouillon's model is *hierarchical*: the opioid first reduces how intense the stimulus feels, then propofol has to suppress what's left.

```text
Constants (Bouillon 2004, Table 4):
  C50_remi = 1.01 ng/mL   γ_remi = 0.72
  C50_prop = 6.68 µg/mL   γ_prop = 6.9
  laryngoscopy intensity without opioid, I0 = 0.83

  I = I0 × (1 − R^γr / (R^γr + (C50_remi × I0)^γr))        R = remi-equivalent Ce
  P(response) = 1 − P^γp / (P^γp + (C50_prop × I)^γp)        P = propofol Ce
```

### The big picture

This week turns concentrations into a clinical answer: *would this patient react to a laryngoscope right now?*

```
case.sims ──percent_meac──► opioid total, as % of MEAC (every opioid added together)
          ──remi_equivalent──► the same total, in remifentanil ng/mL
case.sims["propofol"].ce ─┐
remifentanil-equivalent ──┴──► p_response_laryngoscopy() ──► a probability at every time point
```

Everything is done on whole arrays at once (vectorization). There's no loop over time anywhere in this file.

### Learn it: math on whole arrays 🟢

Empty `scratch.py`:

```python
import numpy as np

prices = np.array([10.0, 20.0, 40.0])
tax = np.array([1.0, 2.0, 4.0])

print(prices + tax)
print(prices * 2)
print(prices / (prices + 10))
print(prices ** 2)

total = np.zeros_like(prices)
for name, column in {"prices": prices, "tax": tax}.items():
    total += column
print(total)

messy = np.array([4.0, -0.0001, 9.0])
print(np.maximum(messy, 0))
print(np.maximum(messy, 0) ** 0.5)
print(5 ** 0.5 == np.maximum(5, 0) ** 0.5)
```

```text
[11. 22. 44.]
[20. 40. 80.]
[0.5        0.66666667 0.8       ]
[ 100.  400. 1600.]
[11. 22. 44.]
[4. 0. 9.]
[2. 0. 3.]
True
```

- Math on an array applies to every element, with no loop. The same formula works on one number or a million.
- `np.zeros_like(x)` makes an array of zeros the same size as `x`.
- `np.maximum(messy, 0)` replaces any negative with 0, one element at a time. A negative number to a fractional power gives `NaN`, and solvers can leave tiny negative rounding errors, so this protects you. Python's `max()` can't do this for arrays.

### Build it: `pd_endpoints.py` 🔴

Create `tci/pd_endpoints.py`, with `REMI_MEAC = 1.0`, and three functions.

**`p_response_laryngoscopy(ce_prop, remi_eq)`** uses the formulas above, with the constants from Step 2. It must work on plain numbers *and* on whole arrays. Protect the powers with `np.maximum(..., 0)`. Check this one first, with plain numbers.

**`percent_meac(case)`** returns an array: 100 × the sum of `sim.ce / sim.drug.meac` across every drug in the case that has a `meac`. Start from `np.zeros_like` of any simulation's `t`. `next(iter(case.sims.values()))` gets you the first simulation.

**`remi_equivalent(case)`** converts percent MEAC into remifentanil-equivalent ng/mL.

<details>
<summary><b>Hint</b></summary>

Write `r = np.maximum(remi_eq, 0) ** g_r` and `p = np.maximum(ce_prop, 0) ** g_p` first. Then each formula fits on one line, using `r` and `p`. There's no loop over time anywhere in this file.

</details>
<details>
<summary><b>Answer</b></summary>

```python
import numpy as np

REMI_MEAC = 1.0   # ng/mL


def percent_meac(case):
    """Sum of every opioid's Ce / MEAC across the case, as a percent. Returns an array."""
    total = np.zeros_like(next(iter(case.sims.values())).t)
    for name, sim in case.sims.items():
        if sim.drug.meac:
            total += sim.ce / sim.drug.meac
    return 100 * total


def remi_equivalent(case):
    return percent_meac(case) / 100 * REMI_MEAC


def p_response_laryngoscopy(ce_prop, remi_eq):
    """Bouillon TW et al. Anesthesiology 2004;100:1353-72. Works on numbers or whole arrays."""
    c50_r, g_r, c50_p, g_p, i0 = 1.01, 0.72, 6.68, 6.9, 0.83
    r = np.maximum(remi_eq, 0) ** g_r       # max(…, 0): tiny negative rounding errors would give NaN
    p = np.maximum(ce_prop, 0) ** g_p
    intensity = i0 * (1 - r / (r + (c50_r * i0) ** g_r))
    return 1 - p / (p + (c50_p * intensity) ** g_p)
```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`percent_meac(case)`** starts with an array of zeros the same length as the time grid (`np.zeros_like`). For each drug that has a `meac`, it adds `Ce ÷ MEAC`. Drugs without a MEAC (propofol, rocuronium…) are skipped.
- **`remi_equivalent(case)`** converts that percentage into remifentanil ng/mL, the unit Bouillon's model was fitted in.
- **`p_response_laryngoscopy`** works on plain numbers *or* arrays. The two lines with `np.maximum(..., 0)` guard against tiny negative rounding errors (a negative number to a fractional power gives `NaN`). The two lines you write are the two formulas from the box above: intensity first, then probability.

</details>

### Check it

Add this at the very bottom of `pd_endpoints.py`:

```python


```
```python
if __name__ == "__main__":
    from patient import Patient
    from case import Case
    from dosing import read_dose_table
    from checks import check

    for prop, remi, expected in [(3, 0, 0.986), (5, 0, 0.671), (3, 1, 0.270),
                                 (4, 0.5, 0.203), (2, 4, 0.065), (4, 2, 0.007)]:
        check(f"P(response), propofol {prop} + remi-eq {remi}",
              p_response_laryngoscopy(prop, remi), expected, tol=0.002)

    case = Case(Patient(40, 70, 170, "M"), read_dose_table("cases/four_hour_case.csv")).run()
    meac = percent_meac(case)
    p = p_response_laryngoscopy(case.sims["propofol"].ce, remi_equivalent(case))
    index = case.sims["propofol"]._index
    for minute, pct, prob in [(3, 370, 0.002), (45, 64, 0.44), (60, 128, 0.10), (180, 61, 0.97)]:
        check(f"% MEAC at {minute} min", meac[index(minute)], pct, tol=1.5)
        check(f"P(response) at {minute} min", p[index(minute)], prob, tol=0.01)
```


### See it 🔴

In `scratch.py`, build the Week 8 case. Call `p_response_laryngoscopy(case.sims["propofol"].ce, remi_equivalent(case))` **once**, with whole arrays. Use `plot_runs` to plot P(response) against time, and do the same for percent MEAC. Find the moments before each fentanyl redose, where P(response) climbs.

<details>
<summary><b>Answer</b></summary>

```python
from case import Case
from dosing import read_dose_table
from patient import Patient
from pd_endpoints import percent_meac, remi_equivalent, p_response_laryngoscopy
from plotting import plot_runs

case = Case(Patient(40, 70, 170, "M"), read_dose_table("cases/four_hour_case.csv")).run()
t = case.sims["propofol"].t
p = p_response_laryngoscopy(case.sims["propofol"].ce, remi_equivalent(case))
plot_runs([("P(response)", t, p)], ylabel="Probability")
plot_runs([("% MEAC", t, percent_meac(case))], ylabel="% MEAC")
```

</details>


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| P(response) is about 0 for the whole case | You passed the *percent* (e.g. 370) instead of remifentanil-equivalents (3.7). StanpumpR itself once had exactly this bug. |
| `nan` values | A negative concentration raised to a fractional power. Keep the `np.maximum(..., 0)` lines. |
| `ValueError: operands could not be broadcast together` | Two arrays of different lengths. All drugs in the case must share `t_end` and `steps_per_min`. |
| Probabilities run the wrong way (higher with more drug) | You returned the probability of *no* response. This function returns the probability of responding. |
| `XX` on the number table only | The formula. Compare each line with the box, one bracket at a time. |

### Things to consider

- **What about dexmedetomidine, ketamine and rocuronium?** StanpumpR (and the literature) don't have a validated combined surface for those with propofol, so StanpumpR shows them against their own typical ranges instead, which is what your Week 8 bands do. Ketamine and dexmedetomidine are known to be opioid-sparing, but adding them to this model would be inventing numbers. Rocuronium has a completely separate endpoint (twitch depression), not loss of response.
- **Laryngoscopy is a very strong stimulus.** P(response) = 0.44 at minute 45 doesn't mean the patient is waking up. It means they'd likely react to a laryngoscope at that moment. This model answers "is this enough for intubation?", not "is this enough for skin closure?".
- The old version of this workbook used the Greco model with illustrative numbers. Bouillon's published hierarchical model replaces it here because it's what StanpumpR actually uses.

### Checkpoint

`p_response_laryngoscopy` with plain numbers:

| propofol Ce | remi-eq Ce | P(response) |
|---|---|---|
| 3 | 0 | **0.986** |
| 5 | 0 | **0.671** |
| 3 | 1 | **0.270** |
| 4 | 0.5 | **0.203** |
| 2 | 4 | **0.065** |
| 4 | 2 | **0.007** |

Propofol 3 µg/mL alone: 99% would respond. Add just 1 ng/mL of remifentanil-equivalent and it falls to 27%. That's the synergy that justifies giving an opioid before laryngoscopy.

The Week 8 case:

| minute | fentanyl Ce | % MEAC | remi-eq | propofol Ce | P(response) |
|---|---|---|---|---|---|
| 3 | 2.22 | 370% | 3.70 | 3.57 | **0.002** |
| 45 (before redose) | 0.39 | 64% | 0.64 | 3.14 | **0.44** |
| 60 | 0.77 | 128% | 1.28 | 3.25 | **0.10** |
| 180 (propofol off) | 0.37 | 61% | 0.61 | 1.87 | **0.97** |

**References:** Bouillon TW et al. Pharmacodynamic interaction between propofol and remifentanil regarding hypnosis, tolerance of laryngoscopy, bispectral index, and electroencephalographic approximate entropy. *Anesthesiology* 2004;100:1353–72 · Gourlay GK et al. Fentanyl blood concentration–analgesic response relationship in the treatment of postoperative pain. *Anesth Analg* 1988;67:329–37 · Shafer SL. *stanpumpR* (opioid MEAC normalization and the Bouillon panel) · Background: Kern SE et al. *Anesthesiology* 2004;100:1373–81; Johnson KB, Syroid ND et al. *Anesth Analg* 2008;106:471–9; Greco WR, Bravo G, Parsons JC. *Pharmacol Rev* 1995;47:331–85

---

## Week 10 — Wake-up prediction, and saving results to JSON

**Goal:** predict minutes-to-wake after an infusion stops, and save any simulation to a file a web page can read later.

**New ideas:** returning `None` as a meaningful answer; replaying data onto a new object; the `json` module; why NumPy arrays need `.tolist()`.

**Read first:** [Python `json` module](https://docs.python.org/3/library/json.html) · [`pathlib`](https://docs.python.org/3/library/pathlib.html)

### The science: context-sensitive half-time

A drug's elimination half-life doesn't tell you how long it takes to wear off after an infusion. Hughes and colleagues (1992) showed that the time for the plasma concentration to halve after stopping depends on how long the infusion ran, which they named the *context-sensitive half-time*. A long infusion fills the peripheral compartments. When you stop, they flow back into the plasma and slow the fall. Your code will show this with no half-life formula anywhere in it.

### The big picture

Two short jobs that both reuse what you have:

```
wake.py     old Simulation's schedule ──replay──► longer Simulation + "pump off" ──► scan Ce ──► minutes to wake
export.py   a finished Simulation ──► JSON text file (for the JavaScript part later)
```

### Learn it: searching, and returning `None` 🟢

If a search can come up empty, returning `None` is the honest answer, and the caller has to check for it. Empty `scratch.py`:

```python
def first_below(times, values, limit, after):
    for t, v in zip(times, values):
        if t > after and v < limit:
            return t
    return None


times = [0, 1, 2, 3, 4]
fuel = [50, 40, 30, 20, 10]

print(first_below(times, fuel, 25, after=0))
print(first_below(times, fuel, 5, after=0))

answer = first_below(times, fuel, 5, after=0)
if answer is None:
    print("never ran low")
```

```text
3
None
never ran low
```

`return` leaves the function as soon as it's reached, so the loop stops at the first match. If the loop finishes without a match, the final `return None` runs.

### Learn it: JSON 🟢

JSON is a plain-text format for numbers, text, lists and dictionaries, and almost every language can read it. It's how Python will hand data to JavaScript in Week 30. Empty `scratch.py`:

```python
import json
from pathlib import Path

import numpy as np

data = {"name": "Rex", "ages": [1, 2, 3], "good": True, "owner": None}
print(json.dumps(data))

heights = np.array([1.5, 2.5])
try:
    json.dumps({"heights": heights})
except TypeError as err:
    print("Problem:", err)
print(json.dumps({"heights": heights.tolist()}))

path = Path("scratch_output/pets.json")
path.parent.mkdir(parents=True, exist_ok=True)
with open(path, "w") as f:
    json.dump(data, f)
with open(path) as f:
    print(json.load(f)["ages"])
```

```text
{"name": "Rex", "ages": [1, 2, 3], "good": true, "owner": null}
Problem: Object of type ndarray is not JSON serializable
{"heights": [1.5, 2.5]}
[1, 2, 3]
```

- `json.dumps` gives text, and `json.dump` writes to a file. `json.load` reads a file back.
- Python's `True` and `None` become JSON's `true` and `null`.
- **JSON can't save a NumPy array directly,** so call `.tolist()` first.
- `path.parent.mkdir(parents=True, exist_ok=True)` makes the folder if it's missing, and doesn't complain if it exists.

Delete the `scratch_output` folder when you're done.

### Build it: `wake.py` 🔴

Create `tci/wake.py`, importing `Simulation`. Write `time_to_wake(old_sim, stop_time, wake_threshold, extra_minutes=180)`:

1. Make a new `Simulation` with the same drug and `steps_per_min`, and with `t_end = stop_time + extra_minutes`.
2. Replay every event from `old_sim.schedule` onto it, using the matching method.
3. Switch the pump off at `stop_time`, and run it.
4. Find the first moment **after** `stop_time` when Ce is below the threshold, and return how many minutes after stopping that was. If it never happens, return `None`.

<details>
<summary><b>Hint</b></summary>

The event must be added last, so that it overrides anything at that same time: `new_sim.rate(stop_time, 0)`. Then walk through `zip(new_sim.t, new_sim.ce)`, like `first_below`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
from engine import Simulation


def time_to_wake(old_sim, stop_time, wake_threshold, extra_minutes=180):
    """Replay old_sim's schedule, switch everything off at stop_time,
    and return minutes from stop until Ce < threshold (or None)."""
    new_sim = Simulation(old_sim.drug, t_end=stop_time + extra_minutes,
                         steps_per_min=old_sim.steps_per_min)
    for at, kind, value in old_sim.schedule:
        if kind == "bolus":
            new_sim.bolus(at, value)
        else:
            new_sim.rate(at, value)
    new_sim.rate(stop_time, 0)
    new_sim.run()
    for t, ce in zip(new_sim.t, new_sim.ce):
        if t > stop_time and ce < wake_threshold:
            return t - stop_time
    return None   # never woke inside the window


```

</details>

### Check it

Add this at the bottom of `wake.py`:

```python
if __name__ == "__main__":
    from patient import Patient
    from pk_models import marsh_drug
    from dosing import read_dose_table, apply_rows, apply_roberts
    from checks import check

    patient = Patient(40, 70, 170, "M")
    for minutes, expected in [(5, 10.7), (120, 30.8)]:
        sim = Simulation(marsh_drug(patient), t_end=minutes)
        sim.bolus(0, 100)
        sim.rate(0, 10)
        check(f"wake after a {minutes}-min infusion", time_to_wake(sim, minutes, 1.2), expected, tol=0.2)

    manual = Simulation(marsh_drug(patient))
    apply_rows(manual, read_dose_table("cases/manual_propofol.csv"), patient)
    check("wake, your Week 5 regimen", time_to_wake(manual, 52, 1.2), 18.0, tol=0.2)

    roberts = Simulation(marsh_drug(patient))
    apply_roberts(roberts, patient.weight)
    check("wake, Roberts stopped at 52", time_to_wake(roberts, 52, 1.2), 14.0, tol=0.2)
```


### Build it: `export.py` 🔴

Create `tci/export.py`, and write `save_sim_json(sim, path, label="")`. It saves a dictionary with the keys `label`, `drug` (the drug's name), `conc_unit`, `t`, `cp` and `ce`, creating the folder if needed.

Add a check block that runs Roberts through 70 kg Marsh, saves it to `../web/data/roberts_70kg.json`, reads the file back, and checks the length of `t` is 361. Then open the file in your editor and look at it. That plain text is what JavaScript will read in Week 30.

<details>
<summary><b>Answer</b></summary>

```python
import json
from pathlib import Path


def save_sim_json(sim, path, label=""):
    data = {
        "label": label,
        "drug": sim.drug.name,
        "conc_unit": sim.drug.conc_unit,
        "t": sim.t.tolist(),
        "cp": sim.cp.tolist(),
        "ce": sim.ce.tolist(),
    }
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    from patient import Patient
    from pk_models import marsh_drug
    from engine import Simulation
    from dosing import apply_roberts
    from checks import check

    patient = Patient(40, 70, 170, "M")
    sim = Simulation(marsh_drug(patient))
    apply_roberts(sim, patient.weight)
    sim.run()
    save_sim_json(sim, "../web/data/roberts_70kg.json", label="Roberts, 70 kg, Marsh")
    with open("../web/data/roberts_70kg.json") as f:
        back = json.load(f)
    check("saved time points", len(back["t"]), 361, tol=0)
    check("saved drug name", back["drug"], "Propofol (Marsh)")
```

</details>


Commit, then write a `DEVLOG.md` entry.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `time_to_wake` returns `None` | The threshold is never reached within `extra_minutes`. Make it longer, or check the threshold's units. |
| The answer is about 50 min too big | You returned `t[i]` instead of `t[i] - stop_time`. |
| `TypeError: Object of type ndarray is not JSON serializable` | Add `.tolist()` to each array before saving. |

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

Now your own regimen from Week 5 (Marsh, Patient A, infusion off at 52 min, threshold 1.2 µg/mL): **18.0 min** to wake, against **14.0 min** for Roberts stopped at the same time. The extra ~0.5 µg/mL you ran during the case costs about 4 minutes at the end. (`time_to_wake` replays a single drug's schedule; for a regimen from a dose table, build the `Simulation` with `apply_rows` first, then pass it in.)

**References:** Hughes MA, Glass PSA, Jacobs JR. Context-sensitive half-time in multicompartment pharmacokinetic models for intravenous anesthetic drugs. *Anesthesiology* 1992;76:334–41 · Bailey JM. Context-sensitive half-times: what are they and how valuable are they in anaesthesiology? *Clin Pharmacokinet* 2002;41:793–9

---

## Week 11A — A real TCI controller: the fast step

**Goal:** replace `solve_ivp` with one fast matrix step, proved identical to your Week 3 engine.

**New ideas:** *superposition* (PK is linear, so results can be added); building a matrix by experiment; NumPy's `@` operator.

**Read first:** [NumPy: matrix multiplication with `@`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)

### The science: how a TCI pump thinks

Every 10 seconds the pump asks one question: *what single rate, run for the next 10 seconds, gets me to the target?*

- **Plasma targeting:** choose the rate that makes **Cp** equal the target at the end of the next 10 s. Simple, and Cp never overshoots, but Ce lags behind for a long time.
- **Effect-site targeting** (what modern pumps default to for propofol): choose the rate so that, if the pump then stopped, the **peak future Ce** would land exactly on the target. To push Ce up fast it runs at full speed briefly. Plasma overshoots on purpose, but Ce never does.

The pump also has a **maximum rate** (for example 1200 mL/h of 10 mg/mL propofol = 200 mg/min). Those first seconds at full speed *are* the "bolus" a TCI pump gives.

**Where this came from.** Shafer and Gregg (1992) published the algorithms for reaching and holding a stable effect-site concentration with a computer-controlled pump. First-generation commercial systems used the Diprifusor module with the Marsh model. They could only target plasma, were limited to pre-filled glass syringes of Diprivan, and later added effect-site display. Today's open systems can target either site, with a choice of models.

Your Week 3 engine calls `solve_ivp` every step, which is far too slow for 360 decisions an hour, each looking 20 minutes ahead. But PK is **linear**. So the state after one 10-second step is always:

```text
next_state = E @ state + F × rate        (state = [A1, A2, A3, Ce])
```

`E` (4×4) and `F` (4 numbers) depend only on the drug and the step length. You can build them **by experiment** with your own `deriv()`: start with 1 unit in compartment 1 and nothing else, step 10 s, and the result is column 0 of `E`; repeat for each compartment. Then start empty with rate = 1, and the result is `F`. After that, every step is one matrix multiply, thousands of times faster.

### The big picture

A real TCI pump is a **control loop**. This lesson builds the fast step it needs, and the next builds the loop:

```
every 10 seconds:
    1. predict: "where is the patient heading if I switch the pump off now?"
    2. decide:  "what rate for the next 10 s gets me to the target?"
    3. act:     run that rate for 10 s, then repeat
```

### Learn it: superposition and matrices, with two water tanks 🟢

Here are two tanks. Each step, 10% of tank A flows to tank B, and 20% of tank B flows out of the system. The rule is linear, so the result from any starting state is a sum of the results from each tank alone. That means one matrix can stand in for the whole rule. Empty `scratch.py`:

```python
import numpy as np


def slow_step(state):
    a, b = state
    return [a * 0.9, b * 0.8 + a * 0.1]


# Build the matrix by experiment: 1 unit in each tank, one at a time
E = np.zeros((2, 2))
for j in range(2):
    start = [0.0, 0.0]
    start[j] = 1.0
    E[:, j] = slow_step(start)
print(E)

x = np.array([100.0, 50.0])
print(slow_step(x))
print(E @ x)

for _ in range(3):
    x = E @ x
print(x.round(2))
```

```text
[[0.9 0. ]
 [0.1 0.8]]
[np.float64(90.0), np.float64(50.0)]
[90. 50.]
[72.9 47.3]
```

- `E[:, j] = ...` fills column `j`, using the slice from Week 3.
- `E @ x` multiplies a matrix by an array. It gives exactly the same answer as the slow function.
- Column 0 of `E` is what one unit in tank A becomes after a step. Column 1 is what one unit in tank B becomes. That's the entire trick, and a thousand steps now cost a thousand multiplications.
- `for _ in range(3):` uses `_` as a name for a loop variable you don't need.

### Build it: `step_matrices` 🔴

Create `tci/tci.py`. Set `UPDATE_MIN = 10 / 60`, because the pump re-decides every 10 seconds. Write `step_matrices(drug, dt=UPDATE_MIN)`, which returns `E` and `F` so that `next = E @ state + F * rate`:

1. `E` starts as `np.zeros((4, 4))`. For each compartment `j`, start with 1 unit in it and nothing elsewhere, run `solve_ivp(deriv, (0, dt), start, args=(drug, 0.0), rtol=1e-10, atol=1e-12)`, and put the final state in column `j`.
2. `F` is the final state after `dt`, starting from all zeros, with the rate set to 1.0.

The tight tolerances matter, because this matrix gets multiplied thousands of times, so small errors would add up.

<details>
<summary><b>Hint</b></summary>

It's the tanks loop, with `solve_ivp` in place of `slow_step`. Remember how to get the final state: `sol.y[:, -1]`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
import numpy as np
from scipy.integrate import solve_ivp

from engine import deriv

UPDATE_MIN = 10 / 60          # the pump re-decides every 10 seconds


def step_matrices(drug, dt=UPDATE_MIN):
    """Build E and F by experiment, so that next = E @ state + F * rate."""
    E = np.zeros((4, 4))
    for j in range(4):
        start = [0.0, 0.0, 0.0, 0.0]
        start[j] = 1.0
        sol = solve_ivp(deriv, (0, dt), start, args=(drug, 0.0), rtol=1e-10, atol=1e-12)
        E[:, j] = sol.y[:, -1]
    sol = solve_ivp(deriv, (0, dt), [0.0, 0.0, 0.0, 0.0], args=(drug, 1.0), rtol=1e-10, atol=1e-12)
    F = sol.y[:, -1]
    return E, F


```

</details>

### Check it

Add this at the bottom of `tci.py`. It compares your fast step with your Week 3 engine: 100 mg in A1, stepped 6 times with `E`, should match `Simulation` after 1 minute.

```python
if __name__ == "__main__":
    from patient import Patient
    from pk_models import marsh_drug, eleveld_drug_reference
    from engine import Simulation
    from checks import check

    # 1. the fast step must match the Week 3 engine
    marsh = marsh_drug(Patient(40, 70, 170, "M"))
    E, F = step_matrices(marsh)
    x = np.array([100.0, 0.0, 0.0, 0.0])
    for _ in range(6):                     # six 10-second steps = 1 minute
        x = E @ x
    slow = Simulation(marsh, t_end=1)
    slow.bolus(0, 100)
    slow.run()
    check("fast step: Cp at 1 min", x[0] / marsh.V1, slow.cp[-1], tol=0.001)
    check("fast step: Ce at 1 min", x[3], slow.ce[-1], tol=0.001)
```


Commit.

### Checkpoint

100 mg in A1 stepped 6 times, Marsh, Patient A: Cp **4.785** and Ce **1.249**, the same as your `Simulation` at 1 minute.

**References:** Shafer SL, Gregg KM. Algorithms to rapidly achieve and maintain stable drug concentrations at the site of drug effect with a computer-controlled infusion pump. *J Pharmacokinet Biopharm* 1992;20:147–69 · Absalom AR et al. *Br J Anaesth* 2009;103:26–37

---

## Week 11B — A real TCI controller: the decision

**Goal:** simulate a TCI pump in plasma and effect-site modes, re-deciding every 10 seconds.

**New ideas:** a *control loop* (measure, decide, act, repeat); bisection.

**Read first:** [Bisection method (plain-language overview)](https://en.wikipedia.org/wiki/Bisection_method)

### The science: why plasma overshoots on purpose

In plasma mode, the pump brings Cp to the target and holds it there, so Ce slowly catches up, which takes a long time. In effect-site mode, it deliberately overshoots Cp, because a higher plasma concentration pushes drug into the effect site faster. Your checkpoint shows how big this is. With Eleveld at a target of 3 µg/mL, plasma mode reaches 99% of target in over half an hour, while effect-site mode gets there in 3 minutes, with Cp peaking above 16 µg/mL.

A patient with poor cardiac reserve might tolerate that plasma peak badly, and Su's 2022 hemodynamic data suggest why: propofol's effects on stroke volume start at a low concentration. That's the tradeoff behind choosing a mode and a target.

### The big picture

```
run_tci() ──► arrays t, cp, ce, rate (one value per 10 s)
```

### Learn it: bisection 🟢

Bisection finds the input that gives a desired output, if the function only ever rises. You keep a low guess and a high guess, test the middle, and throw away the half that can't hold the answer. Each pass halves the range, so 40 passes narrow it by a factor of about a trillion. Empty `scratch.py`:

```python
def speed_for_distance(target, max_speed):
    """What speed covers `target` km in 2 hours, if drag takes away 10% ?"""
    def distance(speed):
        return speed * 2 * 0.9

    if distance(0) >= target:
        return 0.0
    if distance(max_speed) < target:
        return max_speed

    low, high = 0.0, max_speed
    for _ in range(40):
        mid = (low + high) / 2
        if distance(mid) < target:
            low = mid
        else:
            high = mid
    return (low + high) / 2


print(round(speed_for_distance(90, 120), 4))
print(speed_for_distance(500, 120))
print(speed_for_distance(0, 120))
```

```text
50.0
120
0.0
```

Handle the two easy cases first: if you're already there, return 0. If even the maximum can't reach it, return the maximum. Only then do the search.

### Build it: `future_ce` 🟡

In `tci.py`, write `future_ce(E, x, steps)`. It returns an array of Ce for the next `steps` updates if the pump is **off**. Repeat `steps` times: set `x = E @ x`, and store `x[3]`.

<details>
<summary><b>Answer</b></summary>

```python
def future_ce(E, x, steps):
    """Ce for the next `steps` updates if the pump is OFF from now on."""
    out = np.zeros(steps)
    for i in range(steps):
        x = E @ x
        out[i] = x[3]
    return out
```

</details>

### Build it: `run_tci` 🔴

Here's the setup and the skeleton of the plan. You write all of it:

```python
def run_tci(drug, targets, minutes, mode="effect", max_rate=200.0, horizon_min=20.0):
    """Simulate a TCI pump.
    targets  : [(time_min, target), ...], e.g. [(0, 3.0), (20, 2.0)]
    max_rate : pump limit in the drug's dose unit per minute
    Returns arrays t, cp, ce, rate (one value per 10-second update)."""
```

**Before the loop:** build `E` and `F`. Set `n_h = round(horizon_min / UPDATE_MIN)`. `unit = future_ce(E, F.copy(), n_h)` is the Ce response to rate 1 for one step, then off. Set `n = round(minutes / UPDATE_MIN)`, make `x = np.zeros(4)`, and make four zero arrays. `target` starts at `targets[0][1]`.

**On each pass,** with `now = i * UPDATE_MIN`:

1. If any `(time, value)` in `targets` has `time` equal to `now` (within half a step), switch `target`.
2. **Decide `r`.**
   - **Plasma mode.** `free_cp = (E @ x)[0] / drug.V1` is Cp after 10 s with the pump off. `unit_cp = F[0] / drug.V1` is the extra Cp from rate 1 for 10 s. Solve `free_cp + r * unit_cp == target` for `r`.
   - **Effect mode.** `free = future_ce(E, E @ x, n_h)` is Ce ahead with the pump off after this step. If `free.max()` is already at the target, `r = 0`. If `(free + max_rate * unit).max()` can't reach it, `r = max_rate`. Otherwise, bisect `r` between 0 and `max_rate` until `(free + r * unit).max()` equals the target.
3. Clamp it: `r = min(max(r, 0.0), max_rate)`, since a pump can't run backward or past its limit.
4. Record `t[i], cp[i], ce[i], rate[i]`. Cp is `x[0] / drug.V1`, and Ce is `x[3]`.
5. Advance: `x = E @ x + F * r`.

**After the loop,** return `t, cp, ce, rate`.

<details>
<summary><b>Hint</b></summary>

`(free + r * unit).max()` works because of superposition: the future Ce is what happens with the pump off, plus `r` times what one unit of rate does. Bisection with 40 passes is plenty. If a target change never happens, check `abs(when - now) < UPDATE_MIN / 2`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
def run_tci(drug, targets, minutes, mode="effect", max_rate=200.0, horizon_min=20.0):
    """Simulate a TCI pump.
    targets  : [(time_min, target), ...], e.g. [(0, 3.0), (20, 2.0)]
    max_rate : pump limit in the drug's dose unit per minute
    Returns arrays t, cp, ce, rate (one value per 10-second update)."""
    E, F = step_matrices(drug)
    n_h = round(horizon_min / UPDATE_MIN)
    unit = future_ce(E, F.copy(), n_h)      # Ce response to rate 1 for one step, then off
    n = round(minutes / UPDATE_MIN)
    x = np.zeros(4)
    t, cp, ce, rate = (np.zeros(n) for _ in range(4))
    target = targets[0][1]

    for i in range(n):
        now = i * UPDATE_MIN
        for when, value in targets:
            if abs(when - now) < UPDATE_MIN / 2:
                target = value

        if mode == "plasma":
            free_cp = (E @ x)[0] / drug.V1          # Cp after 10 s with the pump off
            unit_cp = F[0] / drug.V1                # extra Cp from rate 1 for 10 s
            r = (target - free_cp) / unit_cp
        else:
            free = future_ce(E, E @ x, n_h)         # Ce ahead, pump off after this step
            if free.max() >= target:
                r = 0.0
            elif (free + max_rate * unit).max() < target:
                r = max_rate
            else:
                low, high = 0.0, max_rate
                for _ in range(40):
                    r = (low + high) / 2
                    if (free + r * unit).max() < target:
                        low = r
                    else:
                        high = r
                r = (low + high) / 2

        r = min(max(r, 0.0), max_rate)              # a pump can't run backwards or past its limit
        t[i], cp[i], ce[i], rate[i] = now, x[0] / drug.V1, x[3], r
        x = E @ x + F * r
    return t, cp, ce, rate


```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`step_matrices`**: for each of the 4 state variables, start with 1 unit in *only* that one, run 10 seconds with the pump off, and store the result as one column of `E`. Then start empty with the pump at rate 1 for 10 seconds: that result is `F`. Because PK is linear, any state and any rate can now be stepped with `E @ x + F * r`.
- **`future_ce(E, x, steps)`** repeats `x = E @ x` and records Ce each time: the future with the pump off.
- **`run_tci`**:
  - `unit` is "what one unit of rate for one step does to future Ce". It never changes, so it's computed once.
  - Each loop: check for a target change, then choose `r` (plasma: one line of algebra; effect-site: bisection), clamp it between 0 and the pump's maximum, record, and step.
- **`printable_schedule`** counts how long the pump ran flat out at the start (that's the bolus), then, for each window of `interval_min` minutes, adds up the drug delivered and divides by the window length.
- **`schedule_table`** turns the result into a pandas table with friendly columns, ready for `.to_excel`.

</details>

### Check it

Add these lines inside the check block in `tci.py`:

```python

    # 2. both targeting modes, Eleveld reference adult, target 3.0
    eleveld = eleveld_drug_reference()
    for mode, peak_cp, reach in [("plasma", 3.00, 31.7), ("effect", 16.7, 2.8)]:
        t, cp, ce, rate = run_tci(eleveld, [(0, 3.0)], 60, mode=mode)
        first = t[np.argmax(ce >= 2.97)]               # first time Ce reaches 99% of target
        check(f"{mode}: peak Cp", cp.max(), peak_cp, tol=0.1)
        check(f"{mode}: Ce reaches 2.97 at (min)", first, reach, tol=0.2)
        check(f"{mode}: Ce never overshoots", ce.max(), 3.0, tol=0.01)
```


### See it 🔴

Plot both modes' Ce and Cp with `plot_runs`, then the pump rate. Then try `targets=[(0, 3.0), (20, 2.0)]`, and watch the pump stop, then resume. Try the same on Marsh for Patient A. Plasma mode should take about 18 minutes to reach 99%, and effect mode about 4, with Cp peaking at only about 7.5. Marsh's larger V1 needs a bigger dose but less plasma overshoot, which is the same difference you saw in Week 6.

Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  fast step` | `step_matrices`: each result must go into column `j` (`E[:, j]`), not row `j`. |
| Effect-site mode overshoots | The horizon is too short for the drug, or you compared Cp instead of Ce in the bisection. |
| A rate is negative | The clamp line `min(max(r, 0.0), max_rate)` is missing. |
| The pump never reacts to a target change | The time comparison. `now` is a decimal, so compare with a tolerance (`abs(now - when) < UPDATE_MIN / 2`), not `==`. |
| Every rate equals `max_rate` | `unit` was built from `E` instead of `F`, so it's all zeros. |
| The bisection loop never ends | Use a fixed number of halvings (`for _ in range(40)`), not `while`. |
| Schedule rates far too high in the first window | You didn't subtract the bolus from the first window. |

### Checkpoint

Propofol, Eleveld reference adult (35 yo, 70 kg, 170 cm, M), target 3.0 µg/mL, max rate 200 mg/min, 10-second updates, 20-minute horizon:

| | plasma targeting | effect-site targeting |
|---|---|---|
| pump at maximum rate | never | first **40 s** (133 mg) |
| peak Cp | **3.00** | **16.7** |
| peak Ce | 3.00 | **3.00** (no overshoot) |
| Ce reaches 2.97 (99%) | **31.7 min** | **2.8 min** |
| drug given, first 5 min | 84.2 mg | 159.1 mg |
| drug given, 60 min | 593.1 mg | 640.8 mg |
| rate at 60 min | 8.06 mg/min | 7.97 mg/min |

- Target change 3.0 → 2.0 at 20 min (effect-site): the pump stops for **360 s**, and Ce reaches 2.02 at **26.2 min**.
- Marsh, Patient A, target 3.0: plasma mode reaches 99% Ce at **18.0 min**. Effect-site mode gets there at **3.8 min**, with Cp peaking at **7.5**.

**References:** Shafer SL, Gregg KM. *J Pharmacokinet Biopharm* 1992;20:147–69 · Absalom AR et al. *Br J Anaesth* 2009;103:26–37 · Eleveld DJ et al. *Br J Anaesth* 2018;120:942–59, corrigendum 121:519 · Su H et al. *Br J Anaesth* 2022;128:806–16

---

## Week 11C — A printable schedule

**Goal:** condense the second-by-second pump record into a printable schedule, at an interval the user chooses, and export it to Excel.

**New ideas:** boolean masks on NumPy arrays; pandas `DataFrame`; `.to_excel`.

**Read first:** [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · [`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)

### The science: a TCI pump without a TCI pump

Where TCI isn't available, a printed manual schedule is the fallback. The longer the interval between rate changes, the further the real concentration drifts from the target. This lesson lets you measure that drift. It's the same idea as Roberts's 10-8-6, which is a printed schedule with very long intervals.

> **Teaching only.** A printed schedule assumes the model is right and the patient is typical. Don't treat these as dosing recommendations.

### The big picture

```
run_tci() ──► t, rate ──► printable_schedule(rate, interval) ──► schedule_table() ──► Excel
                                       │
                                       └── replay through Simulation: how far does Ce drift?
```

### Learn it: masks and pandas 🟢

Empty `scratch.py`:

```python
import numpy as np
import pandas as pd

hours = np.array([0, 1, 2, 3, 4, 5])
rain = np.array([1.0, 0.0, 2.0, 3.0, 0.0, 4.0])

morning = (hours >= 1) & (hours < 4)
print(morning)
print(rain[morning])
print(rain[morning].sum())

table = pd.DataFrame([
    {"day": "Mon", "rain": 3.0},
    {"day": "Tue", "rain": 0.5},
])
print(table)
print(list(table.columns), len(table))
table.to_excel("scratch_rain.xlsx", index=False)
print(pd.read_excel("scratch_rain.xlsx")["rain"].sum())
```

```text
[False  True  True  True False False]
[0. 2. 3.]
5.0
['day', 'rain'] 2
3.5
```

- `(hours >= 1) & (hours < 4)` gives a True/False array, called a *mask*. Use `&`, not `and`, and keep the brackets.
- `rain[morning]` keeps only the matching values.
- A `DataFrame` is a table, and a list of dictionaries is the easiest way to make one. It also prints a neat table, which is shown above with the middle line.
- `.to_excel` needs `openpyxl`, which you installed in Week 0.

Delete `scratch_rain.xlsx`.

### Build it: `printable_schedule` 🟡

Add `import pandas as pd` to the top of `tci.py`. Add this function above the `if __name__` block. Here's the start, which works out the bolus: all the drug given while the pump ran flat out at the very beginning.

```python
def printable_schedule(t, rate, interval_min, max_rate):
    """Condense the 10-second record into: one bolus + one rate per interval.
    Bolus = drug given while the pump ran flat out at the start.
    Each interval's rate = drug delivered in that interval / interval length."""
    dt = UPDATE_MIN
    i = 0
    while i < len(rate) and rate[i] >= max_rate - 1e-9:
        i += 1
    bolus = rate[:i].sum() * dt
    rows = []
    edges = np.arange(0, t[-1] + dt + 1e-9, interval_min)
    for start, end in zip(edges, edges[1:]):
        in_window = (t >= start - 1e-9) & (t < end - 1e-9)
        # your lines here
    return bolus, rows
```

Inside the loop:

1. `delivered` is the drug given in this window: the rates in the window, summed, times `dt`.
2. In the first window, subtract the bolus, because it's printed on its own row.
3. Append `(start, end, delivered / (end - start))` to `rows`.

`zip(edges, edges[1:])` pairs each edge with the next: `(0, 5), (5, 10), ...`. The `1e-9` terms guard against rounding errors in decimals.

<details>
<summary><b>Answer</b></summary>

```python
import pandas as pd
```

```python
def printable_schedule(t, rate, interval_min, max_rate):
    """Condense the 10-second record into: one bolus + one rate per interval.
    Bolus = drug given while the pump ran flat out at the start.
    Each interval's rate = drug delivered in that interval / interval length."""
    dt = UPDATE_MIN
    i = 0
    while i < len(rate) and rate[i] >= max_rate - 1e-9:
        i += 1
    bolus = rate[:i].sum() * dt
    rows = []
    edges = np.arange(0, t[-1] + dt + 1e-9, interval_min)
    for start, end in zip(edges, edges[1:]):
        in_window = (t >= start - 1e-9) & (t < end - 1e-9)
        delivered = rate[in_window].sum() * dt
        if start == 0:
            delivered -= bolus
        rows.append((start, end, delivered / (end - start)))
    return bolus, rows


```

</details>

### Build it: `schedule_table` 🔴

Write `schedule_table(bolus, rows, weight_kg, dose_unit="mg")`, which returns a `DataFrame`. Its first row is `{"from_min": 0, "to_min": 0, "action": "bolus 133 mg"}`, with the bolus rounded. Each schedule row then has `from_min`, `to_min`, `action` (`"infusion"`), and these:

- `mcg_kg_min`: this rate in mcg/kg/min, rounded to 1 decimal. It's the number a person programs into a pump, so it comes first.
- `mg_kg_h`: the same rate in mg/kg/h, rounded to 2 decimals.
- `per_min`, rounded to 2 decimals, and `per_min_units`, like `"mg/min"`.

Be careful if `dose_unit` is `"mcg"`: then a rate is already in mcg.

Also write `replay_schedule(drug, bolus, rows, minutes)`. It makes a `Simulation` with `steps_per_min=6`, gives the bolus at 0, sets each row's rate at its start, runs it, and returns the simulation. Add `from engine import Simulation` at the top of the file, next to the other import from `engine`.

<details>
<summary><b>Hint</b></summary>

Start with `to_mcg = 1000.0 if dose_unit == "mg" else 1.0`. Then mcg/kg/min is `r * to_mcg / weight_kg`, and mg/kg/h is `r * to_mcg / 1000 * 60 / weight_kg`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
from engine import Simulation, deriv
```

```python
def schedule_table(bolus, rows, weight_kg, dose_unit="mg"):
    to_mcg = 1000.0 if dose_unit == "mg" else 1.0
    data = [{"from_min": 0, "to_min": 0, "action": f"bolus {round(bolus)} {dose_unit}"}]
    for start, end, r in rows:
        data.append({"from_min": start, "to_min": end, "action": "infusion",
                     "mcg_kg_min": round(r * to_mcg / weight_kg, 1),
                     "mg_kg_h": round(r * to_mcg / 1000 * 60 / weight_kg, 2),
                     "per_min": round(r, 2), "per_min_units": f"{dose_unit}/min"})
    return pd.DataFrame(data)


def replay_schedule(drug, bolus, rows, minutes):
    """Run the printed schedule through the Week 3 engine, to see how far Ce drifts."""
    sim = Simulation(drug, t_end=minutes, steps_per_min=6)
    sim.bolus(0, bolus)
    for start, end, r in rows:
        sim.rate(start, r)
    return sim.run()


```

</details>

### Check it

Add these lines inside the check block in `tci.py`. They use `t` and `rate` from the effect-site run, which was the last one in the loop.

```python

    # 3. printable schedule from the effect-site run (the last one in the loop)
    bolus, rows = printable_schedule(t, rate, 5, 200.0)
    check("schedule bolus (mg)", bolus, 133.3, tol=0.2)
    check("first 5-min rate (mg/min)", rows[0][2], 5.15, tol=0.05)
    table = schedule_table(bolus, rows, 70, "mg")
    print(table.head(3))
    table.to_excel("tci_schedule_teaching.xlsx", index=False)

    # 4. replay it: longer intervals drift further from the target
    for interval, low, high in [(5, 2.91, 3.02), (15, 2.84, 3.31)]:
        b, r = printable_schedule(t, rate, interval, 200.0)
        replay = replay_schedule(eleveld, b, r, 60)
        after5 = replay.ce[replay.t >= 5]
        check(f"replay every {interval} min: lowest Ce after 5 min", after5.min(), low, tol=0.03)
        check(f"replay every {interval} min: highest Ce after 5 min", after5.max(), high, tol=0.03)
```


Open `tci_schedule_teaching.xlsx`. Overlay the replayed Ce on the TCI Ce with `plot_runs`, at intervals of 5 and 15 minutes, to see the drift. Commit.

### Checkpoint

Printable schedule from the effect-site run: bolus **133.3 mg**.

- **5-minute intervals:** rates 5.15, 10.31, 9.71, 9.27, 8.95, 8.71 mg/min, and so on. Replayed, Ce stays between **2.91 and 3.02** after minute 5.
- **15-minute intervals:** rates 8.39, 8.98, 8.38, 8.08 mg/min. Replayed, Ce wanders between **2.84 and 3.31**.

Longer intervals drift further from the target, which is what the lesson set out to show.

---

## Week 12A — Streamlit basics, and the dose-table tab

**Goal:** a web page where you enter a patient and a dose table, and see every drug's curve, with no code editing.

**New ideas:** Streamlit's *rerun* model; widgets; `st.data_editor`; `st.cache_data`; showing errors on the page.

**Read first:** [Streamlit: Main concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts) · [`st.data_editor`](https://docs.streamlit.io/develop/api-reference/data/st.data_editor) · [Caching](https://docs.streamlit.io/develop/concepts/architecture/caching)

### The science: what you're imitating

StanpumpR, by Steven Shafer, is a free web tool for exactly this: enter a patient and a dose table, and see predicted concentrations. Yours is a simple version of it. Look at the real one at [stanpumpr.io](https://stanpumpr.io) before you start. Remember that it's a tool for teaching and thinking, and yours is too.

### The big picture

`app.py` is a **front end only**. Every number on the screen comes from a function you wrote and checked in Weeks 1–11.

```
sidebar widgets ──► Patient
dose table editor ──► rows ──► Case(...).run() ──► plot_case, percent_meac, p_response_laryngoscopy
TCI inputs ──► run_tci(...) ──► printable_schedule(...) ──► schedule_table(...) ──► download button
```

Streamlit **reruns the whole file from top to bottom every time anything changes**. Widgets remember their values; ordinary variables don't. That one fact explains almost every Streamlit surprise.

```bash
pip install "streamlit>=1.37"
streamlit run app.py             # opens http://localhost:8501
```

### The one rule

`app.py` contains **no pharmacology**. It reads widgets, calls functions you already wrote and tested, and draws what comes back. If you catch yourself writing a formula in `app.py`, move it into a Weeks 5–11 file and check it there.

### Learn it: the rerun model 🟢

Create `tci/scratch_app.py`:

```python
import streamlit as st

st.title("Tip calculator")
st.write("The script just ran from the top.")

bill = st.number_input("Bill", min_value=0.0, value=40.0)
percent = st.slider("Tip %", 0, 30, 20)
share = st.radio("Split between", [1, 2, 4], horizontal=True)

tip = bill * percent / 100
st.write(f"Each person pays {(bill + tip) / share:.2f}")

if st.button("Say hello"):
    st.write("Hello!")

clicks = 0
clicks += 1
st.write(f"Ordinary variable: {clicks}")

if "count" not in st.session_state:
    st.session_state.count = 0
st.session_state.count += 1
st.write(f"Session state: {st.session_state.count}")
```

Run it with this, not with `python`:

```bash
streamlit run scratch_app.py
```

A browser tab opens at `http://localhost:8501`. Move the slider, and press the button a few times.

**Streamlit reruns the whole file from top to bottom every time anything changes.** That's the one fact that explains almost every Streamlit surprise. Watch the bottom two lines. The ordinary variable says 1 forever, because it's recreated on each rerun, while the session-state counter keeps climbing. Also notice that "Hello!" disappears the next time you move the slider: a button is only true for the single rerun it caused.

Press Ctrl+C in the terminal to stop it.

### Learn it: tabs, columns, the data editor and caching 🟢

Replace `scratch_app.py` with this:

```python
import pandas as pd
import streamlit as st

with st.sidebar:
    name = st.text_input("Your name", "Ana")

tab1, tab2 = st.tabs(["Table", "Columns"])

with tab1:
    start = pd.DataFrame([{"item": "tea", "cost": 3.0}, {"item": "cake", "cost": 5.0}])
    edited = st.data_editor(start, num_rows="dynamic", key="menu")
    st.write("Total:", edited["cost"].sum())

with tab2:
    left, right = st.columns(2)
    left.metric("Name", name)
    right.write("Same line as the metric")


@st.cache_data
def slow_square(x):
    import time
    time.sleep(2)
    return x * x


st.write(slow_square(st.slider("Pick a number", 1, 5, 2)))
```

Add a row to the table. Move the slider to a new number, and it takes 2 seconds. Move it back to one you've used, and it's instant, because `@st.cache_data` remembered the answer for those inputs. Inputs to a cached function must be plain values that can be compared, which is why next you'll pass in plain numbers and tuples rather than a `Patient` object.

### Build it: the dose-table tab 🟡

Create `tci/app.py`. Here are the setup and the sidebar. `matplotlib.use("Agg")` must come before anything imports pyplot. It stops `plt.show()` in your plotting functions from trying to open a window from inside a web server.

```python
import matplotlib
matplotlib.use("Agg")

import io

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from case import Case
from patient import Patient
from pd_endpoints import percent_meac, remi_equivalent, p_response_laryngoscopy
from pk_models import DRUGS
from plotting import plot_case, plot_runs

UNITS = ["mg", "mcg", "mg/kg", "mcg/kg", "mg/min", "mg/h", "mg/kg/h",
         "mcg/min", "mcg/kg/min", "mcg/kg/h"]

st.set_page_config(page_title="TCI teaching simulator", layout="wide")
st.title("TCI teaching simulator")
st.caption("Teaching tool. Not for clinical use.")

with st.sidebar:
    st.header("Patient")
    age = st.number_input("Age (years)", min_value=1, max_value=100, value=40, step=1)
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=250.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=230.0, value=170.0)
    sex = st.radio("Sex", ["M", "F"], horizontal=True)
patient = Patient(int(age), float(weight), float(height), sex)
plt.close("all")     # the whole script reruns, so don't let old figures pile up

tab_case, tab_tci = st.tabs(["Dose table (manual)", "TCI (target)"])
```

Run it now. The sidebar and tabs should appear. Then write the first tab, inside `with tab_case:`:

1. **The table.** Start from a `DataFrame` with the rows of your Week 5 regimen, and show it with `st.data_editor(example, num_rows="dynamic", key="dose_table", column_config=...)`. In `column_config`, make `"drug"` a `st.column_config.SelectboxColumn("Drug", options=list(DRUGS), required=True)`, and `"units"` a selectbox of `UNITS`. Use `NumberColumn` for `time` and `amount`.
2. **Model pickers.** For each drug in use (`sorted(set(doses["drug"].dropna()))`), show a `st.selectbox` of `list(DRUGS[drug])`, and collect the answers in a `model_choice` dictionary.
3. **The time slider.** `st.slider("Simulate for (min)", 30, 720, 240, step=30)`.
4. **Rows.** Turn the table into the list of `(time, drug, amount, units)` tuples that `Case` expects, skipping rows with a missing value. `.dropna()` and `.itertuples(index=False)` help.
5. **Run it, with caching.** Above the tabs, write a function decorated with `@st.cache_data` that takes plain values (age, weight, height, sex, a tuple of rows, the model choices, `t_end`), and returns a finished `Case`.
6. **Errors.** Wrap the run in `try`/`except ValueError as err:`, and call `st.error(str(err))` instead of crashing. Your Week 5 and Week 8 messages appear here.
7. **Plot.** `fig, _ = plot_case(case)`, then `st.pyplot(fig)`. If propofol and at least one opioid are in the case, plot P(response) too, using `plot_runs`.

<details>
<summary><b>Hint</b></summary>

For step 4: `rows = [tuple(r) for r in doses[["time", "drug", "amount", "units"]].dropna().itertuples(index=False)]`. The time and amount may arrive as other number types, so convert with `float()` if you see an error. To check for an opioid, look at `sim.drug.meac` for each simulation in the finished case.

</details>
<details>
<summary><b>Answer</b></summary>

```python
import matplotlib
matplotlib.use("Agg")

import io

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from case import Case
from patient import Patient
from pd_endpoints import percent_meac, remi_equivalent, p_response_laryngoscopy
from pk_models import DRUGS
from plotting import plot_case, plot_runs

UNITS = ["mg", "mcg", "mg/kg", "mcg/kg", "mg/min", "mg/h", "mg/kg/h",
         "mcg/min", "mcg/kg/min", "mcg/kg/h"]

st.set_page_config(page_title="TCI teaching simulator", layout="wide")
st.title("TCI teaching simulator")
st.caption("Teaching tool. Not for clinical use.")

with st.sidebar:
    st.header("Patient")
    age = st.number_input("Age (years)", min_value=1, max_value=100, value=40, step=1)
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=250.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=230.0, value=170.0)
    sex = st.radio("Sex", ["M", "F"], horizontal=True)
patient = Patient(int(age), float(weight), float(height), sex)
plt.close("all")     # the whole script reruns, so don't let old figures pile up


@st.cache_data
def run_case(age, weight, height, sex, rows, model_choice, t_end):
    """Cached: inputs are plain values, so unchanged inputs don't recompute."""
    p = Patient(age, weight, height, sex)
    return Case(p, list(rows), model_choice=model_choice, t_end=t_end).run()


tab_case, tab_tci = st.tabs(["Dose table (manual)", "TCI (target)"])

# ---------- tab 1: the case ----------
with tab_case:
    example = pd.DataFrame([
        {"time": 0,  "drug": "propofol", "amount": 140.0, "units": "mg"},
        {"time": 0,  "drug": "propofol", "amount": 150.0, "units": "mcg/kg/min"},
        {"time": 10, "drug": "propofol", "amount": 120.0, "units": "mcg/kg/min"},
        {"time": 52, "drug": "propofol", "amount": 0.0,   "units": "mcg/kg/min"},
    ])
    doses = st.data_editor(
        example,
        num_rows="dynamic",            # lets the user add and delete rows
        key="dose_table",              # Streamlit keeps the edits under this key
        column_config={
            "time": st.column_config.NumberColumn("Time (min)", min_value=0, step=1),
            "drug": st.column_config.SelectboxColumn("Drug", options=list(DRUGS), required=True),
            "amount": st.column_config.NumberColumn("Amount", min_value=0.0),
            "units": st.column_config.SelectboxColumn("Units", options=UNITS, required=True),
        },
    )

    # one model picker per drug in use
    model_choice = {}
    for drug in sorted(set(doses["drug"].dropna())):
        model_choice[drug] = st.selectbox(f"{drug} model", list(DRUGS[drug]))

    t_end = st.slider("Simulate for (min)", 30, 720, 240, step=30)

    clean = doses[["time", "drug", "amount", "units"]].dropna()
    rows = tuple((float(r.time), r.drug, float(r.amount), r.units)
                 for r in clean.itertuples(index=False))

    try:
        case = run_case(int(age), float(weight), float(height), sex, rows, model_choice, t_end)
    except ValueError as err:
        st.error(str(err))
    else:
        fig, _ = plot_case(case)
        st.pyplot(fig)

        has_opioid = any(sim.drug.meac for sim in case.sims.values())
        if "propofol" in case.sims and has_opioid:
            t = case.sims["propofol"].t
            p = p_response_laryngoscopy(case.sims["propofol"].ce, remi_equivalent(case))
            fig2, _ = plot_runs([("P(response to laryngoscopy)", t, p)], ylabel="Probability")
            st.pyplot(fig2)
            fig3, _ = plot_runs([("% MEAC", t, percent_meac(case))], ylabel="% MEAC")
            st.pyplot(fig3)
```

</details>


### If something goes wrong

| What you see | Where to look |
|---|---|
| `ModuleNotFoundError: No module named 'streamlit'` | Your virtual environment isn't active, or Streamlit isn't installed in it. |
| `ImportError: cannot import name ...` | That function's name in the Weeks 1–11 file doesn't match the import line. |
| `DuplicateWidgetID` | Two widgets have the same label. Give one a `key="..."`. |
| A red error box from inside your code | Click it: the traceback names the file and line, which will be in one of your Weeks 1–11 files. Fix it there, then rerun that file's check block. |
| Edits to the table disappear | The `data_editor` is missing its `key`. |
| The page is slow on every click | The case isn't cached. Cache it with `@st.cache_data`, as in the lesson. |
| Numbers differ from earlier weeks | Run that week's file on its own (`python case.py`). If its checks pass, the difference is in how `app.py` builds the inputs. |

### Checkpoint

The default table reproduces your Week 5 Marsh curve (Ce 3.80 at 10 min, 3.20 at 52 min) for the default patient. Paste in the Week 8 case and get the same five panels. Misspell a unit in the table, and you should see your error message on the page, with no crash. Commit.

---

## Week 12B — The TCI tab

**Goal:** a second tab where you pick a drug, model, mode and target, watch the pump decide, and download a printable schedule as Excel.

**New ideas:** `st.line_chart`; `st.download_button`; writing Excel to memory with `io.BytesIO`.

**Read first:** [`st.download_button`](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)

### The science: effect-site versus plasma, seen live

Switch between the two modes and watch Cp overshoot appear and disappear. Try Schnider in plasma mode with a 70 kg patient and then a 120 kg patient: the initial dose barely changes, which is the fixed-V1 problem you read about. Then try Eleveld in effect-site mode at both weights. Now change the target. Engbers and Boveri's point becomes visible here: a Schnider induction target of 5 and an Eleveld induction target of 5 are not the same thing.

### The big picture

```
TCI inputs ──► run_tci(...) ──► printable_schedule(...) ──► schedule_table(...) ──► download button
```

### Learn it: a download from memory 🟢

A download button needs bytes, not a file on disk. `io.BytesIO` acts like a file that lives in memory. Empty `tci/scratch.py`:

```python
import io

import pandas as pd

table = pd.DataFrame([{"a": 1}, {"a": 2}])
buffer = io.BytesIO()
table.to_excel(buffer, index=False)
data = buffer.getvalue()
print(type(data), len(data) > 100)
print(pd.read_excel(io.BytesIO(data))["a"].sum())
```

```text
<class 'bytes'> True
3
```

### Build it: the TCI tab 🔴

At the bottom of `app.py`, add `with tab_tci:`, and import what you need from `tci.py`:

```python
from tci import run_tci, printable_schedule, schedule_table, replay_schedule
```

Lay it out in three rows of `st.columns(3)`:

| Row | Controls |
|---|---|
| 1 | `Drug` selectbox (`list(DRUGS)`, `key="tci_drug"`), `Model` selectbox (`list(DRUGS[drug])`, `key="tci_model"`), and `Targeting` radio of `"effect"` and `"plasma"` |
| 2 | `Target`, default 3.0; `Change target at (min, 0 = never)`, default 0; `New target`, default 2.0 |
| 3 | `Run for (min)` slider, 10–240, default 60; `Syringe concentration (per mL)`, default 10.0; `Pump maximum (mL/h)`, default 1200.0 |

Then:

1. `targets` is `[(0, target)]`, plus `(change_at, new_target)` if `change_at > 0`.
2. `max_rate = pump_max * syringe / 60`, in dose units per minute.
3. Build the drug with `DRUGS[drug][model](patient)`, and call `run_tci`.
4. Show one `st.line_chart` of Cp and Ce, and another of the pump rate. Use a `DataFrame` with `index=t`.
5. Add a subheader and a `st.select_slider` for the printing interval, with `options=[1, 2, 5, 10, 15, 20, 30]` and `value=5`.
6. Show the `schedule_table` with `st.dataframe`.
7. Replay the schedule through `replay_schedule`, and chart its Ce against the TCI Ce.
8. Write the table to an `io.BytesIO`, and offer a `st.download_button`, with a file name that includes the drug, model, mode, target and interval.

<details>
<summary><b>Hint</b></summary>

The replay runs on a different grid from the TCI record, so plot them with two lines using `plot_runs` and `st.pyplot`, rather than one `line_chart`. For the button's `mime`, use `"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
from plotting import plot_case, plot_runs
from tci import run_tci, printable_schedule, schedule_table, replay_schedule
```

```python

# ---------- tab 2: TCI ----------
with tab_tci:
    c1, c2, c3 = st.columns(3)
    drug = c1.selectbox("Drug", list(DRUGS), key="tci_drug")
    model = c2.selectbox("Model", list(DRUGS[drug]), key="tci_model")
    mode = c3.radio("Targeting", ["effect", "plasma"], horizontal=True,
                    format_func=lambda m: "Effect-site" if m == "effect" else "Plasma")
    c4, c5, c6 = st.columns(3)
    target = c4.number_input("Target", min_value=0.1, value=3.0, step=0.1)
    change_at = c5.number_input("Change target at (min, 0 = never)", min_value=0, value=0, step=5)
    new_target = c6.number_input("New target", min_value=0.0, value=2.0, step=0.1)
    c7, c8, c9 = st.columns(3)
    minutes = c7.slider("Run for (min)", 10, 240, 60, step=10)
    syringe = c8.number_input("Syringe concentration (per mL)", min_value=0.01, value=10.0)
    pump_max = c9.number_input("Pump maximum (mL/h)", min_value=1.0, value=1200.0, step=100.0)

    targets = [(0, target)] + ([(change_at, new_target)] if change_at > 0 else [])
    max_rate = pump_max * syringe / 60            # dose units per minute
    drug_obj = DRUGS[drug][model](patient)
    t, cp, ce, rate = run_tci(drug_obj, targets, minutes, mode=mode, max_rate=max_rate)

    st.line_chart(pd.DataFrame({"Cp": cp, "Ce": ce}, index=t))
    st.line_chart(pd.DataFrame({f"Rate ({drug_obj.dose_unit}/min)": rate}, index=t))

    st.subheader("Printable schedule")
    interval = st.select_slider("Print a rate change every (min)",
                                options=[1, 2, 5, 10, 15, 20, 30], value=5)
    bolus, rows_tci = printable_schedule(t, rate, interval, max_rate)
    df = schedule_table(bolus, rows_tci, patient.weight, drug_obj.dose_unit)
    st.dataframe(df)

    replay = replay_schedule(drug_obj, bolus, rows_tci, minutes)
    fig4, _ = plot_runs([("TCI", t, ce), ("Printed schedule", replay.t, replay.ce)],
                        ylabel=f"Ce ({drug_obj.conc_unit})")
    st.pyplot(fig4)

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    st.download_button(
        "Download schedule (Excel)",
        data=buffer.getvalue(),
        file_name=f"{drug}_{model}_{mode}_target{target}_every{interval}min_teaching.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
```

</details>


### Check it

There's no `if __name__` block in `app.py`; the page itself is the check. Start it with `streamlit run app.py` and compare what you see with the numbers from Weeks 5, 8 and 11 (listed in this week's Checkpoint). If a number differs, run that week's file on its own first (`python case.py`, `python tci.py`). If its checks pass, the problem is in how `app.py` builds the inputs.

Commit, and write a `DEVLOG.md` entry: Part 1 is done. You've built a working simulator, by hand, with every number checked.

### Things to consider

- **The rerun model is the whole trick.** Every click reruns `app.py` top to bottom. Widgets remember their own values; plain variables don't. That's why the dose table has a `key` and why the expensive part is cached.
- **Validation lives in your library.** A typo'd unit raises the `ValueError` you wrote in Week 5, and the app just displays it. You didn't write any new checking code for the web page.
- **What to show for long cases?** A methadone case is better viewed over 24–72 hours. Consider choosing the slider's maximum from the drugs in the table.
- **No "Run" button needed on the TCI tab.** An hour of TCI takes about a tenth of a second, so it simply reruns whenever an input changes. (If you ever do put results inside `if st.button(...)`, they vanish on the next rerun, including the one the download button causes. Keep them in `st.session_state` instead.)
- **Syringe concentration matters for the pump limit.** Remifentanil at 50 mcg/mL and propofol at 10 mg/mL give very different maximum rates from the same 1200 mL/h pump. That's why the app asks.
- Stretch: a "Compare models" checkbox that overlays every propofol model using your Week 6 `plot_runs`.

### Checkpoint

- The default table reproduces your Week 5 Marsh curve (Ce 3.80 at 10 min, 3.20 at 52 min) for the default patient.
- Load the Week 8 case (paste the rows in, or add an "Example case" button) and get the same five panels and numbers as Week 8.
- TCI tab, propofol, Eleveld, effect-site, target 3.0, reference adult (35 yo, 70 kg, 170 cm, M): Ce reaches target in about 3 min, peak Cp about 16.7, and the 5-minute printable schedule starts with a 133.3 mg bolus, matching Week 11. The Excel file opens.

**References:** Streamlit documentation (docs.streamlit.io) · Shafer SL. *stanpumpR* (stanpumpr.io), the interface this week imitates

---

# PART 2 — ANESTHESIA MACHINE (Python)

Same habits as Part 1, with a new idea: a **time-stepping** model. Part 1 handed the math to `solve_ivp`. Here you write the stepping yourself, with simple Euler steps, which makes every equation visible.

All concentrations are in **%** (volume percent, i.e. partial pressure). Time is in **minutes**, and `dt = 0.1/60` is a 0.1-second step.

**Where Part 2 ends up:** a Streamlit "machine" (Week 18) with O₂/air/N₂O flowmeters, a vaporizer, a gas monitor showing inspired and end-tidal values, a time-speed control, and a side-by-side mode that shows how 0.5 vs 10 L/min changes how fast everything happens.

### The story of Gas Man

This part follows the same model that James Philip built into **Gas Man**, a simulator used to teach uptake and distribution since the 1980s. His workbook breaks the problem down in a way that your code will mirror, and it's worth keeping nearby. Its main ideas:

- **Everything is a compartment, and every compartment has a time constant.** A time constant τ is volume divided by flow. After 1, 2, 3 and 4 time constants, a compartment has reached 63%, 86%, 95% and 98% of the way to its target.
- **Anesthesia is a chain of compartments.** Vaporizer → circuit → alveoli → blood → brain, muscle and fat. Each one lags behind the one before it.
- **The alveolar curve has parts:** an initial rise, a plateau or "knee", and a slowly climbing tail. Each part means something, and you'll see all of them.

**References:** Philip JH. *Workbook for Gas Man: a simulation and teaching tool*. Harvard Medical School; 2012 · Philip JH. Gas Man: an example of goal-oriented computer-assisted teaching which results in learning. *Int J Clin Monit Comput* 1986;3:165–73 · Eger EI II. *Anesthetic Uptake and Action*. Williams & Wilkins; 1974

---

## Week 13 — `Agent` and `Compartment`

**Goal:** an agent library, and one tissue compartment that exchanges gas with blood.

**New ideas:** `@dataclass` (a class that's mostly data); Euler steps; type hints; a dictionary of objects as a lookup table.

**Read first:** [Python `dataclasses`](https://docs.python.org/3/library/dataclasses.html)

### The science: MAC and partition coefficients

**MAC.** Eger and colleagues (1965) defined minimum alveolar concentration as a standard of potency: the alveolar concentration at which half of patients don't move in response to a surgical incision. It lets you compare very different agents on one scale, and MACs add. That's why `mac_multiple` is a one-line division, and why it's so useful.

**Partition coefficients.** A coefficient λ says how much of a gas a tissue holds compared with its partner at the same partial pressure. Sevoflurane's blood:gas λ of 0.65 means that at equilibrium, a liter of blood holds 0.65 times as much sevoflurane as a liter of alveolar gas. Blood and gas have the same *partial pressure* but different *concentrations*.

This matters for your code. **Partial pressure is what equilibrates, not concentration.** The brain's effect depends on partial pressure, so to compare a tissue with the lungs, you have to divide its concentration by λ. An earlier version of this project forgot this and showed brain at 1.7 MAC when the alveoli were at 1 MAC.

**The tissue time constant.** In Gas Man's terms, each tissue's time constant is its effective volume (real volume × λ) divided by its blood flow. For sevoflurane in VRG, that's 6 × 1.7 / 4.2, or about 2.4 minutes. For fat, it's 14.5 × 48 / 0.35, or about 33 hours. That's why fat keeps rising long after everything else has settled.

**References:** Eger EI, Saidman LJ, Brandstater B. *Anesthesiology* 1965;26:756–63 · Yasuda N, Lockhart SH, Eger EI II, et al. *Anesth Analg* 1991;72:316–24 · Philip JH. *Workbook for Gas Man*, chapters 3–5, 2012

### The big picture

Part 2 builds a different kind of simulator. In Part 1, `solve_ivp` did the time-stepping for you. Here **you** step time forward yourself, in tiny 0.1-second steps, and every equation is visible.

Start a new folder, `machine/`, and copy `checks.py` into it. This week makes the two smallest pieces:

```
agents.py       Agent: one anesthetic's fixed properties (MAC, solubilities)     ← data
compartment.py  Compartment: one tissue that takes up and gives back gas          ← behavior
```

Next week, `VolatilePKModel` will own three compartments (brain-and-organs, muscle, fat) and connect them through the lungs.

### Learn it: `@dataclass` 🟢

Make a new folder, `machine/`. It can't see `tci/`, so copy `checks.py` there, which is rule 2 from the Week 0 section on imports. Create `machine/scratch.py`:

```python
from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    grams: float
    price: float

    def price_per_kg(self) -> float:
        return self.price / self.grams * 1000


apple = Fruit("Apple", 150, 0.5)
print(apple)
print(apple.price_per_kg())

SHELF = {"apple": apple, "plum": Fruit("Plum", 50, 0.25)}
print(SHELF["plum"].price_per_kg())
```

```text
Fruit(name='Apple', grams=150, price=0.5)
3.3333333333333335
5.0
```

Compare this with your `Drug` class. `@dataclass` looks at the listed names and writes `__init__` and `__repr__` for you. It's a shortcut for classes that mostly hold data. `name: str` is a *type hint*, a note saying what kind of value goes there, and so is `-> float`. Python doesn't enforce them, but they help the reader.

### Learn it: an Euler step 🟢

Euler's method is the simplest way to move through time: **new value = old value + rate × dt**. Here's the cooling coffee from Week 3B, by hand this time. Empty `scratch.py`:

```python
class Cup:
    def __init__(self, temp):
        self.temp = temp

    def rate(self, room, k):
        return k * (room - self.temp)

    def update(self, room, k, dt):
        self.temp = max(0, self.temp + self.rate(room, k) * dt)


cup = Cup(90.0)
dt = 0.01
for _ in range(1000):
    cup.update(20.0, 0.2, dt)
print(round(cup.temp, 1))
```

```text
29.5
```

That's 1000 steps of 0.01 minutes, or 10 minutes. It gets the same 29.5 as `solve_ivp` did. `max(0, ...)` clamps the result, so a large step can't push it below zero.

### Build it: `agents.py` 🟡

Create `machine/agents.py`, with an `Agent` dataclass with these fields: `name` (text), and `mac`, `blood_gas`, `brain_blood`, `muscle_blood` and `fat_blood` (decimals). Add a method `mac_multiple(self, partial_pressure)`, which returns how many MACs a partial pressure is, and returns 0 if `mac` is 0. Below it, add the library:

| Key in `AGENTS` | Name | MAC | blood:gas | VRG:blood | muscle:blood | fat:blood |
|---|---|---|---|---|---|---|
| `"sevoflurane"` | Sevoflurane | 2.0 | 0.65 | 1.7 | 3.1 | 48 |
| `"isoflurane"` | Isoflurane | 1.15 | 1.46 | 1.6 | 2.9 | 45 |
| `"desflurane"` | Desflurane | 6.0 | 0.42 | 1.3 | 2.0 | 27 |
| `"nitrous_oxide"` | Nitrous oxide | 104 | 0.47 | 1.1 | 1.2 | 2.3 |

<details>
<summary><b>Answer</b></summary>

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
        if self.mac == 0:
            return 0.0
        return partial_pressure / self.mac


AGENTS = {
    "sevoflurane":   Agent("Sevoflurane",   2.0,  0.65, 1.7, 3.1, 48),
    "isoflurane":    Agent("Isoflurane",    1.15, 1.46, 1.6, 2.9, 45),
    "desflurane":    Agent("Desflurane",    6.0,  0.42, 1.3, 2.0, 27),
    "nitrous_oxide": Agent("Nitrous oxide", 104,  0.47, 1.1, 1.2, 2.3),
}


```

</details>

Add this check at the bottom:

```python
if __name__ == "__main__":
    from checks import check

    print(AGENTS["sevoflurane"])                       # @dataclass wrote this printout for you
    check("sevo 2.6% in MAC", AGENTS["sevoflurane"].mac_multiple(2.6), 1.3)
    check("des 6% in MAC", AGENTS["desflurane"].mac_multiple(6.0), 1.0)
    check("N2O 50% in MAC", AGENTS["nitrous_oxide"].mac_multiple(50), 0.48)
```


### Build it: `compartment.py` 🔴

Create `machine/compartment.py`, with a class `Compartment`, for one tissue:

```
dC/dt = (Q / V) · (C_arterial − C / λ)
```

`C` is the tissue concentration, and `C / λ` is the tissue's partial pressure, the number you can compare with alveolar %.

- `__init__(self, name, volume_L, blood_flow_Lmin)` stores `name`, `volume` and `blood_flow`, and sets `concentration` to 0.
- `partial_pressure(self, lam)`
- `rate_of_change(self, c_arterial, lam)`
- `update(self, c_arterial, lam, dt)` is an Euler step, clamped so it can't go below 0.
- `reset(self)`

Then a function, `create_compartments()`, returns this dictionary:

```python
{
    "VRG":    Compartment("Vessel-rich group", 6.0, 4.2),
    "muscle": Compartment("Muscle",           33.0, 0.9),
    "fat":    Compartment("Fat",              14.5, 0.35),
}
```

<details>
<summary><b>Hint</b></summary>

It's the `Cup`, with a different rate. `rate_of_change` should call `self.partial_pressure(lam)`, so the formula appears in one place only.

</details>
<details>
<summary><b>Answer</b></summary>

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
        return self.concentration / lam

    def rate_of_change(self, c_arterial, lam):
        return (self.blood_flow / self.volume) * (c_arterial - self.partial_pressure(lam))

    def update(self, c_arterial, lam, dt):
        self.concentration = max(0.0, self.concentration + self.rate_of_change(c_arterial, lam) * dt)

    def reset(self):
        self.concentration = 0.0


def create_compartments():
    return {
        "VRG":    Compartment("Vessel-rich group", 6.0, 4.2),
        "muscle": Compartment("Muscle",           33.0, 0.9),
        "fat":    Compartment("Fat",              14.5, 0.35),
    }


```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`@dataclass`** above `class Agent` tells Python "this class is mostly data". It writes `__init__` and `__repr__` for you from the list of fields, so `Agent("Sevoflurane", 2.0, ...)` just works.
- **The fields** are the agent's physical constants: MAC, blood:gas solubility (λ blood:gas), and how soluble it is in brain, muscle and fat compared with blood.
- **`mac_multiple`** converts a partial pressure (%) into multiples of MAC.
- **`AGENTS`** is a lookup table by name, like `DRUGS` in Part 1.
- **`Compartment`** is a regular class because its concentration changes over time:
  - `partial_pressure(lam)` converts tissue concentration into the equivalent gas %, the number you can compare with the lungs.
  - `rate_of_change(...)` is the one equation: (blood flow ÷ volume) × (arterial − tissue partial pressure).
  - `update(...)` takes one small step: rate × dt.
- **`create_compartments()`** builds the standard three tissues for a 70 kg adult.

</details>

Add this check at the bottom:

```python
if __name__ == "__main__":
    from checks import check

    vrg = Compartment("VRG", 6.0, 4.2)
    check("VRG wash-in rate, empty tissue (%/min)", vrg.rate_of_change(2.0, 1.7), 1.4)
    vrg.concentration = 3.4
    check("VRG rate at equilibrium", vrg.rate_of_change(2.0, 1.7), 0.0, tol=1e-9)
    check("VRG partial pressure at equilibrium (%)", vrg.partial_pressure(1.7), 2.0)
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `TypeError: Agent.__init__() missing 1 required positional argument` | One of the `Agent(...)` lines in `AGENTS` has too few numbers. There are six fields. |
| `XX  VRG wash-in rate` | The flow ÷ volume factor (4.2 ÷ 6.0 = 0.7 per minute), or the bracket's order (arterial minus tissue). |
| `XX  VRG rate at equilibrium` (about −0.98 instead of 0) | `rate_of_change` uses the raw tissue concentration where it should use `partial_pressure(lam)`. With an empty tissue both are 0, so only this check catches it. |
| Concentration goes negative later | `update` is missing the `max(0, ...)` clamp. |

### Things to consider

- Why doesn't `Compartment` store which agent it holds? Because the same compartment object works for any agent if λ is passed in. Less stored state means fewer ways to get out of sync.
- **Units trap (a bug in the old workbook):** a VRG *tissue* concentration of 3.4 at equilibrium with 2% alveolar doesn't mean the brain is at 1.7 MAC. Divide by λ first: 3.4 / 1.7 = 2.0% partial pressure = 1.0 MAC. That's why `partial_pressure()` exists.

### Checkpoint

- VRG, sevo (λ 1.7), arterial 2.0%, empty tissue: `rate_of_change` = **1.4 %/min**
- VRG at concentration 3.4: rate ≈ **0**, and `partial_pressure(1.7)` = **2.0**
- `AGENTS["sevoflurane"].mac_multiple(2.6)` = **1.3**

---

## Week 14A — The gas-exchange engine: its helpers

**Goal:** a `VolatilePKModel` that knows its minute ventilation, cardiac output, mixed venous and inspired concentrations.

**New ideas:** `@property` (a value computed when you read it, so it can never be stale); `sum()` with a generator; breaking a long method into small private helpers.

**Read first:** [Python `property`](https://docs.python.org/3/library/functions.html#property)

### The science: what comes back, and what goes in

**Mixed venous.** Blood returning to the lungs is a flow-weighted average of every tissue's partial pressure. Early in a case, the tissues are empty, so venous return carries nothing back, and uptake is large. As tissues fill, the venous partial pressure rises and uptake falls. That's what makes up the slow rising "tail" of the alveolar curve.

**Inspired, and rebreathing.** When the fresh gas flow is at least the minute ventilation, the patient breathes pure fresh gas, so the inspired concentration equals the dial. Below that, part of each breath is rebreathed exhaled gas, which contains less agent. Gas Man treats the circuit as its own compartment with a time constant of circuit volume ÷ fresh gas flow. That's why low flow slows everything down: the circuit itself takes a long time to change. This model uses a simpler mixing rule, which behaves similarly.

**References:** Philip JH. *Workbook for Gas Man*, chapters 3, 5 and 9, 2012 · Eger EI II. *Anesthetic Uptake and Action*, 1974

### The big picture

This is the engine of Part 2. Every call to `step(dt)` moves the whole body forward 0.1 seconds, using five equations **in order**:

```
1. mixed venous   what's coming back to the lungs from all tissues
2. inspired       what the patient breathes in (fresh gas + rebreathed gas)
3. uptake         how much the blood takes out of the lungs right now
4. alveolar       the new lung (end-tidal) concentration
5. tissues        each compartment takes up or gives back a little
```

Each equation needs the one before it. That's why each gets its own small helper method, so you can read the order at a glance in `step()`.

You'll also start `machine_tools.py`, a home for small helpers. The first is `run_minutes`, which calls `step` the right number of times.

### Learn it: `@property` 🟢

A stored value can go stale: if you store a rectangle's area and later change its width, the stored area is wrong. A property is calculated each time you read it, so it can't go stale. Empty `machine/scratch.py`:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(2, 3)
print(r.area)
r.width = 10
print(r.area)

try:
    r.area = 5
except AttributeError as err:
    print("Problem:", err)
```

```text
6
30
```

The last line also prints a message saying the property has no setter. Notice that it's `r.area`, with no brackets, even though it's a method underneath. You can't assign to it, which is what you want from a derived value. Week 16 will show how to add a setter.

### Learn it: `sum()` with a generator, and helpers 🟢

Empty `scratch.py`:

```python
class Order:
    def __init__(self):
        self.items = {"tea": (3.0, 2), "cake": (5.0, 1)}

    @property
    def subtotal(self):
        return sum(price * qty for price, qty in self.items.values())

    def _tax(self):
        return self.subtotal * 0.1

    def _tip(self, percent):
        return self.subtotal * percent / 100

    def total(self, percent):
        tax = self._tax()
        tip = self._tip(percent)
        return self.subtotal + tax + tip


print(Order().subtotal, round(Order().total(20), 2))
```

```text
11.0 14.3
```

`sum(x for ... in ...)` adds up a loop in one line. The `_tax` and `_tip` helpers make `total` read like a sentence, and each helper can be tested on its own. This is **the** key skill for bigger projects: one helper per idea.

### Build it: the model and its helpers 🟡

Create `machine/volatile.py`, importing `create_compartments`. Here's the `__init__`, since it's just the list of the model's settings:

```python
class VolatilePKModel:
    def __init__(self, agent):
        self.agent = agent
        self.compartments = create_compartments()
        self.alveolar = 0.0
        self.circuit = 0.0
        self.dial = 0.0
        self.fresh_gas_flow = 6.0       # becomes a property in Week 16
        self.resp_rate = 14
        self.tidal_volume = 0.5
        self.FRC = 2.5
        self.dead_space_fraction = 0.3
        self.time = 0.0
        self.last_uptake = 0.0
        self.extra_alveolar_rate = 0.0  # hook for the second gas effect (Week 15)
```

Add these:

- **`minute_ventilation`**, a property: respiratory rate × tidal volume.
- **`cardiac_output`**, a property: the sum of the tissue flows, so cardiac output and the compartments can never disagree.
- **`_lambda_for(self, name)`:** `"VRG"` gives `brain_blood`, `"muscle"` gives `muscle_blood`, and `"fat"` gives `fat_blood`.
- **`_mixed_venous(self)`:** `Cv = Σ(Qᵢ · Cᵢ/λᵢ) / Q_total`
- **`_inspired(self)`:** if FGF ≥ MV, `FI = dial`. Otherwise, `FI = (FGF·dial + (MV−FGF)·circuit) / MV`

Test each one on its own. Set a compartment's `concentration` by hand, call the helper, and print the result.

<details>
<summary><b>Hint</b></summary>

For `_mixed_venous`, loop over `self.compartments.items()`, add up `comp.blood_flow * comp.partial_pressure(self._lambda_for(name))`, and divide by `self.cardiac_output`.

</details>
<details>
<summary><b>Answer</b></summary>

```python
from compartment import create_compartments


class VolatilePKModel:
    def __init__(self, agent):
        self.agent = agent
        self.compartments = create_compartments()
        self.alveolar = 0.0
        self.circuit = 0.0
        self.dial = 0.0
        self.fresh_gas_flow = 6.0       # becomes a property in Week 16
        self.resp_rate = 14
        self.tidal_volume = 0.5
        self.FRC = 2.5
        self.dead_space_fraction = 0.3
        self.time = 0.0
        self.last_uptake = 0.0
        self.extra_alveolar_rate = 0.0  # hook for the second gas effect (Week 15)

    # ---- derived values: computed on read, never stored ----
    @property
    def minute_ventilation(self):
        return self.resp_rate * self.tidal_volume

    @property
    def cardiac_output(self):
        # Sum of tissue flows, so CO and the compartments can never disagree.
        return sum(c.blood_flow for c in self.compartments.values())

    def _lambda_for(self, name):
        table = {"VRG": self.agent.brain_blood,
                 "muscle": self.agent.muscle_blood,
                 "fat": self.agent.fat_blood}
        return table[name]

    # ---- one helper per equation keeps step() readable ----
    def _mixed_venous(self):
        total = 0.0
        for name, comp in self.compartments.items():
            total += comp.blood_flow * comp.partial_pressure(self._lambda_for(name))
        return total / self.cardiac_output

    def _inspired(self):
        mv = self.minute_ventilation
        if self.fresh_gas_flow >= mv:
            return self.dial
        return (self.fresh_gas_flow * self.dial + (mv - self.fresh_gas_flow) * self.circuit) / mv


```

</details>

Add a first check at the bottom:

```python
if __name__ == "__main__":
    from agents import AGENTS
    from checks import check

    m = VolatilePKModel(AGENTS["sevoflurane"])
    check("cardiac output = sum of tissue flows (L/min)", m.cardiac_output, 5.45)
    check("minute ventilation (L/min)", m.minute_ventilation, 7.0)
    m.compartments["VRG"].concentration = 1.7
    check("mixed venous with only VRG filled", m._mixed_venous(), 4.2 / 5.45, tol=0.001)
    m.compartments["VRG"].concentration = 0.0

    m.dial = 2.0
    m.fresh_gas_flow = 8.0
    check("high flow: inspired equals the dial", m._inspired(), 2.0)
    m.fresh_gas_flow = 3.5
    m.circuit = 1.0
    check("low flow: half fresh gas, half circuit", m._inspired(), 1.5)
```


Commit.

### Checkpoint

`cardiac_output` is **5.45**, and `_inspired` gives **2.0** at high flow and **1.5** when half of each breath is rebreathed.

---

## Week 14B — The gas-exchange engine: `step()`

**Goal:** advance the whole body by one time step, and watch wash-in and washout.

**New ideas:** order of operations in a time-stepping model; a small tools file.

### The science: the alveolar curve

Open-circuit wash-in has three parts, in Gas Man's terms:

- **Initial rise.** Ventilation fills the lungs, with a time constant of FRC ÷ alveolar ventilation. In this model, that's 2.5 / 4.9, or about half a minute.
- **The plateau, or knee.** Ventilation brings agent in, while blood carries it away, and the two reach a balance. Philip gives the height as:

```
PA = PI / (1 + λ · CO / VA)
```

  So the more soluble an agent is, the lower its plateau. You'll test this formula against your own model below.
- **The tail.** As tissues slowly fill, venous return rises and the alveolar level creeps upward.

**The same equation gives you overpressure.** To reach 1 MAC in the alveoli quickly, you set the dial above 1 MAC. Rearranging the formula gives the setting you need.

**Washout is the mirror image.** Gas Man's wake-up chapter makes this point: wake-up is the inverse of induction. When you turn the dial off, the alveolar level falls first, then the brain. But muscle and fat keep *rising* for a while, because they're still below the blood's partial pressure.

**References:** Philip JH. *Workbook for Gas Man*, chapters 5, 6, 7 and 12, 2012 · Eger EI II. *Anesthesiology* 1963;24:153–7 · Eger EI II. *Anesthetic Uptake and Action*, 1974

### The big picture

1. Mixed venous: `Cv = Σ(Qᵢ · Cᵢ/λᵢ) / Q_total`
2. Inspired: if FGF ≥ MV, `FI = dial`. Otherwise `FI = (FGF·dial + (MV−FGF)·circuit) / MV`
3. Uptake: `U = CO · λ_blood:gas · (FA − Cv)`
4. Alveolar: `dFA/dt = (VA·(FI − FA) − U) / FRC`
5. Tissues: each compartment's `update(FA, λ, dt)`, using the **new** FA

### Build it: `step()` 🔴

Add these to `VolatilePKModel`:

**`step(self, dt)`,** in this exact order:

1. `VA = minute_ventilation × (1 − dead_space_fraction)`
2. `cv` from `_mixed_venous()`, and `fi` from `_inspired()`
3. Equation 3: store the uptake in `self.last_uptake`
4. Equation 4: `dFA = (VA·(FI − FA) − U) / FRC + extra_alveolar_rate`, an Euler step, clamped at 0
5. Equation 5: update each compartment, using the **new** alveolar value
6. `self.circuit = self.alveolar`, a simplification saying the rebreathed gas is alveolar gas
7. `self.time += dt`

**`brain_partial_pressure(self)`:** VRG concentration ÷ brain λ.

**`get_mac_values(self)`:** a dictionary `{"alveolar": ..., "brain": ...}` of MAC multiples, using partial pressures.

**`reset(self)`:** zeroes the alveolar and circuit values, time, and uptake, and resets each compartment.

Then create `machine/machine_tools.py`, with a `run_minutes(model, minutes, dt=0.1/60)` function that calls `model.step(dt)` the right number of times. It only needs `.step`, so later it'll work on a two-gas model too.

<details>
<summary><b>Answer</b></summary>

```python
    def step(self, dt):
        VA = self.minute_ventilation * (1 - self.dead_space_fraction)
        cv = self._mixed_venous()
        fi = self._inspired()
        self.last_uptake = self.cardiac_output * self.agent.blood_gas * (self.alveolar - cv)
        dFA = (VA * (fi - self.alveolar) - self.last_uptake) / self.FRC + self.extra_alveolar_rate
        self.alveolar = max(0.0, self.alveolar + dFA * dt)
        for name, comp in self.compartments.items():
            comp.update(self.alveolar, self._lambda_for(name), dt)
        self.circuit = self.alveolar        # simplification: rebreathed gas = alveolar
        self.time += dt

    def brain_partial_pressure(self):
        return self.compartments["VRG"].partial_pressure(self.agent.brain_blood)

    def get_mac_values(self):
        return {"alveolar": self.agent.mac_multiple(self.alveolar),
                "brain": self.agent.mac_multiple(self.brain_partial_pressure())}

    def reset(self):
        self.alveolar = 0.0
        self.circuit = 0.0
        self.time = 0.0
        self.last_uptake = 0.0
        for comp in self.compartments.values():
            comp.reset()


```

```python
def run_minutes(model, minutes, dt=0.1 / 60):
    """Step any model forward by this many minutes."""
    for _ in range(round(minutes / dt)):
        model.step(dt)


```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`__init__`** sets the patient and machine: three compartments, empty lungs, vaporizer off, ventilation 14 × 0.5 L.
- **`@property`** makes a method look like a plain value: you write `m.minute_ventilation`, not `m.minute_ventilation()`. It's recalculated every time you read it, so it can never be out of date. `cardiac_output` is a property for the same reason: it's always the sum of the tissue flows.
- **`_lambda_for(name)`** picks the right tissue solubility for "VRG", "muscle" or "fat".
- **`_mixed_venous()`** and **`_inspired()`** are equations 1 and 2, each on its own so you can check them separately.
- **`step(dt)`** reads like the list above. `extra_alveolar_rate` is a hook that's 0 for now; Week 15 uses it for the second gas effect.
- **`brain_partial_pressure()`** and **`get_mac_values()`** report the numbers you care about clinically.

`run_minutes` doesn't care what kind of model it gets, only that it has a `step` method. Next week it will run a two-gas model too, without any changes.

</details>

### Check it

Replace the check block at the bottom of `volatile.py` with this:

```python
if __name__ == "__main__":
    from agents import AGENTS
    from machine_tools import run_minutes
    from checks import check

    m = VolatilePKModel(AGENTS["sevoflurane"])
    check("cardiac output = sum of tissue flows (L/min)", m.cardiac_output, 5.45)

    m.dial = 2.0
    m.fresh_gas_flow = 8.0
    expected = {1: (1.186, 0.509, 0.023), 3: (1.425, 1.503, 0.094), 5: (1.549, 2.091, 0.174)}
    for minute in range(1, 6):
        run_minutes(m, 1)
        if minute in expected:
            fa, vrg, muscle = expected[minute]
            check(f"wash-in {minute} min: FA", m.alveolar, fa, tol=0.005)
            check(f"wash-in {minute} min: VRG", m.compartments["VRG"].concentration, vrg, tol=0.005)
            check(f"wash-in {minute} min: muscle", m.compartments["muscle"].concentration, muscle, tol=0.005)
    check("brain partial pressure at 5 min (%)", m.brain_partial_pressure(), 1.23)

    m.dial = 0.0                                     # washout
    run_minutes(m, 1)
    check("washout 6 min: FA", m.alveolar, 0.404, tol=0.005)
    check("washout 6 min: VRG", m.compartments["VRG"].concentration, 1.778, tol=0.005)
    run_minutes(m, 4)
    check("washout 10 min: FA", m.alveolar, 0.133, tol=0.005)
    check("washout 10 min: muscle still rising", m.compartments["muscle"].concentration, 0.210, tol=0.005)

    low = VolatilePKModel(AGENTS["sevoflurane"])
    low.dial = 2.0
    low.fresh_gas_flow = 1.0
    run_minutes(low, 5)
    check("FGF 1 L/min: FA at 5 min", low.alveolar, 0.562, tol=0.005)
```


Every line should start with `OK`. Fix the **first** `XX` before anything else. Then commit.

### Explore it: test Gas Man's plateau formula 🔴

In `scratch.py`, loop over sevoflurane, isoflurane and desflurane, setting each dial to 1 MAC and the flow to 8 L/min. For each, compute the plateau ratio Philip predicts, `1 / (1 + λ · CO / VA)`, where `VA` is 4.9. Then run your model for 1 minute, and print the actual `alveolar / dial`. Your model's tissues are nearly empty at 1 minute, so these should be close.

```text
sevoflurane: predicted 0.58, model at 1 min 0.59
isoflurane: predicted 0.38, model at 1 min 0.42
desflurane: predicted 0.68, model at 1 min 0.67
```

Your code just reproduced the formula in a textbook, from equations you wrote. Isoflurane comes out highest above its prediction, because being more soluble it spends more of that first minute still rising, and venous return has begun to matter.

<details>
<summary><b>Answer</b></summary>

```python
from agents import AGENTS
from machine_tools import run_minutes
from volatile import VolatilePKModel

for key in ["sevoflurane", "isoflurane", "desflurane"]:
    agent = AGENTS[key]
    m = VolatilePKModel(agent)
    m.dial = agent.mac
    m.fresh_gas_flow = 8.0
    predicted = 1 / (1 + agent.blood_gas * m.cardiac_output / 4.9)
    run_minutes(m, 1)
    print(f"{key}: predicted {predicted:.2f}, model at 1 min {m.alveolar / m.dial:.2f}")
```

</details>

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  cardiac output` (5.0) | You typed a number instead of adding up the three `blood_flow` values. |
| FA rises too fast, VRG tracks FA almost exactly | Equation order: tissues updated with the *old* alveolar value, or uptake computed before mixed venous. |
| FA climbs above the dial setting | A sign in equation 4: ventilation adds (FI − FA), uptake *subtracts*. |
| Everything stays at 0 | `run_minutes` loops zero times (check the step count), or the dial is still 0. |
| `XX  brain partial pressure` (2.09 instead of 1.23) | You returned the raw VRG concentration. Divide by the brain solubility. |
| `XX  FGF 1 L/min` but high flow is right | `_inspired`: below minute ventilation, the shortfall is made up from the circuit (rebreathed gas). |
| `AttributeError: can't set attribute` | You assigned to a property (`m.cardiac_output = 5`). Properties are read-only unless you add a setter. |

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

## Week 15 — Two agents: MAC additivity and a correct second gas effect

**Goal:** sevo + N₂O running together, total MAC, and a second gas effect that behaves sensibly.

**New ideas:** *composition* (one object holding two others); why any "per-step" adjustment must scale with `dt`.

### The science: the concentration and second gas effects

When you breathe a high concentration of N₂O, large volumes of it leave the alveoli for the blood. Two things follow.

- **The concentration effect.** The higher the inspired concentration of an agent, the faster its own alveolar level rises toward the inspired level. Gas Man's chapter 8 shows that at 100% inspired, cardiac output has no effect on the alveolar level at all.
- **The second gas effect.** Removing that volume of N₂O shrinks the remaining alveolar gas, which concentrates whatever else is there, such as a volatile agent. It's slight at low N₂O concentrations and dramatic at high ones (Gas Man, chapter 11). Epstein and colleagues described it in 1964, and Stoelting and Eger later added the concentrating explanation.

**A cautionary tale from this project.** An earlier version wrote `alveolar *= 1 + uptake * 0.01` at every step. That's a *per-step* rule, so its effect depended on the step size, and sevoflurane went to infinity within 3 minutes. Anything that happens over time has to be a **rate**, multiplied by `dt` in one place. This lesson does it as a rate term inside dFA/dt: `FA · U / FRC`.

> **What this model leaves out.** Your N₂O sub-model doesn't include the concentration effect on itself, and the second gas effect here is the concentrating part only. So it's modest, and the real effect at high N₂O can be larger. It's a teaching model with the right direction and a sensible size.

**References:** Epstein RM, Rackow H, Salanitre E, Wolf GL. *Anesthesiology* 1964;25:364–71 · Stoelting RK, Eger EI II. *Anesthesiology* 1969;30:273–7 · Taheri S, Eger EI II. *Anesth Analg* 1999;89:774–80 · Korman B, Mapleson WW. *Br J Anaesth* 1997;78:618–25 · Philip JH. *Workbook for Gas Man*, chapters 8 and 11, 2012

### The big picture

Now two gases at once. Instead of making one huge model that handles both, you make **two** `VolatilePKModel`s and a small manager that holds them:

```
DualAgentModel
   ├── self.volatile  (sevo, des or iso)
   └── self.n2o       (nitrous oxide)
step(): step N2O → work out the second gas effect from its uptake → step the volatile
total_mac(): volatile MAC + N2O MAC      (inhaled agents add by MAC)
```

That's *composition*: building something bigger out of pieces you already trust.

### Learn it: composition 🟢

A car *has* an engine and a radio. It doesn't need to know how they work, and it can pass information between them. Empty `machine/scratch.py`:

```python
class Tank:
    def __init__(self):
        self.fuel = 10.0
        self.boost = 0.0

    def step(self, dt):
        self.fuel = max(0.0, self.fuel - (1.0 + self.boost) * dt)


class TwinTanks:
    def __init__(self):
        self.main = Tank()
        self.reserve = Tank()

    def step(self, dt):
        self.main.step(dt)
        self.reserve.boost = 0.5 if self.main.fuel < 5 else 0.0
        self.reserve.step(dt)

    def total(self):
        return self.main.fuel + self.reserve.fuel


t = TwinTanks()
for _ in range(600):
    t.step(0.01)
print(round(t.main.fuel, 2), round(t.reserve.fuel, 2), round(t.total(), 2))
```

```text
4.0 3.5 7.5
```

`TwinTanks` adds no physics of its own. It holds two trusted objects, and passes one's result to the other as a *rate*, which gets multiplied by `dt` in `Tank.step`. So cutting the step size in half wouldn't change the answer much. That's the rule you'll follow for N₂O.

### Build it: `dual.py` 🔴

Create `machine/dual.py`, with a class `DualAgentModel`:

- `__init__(self, volatile_agent, use_second_gas=True)` makes `self.volatile`, a `VolatilePKModel` of the agent, `self.n2o`, a `VolatilePKModel` of nitrous oxide, and stores the flag.
- `set_dials(self, volatile_pct, n2o_pct)` sets both dials.
- `step(self, dt)` first steps N₂O. If the second gas effect is on, then N₂O's uptake in L/min is `max(0, n2o.last_uptake) / 100`, because `last_uptake` is in %·L/min. The concentrating rate in %/min is `FA_volatile × U_N2O / FRC`. Store that in `self.volatile.extra_alveolar_rate`, which your `step()` already adds. If it's off, set that to 0. Then step the volatile.
- `total_mac(self)` adds both models' alveolar MAC.

<details>
<summary><b>Answer</b></summary>

```python
from agents import AGENTS
from volatile import VolatilePKModel


class DualAgentModel:
    def __init__(self, volatile_agent, use_second_gas=True):
        self.volatile = VolatilePKModel(volatile_agent)
        self.n2o = VolatilePKModel(AGENTS["nitrous_oxide"])
        self.use_second_gas = use_second_gas

    def set_dials(self, volatile_pct, n2o_pct):
        self.volatile.dial = volatile_pct
        self.n2o.dial = n2o_pct

    def step(self, dt):
        self.n2o.step(dt)
        if self.use_second_gas:
            # N2O leaving the alveoli shrinks alveolar gas volume and concentrates
            # what's left. last_uptake is in %·L/min, so /100 gives L/min of gas.
            n2o_L_per_min = max(0.0, self.n2o.last_uptake) / 100
            self.volatile.extra_alveolar_rate = (
                self.volatile.alveolar * n2o_L_per_min / self.volatile.FRC)
        else:
            self.volatile.extra_alveolar_rate = 0.0
        self.volatile.step(dt)

    def total_mac(self):
        return (self.volatile.get_mac_values()["alveolar"]
                + self.n2o.get_mac_values()["alveolar"])


```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`__init__`** builds the two sub-models. Nitrous oxide always comes from `AGENTS["nitrous_oxide"]`.
- **`set_dials`** is a convenience that sets both dials at once.
- **`step(dt)`**: N2O steps first, because the volatile needs to know how much N2O just left the lungs. That amount (in L/min) shrinks the alveolar gas volume and concentrates what's left. The model turns it into a *rate* and hands it to the volatile through `extra_alveolar_rate`. Because it's a rate, `step` multiplies it by `dt`, so it behaves the same whatever step size you choose.
- **`total_mac()`** adds the two alveolar MAC fractions.

</details>

### Check it

Add this at the bottom of `dual.py`:

```python
if __name__ == "__main__":
    from machine_tools import run_minutes
    from checks import check

    for use_sge, expected in [(False, {1: 0.593, 3: 0.713, 10: 0.841}),
                              (True,  {1: 0.633, 3: 0.761, 10: 0.878})]:
        m = DualAgentModel(AGENTS["sevoflurane"], use_second_gas=use_sge)
        m.set_dials(1.0, 50)
        m.volatile.fresh_gas_flow = 8.0
        m.n2o.fresh_gas_flow = 8.0
        for minute in range(1, 11):
            run_minutes(m, 1)
            if minute in expected:
                check(f"second gas {'on ' if use_sge else 'off'}: sevo FA at {minute} min",
                      m.volatile.alveolar, expected[minute], tol=0.005)
    check("total MAC at 10 min (second gas on)", m.total_mac(), 0.873, tol=0.005)
```


Then plot volatile FA for both runs on one axis, and commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| Sevo shoots to huge numbers or `inf` | The second gas effect is being multiplied into `alveolar` every step instead of passed as a rate through `extra_alveolar_rate`. |
| `XX` with second gas on, OK with it off | The rate formula: FA × (N2O L/min) ÷ FRC, with uptake divided by 100 to turn %·L/min into L/min. |
| Second gas effect makes no difference | `extra_alveolar_rate` is set but your Week 14 `step()` doesn't add it into dFA/dt. |
| `XX  total MAC` | Each gas's alveolar % divided by *its own* MAC (2.0 for sevo, 104 for N2O). |

### Things to consider

- **Why the old version exploded:** it did `alveolar *= 1 + uptake*0.01` every 0.1 s. With N₂O uptake around 40, that's ×1.4 six hundred times a minute, and sevo went to infinity within 3 minutes. Anything that happens "per step" must be a *rate* multiplied by `dt`, or changing `dt` changes the physics. Here the rate goes into dFA/dt, and `step()` multiplies by `dt` for you.
- This is still a teaching simplification. Modern work (Korman & Mapleson 1997; Hendrickx 2006) suggests the alveolar second gas effect is smaller than the classic diagram implies. Say so in a docstring.
- MAC additivity only applies to *inhaled* agents. Remember this for Week 31.

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

## Week 16A — Oxygen: the fresh gas arithmetic

**Goal:** calculate the FiO₂ the flowmeters deliver, work out the flows for a target, and flag hypoxic mixtures.

**New ideas:** module-level functions and constants; returning a "this worked" flag with a result.

### The science: the hypoxic guard

Oxygen doesn't change anesthetic depth, but it's where a low flow can become dangerous. Modern machines have a hypoxic guard that links O₂ and N₂O flows, so that the delivered mixture can't fall below about 25% O₂ (ISO 80601-2-13). The guard only looks at what goes *into* the circuit, though. As you'll see next lesson, what the patient breathes can be lower.

Air is 21% O₂, so no mix of O₂ and air can give less than 21%. That's why this lesson's function has an "impossible" case.

**References:** ISO 80601-2-13 (anaesthetic workstation safety) · Hendrickx JFA, De Wolf AM. *Anesth Analg* 2018;127:671–5

### The big picture

```
oxygen.py     the arithmetic, as plain functions. It has no memory, so no class is needed
```

### Learn it: a weighted average, and returning a flag 🟢

Empty `machine/scratch.py`:

```python
STRENGTH = {"espresso": 1.00, "milk": 0.00, "drip": 0.40}


def blend_strength(espresso, milk, drip):
    total = espresso + milk + drip
    if total <= 0:
        return 0.0
    return (espresso * STRENGTH["espresso"] + milk * STRENGTH["milk"]
            + drip * STRENGTH["drip"]) / total


def mix_for(target, total):
    if target < 0.40:
        return 0.0, total, False
    espresso = total * (target - 0.40) / (1.00 - 0.40)
    return espresso, total - espresso, True


print(blend_strength(1, 1, 0))
print(mix_for(0.7, 100))
print(mix_for(0.1, 100))
e, d, ok = mix_for(0.7, 100)
print(ok, blend_strength(e, 0, d))
```

```text
0.5
(49.99999999999999, 50.00000000000001, True)
(0.0, 100, False)
True 0.7
```

The flag lets the caller check whether the request was possible, and returning the same three things in both branches means `e, d, ok = ...` always works.

### Build it: `oxygen.py` 🔴

Create `machine/oxygen.py`, with `O2_FRACTION = {"o2": 1.00, "air": 0.21, "n2o": 0.00}`, and these functions:

- **`fresh_gas_fio2(o2_flow, air_flow, n2o_flow)`:** the flow-weighted O₂ fraction. It returns 0 if the total flow is 0.
- **`flows_for_target_fio2(target, total_flow)`:** returns `(o2_flow, air_flow, feasible)`. Below 0.21, it returns all air with `feasible = False`. Otherwise, `Q_O2 = Q_total·(target − 0.21) / (1.00 − 0.21)`, and the rest is air.
- **`fresh_gas_hypoxic(o2_flow, air_flow, n2o_flow, min_fio2=0.25)`:** True if the fresh gas is below the limit.
- **`inspired_hypoxic(circuit_fio2, min_fio2=0.25)`:** True if the circuit is below the limit.

<details>
<summary><b>Answer</b></summary>

```python
O2_FRACTION = {"o2": 1.00, "air": 0.21, "n2o": 0.00}


def fresh_gas_fio2(o2_flow, air_flow, n2o_flow):
    """FiO2 = (Q_O2·1.00 + Q_air·0.21 + Q_N2O·0.00) / (Q_O2 + Q_air + Q_N2O)"""
    total = o2_flow + air_flow + n2o_flow
    if total <= 0:
        return 0.0
    return (o2_flow * O2_FRACTION["o2"] + air_flow * O2_FRACTION["air"]
            + n2o_flow * O2_FRACTION["n2o"]) / total


def flows_for_target_fio2(target, total_flow):
    """Return (o2_flow, air_flow, feasible). Below 0.21 is impossible with O2+air."""
    if target < 0.21:
        return 0.0, total_flow, False
    o2 = total_flow * (target - 0.21) / (1 - 0.21)
    return o2, total_flow - o2, True


def fresh_gas_hypoxic(o2_flow, air_flow, n2o_flow, min_fio2=0.25):
    return fresh_gas_fio2(o2_flow, air_flow, n2o_flow) < min_fio2


def inspired_hypoxic(circuit_fio2, min_fio2=0.25):
    return circuit_fio2 < min_fio2


```

</details>

### Check it

Add this at the bottom of `oxygen.py`. The circuit checks come next lesson.

```python
if __name__ == "__main__":
    from checks import check

    check("O2 1 + air 1", fresh_gas_fio2(1, 1, 0), 0.605, tol=0.0005)
    check("O2 1 + air 1 + N2O 2", fresh_gas_fio2(1, 1, 2), 0.3025, tol=0.0005)
    o2, air, ok = flows_for_target_fio2(0.30, 2.0)
    check("flows for 30% at 2 L/min: O2", o2, 0.228, tol=0.001)
    check("flows for 30% at 2 L/min: air", air, 1.772, tol=0.001)
    check("...and they really give 30%", fresh_gas_fio2(o2, air, 0), 0.30, tol=0.0005)
    check("a target below 21% is flagged as impossible", flows_for_target_fio2(0.15, 2.0)[2], False)
    check("O2 1 + N2O 4 (20% O2) is hypoxic", fresh_gas_hypoxic(1, 0, 4), True)
    check("O2 2 + N2O 2 (50% O2) is not", fresh_gas_hypoxic(2, 0, 2), False)
```


Commit.

### Checkpoint

- `fresh_gas_fio2(1, 1, 0)` = **0.605**, and `fresh_gas_fio2(1, 1, 2)` = **0.3025**
- `flows_for_target_fio2(0.30, 2.0)` → O₂ **0.228**, air **1.772**

---

## Week 16B — Oxygen in the circuit: the low-flow trap

**Goal:** model the FiO₂ the patient actually breathes, including the sag at low flow.

**New ideas:** replacing a stored attribute with a `@property` and a setter, *without breaking older code*.

### The science: why the circuit can fall below the fresh gas

The patient consumes oxygen, about 250 mL/min at rest, and takes it out of the circuit. At a high flow, that doesn't matter, because fresh gas washes the circuit constantly. At a low flow, it does. With a 2 L/min flow set to 30% O₂, you deliver 0.6 L/min of O₂ and the patient removes 0.25, so what's left in the circuit has much less than 30%. Your checkpoint shows the FiO₂ falling to about 17.5%, even though the flowmeters say 30%, and the hypoxic guard has no objection.

**Two time scales.** Gas Man's low-flow chapter shows the circuit's time constant is its volume divided by the fresh gas flow. With 7 L at 2 L/min, that's 3.5 minutes, so the circuit is slow to change at low flow. A circuit flush is a fast way to change it, because it replaces the gas directly.

**That's why FiO₂ monitoring at the patient end matters,** not just knowing what the flowmeters are set to.

**References:** Baum JA. *Low Flow Anaesthesia*. 2nd ed. Butterworth-Heinemann; 2001 · Mapleson WW. The concept of the time constant applied to breathing systems and to the body · Philip JH. *Workbook for Gas Man*, chapter 9, 2012 · Resting adult O₂ consumption ≈ 250 mL/min (standard physiology)

### The big picture

```
fresh-gas FiO2     what the flowmeters deliver right now (instant, simple arithmetic)
circuit FiO2       what the patient actually breathes; drifts toward the fresh gas,
                   slowly at low flow, and SAGS below it because the patient uses O2
```

`fresh_gas_flow` changes from a stored number to a **property** (O₂ + air + N₂O), so turning the flowmeters down automatically slows the volatile too.

### Learn it: a property with a setter 🟢

Your older code says `m.fresh_gas_flow = 8.0`. If `fresh_gas_flow` becomes a property with no setter, all of that breaks. A *setter* lets the old line keep working, by deciding what assigning to it should mean. Empty `machine/scratch.py`:

```python
class Thermometer:
    def __init__(self):
        self.celsius = 20.0

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


t = Thermometer()
print(t.fahrenheit)
t.fahrenheit = 212
print(t.celsius, t.fahrenheit)
```

```text
68.0
100.0 212.0
```

The two methods share one name. Old code that reads or assigns `fahrenheit` can't tell that the underlying storage has changed. This is one of the most useful things a class can do: change how it works inside without breaking anything outside.

### Build it: update `volatile.py` 🟡

**In `__init__`,** delete `self.fresh_gas_flow = 6.0` and add:

```python
        self.o2_flow, self.air_flow, self.n2o_flow = 2.0, 0.0, 0.0
        self.circuit_fio2 = 0.95       # after preoxygenation
        self.V_system = 7.0            # circuit + FRC, treated as one well-mixed volume
        self.vo2 = 0.25                # L/min O2 consumption
        self.use_o2_consumption = True
```

**Add a property, `fresh_gas_flow`,** which is the sum of the three flows, and a setter that treats an assignment as "all of it is oxygen": `o2_flow = value`, `air_flow = 0`, `n2o_flow = 0`. That keeps the old `m.fresh_gas_flow = 8.0` lines working.

**Add `_update_fio2(self, dt)`:**

```
d(FiO2)/dt = [Q·(FiO2_freshgas − FiO2_circuit) − VO2] / V_system
```

It's an Euler step, clamped to the range 0 to 1. `VO2` is 0 if `use_o2_consumption` is off. Import `fresh_gas_fio2` from `oxygen.py`. Call `self._update_fio2(dt)` at the end of `step()`.

Then rerun `python volatile.py` and `python dual.py`. Every earlier line should still say `OK`. If one doesn't, the property or its setter is the place to look. That's the payoff of keeping your checks.

<details>
<summary><b>Answer</b></summary>

```python
from compartment import create_compartments
from oxygen import fresh_gas_fio2
```

```python
        self.o2_flow, self.air_flow, self.n2o_flow = 2.0, 0.0, 0.0
        self.circuit_fio2 = 0.95       # after preoxygenation
        self.V_system = 7.0            # circuit + FRC, treated as one well-mixed volume
        self.vo2 = 0.25                # L/min O2 consumption
        self.use_o2_consumption = True
```

```python
    @property
    def fresh_gas_flow(self):
        return self.o2_flow + self.air_flow + self.n2o_flow

    @fresh_gas_flow.setter
    def fresh_gas_flow(self, value):
        # Older code sets one number: treat it as all oxygen.
        self.o2_flow, self.air_flow, self.n2o_flow = value, 0.0, 0.0

    def _update_fio2(self, dt):
        fresh = fresh_gas_fio2(self.o2_flow, self.air_flow, self.n2o_flow)
        vo2 = self.vo2 if self.use_o2_consumption else 0.0
        rate = (self.fresh_gas_flow * (fresh - self.circuit_fio2) - vo2) / self.V_system
        self.circuit_fio2 = min(1.0, max(0.0, self.circuit_fio2 + rate * dt))

```

```python
        self.time += dt
        self._update_fio2(dt)
```

</details>


### Check it

Add these lines inside the check block in `oxygen.py`. The imports go at the top of the block.

```python

    # circuit FiO2 over time, fresh gas set to 30%
    from agents import AGENTS
    from volatile import VolatilePKModel
    from machine_tools import run_minutes

    for total, vo2_on, expected in [(2, False, {1: 0.788, 5: 0.456, 10: 0.337, 30: 0.300}),
                                    (2, True,  {1: 0.757, 5: 0.361, 10: 0.219, 30: 0.175}),
                                    (10, True, {1: 0.436, 5: 0.276, 10: 0.275, 30: 0.275})]:
        m = VolatilePKModel(AGENTS["sevoflurane"])
        m.o2_flow, m.air_flow, _ = flows_for_target_fio2(0.30, total)
        m.use_o2_consumption = vo2_on
        elapsed = 0
        for minute in (1, 5, 10, 30):
            run_minutes(m, minute - elapsed)
            elapsed = minute
            check(f"{total} L/min, VO2 {'on ' if vo2_on else 'off'}: FiO2 at {minute} min",
                  m.circuit_fio2, expected[minute], tol=0.002)
```


### See it 🔴

Write `machine/run_fio2.py`. Start at 95%, set the flows for a 30% target at 2 L/min, run 30 minutes with consumption on and off, record `circuit_fio2` each minute, and plot both on one graph with a dashed line at 25%.

<details>
<summary><b>Answer</b></summary>

```python
import matplotlib.pyplot as plt

from agents import AGENTS
from machine_tools import run_minutes
from oxygen import flows_for_target_fio2
from volatile import VolatilePKModel

if __name__ == "__main__":
    fig, ax = plt.subplots()
    for consumption in (False, True):
        m = VolatilePKModel(AGENTS["sevoflurane"])
        m.o2_flow, m.air_flow, _ = flows_for_target_fio2(0.30, 2.0)
        m.use_o2_consumption = consumption
        minutes, fio2 = [0], [m.circuit_fio2]
        for minute in range(1, 31):
            run_minutes(m, 1)
            minutes.append(minute)
            fio2.append(m.circuit_fio2)
        ax.plot(minutes, fio2, label=f"VO2 {'on' if consumption else 'off'}")
    ax.axhline(0.25, linestyle="--", label="25%")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Circuit FiO2")
    ax.legend()
    plt.show()
```

</details>


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `AttributeError: property 'fresh_gas_flow' ... has no setter` | Add the `@fresh_gas_flow.setter` shown above. |
| Old checks in `volatile.py` or `dual.py` now print `XX` | The property returns the wrong total, or the setter doesn't zero air and N₂O. Run `python volatile.py` to see which. |
| `ZeroDivisionError` in `fresh_gas_fio2` | All flows are 0. Keep the `if total <= 0` guard first. |
| Circuit FiO₂ jumps straight to the setting | `_update_fio2` isn't multiplying by `dt`, or it's being called with the wrong `dt`. |
| Circuit FiO₂ never sags with consumption on | `use_o2_consumption` isn't being read, or `vo2` isn't subtracted inside the brackets. |
| FiO₂ goes below 0 or above 1 | The clamp `min(1.0, max(0.0, ...))` is missing. |

### Things to consider

- Who else uses `fresh_gas_flow`? `DualAgentModel` gives the N₂O sub-model its own flows. Should the N₂O model read the same machine? Decide whether both sub-models should share one "machine" object. That's a real design decision, and either answer is fine if you write it down in `DEVLOG.md`.
- The O₂ balance is a simplification (it ignores the small change in circuit volume when O₂ is consumed). It's still good enough to show the danger.
- Steady state with consumption is `FiO2_fresh − VO2/Q`. At 30% and 1 L/min that's about 5%, which is lethal. This is why low-flow O₂ needs watching.

### Checkpoint

Circuit FiO₂ starting at 0.95, with fresh gas set to 30%:

| total flow | VO₂ | 1 min | 5 min | 10 min | 30 min |
|---|---|---|---|---|---|
| 2 L/min | off | 0.788 | 0.456 | 0.337 | 0.300 |
| 2 L/min | on | 0.757 | 0.361 | 0.219 ⚠ | 0.175 ⚠ |
| 10 L/min | on | 0.436 | 0.276 | 0.275 | 0.275 |

---

## Week 17 — Decrement times, case scripts, and wrapping up Part 2

**Goal:** context-sensitive decrement times, and a few preset "cases" you can run from the terminal.

**New ideas:** `copy.deepcopy` (simulate a "what if" without touching the real model); `while` loops; measuring *elapsed* time instead of absolute time.

**Read first:** [Python `copy` (shallow vs deep)](https://docs.python.org/3/library/copy.html)

### The science: decrement times

Week 10 showed context sensitivity for propofol. The same thing happens with inhaled agents, for the same reason. Even a low-solubility agent has a slower wash-out after a long case, because muscle and fat have filled and are now giving agent back.

Clinicians care about different decrements for different reasons. Going from about 1.3 MAC to 0.3 MAC is about an 80% decrement, a rough stand-in for waking up. A 90% decrement matters for clearing the remaining effects. As your checkpoint shows, the first half of the wash-out barely changes with case length, while the later decrements grow noticeably.

**References:** Hughes MA, Glass PSA, Jacobs JR. *Anesthesiology* 1992;76:334–41 · Bailey JM. *Clin Pharmacokinet* 2002;41:793–9 · Eger EI II. *Anesthetic Uptake and Action*, 1974 · Philip JH. *Workbook for Gas Man*, chapter 12, 2012

### The big picture

A *what-if* question: "if I turned the vaporizer off right now, how long until the brain level falls by half, by 80%, by 90%?" You can't run that on the real model without ruining it, so you run it on a **copy**:

```
current model ──copy.deepcopy──► independent copy ──dial 0, high flow, step until targets reached──► {50: min, 80: min, 90: min}
(left untouched)
```

`cases.py` then packages a few teaching scenarios you can run from the terminal.

### Learn it: copies, and `while` 🟢

Assigning an object to a new name doesn't copy it. Both names point at the same object. `copy.deepcopy` makes a fully separate one, including the objects inside. Empty `machine/scratch.py`:

```python
import copy


class Bank:
    def __init__(self):
        self.accounts = {"Ana": [100.0]}
        self.year = 0


real = Bank()

same = real
same.year = 5
print(real.year)

what_if = copy.deepcopy(real)
what_if.accounts["Ana"][0] = 999.0
what_if.year = 50
print(real.accounts["Ana"][0], real.year)

start_year = what_if.year
money = 100.0
while money < 200 and (what_if.year - start_year) < 100:
    money = money * 1.1
    what_if.year += 1
print(what_if.year - start_year, round(money, 2))
```

```text
5
100.0 5
8 214.36
```

- `same = real` isn't a copy, so changing one changes both. That can catch you out.
- `what_if` is independent, and `real` stays as it was.
- `while` repeats for as long as its condition is true. Use it when you don't know the number of passes in advance. Always give it a second condition as a cap, so it can't run forever.
- Measure elapsed time by subtracting a saved start (`what_if.year - start_year`), rather than relying on the absolute value. An earlier version of this project made that mistake with its washout timer, so it never ran after 30 minutes.

### Build it: `decrement.py` 🔴

Create `machine/decrement.py`, with this function:

```python
def decrement_times(model, targets=(50, 80, 90), max_minutes=60, dt=0.1/60):
    """Minutes for brain (VRG) concentration to fall by each % after the
    vaporizer is switched off, high-flow washout, starting from model's CURRENT state."""
```

1. Make a deep copy. Never touch the original.
2. Save the copy's starting VRG concentration. If it's under 0.01, return an empty dictionary.
3. Set the dial to 0, and the flows to high (O₂ 10 L/min, others 0). Save `t0 = sim.time`.
4. Step the copy until every target is found, or until `max_minutes` of **washout** time have passed. A target of 80 means "fallen to 20% of the starting concentration". Record elapsed washout minutes in a dictionary, keyed by target, and return it.

<details>
<summary><b>Hint</b></summary>

`while (sim.time - t0) < max_minutes and len(results) < len(targets):`. After each step, work out the fraction remaining, then loop over the targets that aren't in `results` yet.

</details>
<details>
<summary><b>Answer</b></summary>

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
    sim.o2_flow, sim.air_flow, sim.n2o_flow = 10.0, 0.0, 0.0
    t0 = sim.time                  # remember when washout STARTED
    results = {}
    while (sim.time - t0) < max_minutes and len(results) < len(targets):
        sim.step(dt)
        fraction = sim.compartments["VRG"].concentration / start_conc
        for target in targets:
            if target not in results and fraction <= 1 - target / 100:
                results[target] = sim.time - t0
    return results


```

</details>

### Check it

Add this at the bottom of `decrement.py`. It takes a little while, because it runs up to three hours of simulated time in 0.1-second steps.

```python
if __name__ == "__main__":
    from agents import AGENTS
    from volatile import VolatilePKModel
    from machine_tools import run_minutes
    from checks import check

    for case_minutes, (d50, d80, d90) in [(10, (2.9, 6.5, 9.2)), (60, (3.1, 7.0, 10.7)),
                                          (180, (3.2, 7.9, 14.2))]:
        m = VolatilePKModel(AGENTS["sevoflurane"])
        m.dial = 2.0
        m.fresh_gas_flow = 8.0
        run_minutes(m, case_minutes)
        times = decrement_times(m)
        check(f"{case_minutes}-min case: d50", times[50], d50, tol=0.1)
        check(f"{case_minutes}-min case: d80", times[80], d80, tol=0.1)
        check(f"{case_minutes}-min case: d90", times[90], d90, tol=0.1)
    check("the real model wasn't touched (time still 180 min)", m.time, 180, tol=0.01)
```


### Build it: `cases.py` 🔴

Write `machine/cases.py`, with a dictionary of presets:

```python
CASES = {
    "1.3 MAC sevo": dict(agent="sevoflurane", dial=2.6, n2o=0, fgf=6.0),
    "Balanced": dict(agent="sevoflurane", dial=1.2, n2o=60, fgf=6.0),
    "Low-flow trap": dict(agent="sevoflurane", dial=2.0, n2o=0, fgf=0.5),
}
```

Give it a function, `run_case(name, minutes)`, that builds a `DualAgentModel`, sets the dials, and sets the flow on both sub-models. It runs minute by minute, recording the volatile's alveolar level, brain partial pressure and FiO₂, and plots them. Put the demo under `if __name__ == "__main__":`, so importing the file doesn't run it. Have `run_case` return the recorded lists, and check that the `"1.3 MAC sevo"` alveolar level at 10 minutes comes out at about **2.12**.

<details>
<summary><b>Answer</b></summary>

```python
import matplotlib.pyplot as plt

from agents import AGENTS
from dual import DualAgentModel
from machine_tools import run_minutes

CASES = {
    "1.3 MAC sevo": dict(agent="sevoflurane", dial=2.6, n2o=0, fgf=6.0),
    "Balanced": dict(agent="sevoflurane", dial=1.2, n2o=60, fgf=6.0),
    "Low-flow trap": dict(agent="sevoflurane", dial=2.0, n2o=0, fgf=0.5),
}


def run_case(name, minutes):
    c = CASES[name]
    m = DualAgentModel(AGENTS[c["agent"]])
    m.set_dials(c["dial"], c["n2o"])
    m.volatile.fresh_gas_flow = c["fgf"]
    m.n2o.fresh_gas_flow = c["fgf"]
    times, alveolar, brain, fio2 = [], [], [], []
    for minute in range(1, minutes + 1):
        run_minutes(m, 1)
        times.append(minute)
        alveolar.append(m.volatile.alveolar)
        brain.append(m.volatile.brain_partial_pressure())
        fio2.append(m.volatile.circuit_fio2 * 100)
    fig, (top, bottom) = plt.subplots(2, 1, sharex=True)
    top.plot(times, alveolar, label="Alveolar %")
    top.plot(times, brain, label="Brain partial pressure %")
    top.set_title(name)
    top.legend()
    bottom.plot(times, fio2, label="Circuit FiO2 %")
    bottom.set_xlabel("Time (min)")
    bottom.legend()
    plt.show()
    return times, alveolar, brain, fio2


if __name__ == "__main__":
    from checks import check

    times, alveolar, brain, fio2 = run_case("1.3 MAC sevo", 10)
    check("1.3 MAC sevo: alveolar at 10 min", alveolar[-1], 2.12, tol=0.02)
    run_case("Balanced", 10)
    run_case("Low-flow trap", 30)
```

</details>


Commit, and write a `DEVLOG.md` entry. You've finished two projects.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `{}` (empty) for a long case | The loop condition uses `sim.time` instead of `sim.time - t0`, so it thinks time's already up. |
| Times are huge (like 190 min) | You recorded `sim.time` instead of `sim.time - t0`. |
| `KeyError: 90` | That target wasn't reached within `max_minutes`. Make `max_minutes` longer. |
| `XX  the real model wasn't touched` | You used `copy.copy` (shallow), or forgot to copy at all. |
| d80 reached before d50 | The threshold: a target of 80 means "20% left", that is `fraction <= 1 - 80/100`. |

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

d50 barely changes, but d90 grows by about 50% as the muscle and fat fill. This is the same lesson as Week 10, now for inhaled agents.

**References:** Hughes MA, Glass PSA, Jacobs JR. *Anesthesiology* 1992;76:334–41 · Bailey JM. *Clin Pharmacokinet* 2002;41:793–9 · Eger EI II. *Anesthetic Uptake and Action*, 1974 (1.0 and 1.3 MAC depth conventions)

---

## Week 18A — The machine app: controls and session state

**Goal:** the front of an anesthesia machine on a web page: agent choice, flowmeters and a vaporizer, connected to a simulation that survives reruns.

**New ideas:** keeping a running simulation in `st.session_state`; `st.number_input` in columns; a hypoxia warning on the page.

**Read first:** [Streamlit: Session State](https://docs.streamlit.io/develop/concepts/architecture/session-state)

### The science: N₂O comes from the flowmeters

On a real machine there's no N₂O dial. Its concentration is simply its share of the fresh gas: **N₂O % = 100 × N₂O flow ÷ total flow**. A vaporizer, by contrast, *is* a dial, setting its agent's concentration in whatever passes through it. Your helper in this lesson makes this distinction explicit, and makes both sub-models see the same flows.

### The big picture

The machine app, like the TCI app in Week 12, is a **front end only**. All the physics is in Weeks 13–17.

```
sidebar: agent, speed, Start/Stop/Reset
flowmeters + vaporizer ──set_flows / dial──► DualAgentModel (kept in st.session_state)
fragment, every 0.5 s ──run the model (speed × 0.5 s of sim time)──► gas monitor + chart
comparison tab ──two fresh models, run instantly──► overlay plot
```

Two Streamlit ideas are new here. **`st.session_state`** keeps the simulation alive between reruns, so the patient doesn't reset every time you touch a control. **`st.fragment(run_every=...)`** reruns just the monitor on a timer: that's your animation clock.

### Build it: `set_flows` 🟡

Add this to `machine_tools.py`, filling in the rest:

```python
def set_flows(machine, o2, air, n2o):
    """machine is your DualAgentModel. Apply one set of flowmeter readings to both gases."""
    for gas_model in (machine.volatile, machine.n2o):
        # set o2_flow, air_flow and n2o_flow on gas_model
    total = o2 + air + n2o
    # machine.n2o.dial = N2O percent of the fresh gas (0 if total is 0)
```

<details>
<summary><b>Answer</b></summary>

```python
def set_flows(machine, o2, air, n2o):
    """machine is your DualAgentModel. Apply one set of flowmeter readings to both gases."""
    for gas_model in (machine.volatile, machine.n2o):
        gas_model.o2_flow = o2
        gas_model.air_flow = air
        gas_model.n2o_flow = n2o
    total = o2 + air + n2o
    machine.n2o.dial = 100 * n2o / total if total > 0 else 0.0


```

</details>

### Check it

This check runs the low- versus high-flow comparison and the N₂O example without Streamlit, so you know the numbers are right before you build the page. Add it at the bottom of `machine_tools.py`:

```python
if __name__ == "__main__":
    from agents import AGENTS
    from dual import DualAgentModel
    from checks import check

    m = DualAgentModel(AGENTS["sevoflurane"])
    set_flows(m, 4, 0, 6)
    check("N2O dial from flowmeters (%)", m.n2o.dial, 60)
    check("volatile model sees the same N2O flow", m.volatile.n2o_flow, 6)

    # low vs high flow, 1 MAC of each agent, 100% O2
    table = [("sevoflurane", 2.0, 0.5, {1: 0.15, 5: 0.32, 10: 0.44, 20: 0.56}),
             ("sevoflurane", 2.0, 10,  {1: 1.19, 5: 1.55, 10: 1.68, 20: 1.74}),
             ("desflurane",  6.0, 0.5, {1: 0.55, 5: 1.36, 10: 1.88, 20: 2.37}),
             ("isoflurane",  1.15, 10, {1: 0.49, 5: 0.70, 10: 0.80, 20: 0.85})]
    for agent, dial, flow, expected in table:
        m = DualAgentModel(AGENTS[agent])
        set_flows(m, flow, 0, 0)
        m.volatile.dial = dial
        elapsed = 0
        for minute in (1, 5, 10, 20):
            run_minutes(m, minute - elapsed)
            elapsed = minute
            check(f"{agent} {dial}% at {flow} L/min: end-tidal at {minute} min",
                  m.volatile.alveolar, expected[minute], tol=0.006)

    # sevo 2% + 60% N2O at 10 L/min
    m = DualAgentModel(AGENTS["sevoflurane"])
    set_flows(m, 4, 0, 6)
    m.volatile.dial = 2.0
    run_minutes(m, 1)
    check("Et N2O at 1 min (%)", m.n2o.alveolar, 39.8, tol=0.1)
    check("total MAC at 1 min", m.total_mac(), 1.02, tol=0.006)
    run_minutes(m, 9)
    check("Et N2O at 10 min (%)", m.n2o.alveolar, 54.2, tol=0.1)
    check("total MAC at 10 min", m.total_mac(), 1.41, tol=0.006)
```


### Learn it: keeping an object alive across reruns 🟢

Since Streamlit reruns the whole file every time, anything you want to keep has to live in `st.session_state`. Create `machine/scratch_app.py`:

```python
import streamlit as st


class Plant:
    def __init__(self):
        self.height = 1.0

    def grow(self, water):
        self.height += 0.1 * water


with st.sidebar:
    if st.button("Start over"):
        st.session_state.pop("plant", None)

if "plant" not in st.session_state:
    st.session_state.plant = Plant()

plant = st.session_state.plant

water = st.number_input("Water", 0.0, 10.0, 1.0)
if st.button("Water it"):
    plant.grow(water)

st.metric("Height", f"{plant.height:.1f} cm")
```

Run `streamlit run scratch_app.py`. Press the button a few times and watch the height climb. Moving the input doesn't reset it, because the plant lives in session state. Press Ctrl+C when you're done.

### Build it: `machine/app.py`, the controls 🟡

Create `machine/app.py`. These are the imports and the header:

```python
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from agents import AGENTS
from dual import DualAgentModel
from machine_tools import set_flows, run_minutes
from oxygen import fresh_gas_fio2, inspired_hypoxic

DT = 0.1 / 60                                        # 0.1 s steps, in minutes
TICK_S = 0.5                                         # real seconds between screen updates
DIAL_MAX = {"sevoflurane": 8.0, "isoflurane": 5.0, "desflurane": 18.0}

st.set_page_config(page_title="Anesthesia machine", layout="wide")
st.title("Anesthesia machine: uptake and end-tidal gases")
st.caption("Teaching model. Not for clinical use.")
```

Then write:

1. **The sidebar:** a radio for the agent; a `select_slider` called `speed` with options 1, 5, 10, 30 and 60, showing as `10×`; and Start, Stop and Reset buttons in three columns. Start sets `st.session_state.running = True`, and Stop sets it to `False`.
2. **The simulation in session state:** if Reset was pressed, or `"machine"` isn't in session state, or the agent changed, make a new `DualAgentModel`, and store it along with the agent and an empty `history` list. Use `st.session_state.setdefault("running", False)`.
3. **Tabs:** `"Live machine"` and `"Low vs high flow"`.
4. **On the live tab,** in the left of two columns (`st.columns([1, 2])`): number inputs for the O₂, air and N₂O flows, and the vaporizer, using `DIAL_MAX[agent]` as its maximum. Apply them with `set_flows` and `machine.volatile.dial = dial`. If the fresh-gas FiO₂ is under 25%, show `st.error`.

Run it now, and check that Start, Stop and Reset work.

<details>
<summary><b>Answer</b></summary>

```python
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from agents import AGENTS
from dual import DualAgentModel
from machine_tools import set_flows, run_minutes
from oxygen import fresh_gas_fio2, inspired_hypoxic

DT = 0.1 / 60                                        # 0.1 s steps, in minutes
TICK_S = 0.5                                         # real seconds between screen updates
DIAL_MAX = {"sevoflurane": 8.0, "isoflurane": 5.0, "desflurane": 18.0}

st.set_page_config(page_title="Anesthesia machine", layout="wide")
st.title("Anesthesia machine: uptake and end-tidal gases")
st.caption("Teaching model. Not for clinical use.")

# ---------- controls ----------
with st.sidebar:
    agent = st.radio("Agent", ["sevoflurane", "desflurane", "isoflurane"])
    speed = st.select_slider("Time speed", options=[1, 5, 10, 30, 60], value=10,
                             format_func=lambda x: f"{x}×")
    c1, c2, c3 = st.columns(3)
    if c1.button("Start"):
        st.session_state.running = True
    if c2.button("Stop"):
        st.session_state.running = False
    reset = c3.button("Reset")

# ---------- the simulation lives in session_state ----------
if reset or "machine" not in st.session_state or st.session_state.agent != agent:
    st.session_state.machine = DualAgentModel(AGENTS[agent])
    st.session_state.agent = agent
    st.session_state.history = []
st.session_state.setdefault("running", False)
machine = st.session_state.machine

tab_live, tab_compare = st.tabs(["Live machine", "Low vs high flow"])

with tab_live:
    left, right = st.columns([1, 2])
    with left:
        st.subheader("Flowmeters (L/min)")
        o2 = st.number_input("O₂", 0.0, 15.0, 2.0, step=0.1)
        air = st.number_input("Air", 0.0, 15.0, 0.0, step=0.1)
        n2o = st.number_input("N₂O", 0.0, 10.0, 0.0, step=0.1)
        st.subheader("Vaporizer")
        dial = st.number_input(f"{agent} (%)", 0.0, DIAL_MAX[agent], 2.0, step=0.1)
        set_flows(machine, o2, air, n2o)
        machine.volatile.dial = dial
        if o2 + air + n2o > 0 and fresh_gas_fio2(o2, air, n2o) < 0.25:
            st.error("Hypoxic mixture: fresh-gas FiO₂ is below 25%.")
```

</details>


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  N2O dial from flowmeters` | `set_flows`: N₂O % = 100 × N₂O flow ÷ total flow. |
| The monitor doesn't move after Start | The fragment's `run_every` is `None` because `running` was still False when the page last ran fully. Start should set it, and the page must rerun once. |
| The patient resets every time you touch a control | The model isn't stored in `st.session_state`, or your "make a new model" condition is always true. |
| Changing the agent does nothing | The `st.session_state.agent != agent` part of the reset condition. |
| The comparison changes the live patient | You reused `st.session_state.machine` instead of building new `DualAgentModel`s. |
| `XX` in the comparison table | Run `python volatile.py` and `python dual.py` first. If their checks pass, the problem is in `set_flows` or the dial assignment. |
| The page gets slow after a long run | The history list keeps growing. Keep only the last ~2000 snapshots. |

### Checkpoint

Your `machine_tools.py` checks all say `OK`. On the page, the controls appear, the simulation doesn't reset when you change a flow, and O₂ 1 + N₂O 4 shows the hypoxic mixture error.

---

## Week 18B — The machine app: the gas monitor and time-warp

**Goal:** a live gas monitor that updates by itself, with time sped up to as much as 60×.

**New ideas:** `st.fragment(run_every=...)`, a piece of the page that reruns on a timer; a *time multiplier*; `st.metric`.

**Read first:** [Streamlit: fragments](https://docs.streamlit.io/develop/concepts/architecture/fragments) · [`st.metric`](https://docs.streamlit.io/develop/api-reference/data/st.metric)

### The science: watching inspired and end-tidal separate

This is the gas monitor you already know. The difference between inspired and end-tidal is uptake happening in front of you. Early in a case, the gap is wide, because blood is taking agent from the lungs. As tissues fill, end-tidal climbs toward inspired. And when you lower the flow, the inspired level itself stops following the dial closely, because the circuit is rebreathing. Gas Man's advice follows from this: at low flow, you can't assume the dial tells you what the patient breathes.

### The big picture

`st.fragment(run_every=...)` reruns only one function on a timer, without rerunning the whole page. That's your animation clock. With `TICK_S = 0.5`, and 10× speed, each tick advances the simulation by `10 × 0.5` = 5 simulated seconds.

### Learn it: a fragment on a timer 🟢

Replace `machine/scratch_app.py` with this:

```python
import pandas as pd
import streamlit as st

if "ticks" not in st.session_state:
    st.session_state.ticks = 0
    st.session_state.history = []

speed = st.slider("Speed", 1, 10, 1)
st.write("This line only reruns when you move the slider.")


@st.fragment(run_every=0.5)
def clock():
    st.session_state.ticks += speed
    st.session_state.history.append({"tick": st.session_state.ticks,
                                     "value": st.session_state.ticks % 20})
    st.metric("Ticks", st.session_state.ticks)
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df.set_index("tick"))


clock()
```

Run `streamlit run scratch_app.py`. The chart grows by itself. Notice that the rest of the page isn't rerunning. The `fragment` decorator needs Streamlit 1.37 or newer, which is what you installed. Press Ctrl+C when you're done.

### Build it: the gas monitor 🔴

In `app.py`, in the right-hand column of the live tab, write a function called `gas_monitor`, decorated like this:

```python
    with right:
        @st.fragment(run_every=TICK_S if st.session_state.running else None)
        def gas_monitor():
```

Inside it, with `m = st.session_state.machine` and `v = m.volatile`:

1. If running, work out `sim_minutes = speed * TICK_S / 60`, and advance the model by that much, in `DT` steps.
2. Then append a snapshot dictionary to `st.session_state.history`, with `time_min`, `Fi_agent` (`v._inspired()`), `Et_agent`, `Et_N2O`, `FiO2` (as a percent) and `total_MAC`. Keep only the last 2000 snapshots.
3. Show five `st.metric` tiles in `st.columns(5)`, using the latest values from the model.
4. If there's a history, show `st.line_chart` of `Fi_agent` and `Et_agent` against time, and another of `total_MAC`.
5. If `inspired_hypoxic(v.circuit_fio2)`, show `st.warning`.

Call `gas_monitor()` right after defining it.

At 10× speed, set sevo 2% with 6 L/min O₂ and watch Et climb. Then drop the flow to 0.5 L/min, and turn the dial up to see how slowly Et responds. Try O₂ 4 + N₂O 6 (60% N₂O) and watch total MAC climb faster than sevo alone. Then try O₂ 0.2 + N₂O 0.3, and confirm the hypoxic alarms fire.

<details>
<summary><b>Hint</b></summary>

`run_minutes(m, sim_minutes, DT)` from Week 14 does the advancing, and at 60× that's only 300 steps per tick. For the chart: `df = pd.DataFrame(st.session_state.history)`, then `st.line_chart(df.set_index("time_min")[["Fi_agent", "Et_agent"]])`.

</details>
<details>
<summary><b>Answer</b></summary>

```python

    with right:
        @st.fragment(run_every=TICK_S if st.session_state.running else None)
        def gas_monitor():
            m = st.session_state.machine
            v = m.volatile
            if st.session_state.running:
                sim_minutes = speed * TICK_S / 60       # e.g. 10× → 5 sim-seconds per tick
                run_minutes(m, sim_minutes, DT)
                st.session_state.history.append({
                    "time_min": v.time,
                    "Fi_agent": v._inspired(),
                    "Et_agent": v.alveolar,
                    "Et_N2O": m.n2o.alveolar,
                    "FiO2": v.circuit_fio2 * 100,
                    "total_MAC": m.total_mac(),
                })
                st.session_state.history = st.session_state.history[-2000:]

            cols = st.columns(5)
            cols[0].metric("Fi agent", f"{v._inspired():.2f} %")
            cols[1].metric("Et agent", f"{v.alveolar:.2f} %")
            cols[2].metric("Et N₂O", f"{m.n2o.alveolar:.0f} %")
            cols[3].metric("FiO₂", f"{v.circuit_fio2 * 100:.0f} %")
            cols[4].metric("Total MAC", f"{m.total_mac():.2f}")

            df = pd.DataFrame(st.session_state.history)
            if not df.empty:
                st.line_chart(df.set_index("time_min")[["Fi_agent", "Et_agent"]])
                st.line_chart(df.set_index("time_min")[["total_MAC"]])

            if inspired_hypoxic(v.circuit_fio2):
                st.warning("Low inspired oxygen: circuit FiO₂ is below 25%.")

        gas_monitor()
```

</details>


Commit.

### Checkpoint

At 10× speed, sevo 2% at 6 L/min O₂: end-tidal climbs quickly, then slows. Inspired stays at the dial setting as long as the flow is at least the 7 L/min minute ventilation, and falls below the dial when you lower the flow.

---

## Week 18C — The machine app: low flow versus high flow

**Goal:** a side-by-side mode that runs 0.5 vs 10 L/min instantly, to show how flow changes the speed of everything.

**New ideas:** nothing new in the language. This lesson is about using your own model to answer a clinical question.

### The science: flow, solubility and the time to reach a target

Everything in your checkpoint table follows from time constants. At 0.5 L/min, the circuit's time constant is about 14 minutes (7 L ÷ 0.5 L/min), so the circuit itself lags far behind the dial. Gas Man's low-flow and high-flow chapters make the same points with their own exercises, including how much a brief period of high flow at induction speeds things up. Its cost chapter adds the other side: low flow uses much less agent, since less of it is thrown away. Induction with high flow and maintenance with low flow is a common way to get both benefits.

Solubility also matters. Desflurane's advantage shows even at low flow: at 0.5 L/min, it reaches 40% of its dial setting by 20 minutes, sevo only 28%, and iso 16%.

### The big picture

```
comparison tab ──two fresh models, run instantly──► overlay plot
```

The `Run comparison` button only runs when pressed, and creates two new models, so nothing touches your live simulation.

### Build it: the comparison tab 🔴

Add `with tab_compare:` to `app.py`:

1. Number inputs for the vaporizer setting (`key="cmp_dial"`), the low flow (default 0.5) and the high flow (default 10). A slider for minutes, 5–60, default 20.
2. If `st.button("Run comparison")` is pressed, for each of the two flows: make a new `DualAgentModel`, call `set_flows(m, flow, 0, 0)`, set the dial, step minute by minute, and record the end-tidal agent.
3. Make a single matplotlib plot with both curves, plus a dashed line at the dial setting, and show it with `st.pyplot`.

<details>
<summary><b>Answer</b></summary>

```python

with tab_compare:
    st.write("Same agent and dial, two different fresh gas flows, run instantly.")
    cmp_dial = st.number_input("Vaporizer (%)", 0.0, DIAL_MAX[agent], 2.0, step=0.1, key="cmp_dial")
    low = st.number_input("Low flow (L/min O₂)", 0.1, 15.0, 0.5, step=0.1)
    high = st.number_input("High flow (L/min O₂)", 0.1, 15.0, 10.0, step=0.1)
    minutes = st.slider("Minutes", 5, 60, 20)
    if st.button("Run comparison"):
        fig, ax = plt.subplots()
        for label, flow in (("Low", low), ("High", high)):
            m = DualAgentModel(AGENTS[agent])
            set_flows(m, flow, 0, 0)
            m.volatile.dial = cmp_dial
            times, et = [0], [0.0]
            for minute in range(1, minutes + 1):
                run_minutes(m, 1, DT)
                times.append(minute)
                et.append(m.volatile.alveolar)
            ax.plot(times, et, label=f"{label}: {flow} L/min")
        ax.axhline(cmp_dial, linestyle="--", label="Dial")
        ax.set_xlabel("Time (min)")
        ax.set_ylabel("End-tidal agent (%)")
        ax.legend()
        st.pyplot(fig)
```

</details>


Run sevo 2% at 0.5 vs 10 L/min, then desflurane 6% at the same two flows, and compare them with the table below. Commit, and write a `DEVLOG.md` entry: Part 2 is done.

### Things to consider

- **Why a fragment?** Without it, the animation would rerun the *whole* page twice a second, and your number boxes would fight with the timer. The fragment reruns only the monitor; the flowmeters rerun only when you touch them.
- **`run_every=... if running else None`** is the whole start/stop mechanism. `None` means "don't rerun on a timer".
- **What "end-tidal" means here.** Your model's alveolar concentration (FA) stands in for end-tidal. Real end-tidal is a little lower because of dead-space mixing.
- **Low flow is slow for two reasons:** (1) the circuit itself takes time to change (its time constant is circuit volume ÷ fresh gas flow), and (2) at low flow the patient's uptake removes agent faster than fresh gas replaces it. That's why low-flow practice turns the vaporizer *above* the target (overpressure) and why the dial and end-tidal can differ so much.
- **The model's simplification:** rebreathed gas is treated as alveolar gas, and below one minute ventilation all of the shortfall is rebreathed. Real circle systems are messier. The direction and rough size of the effect are right; exact seconds are not.

### Checkpoint

Comparison tab, end-tidal agent (%), vaporizer at 1 MAC, 100% O₂, dial unchanged throughout:

| agent and dial | flow (L/min) | 1 min | 5 min | 10 min | 20 min |
|---|---|---|---|---|---|
| sevo 2% | 0.5 | 0.15 | 0.32 | 0.44 | 0.56 |
| sevo 2% | 2 | 0.52 | 0.91 | 1.12 | 1.27 |
| sevo 2% | 10 | 1.19 | 1.55 | 1.68 | 1.74 |
| des 6% | 0.5 | 0.55 | 1.36 | 1.88 | 2.37 |
| des 6% | 10 | 4.05 | 5.18 | 5.42 | 5.50 |
| iso 1.15% | 0.5 | 0.05 | 0.10 | 0.14 | 0.18 |
| iso 1.15% | 10 | 0.49 | 0.70 | 0.80 | 0.85 |

- Sevo 2% at 10 L/min reaches an end-tidal of 1.6% at about **6.3 min**. At 0.5 L/min it never gets there in 20 minutes. Even with the dial at **8%**, 0.5 L/min takes about **14 min** to reach 2.0%.
- Sevo 2% + 60% N₂O (O₂ 4 + N₂O 6 L/min): end-tidal N₂O **39.8%** at 1 min and **54.2%** at 10 min. Total MAC **1.02** at 1 min and **1.41** at 10 min, against 0.60 and 0.84 for sevo alone.
- Desflurane's solubility advantage shows even at low flow: des at 0.5 L/min reaches 40% of its dial setting by 20 minutes, sevo only 28% and iso 16%.

**References:** Eger EI II. *Anesthetic Uptake and Action*, 1974 · Philip JH. *Gas Man* (gasmanweb.com) · Baum JA. *Low Flow Anaesthesia*, 2nd ed., 2001 · Mapleson WW. The concept of the time constant applied to breathing systems and to the body · Streamlit documentation: fragments (docs.streamlit.io)

---

# PART 3 — BEDSIDE MONITOR (JavaScript, from zero)

No JavaScript experience is assumed. By this point you've written two Python projects, so ideas like variables, functions and loops are familiar, and what's new is the way they're written and the place the code runs.

One idea runs underneath all of Part 3: **a waveform is a list of numbers, one every 4 ms (250 Hz).**

For more practice alongside these lessons, [javascript.info](https://javascript.info/) is the best free tutorial, and the [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) is the reference to search when you're stuck.

---

## Week 19A — A page that talks to you

**Goal:** a web page you typed by hand, running JavaScript you typed by hand, with its output in the browser console.

**New ideas (JS):** HTML tags; `<script>`; the DevTools console; `console.log`; `const` and `let`; numbers and strings; template strings; `if`/`else`; `===`.

**Read first:** [javascript.info: Developer console](https://javascript.info/devtools) · [Variables](https://javascript.info/variables) · [Data types](https://javascript.info/types)

### The science: what the monitor is showing

Each trace you'll build is a picture of one physical event repeating.

| Part of the ECG | What the heart is doing |
|---|---|
| **P wave** | The atria depolarize |
| **PR segment** | The signal is delayed at the AV node |
| **QRS complex** | The ventricles depolarize, and contraction follows |
| **T wave** | The ventricles repolarize |
| **R-R interval** | The time from one beat to the next: 60,000 ÷ heart rate, in ms |

The ECG shows electricity, not blood flow, and that's the reason for building the other traces. A patient can have an organized ECG with no pulse. The arterial line and the pleth show what the heartbeat actually achieved, so in Week 25 you'll trigger them from the ECG's R wave. The capnogram follows breathing instead, and shows CO₂ arriving at the lungs.

### The big picture

Python ran in your terminal. JavaScript runs **inside the web browser**. The browser loads an HTML page, the page says "run this script", and the output goes to a panel called the *console*.

```
index.html ──tells the browser to load──► js/main.js ──prints to──► the console
```

This is your first page in a new language, so this lesson is nearly all 🟢. `main.js` acts as your scratch file through Week 19D. The real monitor code starts going into its own files in Week 19B.

### The smallest possible page 🟢

From `anesthesia-sim/`, make the folders:

```bash
mkdir web
mkdir web/js
```

Create `web/index.html` and type one line:

```html
<h1>Monitor</h1>
```

Save it and double-click the file. A browser opens with the word "Monitor" in large type. That's a real web page: `<h1>` means "heading, level 1", and `</h1>` closes it. Most HTML is like this, an opening tag and a closing tag wrapped around some content.

### A proper page 🟢

The browser was being forgiving. Replace the contents of `index.html` with this:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Monitor</title>
</head>
<body>
  <h1>Monitor</h1>
  <p>Open the console to see what the code is doing.</p>
  <script type="module" src="js/main.js"></script>
</body>
</html>
```

Line by line:

- `<!doctype html>` says this is a modern page. You'll type it at the top of every page.
- `<html lang="en">` wraps everything, and states the page's language.
- `<head>` holds information *about* the page. Nothing in it appears on the page itself.
- `<meta charset="utf-8">` lets symbols such as `µ` and `₂` display correctly.
- `<title>` is the text on the browser tab.
- `<body>` holds what you see.
- `<p>` is a paragraph.
- `<script ...>` is the important one. `src` says which file to run, and `type="module"` turns on the modern way of sharing code between files, which you'll use next lesson.

Now create `web/js/main.js` and type one line:

```js
console.log("hello from main.js");
```

`console.log` is JavaScript's `print`. The semicolon ends the statement. JavaScript can often manage without one, but this course always types it.

### Run a local server 🟢

Double-clicking isn't enough any more, because browsers block scripts of this type on pages opened straight from disk. It's a security rule, not a bug in your code. You need to serve the folder, and Python can do that with one command. In a terminal:

```bash
cd web
python -m http.server 8000
```

That terminal is now busy running the server. Leave it running and open a second terminal if you need one. Ctrl+C stops the server.

In Chrome or Firefox, go to `http://localhost:8000`.

Now open the console: press **F12** (or **Cmd+Opt+J** in Chrome on a Mac) and click the **Console** tab. You should see:

```text
hello from main.js
```

Keep this panel open whenever you work on JavaScript. It's your terminal from now on. You may also see a `404` error for `favicon.ico`. That's only the browser looking for a tab icon, and you can ignore it.

### Try things in the console 🟢

You can type directly into the console, at the prompt on its last line. Each line runs when you press Enter. Try these one at a time:

```js
2 + 2
10 / 4
2 ** 3
"heart" + "beat"
"75" + 5
"75" * 2
0.1 + 0.2
```

You'll see `4`, `2.5`, `8`, `"heartbeat"`, `"755"`, `150` and `0.30000000000000004`.

Look at `"75" + 5`. Python would stop with an error. JavaScript quietly turns the number into text and joins them. **In JavaScript, many mistakes give a strange answer instead of an error.** That's the largest difference from Python, and it's why you'll build a checker next lesson.

### Variables 🟢

Open `main.js`, and below your first line type this. It has nothing to do with medicine, because we're only learning the language:

```js

const shopName = "Corner Cafe";
let cupsSold = 75;

console.log("shop:", shopName);
console.log("cups:", cupsSold);

cupsSold = 80;
console.log("now cups:", cupsSold);
```

Save, then reload the page with Ctrl+R (Cmd+R on a Mac). You reload after every change.

```text
hello from main.js
shop: Corner Cafe
cups: 75
now cups: 80
```

In Python you just write `x = 5`. JavaScript makes you say which kind of variable you're creating:

- **`const`** can never be reassigned. Use this by default.
- **`let`** can be reassigned. Use it when the value needs to change.

You only write `const` or `let` the first time. Notice that `cupsSold = 80;` has neither. Also, JavaScript usually names things `likeThis` rather than Python's `like_this`.

### Template strings 🟢

JavaScript's f-string uses backticks and `${ }`. The backtick key is usually at the top left of the keyboard, and it isn't the same as a single quote. Add this:

```js

const pricePerCup = 3;
console.log(`${shopName} made ${cupsSold * pricePerCup} dollars`);
```

```text
Corner Cafe made 240 dollars
```

### `if`, `else` and `===` 🟢

Add this:

```js

if (cupsSold === 80) {
  console.log("exactly 80");
}

if (cupsSold > 100) {
  console.log("busy day");
} else if (cupsSold < 60) {
  console.log("slow day");
} else {
  console.log("normal day");
}
```

```text
exactly 80
normal day
```

What's different from Python:

- The condition goes in round brackets `( )`.
- Curly braces `{ }` mark the block, not indentation. Indent anyway, so you can read it.
- It's `else if`, not `elif`.
- **Equality is `===`, three equals signs.** JavaScript also has `==`, which converts types first, so `"80" == 80` is `true`. Always use `===`.

In the console, try `"80" == 80`, then `"80" === 80`.

### Your turn: heart rate 🟡

Now apply it. Below your cafe code, create a `let` for a heart rate of `75`, and a `const` for the R-R interval (60000 ÷ heart rate). Then write an `if`/`else if`/`else` that logs a line in exactly this format, using `tachycardia` above 100, `bradycardia` below 60, and `normal rate` otherwise:

```text
HR 75, R-R 800 ms: normal rate
```

Change the heart rate to `150`, then `50`. Save and reload each time, and check that the words change.

<details>
<summary><b>Hint</b></summary>

The `if` is the same shape as the cafe's. You can log inside each branch, or set a `let rateName;` first and do one `console.log` at the end.

</details>
<details>
<summary><b>Answer</b></summary>

```js

let heartRate = 75;
const rr = 60000 / heartRate;
let rateName;

if (heartRate > 100) {
  rateName = "tachycardia";
} else if (heartRate < 60) {
  rateName = "bradycardia";
} else {
  rateName = "normal rate";
}

console.log(`HR ${heartRate}, R-R ${rr} ms: ${rateName}`);
```

</details>

### Your turn: mean arterial pressure 🔴

MAP is approximately `(systolic + 2 × diastolic) ÷ 3`. Create values for a systolic of 120 and a diastolic of 60, then log the MAP. If it's under 65, also log `MAP is low`. You should see:

```text
MAP 80 mmHg
```

Try a pressure of 80/50 too. The MAP should show as 60 and your warning should appear. Be careful with the brackets: without them, the division happens first.

<details>
<summary><b>Answer</b></summary>

```js

const systolic = 120;
const diastolic = 60;
const map = (systolic + 2 * diastolic) / 3;

console.log(`MAP ${map} mmHg`);

if (map < 65) {
  console.log("MAP is low");
}
```

</details>

Commit your work from `anesthesia-sim/`.

### Break it on purpose

Make each change, reload, read the console, then undo it.

1. Add `shopName = "New Cafe";` below the `const`. The console says `TypeError: Assignment to constant variable.`
2. Change one `cupsSold` in a `console.log` to `cupsSol`. The console says `ReferenceError: cupsSol is not defined`. Everything after that line stops running. Click the `main.js:` link beside the error to jump to the line.
3. Delete a closing `}`. The console reports a `SyntaxError`, and *none* of the file runs, not even the first line. The whole file has to make sense before any of it can start.
4. Rename `js/main.js` to `js/mian.js`, reload, and rename it back. The console shows a `404`, which means "file not found".

### If something goes wrong

| What you see | Where to look |
|---|---|
| A blank console, and an error mentioning `CORS` or `origin` | You opened the file by double-clicking. Go to `http://localhost:8000` instead. |
| `This site can't be reached` | The server isn't running. Run `python -m http.server 8000` from inside `web/`. |
| Your changes don't show up | You didn't save, or didn't reload. If it's still old, hard-reload with Ctrl+Shift+R. |
| `404` for `main.js` | The path in `src` doesn't match. It must be `js/main.js`, and the server must be started from inside `web/`. |
| `${heartRate}` appears literally in the output | You used normal quotes instead of backticks. |

### Things to consider

- `const` protects the name, not always the value. You'll see what that means with arrays in Week 19C.
- Why does this course choose `const` by default? Because when you read code later, `const` tells you that value never changes, which is one less thing to keep track of.

### Checkpoint

Your console shows the heart rate and MAP lines, the page shows your heading, and you've seen all four deliberate errors.

---

## Week 19B — Functions, modules and your JavaScript checker

**Goal:** a `gaussian()` function in its own file, and a `tests.html` page that prints `OK` or `XX`, like your Python checks.

**New ideas (JS):** `function`; `return` and `undefined`; `NaN`; `Math`; `typeof`; `&&`; `export` and `import`.

**Read first:** [javascript.info: Functions](https://javascript.info/function-basics) · [Modules, introduction](https://javascript.info/modules-intro)

### The science: building an ECG from bell curves

A real ECG comes from an electrode. A simulator has to make up its numbers, and a good way to do that is to add together bell curves (Gaussians), one for each wave, because each wave is a smooth bump with a height, a position and a width.

| The Gaussian's input | On the ECG |
|---|---|
| `amp` | Height of the wave. It's negative for Q and S, which point down |
| `center` | When in the beat it happens |
| `width` | How narrow it is: QRS is sharp, T is broad |

The same idea is used in serious work. McSharry and colleagues (2003) built a well-known synthetic ECG generator around Gaussians for the P, Q, R, S and T waves. Your version is simpler, placing fixed Gaussians in a beat, but the building block is the same.

**Reference:** [McSharry PE, Clifford GD, Tarassenko L, Smith LA. A dynamical model for generating synthetic electrocardiogram signals. *IEEE Trans Biomed Eng* 2003;50:289–94](https://physionet.org/content/ecgsyn/1.0.0/paper/index.shtml)

### The big picture

JavaScript has no `if __name__ == "__main__":` block, so the checks live on a page of their own.

```
index.html ─► js/main.js  ──┐
                            ├──imports──► js/math.js
tests.html ─► js/tests.js ──┘
```

### Learn it: functions 🟢

Empty `main.js` and type this:

```js
function addTip(bill, tip = 0.2) {
  return bill * (1 + tip);
}

console.log(addTip(50));
console.log(addTip(50, 0.1));
```

Start your server if it isn't running, then reload.

```text
60
55.00000000000001
```

There's that rounding noise again, the same as in Python. Here's the same function in Python:

```python
def add_tip(bill, tip=0.2):
    return bill * (1 + tip)
```

The word is `function` instead of `def`, the body sits in `{ }`, and the statement ends in `;`. Otherwise the two are the same.

### Learn it: how functions fail 🟢

Add these lines, then reload:

```js

function forgotReturn(bill) {
  bill * 2;
}

console.log(forgotReturn(50));
console.log(addTip());
```

```text
undefined
NaN
```

Neither of these is an error, and in Python both would be.

- A function with no `return` gives back **`undefined`**, meaning "no value". (Python gives back `None`, but `None` makes your next line of math crash. `undefined` usually doesn't.)
- You called `addTip()` with no input, so `bill` was `undefined`, and doing math with `undefined` gives **`NaN`**, or "not a number".

`NaN` also spreads: any math involving `NaN` gives `NaN`. A mistake early in a calculation can come out as a `NaN` many steps later, with no message. A checker catches this, so you'll build one shortly.

### Learn it: `Math`, and a detail about powers 🟢

Add these lines:

```js

console.log(Math.abs(5 - 8));
console.log(Math.round(2.6));
console.log(Math.exp(0));
console.log(-(3 ** 2));
console.log((1.23456).toFixed(2));
console.log(typeof 5, typeof "five");
console.log(5 > 2 && 1 > 2);
```

```text
3
3
1
-9
1.23
number string
false
```

- `Math.exp(x)` is eˣ, and `**` means "to the power of", as in Python.
- JavaScript refuses to run `-3 ** 2`, because it's unclear which should happen first, the minus or the power. The brackets in `-(3 ** 2)` are required.
- `.toFixed(2)` gives text with 2 decimals.
- `typeof` gives a value's type as text.
- `&&` is Python's `and`. `||` is `or`, and `!` is `not`.

### Learn it: modules 🟢

JavaScript shares code between files in a very similar way to Python, with two differences you need to type. Create `web/js/shapes.js`:

```js
export function squareArea(side) {
  return side ** 2;
}

function secretHelper() {
  return "you can't import me";
}
```

Then replace everything in `main.js` with this:

```js
import { squareArea } from "./shapes.js";

console.log(squareArea(3));
```

```text
9
```

| | Python | JavaScript |
|---|---|---|
| Making something shareable | Everything is shareable | You must write `export` in front of it |
| Bringing it in | `from shapes import square_area` | `import { squareArea } from "./shapes.js";` |
| Several things | `from shapes import a, b` | `import { a, b } from "./shapes.js";` |
| The file's name | No `.py` | The full name with `.js`, starting with `./`, which means "this folder" |
| The whole file | `import shapes`, then `shapes.a` | `import * as shapes from "./shapes.js";`, then `shapes.a` |
| Renaming | `from shapes import a as b` | `import { a as b } from "./shapes.js";` |

Classes and constants import the same way, as long as they have `export` in front. This all works because of `type="module"` in your HTML.

### Build it: `gaussian` 🟡

Now the first real file of the monitor. Create `web/js/math.js`, with an exported function:

```
gaussian(x, amp, center, width) = amp · e^( −(x − center)² / (2 · width²) )
```

Test it from `main.js`, by importing it and logging these two calls:

```js
console.log(gaussian(0.4, 1, 0.4, 0.04));
console.log(gaussian(0.5, 1, 0.4, 0.04));
```

<details>
<summary><b>Hint</b></summary>

The power needs brackets, as you just saw: `-((x - center) ** 2)`. Then divide by `(2 * width ** 2)`, and put that whole thing inside `Math.exp( )`.

</details>
<details>
<summary><b>Answer</b></summary>

```js
export function gaussian(x, amp, center, width) {
  return amp * Math.exp(-((x - center) ** 2) / (2 * width ** 2));
}
```

</details>

You should see:

```text
1
0.0439369336234075
```

At the center, the height equals `amp`. A little way off the center, it has nearly vanished.

### Build it: a page for checks 🟡

Create `web/tests.html`. You don't need to be shown this one: it's your `index.html`, with the title `Tests`, a heading of `Open the console`, no paragraph, and a script of `js/tests.js`.

<details>
<summary><b>Answer</b></summary>

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Tests</title>
</head>
<body>
  <h1>Open the console</h1>
  <script type="module" src="js/tests.js"></script>
</body>
</html>
```

</details>

### Build it: the JavaScript checker 🟡

Create `web/js/tests.js`. You've already built this tool once, in `checks.py`. Now translate it, using this table:

| Python | JavaScript |
|---|---|
| `tol=0.01` | `tol = 0.01` |
| `isinstance(got, (int, float))` | `typeof got === "number"` |
| `and` | `&&` |
| `not ok` | `!ok` |
| `abs(...)` | `Math.abs(...)` |
| `f"{got:.4f}"` | `got.toFixed(4)` |
| `failures += 1` | `failures++` |
| `# note` | `// note` |

Your `check(label, got, expected, tol = 0.01)` should:

- Compare within `tol` if **both** values are numbers. Otherwise, compare with `===`.
- Show `got` with 4 decimals if it's a number, or as it is otherwise.
- Log one line in the same format as Python: `OK  label: got ..., expected ...`
- Add one to a `let failures = 0;`, declared above the function, whenever a check fails.

Import `gaussian` at the top. Below your function, add two checks and a summary. The summary has to stay the **last** thing in the file:

```js
// --- Week 19B ---
check("gaussian peak", gaussian(0.4, 1, 0.4, 0.04), 1.0);
check("gaussian 0.1 away", gaussian(0.5, 1, 0.4, 0.04), 0.0439, 0.0001);

// summary: keep this last
if (failures === 0) {
  console.log("ALL OK");
} else {
  console.log(`${failures} XX: fix the first one`);
}
```

Go to `http://localhost:8000/tests.html`, open the console there, and you should see:

```text
OK  gaussian peak: got 1.0000, expected 1
OK  gaussian 0.1 away: got 0.0439, expected 0.0439
ALL OK
```

<details>
<summary><b>Hint</b></summary>

Declare `let ok;` and `let shown;` at the start of the function, before the `if`. A variable created inside `{ }` exists only inside those braces, so if you declared them inside the `if`, you couldn't use them afterward.

</details>
<details>
<summary><b>Answer</b></summary>

```js
import { gaussian } from "./math.js";

let failures = 0;

function check(label, got, expected, tol = 0.01) {
  let ok;
  let shown;

  if (typeof got === "number" && typeof expected === "number") {
    ok = Math.abs(got - expected) <= tol;
    shown = got.toFixed(4);
  } else {
    ok = got === expected;
    shown = got;
  }

  let mark = "OK";
  if (!ok) {
    mark = "XX";
    failures++;
  }

  console.log(`${mark}  ${label}: got ${shown}, expected ${expected}`);
}

// --- Week 19B ---
check("gaussian peak", gaussian(0.4, 1, 0.4, 0.04), 1.0);
check("gaussian 0.1 away", gaussian(0.5, 1, 0.4, 0.04), 0.0439, 0.0001);

// summary: keep this last
if (failures === 0) {
  console.log("ALL OK");
} else {
  console.log(`${failures} XX: fix the first one`);
}
```

</details>

From now on, you add new checks just above the `// summary` line, and any new imports at the top.

### Your turn 🔴

Add two more exported functions to `math.js`:

1. `rrMs(hr)` gives the R-R interval in ms.
2. `samplesPerBeat(hr)` gives the number of samples in one beat at 250 samples per second, rounded to a whole number. It should call `rrMs`.

Import them in `tests.js`, by adding them to the top line, and write four checks: the R-R interval and the samples per beat, at 75 and 150 bpm. Sample counts must match exactly, so use a tolerance of `0`. You should see:

```text
OK  R-R at 75 bpm: got 800.0000, expected 800
OK  R-R at 150 bpm: got 400.0000, expected 400
OK  samples per beat at 75 bpm: got 200.0000, expected 200
OK  samples per beat at 150 bpm: got 100.0000, expected 100
ALL OK
```

<details>
<summary><b>Hint</b></summary>

There are `rrMs(hr) / 1000` seconds in a beat, and 250 samples in each second. `Math.round()` gives a whole number.

</details>
<details>
<summary><b>Answer</b></summary>

In `math.js`:

```js

export function rrMs(hr) {
  return 60000 / hr;
}

export function samplesPerBeat(hr) {
  return Math.round(rrMs(hr) * 250 / 1000);
}
```

In `tests.js`, on the top line:

```js
import { gaussian, rrMs, samplesPerBeat } from "./math.js";
```

And above the summary:

```js
check("R-R at 75 bpm", rrMs(75), 800);
check("R-R at 150 bpm", rrMs(150), 400);
check("samples per beat at 75 bpm", samplesPerBeat(75), 200, 0);
check("samples per beat at 150 bpm", samplesPerBeat(150), 100, 0);
```

</details>

Commit.

### Break it on purpose

1. In `math.js`, remove the word `export` from `gaussian`. Reload `tests.html`. The console says `The requested module './math.js' does not provide an export named 'gaussian'`. (Firefox words this differently.)
2. Change `"./math.js"` to `"./math"` in `tests.js`. You'll see a `404` and a module load error, because the `.js` ending is required.
3. Remove `return` from `rrMs`. Look at how the checks print: `got undefined` and `got NaN`, each marked `XX`. Your checker just caught a bug that JavaScript itself stayed silent about.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `does not provide an export named ...` | That function is missing `export`, or its name is spelled differently in the two files. |
| `Failed to load module script` or a `404` | A wrong path. It needs `./`, the `.js`, and matching spelling. |
| `Cannot use import statement outside a module` | The `<script>` tag is missing `type="module"`. |
| `got NaN` | A function received `undefined`, often from a misspelled name or a missing argument. |
| `got undefined` | A function is missing its `return`. |
| `Unary operator used immediately before exponentiation expression` | You wrote `-a ** 2`. Put brackets around it: `-(a ** 2)`. |
| No summary line at the bottom | Something crashed before the end. Look for a red error higher up. |

### Things to consider

- `tests.js` and your Python `checks.py` do the same job, and you wrote both yourself, so when a check looks wrong later, you'll know exactly how to investigate.
- Why keep `math.js` free of anything that touches the page? Because a file with only calculations can be tested from any page.

### Checkpoint

`tests.html` ends in `ALL OK`, and `gaussian(0.5, 1, 0.4, 0.04)` ≈ **0.0439**.

---

## Week 19C — Lists of numbers: arrays and loops

**Goal:** `linspace()`, and your first waveform: a P wave stored as a list of numbers.

**New ideas (JS):** arrays; `.length`; `.push`; the `for` loop; `for...of`; `Math.max` with `...`.

**Read first:** [javascript.info: Arrays](https://javascript.info/array) · [Loops](https://javascript.info/while-for)

### The science: a waveform is sampled

A monitor doesn't store a continuous line. It measures the signal many times a second and stores the numbers. This course uses 250 samples per second, or one every 4 ms.

That sets how much detail you get. A P wave of 80 ms is 20 samples, and a QRS of 100 ms is 25. Sampling can miss the top of a narrow peak, which you'll actually see in Week 21: the R wave in a 25-sample QRS reaches only 0.917 instead of 1.0, because no sample lands exactly on the top.

### The big picture

Every trace on the monitor is an array of numbers. By the end of this lesson you'll have made one.

```
linspace(5) ──► [0, 0.25, 0.5, 0.75, 1] ──gaussian at each x──► a P wave
```

### Learn it: arrays 🟢

Empty `main.js` and type this:

```js
const snacks = ["apple", "nuts", "cheese"];

console.log(snacks.length);
console.log(snacks[0]);
console.log(snacks[2]);
console.log(snacks[3]);

snacks.push("grapes");
console.log(snacks.length);
```

Go back to `http://localhost:8000`.

```text
3
apple
cheese
undefined
4
```

- `snacks.length` is Python's `len(snacks)`. It has no brackets after it.
- `snacks.push("grapes")` is Python's `snacks.append("grapes")`.
- Positions start at 0, as in Python.
- Reading past the end gives `undefined`. Python would raise an `IndexError`. That's one more silent failure to watch for.
- `snacks` is a `const`, yet `push` worked. `const` means the name will always point to this same array, but the contents of the array can still change.

### Learn it: the `for` loop 🟢

Add this:

```js

for (let i = 0; i < 3; i++) {
  console.log("i is", i);
}
```

```text
i is 0
i is 1
i is 2
```

This does what Python's `for i in range(3):` does, in three visible parts separated by semicolons:

| Part | Meaning |
|---|---|
| `let i = 0` | Start here |
| `i < 3` | Keep going while this is true |
| `i++` | After each pass, add 1 |

When you only want the values, and not their positions, there's a shorter form. Type this:

```js

for (const snack of snacks) {
  console.log(`I like ${snack}`);
}
```

```text
I like apple
I like nuts
I like cheese
I like grapes
```

That's `for snack in snacks:`. Be careful to write **`of`** here. JavaScript also has a `for...in`, which gives you something else.

### Learn it: building an array 🟢

Here's the most common pattern in Part 3. Type this function, which makes a list of the first `n` even numbers:

```js

function firstEvens(n) {
  const out = [];
  for (let i = 0; i < n; i++) {
    out.push(i * 2);
  }
  return out;
}

const evens = firstEvens(4);
console.log(evens.length, evens[3]);
console.log(Math.max(2, 9, 4));
console.log(Math.max(...evens));
```

```text
4 6
9
6
```

Make an empty array, loop, push, return. `Math.max` wants separate numbers, not an array, so `...evens` spreads the array out into separate values.

### Build it: `linspace` 🟡

In `math.js`, write and export `linspace(n)`, which gives `n` evenly spaced values from 0 to 1. For example, `linspace(5)` gives `[0, 0.25, 0.5, 0.75, 1]`. Each value is its position divided by `n - 1`. Use the same pattern as `firstEvens`.

Add `linspace` to the import line at the top of `tests.js`, and these above the summary:

```js
// --- Week 19C ---
check("linspace(5) has 5 values", linspace(5).length, 5, 0);
check("linspace(3) middle value", linspace(3)[1], 0.5);
check("linspace(5) last value", linspace(5)[4], 1);
check("linspace(1) doesn't divide by zero", linspace(1)[0], 0);
```

If you wrote the simple version, the first three pass and the last fails:

<details>
<summary><b>Answer</b>: the simple version</summary>

```js

export function linspace(n) {
  const out = [];
  for (let i = 0; i < n; i++) {
    out.push(i / (n - 1));
  }
  return out;
}
```

</details>

```text
OK  linspace(5) has 5 values: got 5.0000, expected 5
OK  linspace(3) middle value: got 0.5000, expected 0.5
OK  linspace(5) last value: got 1.0000, expected 1
XX  linspace(1) doesn't divide by zero: got NaN, expected 0
1 XX: fix the first one
```

With `n = 1`, the code calculates `0 / 0`, which is `NaN`. Python would have crashed there. JavaScript carried on, and your checker caught it.

### Your turn: fix it 🟡

Change the loop so that if `n` is 1, it pushes `0`, and otherwise it pushes what it does now.

<details>
<summary><b>Answer</b></summary>

```js
export function linspace(n) {
  const out = [];
  for (let i = 0; i < n; i++) {
    if (n === 1) {
      out.push(0);
    } else {
      out.push(i / (n - 1));
    }
  }
  return out;
}
```

</details>

```text
OK  linspace(1) doesn't divide by zero: got 0.0000, expected 0
ALL OK
```

### Your turn: your first waveform 🔴

Write this function in `math.js`:

**`pWave(n, amp = 0.15)`** returns an array of `n` numbers. For each `x` in `linspace(n)`, the value is a Gaussian with height `amp`, center `0.5` and width `0.15`.

Add `pWave` to the import line, then write checks that produce these results, using a tolerance of `0.0001` for the wave values and `0` for the count. Index 10 is the middle of 21 samples. The last check uses `pWave(21, 0.3)`.

```text
OK  P wave has 21 samples: got 21.0000, expected 21
OK  P wave peaks in the middle: got 0.1500, expected 0.15
OK  P wave is small at the edge: got 0.0006, expected 0.0006
OK  tallest sample equals amp: got 0.1500, expected 0.15
OK  amp can be changed: got 0.3000, expected 0.3
ALL OK
```

<details>
<summary><b>Hint</b></summary>

Same pattern again, using `for...of` over `linspace(n)`. In `tests.js`, store `const p = pWave(21);` first, so the checks can read `p[10]` and `Math.max(...p)`.

</details>
<details>
<summary><b>Answer</b></summary>

In `math.js`:

```js

export function pWave(n, amp = 0.15) {
  const out = [];
  for (const x of linspace(n)) {
    out.push(gaussian(x, amp, 0.5, 0.15));
  }
  return out;
}
```

In `tests.js`:

```js
const p = pWave(21);
check("P wave has 21 samples", p.length, 21, 0);
check("P wave peaks in the middle", p[10], 0.15, 0.0001);
check("P wave is small at the edge", p[0], 0.0006, 0.0001);
check("tallest sample equals amp", Math.max(...p), 0.15, 0.0001);
check("amp can be changed", pWave(21, 0.3)[10], 0.3, 0.0001);
```

</details>

That array of 21 numbers is a P wave. In Week 21 it gets drawn on a canvas, and from there the rest of the monitor is more waves like this one.

Commit.

### Break it on purpose

1. In `linspace`, change `i < n` to `i <= n`. The length check goes `XX`, because you've made one value too many. This off-by-one mistake is a very common bug.
2. Change `const out = [];` to `const out;`. The console says `Missing initializer in const declaration`, because a `const` must get its value immediately.
3. In `pWave`, change `of` to `in`, and read the results. The `for...in` loop gives you positions as text (`"0"`, `"1"`, ...), and the numbers come out wrong with no error. This is why you were warned about it.
4. Change the check to `Math.max(p)`, without the `...`. You get `NaN`.

### If something goes wrong

| What you see | Where to look |
|---|---|
| A loop never ends and the tab freezes | The `i++` is missing, or the condition can never become false. Close the tab, fix the code, and reopen it. |
| `linspace(5)` has 6 values | `i <= n` should be `i < n`. |
| `Cannot read properties of undefined (reading 'length')` | The function forgot to `return` its array. |
| `Identifier 'p' has already been declared` | You declared the same name twice in `tests.js`. Pick a new name. |
| `P wave peaks in the middle` shows `got 0.0000` | A `for...in` where you wanted `for...of`, or the arguments to `gaussian` are in the wrong order. |

### Things to consider

- Later you'll learn `.map()`, which does this empty-array-and-push pattern in one line, like a Python list comprehension. You'll appreciate it more for having typed the long way first.
- Next, in Week 19D, you'll bundle data and functions together with JavaScript classes, using a scratch example first. Then the monitor can start to take shape.

### Checkpoint

`tests.html` ends in `ALL OK`. `pWave(21)` has **21** samples, peaks at **0.15** in the middle, and is about **0.0006** at the edges.

**References:** *Project 3: Medical Waveform Training Platform* textbook, Ex 1.1 (Gaussian ECG components)

---

## Week 19D — Objects and classes in JavaScript

**Goal:** translate your Python `Compartment` class into JavaScript.

**New ideas (JS):** object literals; `class`, `constructor`, `this`; `new`; JSON.stringify; `Math.max` for clamping.

**Read first:** [javascript.info: Objects](https://javascript.info/object) · [Class basic syntax](https://javascript.info/class)

### The science: the same equation, in another language

There's no new science here, which is the point. This is the compartment from Week 13: `dC/dt = (Q/V) · (C_arterial − C/λ)`. Translating something you already understand is the fastest way to learn a second language, because when something goes wrong, you know the problem is the language, not the idea. In Week 29, you'll use this class for the whole anesthesia machine, and the two languages will have to agree to 3 decimal places.

### The big picture

```
math.js   gets one more export: class Compartment
```

### Learn it: objects and classes 🟢

Empty `main.js` and type this:

```js
const rex = { name: "Rex", age: 3 };

console.log(rex.name, rex["age"]);
rex.age = 4;
rex.toy = "ball";
console.log(JSON.stringify(rex));
console.log(rex.colour);

class Dog {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  speak() {
    return `${this.name} says woof`;
  }

  birthday() {
    this.age = this.age + 1;
  }
}

const fido = new Dog("Fido", 7);
console.log(fido.speak());
fido.birthday();
console.log(fido.age);
```

```text
Rex 3
{"name":"Rex","age":4,"toy":"ball"}
undefined
Fido says woof
8
```

Here's Week P2's `Dog` translated:

| Python | JavaScript |
|---|---|
| `{"name": "Rex"}` and `d["name"]` | `{ name: "Rex" }` and `d.name` or `d["name"]` |
| `class Dog:` | `class Dog {` |
| `def __init__(self, name):` | `constructor(name) {` |
| `self.name = name` | `this.name = name;` |
| `def speak(self):` | `speak() {`. You don't list `this` as an input |
| `Dog("Rex", 3)` | `new Dog("Rex", 3)`. You must write `new` |
| `def __repr__` | No direct equal. Use `JSON.stringify(obj)` when you need to see inside |

`rex.colour` gives `undefined`, not an error. It's the same silent failure as before.

### Build it: `Compartment` 🔴

At the end of `math.js`, write and export `class Compartment`:

- `constructor(name, volumeL, flowLmin)` stores `name`, `volume` and `flow`, and sets `concentration` to 0.
- `partialPressure(lam)`
- `rateOfChange(cArterial, lam)`
- `update(cArterial, lam, dt)` is an Euler step, clamped with `Math.max(0, ...)`.

Keep your Python `compartment.py` open beside it.

<details>
<summary><b>Hint</b></summary>

It's the same as Python with `self.` changed to `this.`. Inside a class, you must write `this.` every time, or you'll get a `ReferenceError`.

</details>
<details>
<summary><b>Answer</b></summary>

```js

export class Compartment {
  constructor(name, volumeL, flowLmin) {
    this.name = name;
    this.volume = volumeL;
    this.flow = flowLmin;
    this.concentration = 0;
  }

  partialPressure(lam) {
    return this.concentration / lam;
  }

  rateOfChange(cArterial, lam) {
    return (this.flow / this.volume) * (cArterial - this.partialPressure(lam));
  }

  update(cArterial, lam, dt) {
    this.concentration = Math.max(0, this.concentration + this.rateOfChange(cArterial, lam) * dt);
  }
}
```

</details>

### Check it

Add `Compartment` to the import line at the top of `tests.js`, and these lines above the summary:

```js
// --- Week 19D ---
const vrg = new Compartment("VRG", 6, 4.2);
check("Compartment wash-in rate (same as Python)", vrg.rateOfChange(2.0, 1.7), 1.4);
vrg.concentration = 3.4;
check("Compartment at equilibrium", vrg.rateOfChange(2.0, 1.7), 0, 1e-9);
vrg.update(2.5, 1.7, 0.1);
check("Compartment after one Euler step", vrg.concentration, 3.435, 0.001);
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `ReferenceError: volume is not defined` | You wrote `volume` instead of `this.volume` inside the class. |
| `Class constructor Compartment cannot be invoked without 'new'` | You forgot `new`. |
| `got NaN` | A misspelled property, such as `this.volume` set but `this.vol` read. It gives `undefined`, and math on that gives `NaN`. |
| `does not provide an export named 'Compartment'` | `export` is missing in front of `class`. |

### Checkpoint

`tests.html` ends in `ALL OK`, and the wash-in rate matches Python's **1.4**. You've now covered the language itself. From here on, it's about the browser.

---

## Week 20A — HTML: building the page

**Goal:** a monitor page with a heading, labeled controls and dark monitor styling.

**New ideas:** common HTML elements; `id` and `class`; `<label>`, `<input>`, `<select>`, `<span>`; CSS rules and classes.

**Read first:** [MDN: HTML basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content) · [MDN: CSS basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Styling_the_content)

### The science: why monitors look the way they do

The black screen and bright traces began as a property of the oscilloscope tube, and they've stayed because they work: bright lines on black are easy to read in a dim OR from across the room. Colors are fairly consistent by convention, such as green for ECG, red for arterial pressure, cyan or blue for pleth and yellow for CO₂. You'll use that convention, so the page reads like a real monitor.

### The big picture

```
index.html   what's on the page (structure)
style.css    how it looks
main.js      how it behaves (next lesson)
```

### Learn it: a scratch page 🟢

From now on `main.js` is real code, so scratch work needs a home of its own. You've built this kind of page twice now, so type this from what you know into `web/scratch.html`, with a form and some styling:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Scratch</title>
  <link rel="stylesheet" href="scratch.css">
</head>
<body>
  <h1>Coffee order</h1>
  <p class="note">Choose your order.</p>
  <label>Cups <input id="cups" type="range" min="1" max="10" value="2"></label>
  <span id="cups-out">2</span>
  <label>Size
    <select id="size">
      <option value="small">Small</option>
      <option value="large">Large</option>
    </select>
  </label>
  <label><input id="milk" type="checkbox"> Milk</label>
  <p>Total: <span id="total" class="big">?</span></p>
  <script type="module" src="js/scratch.js"></script>
</body>
</html>
```

And `web/scratch.css`:

```css
body {
  background: #222;
  color: #eee;
  font-family: sans-serif;
}

.note {
  color: gray;
}

.big {
  font-size: 2em;
  color: orange;
}

#total {
  font-weight: bold;
}
```

And an empty `web/js/scratch.js`. Open `http://localhost:8000/scratch.html`.

- `<input type="range">` is a slider. `type="checkbox"` is a tick box. They have no closing tag.
- `<select>` with `<option>`s is a drop-down menu. `value` is what your code will read.
- `<label>` ties text to a control, so clicking the text works too.
- `<span>` is an empty container for text within a line. You'll fill these in from JavaScript.
- **`id` names one specific element,** so JavaScript can find it. It must be unique on the page.
- **`class` names a group** that shares a style.
- In CSS, `body { }` styles that kind of element, `.note { }` styles a class, and `#total { }` styles one id. `<link>` connects the CSS file to the page.

### Build it: the monitor page 🟡

Add these to `index.html`.

1. In the `<head>`, link a stylesheet: `style.css`.
2. Replace the `<p>` paragraph with a section containing these controls, above the `<script>`:
   - A label "Heart rate" and a slider with `id="hr"`, from 30 to 200, starting at 75.
   - A `<span id="hr-out">` showing the value, followed by "bpm".
   - A paragraph: "R-R interval: `<span id="rr-out">`? ms, samples/beat: `<span id="n-out">`?".
   - A drop-down with `id="rhythm"` and options NSR, AFIB, VTACH, VFIB and CHB.

Then write `web/style.css`. Give it a dark background, green text, and a `.controls` class for the section. Use classes, not inline styles.

<details>
<summary><b>Answer</b></summary>

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
  <section class="controls">
    <label>Heart rate <input id="hr" type="range" min="30" max="200" value="75"></label>
    <span id="hr-out">75</span> bpm
    <p>R-R interval: <span id="rr-out">?</span> ms, samples/beat: <span id="n-out">?</span></p>
    <label>Rhythm
      <select id="rhythm">
        <option value="NSR">NSR</option>
        <option value="AFIB">AFIB</option>
        <option value="VTACH">VTACH</option>
        <option value="VFIB">VFIB</option>
        <option value="CHB">CHB</option>
      </select>
    </label>
  </section>
  <script type="module" src="js/main.js"></script>
</body>
</html>
```

```css
body {
  background: #111;
  color: #0f0;
  font-family: sans-serif;
}

.controls {
  border: 1px solid #333;
  padding: 0.5em;
  margin-bottom: 0.5em;
}

.controls label {
  margin-right: 1em;
}
```

</details>

Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| Styles don't apply | `<link>` path doesn't match the file, or you need a hard reload (Ctrl+Shift+R). |
| A `404` for `style.css` | The file isn't in `web/`, or the name is spelled differently. |
| An element appears in the wrong place | A tag that isn't closed. Look at the matching `</section>` and `</select>`. |
| A slider shows but doesn't move | That's normal for now. There's no JavaScript on it yet. |

### Checkpoint

The page is dark with green text, and has a slider and a menu. Nothing responds yet. That's next lesson.

---

## Week 20B — The DOM and events

**Goal:** a heart-rate slider that live-updates the R-R interval and samples per beat.

**New ideas (JS):** the DOM (the page as JS objects); `document.getElementById`; `addEventListener`; `.textContent`; `parseFloat`.

**Read first:** [javascript.info: Document (the DOM)](https://javascript.info/document), first five chapters · [Introduction to browser events](https://javascript.info/events)

### The science: rate and interval

Heart rate and R-R interval are the same information in different forms, 60,000 ÷ HR in ms. The monitor needs the interval, because it builds beats sample by sample. At 75 bpm, each beat lasts 800 ms, or 200 samples. At 150 bpm, it's 400 ms, or 100 samples. That has a physiological consequence you'll see later: at high rates, diastole shrinks far more than systole.

### The big picture

The **DOM** (Document Object Model) is the page as JavaScript sees it: every element in your HTML becomes an object you can read and change.

```
<input id="hr">  ──document.getElementById("hr")──► hrSlider (a JS object)
slider moves ──"input" event──► render() ──► reads hrSlider.value, writes text into <span id="rr-out">
```

This is the pattern for every control from here on: **find the element, listen for an event, update the page.**

### Learn it: the coffee page comes alive 🟢

Type this into `web/js/scratch.js`:

```js
const cups = document.getElementById("cups");
const cupsOut = document.getElementById("cups-out");
const size = document.getElementById("size");
const milk = document.getElementById("milk");
const total = document.getElementById("total");

function render() {
  const n = parseFloat(cups.value);
  const price = size.value === "large" ? 4 : 3;
  const extra = milk.checked ? 0.5 : 0;
  cupsOut.textContent = n;
  total.textContent = `$${n * (price + extra)}`;
}

cups.addEventListener("input", render);
size.addEventListener("change", render);
milk.addEventListener("change", render);
render();

console.log(typeof cups.value, cups.value + 1);
console.log(total.textContent);
```

```text
string 21
$6
```

Move the slider and change the menu to see it respond.

- `document.getElementById("cups")` finds the element. It runs once, and the result is kept in a `const`.
- **Slider values are always strings.** See the console: `cups.value + 1` is `"21"`, not 3. That's why you need `parseFloat`.
- `.textContent` sets the text inside an element.
- `condition ? a : b` picks one of two values, like Python's `a if condition else b`.
- **`addEventListener("input", render)` passes the function itself, with no brackets.** Writing `render()` there would call it once immediately and pass along its return value. It's the same idea as storing functions in your `DRUGS` dictionary.
- `"input"` fires continuously while a slider moves. `"change"` fires when a menu or checkbox changes.
- The last `render()` fills in the page at the start, before anyone touches anything.

### Build it: `main.js` 🔴

Empty `main.js`, and write this for real:

1. Import `rrMs` and `samplesPerBeat` from `math.js`.
2. Find the `hr`, `hr-out`, `rr-out`, `n-out` and `rhythm` elements.
3. Write `render()`, which reads the slider, writes the heart rate, the rounded R-R interval and the samples per beat onto the page.
4. Call it on every `"input"` of the slider, and once at the start.
5. When the rhythm menu changes, log the choice with `console.log`.

<details>
<summary><b>Answer</b></summary>

```js
import { rrMs, samplesPerBeat } from "./math.js";

const hrSlider = document.getElementById("hr");
const hrOut = document.getElementById("hr-out");
const rrOut = document.getElementById("rr-out");
const nOut = document.getElementById("n-out");
const rhythmSelect = document.getElementById("rhythm");

function render() {
  const hr = parseFloat(hrSlider.value);   // slider values are STRINGS
  hrOut.textContent = hr;
  rrOut.textContent = Math.round(rrMs(hr));
  nOut.textContent = samplesPerBeat(hr);
}

hrSlider.addEventListener("input", render);  // runs every time the slider moves
rhythmSelect.addEventListener("change", () => console.log(rhythmSelect.value));
render();                                    // and once at start
```

</details>


`() => console.log(...)` is an *arrow function*: a small unnamed function, like Python's `lambda`. Commit.

### Check it

This lesson is all page wiring, so the page itself is the check. Drag the slider to 75 and you should read **800 ms** and **200** samples/beat. At 150, it's **400 ms** and **100**.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `Cannot read properties of null (reading 'value')` | `getElementById` found nothing. The `id` in the HTML and in the JS don't match exactly, or the `<script>` tag comes *before* the HTML it uses. |
| R-R shows something like `800.0000001` | Round it: `Math.round(...)`. |
| The numbers never change | `addEventListener` is attached to the wrong element, or you wrote `render()` (calling it once) instead of `render`. |
| HR shows `755` when you expected 80 | String joining: `"75" + 5`. Wrap the slider value in `parseFloat`. |

### Checkpoint

HR 75 → R-R **800 ms**, **200** samples/beat. HR 150 → **400 ms**, **100** samples.

---

## Week 21A — Drawing on a canvas

**Goal:** draw any list of numbers as a line on the page.

**New ideas (JS):** `<canvas>` and its 2-D drawing context; mapping values to pixels; default values in an options object; `forEach`.

**Read first:** [MDN Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial): *Basic usage* and *Drawing shapes* · [javascript.info: Destructuring](https://javascript.info/destructuring-assignment)

### The science: reading a trace

The vertical scale of a monitor trace is just a mapping from a physiological value to a position on the screen. A real ECG has a standard scale, typically 1 mV per 10 mm, and arterial traces have a pressure scale. Getting this mapping right is what makes the picture mean something. Your `valueToY` function is that mapping.

### The big picture

```
draw.js  pixels only: valueToY() and drawStatic(canvas, values)
```

`draw.js` never computes physiology, so a drawing bug and a physiology bug can never hide inside each other.

### Learn it: canvas drawing 🟢

Add a canvas to `scratch.html`, above the `<script>`:

```html
  <canvas id="pic" width="300" height="100"></canvas>
```

Then replace everything in `scratch.js` with this:

```js
const canvas = document.getElementById("pic");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "#000";
ctx.fillRect(0, 0, canvas.width, canvas.height);

ctx.strokeStyle = "#0f0";
ctx.lineWidth = 2;
ctx.beginPath();
ctx.moveTo(10, 90);
ctx.lineTo(100, 10);
ctx.lineTo(200, 50);
ctx.stroke();

const heights = [2, 5, 3];
heights.forEach((h, i) => {
  console.log(i, h);
});

function settings(name, { size = 10, color = "red" } = {}) {
  console.log(name, size, color);
}
settings("a");
settings("b", { color: "blue" });
```

```text
0 2
1 5
2 3
a 10 red
b 10 blue
```

- A `<canvas>` is a blank pixel grid. `getContext("2d")` gives you the object you draw with.
- **y = 0 is at the top** of a canvas, and y grows downward. That's why (10, 90) is at the bottom left.
- `beginPath`, `moveTo` (lift the pen), `lineTo` (draw), then `stroke` (actually paint it). Forgetting `stroke()` draws nothing, with no error.
- `forEach((h, i) => ...)` runs a function for each item, passing the value and its position.
- `{ size = 10, color = "red" } = {}` in a function's inputs is JS's version of keyword arguments. You pass an object, and anything you leave out takes its default.

### Build it: `draw.js` 🔴

Create `web/js/draw.js`, with two exported functions:

**`valueToY(v, min, max, height)`** maps a value to a y pixel, so that `min` lands at the bottom (`height`), and `max` at the top (0). First turn `v` into a 0-to-1 range, then flip it.

**`drawStatic(canvas, values, { min = -0.5, max = 1.5, color = "#0f0" } = {})`** paints the canvas black, then draws one connected line through all the values, spread evenly across the width. x for point `i` is `(i / (values.length - 1)) * canvas.width`.

<details>
<summary><b>Hint</b></summary>

`const normalized = (v - min) / (max - min);` then `return height * (1 - normalized);`. In `drawStatic`, use `moveTo` when `i === 0`, and `lineTo` for the rest.

</details>
<details>
<summary><b>Answer</b></summary>

```js
export function valueToY(v, min, max, height) {
  const normalized = (v - min) / (max - min);
  return height * (1 - normalized);       // canvas y = 0 is the TOP, so flip
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
    if (i === 0) {
      ctx.moveTo(x, y);
    } else {
      ctx.lineTo(x, y);
    }
  });
  ctx.stroke();
}
```

</details>

### Check it

Add an import to the top of `tests.js`, and the lines below above the summary. Remember that tests have no real page to draw on, so `valueToY` is what gets checked.

```js
import { valueToY } from "./draw.js";
```

```js
// --- Week 21A ---
check("valueToY: min is the bottom", valueToY(-0.5, -0.5, 1.5, 200), 200);
check("valueToY: max is the top", valueToY(1.5, -0.5, 1.5, 200), 0);
check("valueToY: middle", valueToY(0.5, -0.5, 1.5, 200), 100);
```


Then draw your `pWave(100)` on a canvas in `scratch.js`, with `min: 0` and `max: 0.2`. You should see a smooth bump. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| The trace is upside down | `valueToY` is missing the `1 -` flip. |
| Nothing is drawn, but there are no errors | `ctx.stroke()` is missing, or the stroke color matches the background. |
| A line shoots in from the corner | You used `lineTo` for the first point instead of `moveTo`. |
| `Cannot read properties of null (reading 'getContext')` | The `id` doesn't match, or the `<script>` tag comes before the `<canvas>`. |

### Checkpoint

`valueToY(0.5, -0.5, 1.5, 200)` is **100**, and your P wave appears as a smooth bump.

---

## Week 21B — One heartbeat

**Goal:** generate and draw a single normal-sinus beat.

**New ideas (JS):** `.map` (JS's list comprehension); arrow functions; returning an object; shorthand properties; `new Array(n).fill(0)`.

**Read first:** [javascript.info: Array methods](https://javascript.info/array-methods) (`map`, `forEach`)

### The science: the shape and timing of a beat

A normal beat in this model has this order and timing:

| Part | Duration | Note |
|---|---|---|
| P wave | 80 ms | Starts at 5% of the beat |
| PR gap | 40 ms | AV node delay |
| QRS | 100 ms | R peak 40% of the way through |
| ST segment | 100 ms | Flat |
| T wave | 160 ms | Ends at the baseline |

The rest of the beat is flat. So as the heart rate rises, the flat diastolic part shrinks first.

An earlier version of this project left a small step in the trace, because a wide Gaussian isn't quite zero at its edges. The T wave is at 13% height at its edge. The fix is to subtract the edge value, then rescale. It's a small detail, but one you'd see on the screen.

**Reference:** *Project 3: Medical Waveform Training Platform* textbook, Ex 1.1 and 1.3

### The big picture

```
ecg.js   numbers only: P, QRS and T waves, and nsrBeat(rrMs) → { samples, rOffset, rrMs }
draw.js  pixels only:  valueToY() and drawStatic(canvas, values)
main.js  wires them together: slider → nsrBeat → drawStatic
```

`ecg.js` never touches the page, so `tests.js` can check every number it makes.

### Learn it: `.map` and returning objects 🟢

Replace `scratch.js` with this:

```js
const prices = [10, 20, 30];

const withTax = prices.map(p => p * 1.5);
console.log(JSON.stringify(withTax));

const plus = prices.map(p => p + 1 + 2);
console.log(JSON.stringify(plus));

function place(track, start, song) {
  for (let i = 0; i < song.length; i++) {
    const j = start + i;
    if (j >= 0 && j < track.length) {
      track[j] = song[i];
    }
  }
}

const track = new Array(6).fill(0);
place(track, 4, [7, 8, 9]);
console.log(JSON.stringify(track));

function album(n) {
  const title = "Live";
  return { title, tracks: n, longest: n * 3 };
}
const a = album(4);
console.log(a.title, a.longest);
```

```text
[15,30,45]
[13,23,33]
[0,0,0,0,7,8]
Live 12
```

- `prices.map(p => p * 1.5)` makes a new array by applying a function to each item. It's JS's list comprehension, and it replaces the empty-array-and-push pattern you typed in Week 19C.
- `new Array(6).fill(0)` makes an array of six zeros.
- `place` copies one array into another at a position, skipping anything that would fall off the end, because a later check `j < track.length` protects it.
- `{ title, tracks: n }` makes an object. Writing `title` alone is shorthand for `title: title`.

### Build it: `ecg.js` 🔴

Create `web/js/ecg.js`. Import `linspace` and `gaussian` from `math.js`, and export:

- **`SAMPLE_RATE = 250`**, and **`samplesFor(ms)`**, the number of samples in `ms` milliseconds, rounded, and at least 1.
- **`pWave(n, amp = 0.15)`.** You wrote this in `math.js` in Week 19C. Move it here, since it's ECG code, and rewrite it with `.map`: a Gaussian with center 0.5 and width 0.15. Delete it from `math.js`, and import it from `ecg.js` in `tests.js`.
- **`qrsComplex(n, q = -0.1, r = 1.0, s = -0.2)`.** Q, R and S are three narrow Gaussians (width 0.04) at x = 0.2, 0.4 and 0.6, with amplitudes q, r and s, added together.
- **`tWave(n, amp = 0.3)`.** A Gaussian with center 0.5 and width 0.25, with zero at both edges and `amp` at the peak. Calculate the edge height, `edge = Math.exp(-(0.5 ** 2) / (2 * 0.25 ** 2))`, subtract it, then rescale by `(1 - edge)`.
- **`place(buf, start, wave)`**, as in the scratch file, exported so that later lessons can use it.
- **`nsrBeat(rrMs)`.** Make a zero-filled beat of the right length. The start of P is at `Math.floor(0.05 * total)`. Then, in order: P, the PR gap, QRS, the ST segment and T, using the durations in the table. Place the three waves. Return an object with `samples`, `rOffset` (the position of the R peak, 40% of the way into the QRS) and `rrMs`.

<details>
<summary><b>Hint</b></summary>

In `tWave`: `linspace(n).map(x => amp * (gaussian(x, 1, 0.5, 0.25) - edge) / (1 - edge))`. In `nsrBeat`, `qrsStart = pStart + pS + gap`, and `tStart = qrsStart + qS + stS`. `rOffset` is `qrsStart + Math.round(0.4 * qS)`.

</details>
<details>
<summary><b>Answer</b></summary>

```js
import { linspace, gaussian } from "./math.js";

export const SAMPLE_RATE = 250;
export const samplesFor = ms => Math.max(1, Math.round(ms * SAMPLE_RATE / 1000));

export function pWave(n, amp = 0.15) {
  return linspace(n).map(x => gaussian(x, amp, 0.5, 0.15));
}

export function qrsComplex(n, q = -0.1, r = 1.0, s = -0.2) {
  return linspace(n).map(x => gaussian(x, q, 0.2, 0.04) + gaussian(x, r, 0.4, 0.04) + gaussian(x, s, 0.6, 0.04));
}

export function tWave(n, amp = 0.3) {
  // A width-0.25 gaussian is still 13% high at its edges. Subtract that, then rescale.
  const edge = Math.exp(-(0.5 ** 2) / (2 * 0.25 ** 2));
  return linspace(n).map(x => amp * (gaussian(x, 1, 0.5, 0.25) - edge) / (1 - edge));
}

export function place(buf, start, wave) {
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
  const qrsStart = pStart + pS + gap;
  const tStart = qrsStart + qS + stS;
  place(beat, pStart, pWave(pS));
  place(beat, qrsStart, qrsComplex(qS));
  place(beat, tStart, tWave(tS));
  return { samples: beat, rOffset: qrsStart + Math.round(0.4 * qS), rrMs };
}
```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`SAMPLE_RATE` and `samplesFor(ms)`** turn milliseconds into a number of samples at 250 Hz. Every duration in the ECG goes through this one function.
- **`pWave`, `qrsComplex`, `tWave`** each return an array of `n` numbers. `.map(x => ...)` is JS's list comprehension: it turns every x into a value.
- **The T-wave fix** subtracts the value the curve has at its edges, so the wave starts and ends exactly at zero.
- **`place(buf, start, wave)`** copies one wave into the beat at a position, skipping anything that would fall off the end.
- **`nsrBeat(rrMs)`** makes an empty beat of the right length, works out where each wave starts, places them, and returns an **object** with three named parts. Later weeks rely on `rOffset` to know exactly when the R-wave happens.
- **`valueToY`** flips the axis, because canvas y = 0 is the **top** of the screen.
- **`drawStatic`** paints the background black, then draws one connected line through all the points.

</details>

### Check it

In `math.js`, delete `pWave`. In `tests.js`, take `pWave` off the import from `math.js`, and add these imports at the top:

```js
import { nsrBeat, tWave, qrsComplex, pWave } from "./ecg.js";
```

Then add these above the summary:

```js
// --- Week 21B ---
const beat = nsrBeat(800);
check("NSR 800 ms: samples", beat.samples.length, 200, 0);
check("NSR 800 ms: R-wave index", beat.rOffset, 50, 0);
check("NSR 800 ms: tallest sample is the R wave", beat.samples[beat.rOffset], Math.max(...beat.samples), 1e-9);
check("QRS peak in the 25-sample beat", beat.samples[beat.rOffset], 0.917, 0.002);
check("QRS peak with 41 samples", Math.max(...qrsComplex(41)), 1.0, 0.001);
check("T wave starts at 0", tWave(40)[0], 0, 1e-9);
check("T wave ends at 0", tWave(40)[39], 0, 1e-9);
check("NSR 400 ms: samples", nsrBeat(400).samples.length, 100, 0);
```


### Build it: draw it on the page 🟡

Add `<canvas id="ecg" width="900" height="200"></canvas>` to `index.html`, above the `<script>`. In `main.js`, import `nsrBeat` and `drawStatic`, find the canvas, and in `render()`, draw `nsrBeat(rrMs(hr)).samples`. Changing the heart rate should redraw the beat.

<details>
<summary><b>Answer</b></summary>

```html
  <canvas id="ecg" width="900" height="200"></canvas>
```

```js
import { rrMs, samplesPerBeat } from "./math.js";
import { nsrBeat } from "./ecg.js";
import { drawStatic } from "./draw.js";
```

```js
  nOut.textContent = samplesPerBeat(hr);
  drawStatic(document.getElementById("ecg"), nsrBeat(rrMs(hr)).samples);
```

</details>


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  NSR 800 ms: R-wave index` | The start positions: P starts at 5% of the beat, then P + PR gap, then the QRS. The R is 40% of the way into the QRS. |
| `XX  T wave starts at 0` | The edge correction in `tWave`: subtract `edge`, then divide by `(1 - edge)`. |
| `XX  QRS peak in the 25-sample beat` | Check `qrsComplex` with 41 samples first (should be exactly 1.0). If that passes, the 25-sample value of 0.917 is right; the grid just doesn't land exactly on the peak. |
| The trace is upside down | `valueToY` is missing the `1 -` flip. |
| Nothing is drawn but no errors | `ctx.stroke()` is missing at the end, or the stroke color matches the background. |
| `TypeError: ... is not iterable` | A wave function forgot to `return` its array. |

### Things to consider

- `{ min = -0.5, max = 1.5 } = {}` in a parameter list is *destructuring with defaults*, JS's version of keyword arguments. Call it as `drawStatic(c, v, { max: 2 })`.
- At HR 150 the components need 120 samples, but the beat has only 100. What does `place` do with the T wave? (Real QT intervals shorten with rate. Your stretch could model that.)

### Checkpoint

`nsrBeat(800)`: **200** samples, pStart **10**, qrsStart **40**, tStart **90**, rOffset **50**. The tallest sample is the R wave, at index 50, with height **0.917**: the 25-sample QRS grid doesn't land exactly on its centre. (`qrsComplex(41)` peaks at exactly **1.0**.) The T wave starts and ends at exactly **0**.

---

## Week 22A — Animation: the loop

**Goal:** something that moves smoothly on the page, at a speed that doesn't depend on the computer.

**New ideas (JS):** `requestAnimationFrame`; `performance.now`; measuring real time between frames; carrying a fraction forward.

**Read first:** [MDN: Canvas basic animations](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations) · [MDN: `requestAnimationFrame`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame)

### The science: real time matters

An ECG sweep speed is a real physical quantity. A paper strip typically runs at 25 mm/s, and a clinician reads rate from the spacing. So the trace has to run at the correct speed in *real time*, whether the computer draws 30 or 144 frames a second. The trick is to generate samples based on elapsed real time rather than per frame.

### The big picture

```
loop(now)   about 60 times a second: "how many samples are due since last frame?"
            → produce that many → draw
```

### Learn it: a moving dot 🟢

Replace `scratch.js` with this. It still uses your scratch canvas:

```js
const canvas = document.getElementById("pic");
const ctx = canvas.getContext("2d");

const PIXELS_PER_SECOND = 60;
let x = 0;
let lastT = performance.now();
let frames = 0;

function loop(now) {
  requestAnimationFrame(loop);
  const dt = Math.min(0.1, (now - lastT) / 1000);
  lastT = now;
  frames++;

  x = (x + PIXELS_PER_SECOND * dt) % canvas.width;

  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#0f0";
  ctx.fillRect(x, 45, 10, 10);
}

requestAnimationFrame(loop);
console.log("started");
```

```text
started
```

A green square crosses the canvas every 5 seconds.

- `requestAnimationFrame(loop)` asks the browser to call `loop` before its next screen refresh, about 60 times a second. Calling it again inside `loop` keeps it going.
- The browser passes in the current time in ms, which is `now`.
- `dt` is the real time since the last frame, in seconds. Moving by `speed × dt` is what makes the speed correct on any computer.
- `Math.min(0.1, ...)` caps it. If you switch tabs, the browser pauses, so the next `dt` could be huge.
- `%` wraps `x` back to the start, the same as in Python.

### Learn it: owing a fraction 🟢

At 250 samples per second and 60 frames per second, each frame owes about 4.17 samples. You can't produce a fraction of a sample, so you keep the leftover and carry it forward. Replace `scratch.js` with this:

```js
const SAMPLE_RATE = 250;
let carry = 0;
let produced = 0;

for (let frame = 0; frame < 60; frame++) {
  const dt = 1 / 60;
  carry += dt * SAMPLE_RATE;
  while (carry >= 1) {
    carry -= 1;
    produced++;
  }
}

console.log(produced);
```

```text
250
```

Sixty frames add up to exactly 250 samples, one second's worth, with no drift. JS's `while` works the same as Python's.

### Checkpoint

The square moves at the same speed whatever the frame rate, and you can explain why `dt` is capped. There's nothing to commit to the project yet. This lesson's ideas go into the monitor in Week 22C.

---

## Week 22B — The sweep: a ring buffer

**Goal:** a `Sweep` class that takes samples one at a time, and draws them as a sweeping trace.

**New ideas (JS):** `Float32Array`; a *ring buffer* (an index that wraps with `%`); `NaN` as "blank"; `Object.assign`.

### The science: why a sweep has a gap

A bedside monitor doesn't scroll. It paints left to right, and overwrites the previous sweep as it goes, with a small blank gap ahead of the cursor, so you can see where "now" is. The old data stays visible for comparison. It's why you can look at the left of the screen and see what happened a few seconds ago.

**How it fits on the screen.** With a 900-pixel canvas and 6 seconds per sweep, there are 1500 samples for 900 columns, or about 1.67 samples per column. So several samples have to share a column. If you just kept the last one, you could miss the tip of the QRS, which is very narrow. So `Sweep` keeps the sample *farthest from the baseline* in each column. It's a small decision that preserves what a clinician needs to see.

**Reference:** *Project 3* textbook, Ex 1.6 (canvas display)

### The big picture

```
Sweep.push(v)          collects samples into screen columns and moves the cursor
Sweep.draw()           paints the columns, lifting the pen over the gap
```

### Learn it: a ring buffer 🟢

A ring buffer is a fixed-size array where the write position wraps around to the start. Here's a seat-numbering example. Replace `scratch.js` with this:

```js
const seats = new Float32Array(5).fill(NaN);
let cursor = 0;

for (const person of [10, 20, 30, 40, 50, 60, 70]) {
  seats[cursor] = person;
  cursor = (cursor + 1) % seats.length;
}

console.log(Array.from(seats).join(","));
console.log(cursor);
console.log(Number.isNaN(NaN), NaN === NaN);

const settings = {};
Object.assign(settings, { speed: 3, color: "red" });
console.log(settings.speed, settings.color);
```

```text
60,70,30,40,50
2
true false
3 red
```

- `Float32Array` is an array of decimal numbers with a fixed size, which is faster than a plain array for this.
- `(cursor + 1) % seats.length` wraps it around. The sixth person overwrote the first seat.
- `NaN` makes a good "blank" marker, but **`NaN === NaN` is false**. You must test it with `Number.isNaN(x)`.
- `Object.assign(this, { a, b })` is a short way of setting several attributes at once.

### Build it: `sweep.js` 🟡

Create `web/js/sweep.js`. Here's the constructor, since it's mainly settings:

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
```

Add these methods:

- **`push(v)`:** adds `v` to `pending`, and adds 1 to `acc`. If `acc` has reached `samplesPerColumn`, subtract that from `acc`, store `_combine(pending)` at the cursor, clear `pending`, and advance the cursor with wrapping. Then set the next 12 columns ahead of the cursor to `NaN`, for the gap.
- **`_combine(samples)`:** in `"last"` mode, returns the last sample. Otherwise, returns the sample farthest from `baseline`.
- **`y(v)`:** your `valueToY`, using this sweep's `min`, `max` and height.
- **`draw()`:** paints the canvas black, then walks across the columns drawing a line. Set the `lineWidth` to 1.7. When a column is `NaN`, lift the pen, so the next good column starts a new segment.

<details>
<summary><b>Hint</b></summary>

For `_combine`, track the best sample so far, comparing `Math.abs(v - this.baseline)`. For `draw`, keep `let penDown = false;`. If a value is `NaN`, set it false and `continue`. Otherwise, use `penDown ? c.lineTo(x, y) : c.moveTo(x, y); penDown = true;`.

</details>
<details>
<summary><b>Answer</b></summary>

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
      for (let k = 0; k < 12; k++) {
        this.columns[(this.cursor + k) % this.w] = NaN;
      }
    }
  }

  _combine(samples) {
    if (this.mode === "last") return samples[samples.length - 1];
    // "extreme": keep the sample farthest from baseline, so the QRS spike survives
    let best = samples[0];
    for (const v of samples) {
      if (Math.abs(v - this.baseline) > Math.abs(best - this.baseline)) best = v;
    }
    return best;
  }

  y(v) {
    return this.h * (1 - (v - this.min) / (this.max - this.min));
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
      const y = this.y(v);
      if (penDown) {
        c.lineTo(x, y);
      } else {
        c.moveTo(x, y);
      }
      penDown = true;
    }
    c.stroke();
  }
}
```

</details>

### Check it

A test doesn't need a real canvas, so it passes in a fake object that has only what the constructor reads. Add the import at the top of `tests.js`, and these lines above the summary:

```js
import { Sweep } from "./sweep.js";
```

```js
// --- Week 22B ---
const fakeCanvas = { width: 900, height: 200, getContext: () => ({}) };   // no drawing needed to test the math
const sweep = new Sweep(fakeCanvas);
check("samples per column (1500 / 900)", sweep.samplesPerColumn, 1.6667, 0.0001);
for (let i = 0; i < 750; i++) sweep.push(0);
check("cursor after 750 samples (3 s = half a screen)", sweep.cursor, 450, 1);
check("'extreme' keeps the spike", sweep._combine([0.1, -0.05, 0.9, 0.2]), 0.9);
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| The trace streaks across the gap | The pen isn't lifting. Set `penDown = false` on a `NaN`. |
| The QRS looks uneven or sometimes vanishes | `mode` is `"last"`, or `_combine` isn't keeping the extreme sample. |
| A sweep takes the wrong time | `samplesPerColumn` is off, or `acc -= samplesPerColumn` is resetting it to 0 instead. |
| `XX  cursor after 750 samples` | The cursor isn't wrapping, or `acc` isn't carrying its remainder. |

### Checkpoint

`samplesPerColumn` is **1.6667**, and after 750 samples the cursor is at about **450**, half the screen, or 3 seconds.

---

## Week 22C — The sweeping trace

**Goal:** a continuous ECG sweeping left to right at the right speed, with the HR displayed and a flash on every R-wave.

**New ideas (JS):** *callbacks*, where one object tells others "an R-wave just happened"; functions as inputs.

### The science: the R-wave as a trigger

On a real monitor, the QRS is what the machine detects and beeps on, and other devices synchronize to it: a pulse-ox tone, a defibrillator's sync mode, and an intra-aortic balloon. The whole of your Part 3 is built the same way. The arterial line, pleth and balloon all listen for R-waves, and none of them needs to know how the ECG is made. This is the most important design choice in Part 3.

### The big picture

Now the trace moves. Three pieces, each with one job:

```
CardiacSource.next()   hands out ONE sample at a time, fetching a new beat when the old one runs out;
                       tells its listeners whenever the R-wave sample goes past
Sweep.push(v)          collects samples into screen columns and moves the cursor
loop(now)              ~60 times a second: "how many samples are due since last frame?"
                       → push that many → draw
```

The R-wave **listener** idea is the most important design choice in Part 3. Next weeks, the arterial line, the pleth and the IABP all just *listen* for R-waves. None of them needs to know how the ECG is made.

### Learn it: callbacks 🟢

A callback is a function you hand to an object, for it to call when something happens. Replace `scratch.js` with this:

```js
class Doorbell {
  constructor() {
    this.listeners = [];
  }

  onRing(fn) {
    this.listeners.push(fn);
  }

  press(who) {
    this.listeners.forEach(fn => fn(who));
  }
}

const bell = new Doorbell();
const log = [];

bell.onRing(who => log.push(`dog barks at ${who}`));
bell.onRing(who => log.push(`light turns on for ${who}`));

bell.press("Ana");
console.log(log.join("; "));
console.log(log.length);
```

```text
dog barks at Ana; light turns on for Ana
2
```

The doorbell knows nothing about dogs or lights. Anything can sign up, and it just calls whoever is on its list. You could add a third listener without changing `Doorbell` at all. That's exactly how the monitor will work.

### Build it: `cardiac.js` 🔴

Create `web/js/cardiac.js`, importing `nsrBeat`. Write and export `class CardiacSource`:

- `constructor(getRR)` stores `getRR`, a **function** that returns the current R-R in ms. It also sets `beatFn` to `nsrBeat`, an empty `buffer`, `index` to 0, `current` to `null`, and an empty `listeners` list.
- `onR(fn)` adds a listener.
- `next()` returns one sample at a time. If `index` has reached the end of the buffer, get a fresh beat from `beatFn(getRR())`, store it in `current`, use its samples as the buffer, and reset `index`. If `index` equals `current.rOffset`, call each listener with the current beat. Then return the sample at `index`, and advance it.

<details>
<summary><b>Answer</b></summary>

```js
import { nsrBeat } from "./ecg.js";

export class CardiacSource {
  constructor(getRR) {
    this.getRR = getRR;          // a FUNCTION that returns the current R-R in ms
    this.beatFn = nsrBeat;       // swapped when the rhythm changes (Week 23)
    this.buffer = [];
    this.index = 0;
    this.current = null;
    this.listeners = [];
  }

  onR(fn) { this.listeners.push(fn); }   // "call fn every time there's an R-wave"

  next() {
    if (this.index >= this.buffer.length) {
      this.current = this.beatFn(this.getRR());
      this.buffer = this.current.samples;
      this.index = 0;
    }
    if (this.index === this.current.rOffset) {
      this.listeners.forEach(fn => fn(this.current));
    }
    return this.buffer[this.index++];
  }
}
```

</details>

### Check it

```js
import { CardiacSource } from "./cardiac.js";
```

Add that import at the top of `tests.js`, and these lines above the summary:

```js
// --- Week 22C ---
const heart = new CardiacSource(() => 800);
const rTimes = [];
let sampleNo = 0;
heart.onR(() => rTimes.push(sampleNo));
for (sampleNo = 0; sampleNo < 1000; sampleNo++) heart.next();
check("first R-wave at sample", rTimes[0], 50, 0);
check("R-waves 200 samples apart (800 ms)", rTimes[1] - rTimes[0], 200, 0);
check("R-waves in 1000 samples", rTimes.length, 5, 0);
```


### Build it: the loop 🔴

Now rewrite `main.js`. Keep the slider code and `render()` (without the `drawStatic` line), then add:

1. A `Sweep` on the `ecg` canvas.
2. A `CardiacSource` whose `getRR` reads the slider: `() => 60000 / parseFloat(hrSlider.value)`.
3. A `loop(now)` function using the pattern from Week 22A: work out `dt`, add `dt * SAMPLE_RATE` to `carry`, and while `carry >= 1`, push `heart.next()` to the sweep. Then draw it.
4. A `heart.onR(...)` listener that flashes something on every R-wave. Add `<span id="beat">♥</span>` to the page and give it the CSS class `.flash` for 100 ms using `classList.add`, then `setTimeout(() => el.classList.remove("flash"), 100)`.
5. Show the HR as a big number next to the trace.

Time one full sweep with a stopwatch. It should take 6 seconds.

<details>
<summary><b>Answer</b></summary>

```js
import { rrMs, samplesPerBeat } from "./math.js";
import { SAMPLE_RATE } from "./ecg.js";
import { Sweep } from "./sweep.js";
import { CardiacSource } from "./cardiac.js";

const hrSlider = document.getElementById("hr");
const hrOut = document.getElementById("hr-out");
const rrOut = document.getElementById("rr-out");
const nOut = document.getElementById("n-out");
const rhythmSelect = document.getElementById("rhythm");
const beatEl = document.getElementById("beat");
const hrBig = document.getElementById("hr-big");

function render() {
  const hr = parseFloat(hrSlider.value);   // slider values are STRINGS
  hrOut.textContent = hr;
  hrBig.textContent = hr;
  rrOut.textContent = Math.round(rrMs(hr));
  nOut.textContent = samplesPerBeat(hr);
}

hrSlider.addEventListener("input", render);
rhythmSelect.addEventListener("change", () => console.log(rhythmSelect.value));
render();

const ecgSweep = new Sweep(document.getElementById("ecg"));
const heart = new CardiacSource(() => 60000 / parseFloat(hrSlider.value));

heart.onR(() => {
  beatEl.classList.add("flash");
  setTimeout(() => beatEl.classList.remove("flash"), 100);
});

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

In `index.html`, above the canvas:

```html
  <p class="vitals"><span id="beat">♥</span> HR <span id="hr-big" class="big">75</span></p>
```

And in `style.css`:

```css

.big {
  font-size: 2.5em;
  font-weight: bold;
}

.flash {
  color: #fff;
  font-size: 1.4em;
}

canvas {
  display: block;
  margin-bottom: 4px;
}
```

</details>


Commit, and write a `DEVLOG.md` entry.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  cursor after 750 samples` (it's 750) | `push` moves the cursor every sample. The cursor should only move when `acc` reaches `samplesPerColumn`. |
| One sweep takes 7.2 s, not 6 | You round 1.67 up to 2 instead of carrying the fraction in `acc`. |
| QRS spikes look chopped or short | `_combine` isn't keeping the most extreme value, or `mode` is `"last"`. |
| `XX  first R-wave at sample` | `CardiacSource.next()` compares `index` with `rOffset` *after* incrementing it. Compare first, then `index++`. |
| The trace races or crawls | `dt` isn't in seconds (divide by 1000), or `carry` isn't reduced by 1 per pushed sample. |
| The page freezes after switching tabs | Cap `dt` (`Math.min(0.1, ...)`) so a long pause doesn't push thousands of samples at once. |

### Things to consider

- Why the `acc` counter instead of "every 2 samples"? 1500 samples across 900 pixels is 1.67 samples per column. Rounding to 2 would make each sweep take 7.2 seconds.
- Why "extreme" instead of averaging? Averaging a QRS spike with its near-zero neighbours shrinks it. Try `mode: "last"` on the ECG to see the R-waves get chopped.
- `onR` is the architectural heart of Part 3. The arterial line, the pleth and the IABP will all *listen* for R-waves instead of knowing anything about the ECG. Python has the same pattern (any list of functions you call), and JS uses it everywhere.

### Checkpoint

A smooth green sweep, 6 seconds per screen, a crisp QRS, and the heart symbol flashing in step with the R-waves.

---

## Week 23 — Patient state, controls and smooth transitions

**Goal:** one object holding the patient's vitals, controls that change it, and an HR that ramps instead of jumping.

**New ideas (JS):** a shared state object exported from a module; writing one function to bind many sliders; `switch`.

**Read first:** [javascript.info: Objects](https://javascript.info/object) · [`switch`](https://javascript.info/switch)

### The science: MAP is an estimate

MAP ≈ (SBP + 2·DBP) / 3 is a rule of thumb. It comes from diastole lasting about twice as long as systole at normal rates. A real monitor integrates the area under the arterial curve instead, so it stays correct at high heart rates and with unusual waveforms, when this formula doesn't. Heart rate doesn't jump instantly in real life either, which is why this lesson ramps it.

**References:** *Project 3* textbook, Ex 1.4 · Deranged Physiology, *Normal arterial line waveforms*. derangedphysiology.com

### The big picture

Up to now, the heart rate lived in a slider. This week makes **one shared object, `P`**, the patient's single source of truth. Everything reads from it; only the controls (and later, scenarios) write to it.

```
sliders ──bindSlider──► P  ◄── read by CardiacSource (HR, rhythm), the vitals panel, later the pumps and devices
                        │
                 nextEffectiveHR() moves P.hr toward P.targetHr a little each beat
```

### Learn it: shared state, `switch`, and binding many controls 🟢

An object exported from a module is shared: every file that imports it sees the same one. Replace `scratch.js` with this:

```js
const Settings = { volume: 5, mode: "day" };

function brightnessFor(mode) {
  switch (mode) {
    case "day":
      return 100;
    case "night":
      return 20;
    default:
      return 50;
  }
}

console.log(brightnessFor("night"), brightnessFor("anything"));

const key = "volume";
Settings[key] = 9;
console.log(Settings.volume);

function moveToward(current, target, step) {
  if (current < target) return Math.min(current + step, target);
  return Math.max(current - step, target);
}
console.log(moveToward(10, 12, 5), moveToward(10, 2, 5));

function bindNumber(el, name, { onChange } = {}) {
  const update = () => {
    Settings[name] = parseFloat(el.value);
    if (onChange) onChange(Settings[name]);
  };
  el.addEventListener("input", update);
  update();
}

bindNumber(document.getElementById("cups"), "cups", { onChange: v => console.log("cups is", v) });
```

```text
20 50
9
12 5
cups is 2
```

- `switch` compares one value against several `case`s. It's a neat replacement for a long `if`/`else if`. The `return` ends each case. Without a `return`, you need a `break`.
- `Settings[key]` reads or writes a property whose name is in a variable. This is what lets one function handle every slider.
- `bindNumber` works for any element and any setting. It's written once, and used many times.

### Build it: `patient.js` 🔴

Create `web/js/patient.js`, exporting this object, then two functions:

```js
export const P = {
  hr: 75, targetHr: 75,
  sbp: 120, dbp: 80,
  spo2: 98, rr: 14, etco2: 38,
  rhythm: "NSR",
  nativeCO: 4.5,          // L/min. Make it LOW for cardiogenic-shock scenarios (Week 27)
};
```

- **`nextEffectiveHR(step = 5)`** moves `P.hr` toward `P.targetHr` by at most `step`, without overshooting, and returns `P.hr`. It's called once per beat.
- **`map()`** returns the rounded `(sbp + 2·dbp) / 3`.

<details>
<summary><b>Answer</b></summary>

```js
export const P = {
  hr: 75, targetHr: 75,
  sbp: 120, dbp: 80,
  spo2: 98, rr: 14, etco2: 38,
  rhythm: "NSR",
  nativeCO: 4.5,          // L/min. Make it LOW for cardiogenic-shock scenarios (Week 27)
};

export function nextEffectiveHR(step = 5) {
  // Called once per beat: move P.hr toward P.targetHr by at most `step`.
  if (P.hr < P.targetHr) {
    P.hr = Math.min(P.hr + step, P.targetHr);
  } else {
    P.hr = Math.max(P.hr - step, P.targetHr);
  }
  return P.hr;
}

export function map() {
  return Math.round((P.sbp + 2 * P.dbp) / 3);
}
```

</details>

### Check it

Add the import to the top of `tests.js`, and these lines above the summary:

```js
import { P, nextEffectiveHR, map } from "./patient.js";
```

```js
// --- Week 23 ---
P.hr = 75; P.targetHr = 130;
let beatsToTarget = 0;
while (P.hr !== P.targetHr && beatsToTarget < 100) { nextEffectiveHR(); beatsToTarget++; }
check("beats to ramp 75 → 130", beatsToTarget, 11, 0);
P.targetHr = 60; nextEffectiveHR();
check("ramps down too", P.hr, 125, 0);
P.sbp = 120; P.dbp = 80; check("MAP 120/80", map(), 93, 0);
P.sbp = 90;  P.dbp = 60; check("MAP 90/60", map(), 70, 0);
P.sbp = 180; P.dbp = 100; check("MAP 180/100", map(), 127, 0);
P.sbp = 120; P.dbp = 80;                         // put the patient back
```


### Build it: `controls.js`, and the rhythm switch 🔴

**`web/js/controls.js`:** write and export `bindSlider(id, key, { onChange } = {})`. It finds the element with that `id`, and the element with the id `` `${id}-out` ``, if there is one. On every `"input"`, and once at the start, it reads the number, stores it in `P[key]`, shows it in the out element, and calls `onChange` if one was given.

**`cardiac.js`:** add a function, `beatFor(rhythm)`, with a `switch`. Only NSR exists for now, so make every case return `nsrBeat` through a `default`. In `next()`, right before fetching a fresh beat, set `this.beatFn = beatFor(P.rhythm)`.

**`index.html`:** add sliders with ids `sbp`, `dbp`, `spo2`, `rr` and `etco2`, each with a `-out` span. Then add a vitals panel with spans for HR, BP, MAP, SpO₂, RR and EtCO₂.

**`main.js`:** rewrite it so everything reads from `P`. Bind every slider. Bind the `hr` slider to `targetHr`, and make `getRR` call `nextEffectiveHR()`, so the heart rate ramps once per beat. Wire the rhythm menu to `P.rhythm`. Refresh the vitals panel in `loop()`.

<details>
<summary><b>Answer</b></summary>

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
```

```js
import { nsrBeat } from "./ecg.js";
import { P } from "./patient.js";

function beatFor(rhythm) {
  switch (rhythm) {
    default:
      return nsrBeat;
  }
}

export class CardiacSource {
  constructor(getRR) {
    this.getRR = getRR;          // a FUNCTION that returns the current R-R in ms
    this.beatFn = nsrBeat;
    this.buffer = [];
    this.index = 0;
    this.current = null;
    this.listeners = [];
  }

  onR(fn) { this.listeners.push(fn); }   // "call fn every time there's an R-wave"

  next() {
    if (this.index >= this.buffer.length) {
      this.beatFn = beatFor(P.rhythm);
      this.current = this.beatFn(this.getRR());
      this.buffer = this.current.samples;
      this.index = 0;
    }
    if (this.index === this.current.rOffset) {
      this.listeners.forEach(fn => fn(this.current));
    }
    return this.buffer[this.index++];
  }
}
```

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
  <section class="vitals">
    <span id="beat">♥</span>
    HR <span id="v-hr" class="big">75</span>
    BP <span id="v-bp" class="big">120/80</span> (<span id="v-map">93</span>)
    SpO₂ <span id="v-spo2" class="big">98</span>
    RR <span id="v-rr" class="big">14</span>
    EtCO₂ <span id="v-etco2" class="big">38</span>
  </section>
  <canvas id="ecg" width="900" height="200"></canvas>
  <section class="controls">
    <label>HR <input id="hr" type="range" min="30" max="200" value="75"></label><span id="hr-out">75</span>
    <label>SBP <input id="sbp" type="range" min="50" max="220" value="120"></label><span id="sbp-out">120</span>
    <label>DBP <input id="dbp" type="range" min="20" max="130" value="80"></label><span id="dbp-out">80</span>
    <label>SpO₂ <input id="spo2" type="range" min="50" max="100" value="98"></label><span id="spo2-out">98</span>
    <label>RR <input id="rr" type="range" min="4" max="40" value="14"></label><span id="rr-out">14</span>
    <label>EtCO₂ <input id="etco2" type="range" min="0" max="80" value="38"></label><span id="etco2-out">38</span>
    <label>Rhythm
      <select id="rhythm">
        <option value="NSR">NSR</option>
        <option value="AFIB">AFIB</option>
        <option value="VTACH">VTACH</option>
        <option value="VFIB">VFIB</option>
        <option value="CHB">CHB</option>
      </select>
    </label>
  </section>
  <script type="module" src="js/main.js"></script>
</body>
</html>
```

```js
import { SAMPLE_RATE } from "./ecg.js";
import { Sweep } from "./sweep.js";
import { CardiacSource } from "./cardiac.js";
import { P, nextEffectiveHR, map } from "./patient.js";
import { bindSlider } from "./controls.js";

const byId = id => document.getElementById(id);

bindSlider("hr", "targetHr");
bindSlider("sbp", "sbp");
bindSlider("dbp", "dbp");
bindSlider("spo2", "spo2");
bindSlider("rr", "rr");
bindSlider("etco2", "etco2");

const rhythmSelect = byId("rhythm");
rhythmSelect.addEventListener("change", () => { P.rhythm = rhythmSelect.value; });

const beatEl = byId("beat");

function flashHeart() {
  beatEl.classList.add("flash");
  setTimeout(() => beatEl.classList.remove("flash"), 100);
}

function updateVitals() {
  byId("v-hr").textContent = P.hr;
  byId("v-bp").textContent = `${P.sbp}/${P.dbp}`;
  byId("v-map").textContent = map();
  byId("v-spo2").textContent = P.spo2;
  byId("v-rr").textContent = P.rr;
  byId("v-etco2").textContent = P.etco2;
}

const ecgSweep = new Sweep(byId("ecg"));
const heart = new CardiacSource(() => 60000 / nextEffectiveHR());

function onBeat(beat) {
  flashHeart();
}
heart.onR(onBeat);

function pushSamples() {
  ecgSweep.push(heart.next());
}

function drawAll() {
  ecgSweep.draw();
  updateVitals();
}

let carry = 0;
let lastT = performance.now();

function loop(now) {
  requestAnimationFrame(loop);
  const dt = Math.min(0.1, (now - lastT) / 1000);   // cap: tab-switch pauses can make dt huge
  lastT = now;
  carry += dt * SAMPLE_RATE;                         // samples "owed" since last frame
  while (carry >= 1) {
    carry -= 1;
    pushSamples();
  }
  drawAll();
}

requestAnimationFrame(loop);
```

</details>


`pushSamples`, `onBeat` and `drawAll` are small functions on purpose. Each later lesson changes only one of them. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  beats to ramp` (1 instead of 11) | `nextEffectiveHR` sets `P.hr = P.targetHr` directly. It should move by at most `step`. |
| HR overshoots and oscillates | The clamp: use `Math.min(target, hr + step)` going up and `Math.max(target, hr - step)` going down. |
| `XX  MAP 90/60` | The formula, or a missing `Math.round`. |
| A slider moves but nothing changes | `bindSlider` was given the wrong `key`; `"targetHR"` ≠ `"targetHr"`. |
| Rhythm changes mid-beat and the trace glitches | Read `P.rhythm` only where `CardiacSource` fetches a new beat. |

### Things to consider

- Rhythm changes should take effect at the **next beat**, not in the middle of one. Where in `CardiacSource.next()` is the safe place to check `P.rhythm`?
- `P` is imported by many files, and they all share the *same* object. Changing `P.sbp` anywhere is seen everywhere. That's convenient, but it's also how big projects get confusing, so only `controls.js` (and later, scenarios) should *write* to `P`.

### Checkpoint

Target HR 75 → 130 with step 5: **11 beats** to arrive. MAP for 120/80 = **93**, 90/60 = **70**, 180/100 = **127**.

---

## Week 24A — Atrial fibrillation

**Goal:** irregular AFib with a fibrillatory baseline, and beat-to-beat changes in pulse strength.

**New ideas (JS):** `Math.random()`; building a signal from sines; carrying extra data along on an object (`ampMod`).

**Read first:** [javascript.info: Math](https://javascript.info/number)

### The science: why AFib's pulse varies

In AFib, there's no organized atrial contraction, so there's no P wave, just a fine irregular baseline. The ventricles respond irregularly. And a beat that comes early has had less time to fill, so it ejects less. That's why a patient in AFib can have a pulse that varies beat to beat, with some beats too weak to feel at the wrist, known as a pulse deficit.

This model captures that with `ampMod`, the beat's filling compared with normal. It's carried along on the beat object for the arterial line to read in Week 25.

**Reference:** *Project 3* textbook, Ex 4.1 (atrial fibrillation)

### The big picture

```
afibBeat(rr)   a whole beat: random R-R, no P wave, wobbly baseline, ampMod = how well the ventricle filled
```

### Learn it: randomness and sines 🟢

Replace `scratch.js` with this:

```js
const r = Math.random();
console.log(r >= 0 && r < 1);

const shift = (Math.random() * 2 - 1) * 0.3;
console.log(shift >= -0.3 && shift <= 0.3);

function clamp(x, low, high) {
  return Math.max(low, Math.min(high, x));
}
console.log(clamp(5, 1, 3), clamp(-5, 1, 3), clamp(2, 1, 3));

const hz = 2;
const samples = [];
for (let i = 0; i < 5; i++) {
  const seconds = i / 8;
  samples.push(Math.sin(2 * Math.PI * hz * seconds).toFixed(2));
}
console.log(samples.join(" "));
```

```text
true
true
3 1 2
0.00 1.00 0.00 -1.00 -0.00
```

- `Math.random()` gives a number from 0 up to (not including) 1. `(Math.random() * 2 - 1) * 0.3` turns it into a value from −0.3 to 0.3.
- `Math.max(low, Math.min(high, x))` is the standard clamp.
- A sine wave at `hz` cycles per second has the value `Math.sin(2π · hz · t)` at time `t`, and for sample `i`, `t` is `i / sampleRate`.

### Build it: `afibBeat` 🔴

Add these to `ecg.js`. `randn` is given, because it's a math recipe rather than something to derive. It gives bell-curve noise, with a mean of 0 and a standard deviation of 1.

```js
export function randn() {                    // standard-normal noise (Box–Muller)
  let u = 0, v = 0;
  while (!u) u = Math.random();
  while (!v) v = Math.random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}
```

Then **`afibBeat(baseRrMs, irregularity = 0.3)`**:

1. `r` is a random value from −`irregularity` to +`irregularity`. `actual` is `baseRrMs * (1 + r)`, rounded and clamped to 300–1500 ms.
2. The baseline: start with zeros. For each frequency in 5.8, 7.3, 9.1 and 6.5 Hz, pick one random phase, and add a small sine (amplitude about 0.02) to every sample. Then add a tiny `randn()` noise, about 0.005, to every sample.
3. **Add**, don't `place`, a `qrsComplex` at 25% of the beat, so the baseline stays underneath. Add a `tWave` after the ST segment, skipping anything past the end.
4. `fill` is `actual / baseRrMs`, clamped to 0.5–1.15. A shorter beat fills less.
5. Return `{ samples, rOffset, rrMs: actual, ampMod: fill }`.

Add an `add(buf, start, wave)` helper like `place`, except that it uses `+=`. In `cardiac.js`, add a case for `"AFIB"` to the `switch`.

<details>
<summary><b>Hint</b></summary>

Pick the phase once per frequency, outside the sample loop: `const phase = Math.random() * 2 * Math.PI;`. The time of sample `i` is `i / SAMPLE_RATE` seconds.

</details>
<details>
<summary><b>Answer</b></summary>

```js

export function randn() {                    // standard-normal noise (Box–Muller)
  let u = 0, v = 0;
  while (!u) u = Math.random();
  while (!v) v = Math.random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

export function add(buf, start, wave) {
  for (let i = 0; i < wave.length; i++) {
    const j = start + i;
    if (j >= 0 && j < buf.length) buf[j] += wave[i];
  }
}

export function afibBeat(baseRrMs, irregularity = 0.3) {
  const r = (Math.random() * 2 - 1) * irregularity;
  const actual = Math.max(300, Math.min(1500, Math.round(baseRrMs * (1 + r))));
  const total = samplesFor(actual);
  const samples = new Array(total).fill(0);
  for (const hz of [5.8, 7.3, 9.1, 6.5]) {
    const phase = Math.random() * 2 * Math.PI;
    for (let i = 0; i < total; i++) {
      samples[i] += 0.02 * Math.sin(2 * Math.PI * hz * (i / SAMPLE_RATE) + phase);
    }
  }
  for (let i = 0; i < total; i++) samples[i] += 0.005 * randn();

  const qS = samplesFor(100), stS = samplesFor(100), tS = samplesFor(160);
  const qrsStart = Math.floor(0.25 * total);
  add(samples, qrsStart, qrsComplex(qS));
  add(samples, qrsStart + qS + stS, tWave(tS));
  const fill = Math.max(0.5, Math.min(1.15, actual / baseRrMs));
  return { samples, rOffset: qrsStart + Math.round(0.4 * qS), rrMs: actual, ampMod: fill };
}
```

```js
import { nsrBeat, afibBeat } from "./ecg.js";
```

```js
    case "AFIB":
      return afibBeat;
    default:
```

</details>

### Check it

Add `afibBeat` to the top of `tests.js`, and these lines above the summary. `nsrBeat` is there already. The answer can't be a single number, because it's random, so these check the **range** across 2000 beats.

```js
import { afibBeat } from "./ecg.js";
```

```js
// --- Week 24A ---
let shortest = Infinity, longest = 0;
for (let i = 0; i < 2000; i++) {
  const b = afibBeat(800);
  shortest = Math.min(shortest, b.rrMs);
  longest = Math.max(longest, b.rrMs);
}
check("AFib shortest R-R ≥ 560", shortest >= 560, true);
check("AFib longest R-R ≤ 1040", longest <= 1040, true);
check("AFib R-R really varies", longest - shortest > 300, true);
```


Choose AFIB on the page. Check for no P waves, a wobbly baseline and uneven spacing. Commit.

### Checkpoint

AFib at base 800 ms, irregularity 0.3: every R-R falls in **560–1040 ms**.

---

## Week 24B — The ectopy overlay

**Goal:** PVCs that can be injected into *any* rhythm.

**New ideas (JS):** a *wrapper* that takes a beat function and returns a modified beat; methods on a plain object; `??`.

**Read first:** [javascript.info: Object methods and `this`](https://javascript.info/object-methods)

### The science: PVCs, the compensatory pause and potentiation

A premature ventricular contraction comes early, starts in the ventricle, and spreads slowly, so the QRS is wide, and the T wave points the opposite way. Because it's early, the ventricle hasn't filled, so it ejects weakly. Here `ampMod` is 0.2.

Then there's a **compensatory pause** before the next normal beat, which gives the ventricle extra time to fill. Next, the post-PVC beat is stronger than usual, called **post-extrasystolic potentiation**, here `ampMod` 1.3. Patients sometimes feel this one as a "thump".

**Bigeminy** means a PVC every second beat, and **trigeminy** means every third.

**Reference:** *Project 3* textbook, Ex 4.2 (ectopy overlay, PVCs, compensatory pause, post-extrasystolic potentiation)

### The big picture

Two new behaviors, built so they combine freely:

```
afibBeat(rr)                    a whole beat: random R-R, no P wave, wobbly baseline, ampMod = how well the ventricle filled
Ectopy.next(beatFn, rr)         a WRAPPER: either returns a PVC, or calls beatFn(rr) and adjusts its ampMod
CardiacSource ──calls──► Ectopy.next(this.beatFn, rr) ──calls──► nsrBeat / afibBeat / ...
```

Because `Ectopy` wraps *whichever* beat function it's given, PVCs work over NSR, AFib and every rhythm you add later, with no changes to those rhythms.

### Learn it: a wrapper 🟢

A wrapper takes a function as an input, and either calls it or does something else. It adds behavior to any function without changing that function. Replace `scratch.js` with this:

```js
function plainCoffee(size) {
  return { drink: "coffee", size };
}

function plainTea(size) {
  return { drink: "tea", size };
}

const Barista = {
  count: 0,
  lastWasFree: false,

  shouldBeFree() {
    return this.count % 3 === 2;
  },

  serve(makeDrink, size) {
    const free = this.shouldBeFree();
    const afterFree = this.lastWasFree;
    this.lastWasFree = free;
    this.count++;
    const order = makeDrink(size);
    order.price = free ? 0 : 3;
    if (afterFree) order.note = "thanks for coming back";
    return order;
  },
};

for (const maker of [plainCoffee, plainTea, plainCoffee, plainTea]) {
  console.log(JSON.stringify(Barista.serve(maker, "large")));
}

const box = {};
console.log(box.tip ?? 1, (box.tip ?? 1) * 2);
const zero = { tip: 0 };
console.log(zero.tip ?? 1, zero.tip || 1);
```

```text
{"drink":"coffee","size":"large","price":3}
{"drink":"tea","size":"large","price":3}
{"drink":"coffee","size":"large","price":0}
{"drink":"tea","size":"large","price":3,"note":"thanks for coming back"}
1 2
0 1
```

- `Barista.serve(maker, size)` works with any drink function. Coffee and tea don't change, and neither needs to know about free drinks. The same will be true of your rhythms and `Ectopy`.
- An object can have methods and use `this`, without any class. Use this when you only need one of something.
- `x ?? 1` means "use 1 if `x` is missing". Unlike `||`, it keeps a real 0.

### Build it: `pvcComplex` and `Ectopy` 🔴

**`pvcComplex(n, amp = 1.5)`** in `ecg.js`: a wide main deflection, a shoulder, and a T wave in the opposite direction, added together:

```
gaussian(x, amp, 0.30, 0.10) + gaussian(x, amp·0.5, 0.45, 0.08) + gaussian(x, −amp·0.4, 0.75, 0.12)
```

**`web/js/ectopy.js`**, exporting an object `Ectopy`:

- `enabled: false`, `pattern: "random"`, `freq: 0.1`, `count: 0`, `lastWasPVC: false`.
- **`shouldFire()`:** false if it's not enabled, or if the last beat was a PVC, because there are never two in a row. For `"bigeminy"`, it's `count % 2 === 1`. For `"trigeminy"`, it's `count % 3 === 2`. Otherwise, it fires at random, with probability `freq`.
- **`next(baseBeatFn, rrMs)`:** work out `fire` and `afterPVC` as in the `Barista`, and add one to `count`.
  - If firing: `coupling = rrMs * (0.6 to 0.8)`, at random. Make a zero-filled buffer of length `samplesFor(2 * rrMs)`, which gives the compensatory pause. Place `pvcComplex(samplesFor(160), 1.6)` at the coupling point. Return `{ samples, rOffset, rrMs: coupling, ampMod: 0.2 }`, where `rOffset` is 30% of the way into the PVC.
  - Otherwise: call `baseBeatFn(rrMs)`. If this follows a PVC, multiply its `ampMod` (default 1) by 1.3. Set `beat.ampMod` either way, and return it.

In `cardiac.js`, call `Ectopy.next(this.beatFn, rr)` in place of `this.beatFn(rr)`. Add a checkbox with the id `pvc` and a pattern `<select>` with the id `pvc-pattern`, wired up in `main.js`.

<details>
<summary><b>Answer</b></summary>

```js

export function pvcComplex(n, amp = 1.5) {
  // wide main deflection + shoulder + T wave in the OPPOSITE direction
  return linspace(n).map(x => gaussian(x, amp, 0.30, 0.10) + gaussian(x, amp * 0.5, 0.45, 0.08)
                              + gaussian(x, -amp * 0.4, 0.75, 0.12));
}
```

```js
import { samplesFor, pvcComplex, place } from "./ecg.js";

export const Ectopy = {
  enabled: false,
  pattern: "random",    // "random" | "bigeminy" | "trigeminy"
  freq: 0.1,
  count: 0,
  lastWasPVC: false,

  shouldFire() {
    if (!this.enabled || this.lastWasPVC) return false;    // never two in a row
    if (this.pattern === "bigeminy") return this.count % 2 === 1;
    if (this.pattern === "trigeminy") return this.count % 3 === 2;
    return Math.random() < this.freq;
  },

  next(baseBeatFn, rrMs) {
    const fire = this.shouldFire();
    const afterPVC = this.lastWasPVC;
    this.lastWasPVC = fire;
    this.count++;
    if (fire) {
      const coupling = rrMs * (0.6 + 0.2 * Math.random());
      const samples = new Array(samplesFor(2 * rrMs)).fill(0);    // compensatory pause
      const start = samplesFor(coupling);
      const n = samplesFor(160);
      place(samples, start, pvcComplex(n, 1.6));
      return { samples, rOffset: start + Math.round(0.3 * n), rrMs: coupling, ampMod: 0.2 };   // weak ejection
    }
    const beat = baseBeatFn(rrMs);
    beat.ampMod = (beat.ampMod ?? 1) * (afterPVC ? 1.3 : 1);
    return beat;
  },
};
```

```js
import { P } from "./patient.js";
import { Ectopy } from "./ectopy.js";
```

```js
      this.current = Ectopy.next(this.beatFn, this.getRR());
```

```html
    <label><input id="pvc" type="checkbox"> PVCs</label>
    <select id="pvc-pattern">
      <option value="random">Random</option>
      <option value="bigeminy">Bigeminy</option>
      <option value="trigeminy">Trigeminy</option>
    </select>
```

```js
import { bindSlider } from "./controls.js";
import { Ectopy } from "./ectopy.js";
```

```js
byId("pvc").addEventListener("change", e => { Ectopy.enabled = e.target.checked; });
byId("pvc-pattern").addEventListener("change", e => { Ectopy.pattern = e.target.value; });

```

</details>

### Check it

```js
import { Ectopy } from "./ectopy.js";
```

Add that import at the top of `tests.js`, and these lines above the summary:

```js
// --- Week 24B ---
Ectopy.enabled = true; Ectopy.pattern = "bigeminy"; Ectopy.count = 0; Ectopy.lastWasPVC = false;
const ampMods = [];
for (let i = 0; i < 6; i++) ampMods.push(Ectopy.next(nsrBeat, 800).ampMod);
check("bigeminy pulse strengths", ampMods.join(","), "1,0.2,1.3,0.2,1.3,0.2");
Ectopy.enabled = false;
```


Turn on PVCs over NSR, then over AFib, without changing `afibBeat`. That's the overlay doing its job. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  AFib shortest/longest R-R` | The random factor: `(Math.random() * 2 - 1) * irregularity` gives −0.3 to +0.3. |
| AFib has no wobbly baseline | The QRS was *placed* over the baseline (erasing it) instead of *added*. |
| `XX  bigeminy pulse strengths` | `shouldFire` for bigeminy (`count % 2 === 1`), or `count`/`lastWasPVC` updated in the wrong order in `next()`. Save `afterPVC` *before* overwriting `lastWasPVC`. |
| Two PVCs in a row | The `this.lastWasPVC` guard at the top of `shouldFire`. |
| `TypeError: baseBeatFn is not a function` | `CardiacSource` passed `this.beatFn(rr)` (the result) instead of `this.beatFn` (the function). |

### Things to consider

- **Place vs add:** NSR's baseline is zeros, so overwriting is fine. AFib's baseline is the fibrillation squiggle, so you must *add* the QRS on top or you'll erase it.
- Why an overlay instead of separate NSR, NSR+PVC, AFib and AFib+PVC rhythms? Count how many rhythms you'd need for 5 rhythms × 3 ectopy types.
- In AFib there's no sinus node to "reset", so a true compensatory pause doesn't really apply. Your overlay always adds one. Is that worth fixing? (Stretch.)

### Checkpoint

Bigeminy for beats 0–5: normal, **PVC**, normal, **PVC**, normal, **PVC**. The `ampMod`s are 1, **0.2**, **1.3**, 0.2, 1.3, ...

---

## Week 25A — The arterial line

**Goal:** an arterial pressure trace that rises 150 ms after each R-wave, with a realistic shape at *any* heart rate.

**New ideas (JS):** a per-sample *state machine*; a queue of delayed events (`push`/`shift`).

### The science: the arterial waveform

An arterial trace has a sharp upstroke as the ventricle ejects, a peak at systole, and a slow decline during runoff, broken by the **dicrotic notch**. The notch marks the aortic valve closing, about a third of the way down the descending limb. There's a delay between the R-wave and the upstroke, as the electrical signal becomes a contraction and the pressure wave travels to the catheter. This model uses 150 ms.

Pressure doesn't fall to a fixed diastolic value in a set time. It decays continuously until the next beat interrupts it. So at fast heart rates, there's less time for runoff, and end-diastolic pressure rises. Your model shows that with no special code: 81 mmHg at HR 60, and 92 mmHg at HR 150.

The old arterial pulse was a fixed 350 ms shape followed by a flat line. That gave a flat plateau at slow heart rates, a 3 mmHg step at the end of every beat, and a dicrotic notch far too early. It also broke at fast rates. The new design never "ends" a pulse:

- On each upstroke, rise from **wherever the pressure is now** to systolic, over about 100 ms (using `smoothstep`).
- After the peak, decay toward diastolic continuously: `dia + pp · exp(−t/τ)`, with τ ≈ 250 ms.
- Add a small notch at about 300 ms after the upstroke starts (end of ejection) and a small dicrotic bump just after it.
- The next beat starts from the current value, so there's never a jump. As a bonus, end-diastolic pressure *rises* at fast heart rates (less time to run off), which is physiologically right.

**References:** Stouffer GA. Arterial pressure (ch. 4). thoracickey.com/4-arterial-pressure/ · Deranged Physiology, *Normal arterial line waveforms*. derangedphysiology.com · *Arterial Lines*. anaestheasier.com/arterial-lines/ · *Broader applications of arterial pressure waveform analysis*. *BJA Education* 2017

### The big picture

The arterial line is driven by the ECG but knows nothing about it:

```
CardiacSource ──R-wave──► your onR listener ──art.trigger(sys, dia)──► PulsePump
                                                                         │  waits 150 ms (the queue)
                                                                         ▼
loop ──art.next() every sample──► one pressure value ──► arterial Sweep
```

`PulsePump` is a **state machine**: it remembers where the pressure is right now and what beat it's in, and each call to `next()` moves it forward one sample. The pleth uses the *same class* with different settings.

### Learn it: a state machine and a queue 🟢

A state machine remembers where it is, and each call moves it forward one step. Here's a kettle that responds to delayed commands. Replace `scratch.js` with this:

```js
class Kettle {
  constructor() {
    this.temp = 20;
    this.pending = [];
    this.heating = false;
  }

  order(delay) {
    this.pending.push({ left: delay });
  }

  next() {
    for (const p of this.pending) p.left--;
    if (this.pending.length && this.pending[0].left <= 0) {
      this.pending.shift();
      this.heating = true;
    }
    if (this.heating) {
      this.temp += 10;
    } else {
      this.temp = 20 + (this.temp - 20) * 0.5;
    }
    if (this.temp >= 50) this.heating = false;
    return this.temp;
  }
}

const k = new Kettle();
k.order(2);
const out = [];
for (let i = 0; i < 7; i++) out.push(k.next());
console.log(out.join(" "));
```

```text
20 30 40 50 35 27.5 23.75
```

- `this.pending` is a queue. `push` adds to the end, and `shift` removes the first item, so orders come out in the order they went in.
- Each `next()` counts down the queue, then does one step of work. There's no timer: time passes only when `next()` is called, once per sample.
- `this.temp` carries over between calls, so each step starts from wherever the last one finished. That's the key to the arterial design: **no jumps**.

### Build it: `pulse.js` 🔴

Create `web/js/pulse.js`, importing `samplesFor` and `SAMPLE_RATE`. Add these two small helpers, which are short math recipes:

```js
const smoothstep = u => u * u * (3 - 2 * u);
const bump = (t, c, w) => Math.exp(-((t - c) ** 2) / (2 * w * w));
```

`smoothstep` eases from 0 to 1, and `bump` is a Gaussian. Write and export `class PulsePump`:

- **`constructor({ delayMs = 150, riseMs = 100, tauMs = 250, notchMs = 300, notchDepth = 0.08, bumpSize = 0.05, start = 80, minRise = 2 } = {})`** stores the settings. `this.delay = samplesFor(delayMs)`. Set `this.value = start`, an empty `pending` queue, `this.beat = null`, and `this.t = 0`.
- **`trigger(sys, dia, sharp = 1)`** adds `{ left: this.delay, sys, dia, sharp }` to the queue.
- **`next()`:**
  1. Count down the queue. If the first item is due, start a new beat: `this.beat = { base: this.value, sys: Math.max(p.sys, this.value + this.minRise), dia: p.dia, sharp: p.sharp }`, and `this.t = 0`. The `Math.max` stops a weak beat from pointing the upstroke downward. `minRise` is in the pump's own units, 2 mmHg here.
  2. If there's no beat yet, return `this.value`.
  3. Work out `ms` since the upstroke began: `(this.t * 1000) / SAMPLE_RATE`. With `pp = sys − dia`:
     - **Upstroke,** if `ms < riseMs`: `base + (sys − base) · smoothstep(ms / riseMs)`
     - **Runoff,** otherwise: `dia + pp · e^(−(ms − riseMs)/tauMs) − notchDepth · pp · sharp · bump(ms, notchMs, 15) + bumpSize · pp · sharp · bump(ms, notchMs + 40, 25)`
  4. Add 1 to `this.t`, store the value, and return it.

<details>
<summary><b>Answer</b></summary>

```js
import { samplesFor, SAMPLE_RATE } from "./ecg.js";

const smoothstep = u => u * u * (3 - 2 * u);
const bump = (t, c, w) => Math.exp(-((t - c) ** 2) / (2 * w * w));

export class PulsePump {
  constructor({ delayMs = 150, riseMs = 100, tauMs = 250, notchMs = 300,
                notchDepth = 0.08, bumpSize = 0.05, start = 80, minRise = 2 } = {}) {
    Object.assign(this, { riseMs, tauMs, notchMs, notchDepth, bumpSize, minRise });
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
      this.beat = { base: this.value, sys: Math.max(p.sys, this.value + this.minRise), dia: p.dia, sharp: p.sharp };
      this.t = 0;
    }
    if (!this.beat) return this.value;
    const ms = (this.t * 1000) / SAMPLE_RATE;
    const b = this.beat;
    const pp = b.sys - b.dia;
    let v;
    if (ms < this.riseMs) {
      v = b.base + (b.sys - b.base) * smoothstep(ms / this.riseMs);
    } else {
      v = b.dia + pp * Math.exp(-(ms - this.riseMs) / this.tauMs)
          - this.notchDepth * pp * b.sharp * bump(ms, this.notchMs, 15)
          + this.bumpSize * pp * b.sharp * bump(ms, this.notchMs + 40, 25);
    }
    this.t++;
    this.value = v;
    return v;
  }
}
```

</details>
<details>
<summary><b>How the code works</b></summary>

- **`smoothstep` and `bump`** are two small shape helpers: a smooth 0-to-1 ramp, and a bell-shaped bump.
- **The constructor** stores the shape settings (rise time, decay time, notch timing and sizes) and turns the 150 ms delay into samples. `start` is the pressure before the first beat.
- **`trigger(sys, dia, sharp)`** doesn't change the pressure; it adds an entry to `pending` with a countdown. That's how the delay works.
- **`next()`**:
  1. Count every pending beat down by one sample. When the first reaches zero, start a new beat: remember the pressure it starts from (`base`), its targets, and reset the beat clock `t`.
  2. Work out the pressure for this moment of the beat: the upstroke if it's early, the decay plus notch and bump if it's later.
  3. Save it as `this.value` (so the *next* beat can start from it) and return it.

</details>

### Check it

These lines drive a `PulsePump` with fake R-waves, with no ECG or canvas, and check the numbers in the checkpoint. Add the import at the top of `tests.js`, and these lines above the summary:

```js
import { PulsePump } from "./pulse.js";
```

```js
// --- Week 25 ---
// Drive the pump with a fake R-wave every R-R interval: no ECG or canvas needed.
function runPump(hr, { iabp = false, amps = [], beats = 8 } = {}) {
  const pump = new PulsePump();
  if (pump.iabp) pump.iabp.enabled = iabp;
  const rr = Math.round(60000 / hr * 250 / 1000);
  const out = [];
  for (let i = 0; i < rr * beats; i++) {
    if (i % rr === 0) {
      if (iabp) pump.deflate();
      pump.trigger(80 + 40 * (amps[i / rr] ?? 1), 80);
    }
    out.push(pump.next());
  }
  return { out, rr };
}
for (const [hr, edp] of [[60, 81.1], [75, 82.5], [150, 92.4]]) {
  const { out, rr } = runPump(hr);
  const lastTwo = out.slice(-2 * rr);
  check(`HR ${hr}: peak`, Math.max(...lastTwo), 120.0, 0.1);
  check(`HR ${hr}: end-diastolic`, out[rr * 7 + 37 - 1], edp, 0.1);  // just before the 8th upstroke
}
const pvc = runPump(75, { amps: [1, 1, 1, 0.2, 1.3, 1], beats: 6 }).out;
const peaks = [1, 2, 3, 4, 5].map(k => Math.max(...pvc.slice(k * 200 + 37, k * 200 + 87)).toFixed(0));
check("peaks normal, normal, PVC, post-PVC, normal", peaks.join(","), "120,120,88,132,120");
```


The `if (pump.iabp)` line does nothing for now, since the balloon arrives in Week 28. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  HR 75: end-diastolic` | The decay: `dia + pp * exp(-(ms - riseMs) / tauMs)`. Check `ms` is in milliseconds (`t * 1000 / SAMPLE_RATE`). |
| `XX  ... peak` (not 120) | The upstroke must end exactly at `sys` when `ms` reaches `riseMs`. |
| A step or jump at the start of each beat | The new beat's `base` must be the *current* `this.value`, not `dia`. |
| `XX  peaks normal, normal, PVC...` (the PVC beat goes down) | The `Math.max(p.sys, this.value + 2)` guard when starting a beat. |
| The arterial line is flat | Nothing calls `trigger`: check your `heart.onR(...)` listener. Or `next()` isn't called in the loop. |
| The pleth looks identical to the arterial line | It needs its own `PulsePump` with `delayMs: 250`, `start: 0` and the 0–1 amplitude. |

### Checkpoint

Triggering 120/80 every R-R, once steady:

| HR | peak | end-diastolic (just before upstroke) |
|---|---|---|
| 60 | 120.0 | **81.1** |
| 75 | 120.0 | **82.5** |
| 150 | 120.0 | **92.4** |

Triggering every 800 ms with `ampMod`s 1, 1, 0.2, 1.3, 1 gives peaks **120, 120, 88, 132, 120**.

---

## Week 25B — Wiring it up, and the pleth

**Goal:** arterial and pleth traces on the page, each triggered by the ECG's R-wave.

**New ideas (JS):** reusing one class with different options.

### The science: what the pleth height means

The plethysmograph trace comes from pulse oximetry. Its **height reflects perfusion at the finger, not the saturation.** The SpO₂ number comes from the ratio of how red and infrared light are absorbed, and the trace is a different thing. It's a common confusion: a small pleth trace doesn't mean low saturation, but it may mean the SpO₂ number is less reliable. The pulse reaches the finger later than the arterial line in the aorta, which is why the pleth has a longer delay.

**Reference:** *Capnography and Pulse Oximetry*, StatPearls NBK539754

### The big picture

```
heart.onR ──► onBeat(beat) ──► art.trigger(sys, dia)
                           └─► pleth.trigger(0.7 × amp, 0)
loop ──► art.next() and pleth.next() each sample ──► two more Sweeps
```

### Build it: the wiring 🔴

In `index.html`, add two more canvases after `ecg`: `art` and `pleth`, each 900 × 120.

In `main.js`:

1. Make `art = new PulsePump()`, and `pleth = new PulsePump({ delayMs: 250, start: 0, riseMs: 130, minRise: 0.02 })`. It's the same class with different settings. The pleth's scale runs from 0 to 1, not in mmHg, so its `minRise` must be small too, or every pulse goes off the top of the screen.
2. Make sweeps: arterial in red (`"#f33"`), range 40–160, and pleth in cyan (`"#0ff"`), range −0.1 to 1. Use `mode: "last"` for both, since neither has narrow spikes.
3. In `onBeat(beat)`: `amp = beat.ampMod ?? 1`. Then `sys = P.dbp + (P.sbp − P.dbp) · amp`, and trigger `art` with `(sys, P.dbp)`. Trigger `pleth` with `(0.7 * amp, 0)`.
4. In `pushSamples`, push each pump's `next()` to its sweep. In `drawAll`, draw them.

<details>
<summary><b>Answer</b></summary>

```html

  <canvas id="art" width="900" height="120"></canvas>
  <canvas id="pleth" width="900" height="120"></canvas>
```

```js
import { Ectopy } from "./ectopy.js";
import { PulsePump } from "./pulse.js";
```

```js
const ecgSweep = new Sweep(byId("ecg"));
const artSweep = new Sweep(byId("art"), { color: "#f33", min: 40, max: 160, mode: "last" });
const plethSweep = new Sweep(byId("pleth"), { color: "#0ff", min: -0.1, max: 1, mode: "last" });
const art = new PulsePump();                          // arterial: mmHg
const pleth = new PulsePump({ delayMs: 250, start: 0, riseMs: 130, minRise: 0.02 });
```

```js
function onBeat(beat) {
  flashHeart();
  const amp = beat.ampMod ?? 1;                       // ?? = "use 1 if ampMod is missing"
  const sys = P.dbp + (P.sbp - P.dbp) * amp;
  art.trigger(sys, P.dbp);
  pleth.trigger(0.7 * amp, 0);
}
```

```js
function pushSamples() {
  ecgSweep.push(heart.next());
  artSweep.push(art.next());
  plethSweep.push(pleth.next());
}
```

```js
function drawAll() {
  ecgSweep.draw();
  artSweep.draw();
  plethSweep.draw();
  updateVitals();
}
```

</details>


### Check it

Add these lines above the summary in `tests.js`:

```js
// --- Week 25B ---
const plethTest = new PulsePump({ delayMs: 250, start: 0, riseMs: 130, minRise: 0.02 });
let plethPeak = 0;
for (let i = 0; i < 1000; i++) {
  if (i % 200 === 0) plethTest.trigger(0.7, 0);
  plethPeak = Math.max(plethPeak, plethTest.next());
}
check("pleth peak stays on its 0-to-1 scale", plethPeak, 0.7, 0.01);
```


Check the timing by eye: QRS → about 150 ms → arterial upstroke → about 100 ms later → pleth upstroke. Turn on PVCs and AFib, and watch the beat-to-beat pulse changes. Commit.

### Things to consider

- What should happen when a weak PVC beat's "systolic" target is *lower* than the pressure the line is already at? Try it without any guard and watch the upstroke go the wrong way, then add one.
- The notch sits at a fixed ~300 ms because ejection time changes much less than diastole as HR changes. Real ejection does shorten somewhat at high HR. That's a possible stretch.
- Both traces use the *same class*. If you find yourself copying `PulsePump` to make `PlethPump`, stop and add an option instead.

### Checkpoint

Trigger 120/80 every R-R in a loop (no ECG needed; the Week 25 check lines do exactly this) and record a few beats once it's steady:

| HR | peak | end-diastolic (just before upstroke) |
|---|---|---|
| 60 | 120.0 | **81.1** |
| 75 | 120.0 | **82.5** |
| 150 | 120.0 | **92.4** |

Triggering every 800 ms with ampMods 1, 1, 0.2, 1.3, 1 (so `sys = 80 + 40 × ampMod`) gives peaks **120, 120, 88, 132, 120**.

**References:** Stouffer GA. Arterial pressure (ch. 4). thoracickey.com/4-arterial-pressure/ · Deranged Physiology, *Normal arterial line waveforms*. derangedphysiology.com · *Arterial Lines*. anaestheasier.com/arterial-lines/ · *Broader applications of arterial pressure waveform analysis*. *BJA Education* 2017 (dicrotic notch about ⅓ down the descending limb). bjaed.org · *Capnography and Pulse Oximetry*, StatPearls NBK539754 (pleth height reflects perfusion, not saturation) · *Project 3* textbook, Ex 4.3 and 5.1

---

## Week 26A — Capnography

**Goal:** a CO₂ trace on the *breathing* clock.

**New ideas (JS):** a second, independent clock; a *pure* function (same inputs, same output, no hidden state).

### The science: the four phases of a capnogram

| Phase | Part of the breath | What's happening |
|---|---|---|
| Baseline | Inspiration and dead space | CO₂-free gas |
| Upstroke | Early expiration | Dead space gives way to alveolar gas |
| Plateau | Most of expiration | Alveolar gas, rising slightly. The end of it is EtCO₂ |
| Downstroke | Inspiration begins | Fresh gas sweeps past the sensor |

Normal EtCO₂ is 35–45 mmHg. EtCO₂ depends on cardiac output as well as ventilation, because CO₂ has to be delivered to the lungs. That's why it falls with low output, pulmonary embolism or cardiac arrest, and why its sudden rise can be an early sign of return of circulation.

**References:** *Capnography and Pulse Oximetry*, StatPearls NBK539754 · *Components of a time capnogram*, capnography.com · LITFL, *Capnography Waveform Interpretation* · *Project 3* textbook, Ex 5.2

### The big picture

Capnography runs on the **breathing** clock, not the heart:

```
Capno.next() every sample ──advance phase by (1/250 s) ÷ breath length──► capnoValue(phase, P.etco2) ──► capno Sweep
```

The shape is now a separate *pure* function, `capnoValue(phase, etco2)`: same inputs, same output, no hidden state. That makes it easy to check (and to explain to someone else). The lethal rhythms are just more beat functions for your rhythm `switch`.

### Learn it: a phase clock, and a pure function 🟢

A phase is a number that goes from 0 to 1 across a cycle, then wraps around. Replace `scratch.js` with this:

```js
function brightness(phase) {
  if (phase < 0.25) {
    return phase / 0.25;
  } else if (phase < 0.75) {
    return 1;
  } else {
    return 1 - (phase - 0.75) / 0.25;
  }
}

console.log(brightness(0.1).toFixed(2), brightness(0.5), brightness(0.9).toFixed(2));

const Lamp = {
  phase: 0,
  next(dt, period) {
    this.phase += dt / period;
    if (this.phase >= 1) this.phase -= 1;
    return brightness(this.phase);
  },
};

let highest = 0;
for (let i = 0; i < 100; i++) {
  highest = Math.max(highest, Lamp.next(0.1, 4));
}
console.log(highest, Lamp.phase.toFixed(2));
```

```text
0.40 1 0.40
1 0.50
```

`brightness` is **pure**: the same input always gives the same output, and it remembers nothing. So it's easy to test, and easy to explain. `Lamp` holds the state, and calls the pure function. Keeping the two apart is a good general habit.

To work out how far you are through a straight-line section, `(phase - start) / length` goes from 0 to 1.

### Build it: `capno.js` 🔴

Create `web/js/capno.js`, importing `SAMPLE_RATE` and `P`, and export:

- **`capnoValue(f, e)`**, with `f` as the phase and `e` as EtCO₂:
  - `f < 0.40`: 0
  - `0.40 ≤ f < 0.50`: rises in a straight line from 0 to `e`
  - `0.50 ≤ f < 0.85`: `e`
  - `0.85 ≤ f < 1.00`: falls in a straight line from `e` to 0
- **`Capno`**, an object with `phase: 0`, and a `next()` method. The breath period in seconds is `60 / Math.max(1, P.rr)`. Add `(1 / SAMPLE_RATE) / period` to the phase, wrap it, and return `capnoValue(this.phase, P.etco2)`.

Then add a capno canvas to the page, 900 × 100, with a yellow sweep (`"#ff0"`), range 0–50, and `mode: "last"`. It's driven by `Capno.next()` in `pushSamples`.

<details>
<summary><b>Answer</b></summary>

```js
import { SAMPLE_RATE } from "./ecg.js";
import { P } from "./patient.js";

export const Capno = {
  phase: 0,          // 0 -> 1 across one breath
  next() {
    const period = 60 / Math.max(1, P.rr);           // seconds per breath
    this.phase += (1 / SAMPLE_RATE) / period;
    if (this.phase >= 1) this.phase -= 1;
    return capnoValue(this.phase, P.etco2);
  },
};

// The shape on its own: same inputs, same output, nothing remembered. Easy to check.
export function capnoValue(f, e) {
  if (f < 0.40) return 0;                             // baseline
  if (f < 0.50) return e * (f - 0.40) / 0.10;         // expiratory upstroke
  if (f < 0.85) return e;                             // alveolar plateau
  return e * (1 - (f - 0.85) / 0.15);                 // inspiratory downstroke
}
```

```html

  <canvas id="capno" width="900" height="100"></canvas>
```

```js
import { PulsePump } from "./pulse.js";
import { Capno } from "./capno.js";
```

```js
const capnoSweep = new Sweep(byId("capno"), { color: "#ff0", min: 0, max: 50, mode: "last" });
const art = new PulsePump();                          // arterial: mmHg
```

```js
  plethSweep.push(pleth.next());
  capnoSweep.push(Capno.next());
```

```js
  plethSweep.draw();
  capnoSweep.draw();
```

</details>

### Check it

```js
import { capnoValue } from "./capno.js";
```

Add that import to the top of `tests.js`, and these lines above the summary:

```js
// --- Week 26A ---
check("capno phase 0.20 (baseline)", capnoValue(0.20, 38), 0);
check("capno phase 0.45 (upstroke)", capnoValue(0.45, 38), 19);
check("capno phase 0.70 (plateau)", capnoValue(0.70, 38), 38);
check("capno phase 0.92 (downstroke)", capnoValue(0.92, 38), 20.27);
```


Change the RR slider and watch the breaths spread out, independent of the heart. Commit.

### Checkpoint

RR 14 → **4.29 s** per breath, **1071** samples per breath. With EtCO₂ 38: phase 0.20 → **0**, 0.45 → **19**, 0.70 → **38**, 0.92 → **≈20.3**.

---

## Week 26B — Lethal rhythms and alarms

**Goal:** VTach, VFib and complete heart block, and visible alarms.

**New ideas (JS):** returning "no R-wave" from a beat; state that persists between calls in a plain object; toggling CSS classes with `classList.toggle`; CSS animations.

**Read first:** [MDN: `classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) · [MDN: Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)

### The science: what each rhythm does to the pulse

- **Ventricular tachycardia.** Wide complexes at 150–250 bpm. There's little time to fill, so the pulse is weak (here `ampMod` 0.35), and it may be absent altogether.
- **Ventricular fibrillation.** Chaotic electrical activity, with no organized contraction and no cardiac output. In your model it has no R-wave, so nothing triggers the pumps, and the arterial line decays flat. You don't have to code that part. It follows directly from the design.
- **Complete heart block.** The atria and ventricles beat independently, with no relationship between P waves and QRS complexes. That's why this needs *two clocks*. Atrial rate is usually about 80, and the ventricular escape rate about 40.

**Reference:** *Project 3* textbook, Ex 5.3

### The big picture

The lethal rhythms are more beat functions for your rhythm `switch`. Alarms are one line each, turning a CSS class on or off.

### Learn it: two clocks, and alarms 🟢

Add `.alarm` to `scratch.css`:

```css

.alarm {
  color: red;
  animation: blink 1s infinite;
}

@keyframes blink {
  50% { opacity: 0.2; }
}
```

Replace `scratch.js` with this:

```js
const Bus = {
  phaseMin: 0,
  arrivals(tripMin, everyMin) {
    const found = [];
    let t = 0;
    while (this.phaseMin + (tripMin - t) >= everyMin) {
      t += everyMin - this.phaseMin;
      found.push(t);
      this.phaseMin = 0;
    }
    this.phaseMin += tripMin - t;
    return found;
  },
};

console.log(JSON.stringify(Bus.arrivals(25, 10)));
console.log(JSON.stringify(Bus.arrivals(25, 10)));

const el = document.getElementById("total");
el.classList.toggle("alarm", 5 > 3);
console.log(el.classList.contains("alarm"));
el.classList.toggle("alarm", 5 < 3);
console.log(el.classList.contains("alarm"));
```

```text
[10,20]
[5,15,25]
true
false
```

- `Bus.phaseMin` persists between calls. The second trip's first bus comes after 5 minutes rather than 10, because the leftover from the first trip carried over. Complete heart block needs exactly this: the atria don't restart with each ventricular beat.
- `classList.toggle("alarm", condition)` adds the class if the condition is true, and removes it if false. It's one line per alarm.

### Build it: the rhythms 🔴

Add these to `ecg.js`:

**`vtachBeat(rrMs)`:** `actual` is `rrMs` clamped to 240–400 ms, which forces 150–250 bpm. Place a wide `pvcComplex(samplesFor(200))` at the start of the buffer, with no P wave. `rOffset` is 30% into the complex. Return `{ samples, rOffset, rrMs: actual, ampMod: 0.35 }`.

**`vfibChunk(ms = 500)`:** a chaotic sum of a few sines (4–8 Hz, random phases, amplitude around 0.2) plus some `randn()` noise. Return `{ samples, rOffset: -1, rrMs: ms }`. Since `-1` never matches `index`, nothing triggers the pumps.

**`CHB`:** an object with `atrialPhaseMs: 0`, and a method `beat(rrMsIgnored, atrialRate = 80, ventricularRate = 40)`:

1. `rr = 60000 / ventricularRate`. Make a zero-filled buffer.
2. Add a QRS at 30% of the beat, and a T wave after its ST segment.
3. Walk the atrial clock through this beat using `ppMs = 60000 / atrialRate`, as in the `Bus`: each time it passes a P–P interval, add a `pWave` at that offset. Carry the remainder over.
4. Return `{ samples, rOffset, rrMs: rr }`.

In `cardiac.js`, add the cases: `"VTACH"` returns `vtachBeat`, `"VFIB"` returns `() => vfibChunk()`, and `"CHB"` returns `rr => CHB.beat(rr)`.

<details>
<summary><b>Answer</b></summary>

```js

export function vtachBeat(rrMs) {
  const actual = Math.max(240, Math.min(400, rrMs));    // forces 150–250 bpm
  const samples = new Array(samplesFor(actual)).fill(0);
  const n = samplesFor(200);
  place(samples, 0, pvcComplex(n, 1.5));
  return { samples, rOffset: Math.round(0.3 * n), rrMs: actual, ampMod: 0.35 };
}

export function vfibChunk(ms = 500) {
  const total = samplesFor(ms);
  const samples = new Array(total).fill(0);
  for (const hz of [4.1, 5.3, 6.7, 7.9]) {
    const phase = Math.random() * 2 * Math.PI;
    const size = 0.1 + 0.2 * Math.random();
    for (let i = 0; i < total; i++) {
      samples[i] += size * Math.sin(2 * Math.PI * hz * (i / SAMPLE_RATE) + phase);
    }
  }
  for (let i = 0; i < total; i++) samples[i] += 0.03 * randn();
  return { samples, rOffset: -1, rrMs: ms };   // rOffset -1: NO R-wave, so no pulse
}

// Complete heart block: TWO independent clocks writing into one buffer.
export const CHB = {
  atrialPhaseMs: 0,               // persists between beats, which is the whole point
  beat(rrMsIgnored, atrialRate = 80, ventricularRate = 40) {
    const rr = 60000 / ventricularRate;
    const total = samplesFor(rr);
    const samples = new Array(total).fill(0);
    const qS = samplesFor(120), stS = samplesFor(100), tS = samplesFor(160), pS = samplesFor(80);
    const qrsStart = Math.floor(0.3 * total);
    add(samples, qrsStart, qrsComplex(qS));
    add(samples, qrsStart + qS + stS, tWave(tS));

    const ppMs = 60000 / atrialRate;
    let t = 0;
    while (this.atrialPhaseMs + (rr - t) >= ppMs) {
      t += ppMs - this.atrialPhaseMs;
      add(samples, samplesFor(t), pWave(pS));
      this.atrialPhaseMs = 0;
    }
    this.atrialPhaseMs += rr - t;
    return { samples, rOffset: qrsStart + Math.round(0.4 * qS), rrMs: rr };
  },
};
```

```js
import { nsrBeat, afibBeat, vtachBeat, vfibChunk, CHB } from "./ecg.js";
```

```js
    case "VTACH":
      return vtachBeat;
    case "VFIB":
      return () => vfibChunk();
    case "CHB":
      return rr => CHB.beat(rr);
    default:
```

</details>

### Check it

```js
import { vtachBeat, vfibChunk, CHB } from "./ecg.js";
```

Add that import to the top of `tests.js`, and these lines above the summary:

```js
// --- Week 26B ---
check("VTach forces R-R down to 400 ms", vtachBeat(800).rrMs, 400, 0);
check("VTach caps at 240 ms", vtachBeat(200).rrMs, 240, 0);
check("VFib has no R-wave", vfibChunk().rOffset, -1, 0);
check("CHB ventricular R-R at rate 40", CHB.beat(800).rrMs, 1500, 0);
const phaseBefore = CHB.atrialPhaseMs;
check("CHB atrial phase carries over (0 to 750 ms)", phaseBefore >= 0 && phaseBefore < 750, true);
```


### Build it: alarms 🔴

PVCs and VFib are bigger than a normal QRS, so first widen the ECG's scale in `main.js`: `new Sweep(byId("ecg"), { min: -1, max: 2.2 })`. Then, in `style.css`, add the `.alarm` rule and `@keyframes` from your scratch file. In `updateVitals`, use `classList.toggle`:

- On `v-hr`: when the rhythm is VTACH or VFIB.
- On `v-bp`: when `map()` is under 65.
- On `v-spo2`: when `P.spo2` is under 90.

<details>
<summary><b>Answer</b></summary>

```css

.alarm {
  color: red;
  animation: blink 1s infinite;
}

@keyframes blink {
  50% { opacity: 0.2; }
}
```

```js
const ecgSweep = new Sweep(byId("ecg"), { min: -1, max: 2.2 });
```

```js
  byId("v-etco2").textContent = P.etco2;
  byId("v-hr").classList.toggle("alarm", P.rhythm === "VTACH" || P.rhythm === "VFIB");
  byId("v-bp").classList.toggle("alarm", map() < 65);
  byId("v-spo2").classList.toggle("alarm", P.spo2 < 90);
```

</details>


Choose VFib on the page. The arterial line and pleth should decay flat, because nothing triggers them. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  capno phase 0.45` | The upstroke band: `e * (f - 0.40) / 0.10`. |
| `XX  capno phase 0.92` | The downstroke band: `e * (1 - (f - 0.85) / 0.15)`. |
| The CO₂ trace speeds up with HR | `Capno.next()` is using the heart rate instead of `P.rr`. |
| VFib still has a pulse | `vfibChunk` is returning a real `rOffset`; it must be `-1`. |
| CHB P waves line up with every QRS | The atrial clock is being reset each beat instead of carried over. |
| The alarm never blinks | `classList.toggle("alarm", condition)` is on the wrong element, or the CSS `@keyframes blink` is missing. |

### Things to consider

- Change HR and the CO₂ trace shouldn't change at all. That's a quick way to prove your two clocks are independent.
- Naming varies between books: some call the inspiratory downstroke "phase 0" and reserve "phase IV" for an end-plateau upswing. Write a one-line comment about which convention you're using.
- VFib and asystole are cardiac-arrest rhythms. The "flat arterial line" is the point of the lesson: no effective circulation.

### Checkpoint

- RR 14 → **4.29 s** per breath, **1071** samples per breath.
- With EtCO₂ 38: phase 0.20 → **0**, 0.45 → **19**, 0.70 → **38**, 0.92 → **≈20.3**.

**References:** *Capnography and Pulse Oximetry*, StatPearls NBK539754 (four phases; normal EtCO₂ 35–45 mmHg) · *Components of a time capnogram*, capnography.com · LITFL, *Capnography Waveform Interpretation* · NUEM Blog / EMS1 (EtCO₂ falls with low cardiac output, PE, arrest) · *Project 3* textbook, Ex 5.2 and 5.3

---

## Week 27A — Mechanical circulatory support: the device model

**Goal:** devices that flatten the arterial pulse as flow rises, raise MAP on VA-ECMO, and change SpO₂ correctly for VV vs VA.

**New ideas (JS):** objects with methods that read each other through `this`; a device "manager" that combines several devices into one effect.

### The science: what support does to the waveform

**Impella** is a microaxial pump across the aortic valve, moving blood continuously from the LV to the aorta. **VA-ECMO** returns oxygenated blood to the arterial side. Both provide continuous, non-pulsatile flow, so as device flow rises and native ejection falls, the pulse pressure narrows. A pulse pressure above about 10 mmHg suggests the LV is still ejecting.

**The LV distension problem.** VA-ECMO returns blood against the aortic valve, raising afterload. A failing LV may not be able to open the valve, so it distends. Adding an Impella unloads the ventricle, a combination often called "ECPELLA". Your `lvRisk()` is a teaching simplification of this tradeoff.

**VV versus VA for oxygen.** VV-ECMO is **in series**: blood is oxygenated before it reaches the lungs, so its effect depends on how much of the venous return it captures. VA-ECMO is **in parallel**: its oxygenated blood mixes with whatever the heart and lungs produced. An earlier version of this project mixed VV in parallel, and gave 92% where about 98% is expected.

**References:** *Unloading the Left Ventricle in Venoarterial ECMO*. *Circulation* 2022. doi:10.1161/CIRCULATIONAHA.122.062371 · *LV distension and venting strategies on VA-ECMO*, PMC6531683 · *Flow Optimization… Prevention of LV Distention during VA-ECMO*, IntechOpen 2018 · *Project 3* textbook, Ex 6.1, 6.3–6.5

### The big picture

Devices don't make their own waveforms. They **modify** what the pulse pumps get:

```
devices.pulsatility()  how much of the flow is pulsatile (1 = no support, → 0.08 at full support)
devices.mapOffset()    how much VA-ECMO raises mean pressure
devices.spo2(native)   oxygen saturation after ECMO mixing
devices.lvRisk()       VA-ECMO afterload minus Impella unloading
            │
heart.onR listener ──uses all of these──► art.trigger(sys, dia, sharp) and pleth.trigger(...)
```

All device logic is in one object, so the arterial line, the pleth and the readouts all ask the same place.

### Learn it: objects that consult each other 🟢

Here's a house with two heaters, and one object that answers questions about them both. Replace `scratch.js` with this:

```js
const house = {
  gas: {
    on: false,
    level: 0,
    table: [0, 2, 4, 6],
    output() { return this.on ? this.table[this.level] : 0; },
  },
  solar: {
    on: false,
    panels: 3,
    output() { return this.on ? this.panels * 0.5 : 0; },
  },
  total() {
    return this.gas.output() + this.solar.output();
  },
  shareFromGas() {
    const t = this.total();
    if (t === 0) return 0;
    return this.gas.output() / t;
  },
};

console.log(house.total());
house.gas.on = true;
house.gas.level = 2;
house.solar.on = true;
console.log(house.total(), house.shareFromGas().toFixed(2));
```

```text
0
5.5 0.73
```

Inside `gas.output()`, `this` is `gas`. Inside `total()`, `this` is `house`, so it can reach both heaters. All the logic is in one place, and anything that needs to know the total asks `house`.

### Build it: `devices.js` 🔴

Create `web/js/devices.js`, importing `P`, and export an object named `devices`, starting like this:

```js
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
```

Add these methods:

- **`pulsatility()`:** `linear = nativeCO / (nativeCO + deviceFlow)`, where device flow is the Impella flow plus ECMO arterial flow. Return `max(0.08, linear²)`. Squaring it is a **tuning choice**, made so high flow flattens the a-line hard, as it does clinically.
- **`mapOffset()`:** VA-ECMO raises mean pressure by about 2.2 mmHg per L/min of arterial flow.
- **`spo2(nativeSpo2)`:** if ECMO is off, or its flow is 0, return the native value. For **VV**, `frac = min(1, flow / CO)`, and the result is `frac·100 + (1 − frac)·native`. For **VA**, it's a flow-weighted mix of `nativeCO` at `nativeSpo2`, and `flow` at 100.
- **`lvRisk()`:** 0 unless VA-ECMO is on. Otherwise, it's the ECMO load (`0.2 × ECMO flow`) minus the Impella unloading (`0.25 × Impella flow`), and never below 0.

<details>
<summary><b>Answer</b></summary>

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
    return Math.max(0.08, linear ** 2);
  },

  mapOffset() {
    return 2.2 * this.ecmo.arterialFlow();
  },

  spo2(nativeSpo2) {
    const e = this.ecmo;
    if (!e.on || e.flow === 0) return nativeSpo2;
    if (e.mode === "VV") {
      // VV: ECMO is IN SERIES. A fraction of venous return (flow / CO) is fully
      // oxygenated before it reaches the lungs. Recirculation is ignored.
      const frac = Math.min(1, e.flow / P.nativeCO);
      return frac * 100 + (1 - frac) * nativeSpo2;
    }
    // VA: oxygenated blood joins the arterial side IN PARALLEL with native output
    return (P.nativeCO * nativeSpo2 + e.flow * 100) / (P.nativeCO + e.flow);
  },

  lvRisk() {
    // VA-ECMO adds afterload; an Impella unloads the LV ("ECPELLA")
    if (!this.ecmo.on || this.ecmo.mode !== "VA") return 0;
    return Math.max(0, 0.2 * this.ecmo.flow - 0.25 * this.impella.flow());
  },
};
```

</details>

### Check it

Add the import to the top of `tests.js`, and these lines above the summary:

```js
import { devices } from "./devices.js";
```

```js
// --- Week 27 ---
P.nativeCO = 4.5;
devices.impella.on = true;
for (const [level, puls] of [[0, 1.0], [3, 0.479], [6, 0.342], [9, 0.261]]) {
  devices.impella.level = level;
  check(`Impella P${level}: pulsatility`, devices.pulsatility(), puls, 0.001);
}
devices.impella.on = false;
devices.ecmo.on = true; devices.ecmo.mode = "VA"; devices.ecmo.flow = 6.0;
check("VA-ECMO 6 L/min: pulsatility", devices.pulsatility(), 0.184, 0.001);
check("VA-ECMO 6 L/min: MAP rises by", devices.mapOffset(), 13.2, 0.05);
devices.ecmo.flow = 4.0;
check("VA-ECMO 4 L/min: LV risk", devices.lvRisk(), 0.8);
devices.impella.on = true; devices.impella.level = 6;
check("…add Impella P6: LV risk", devices.lvRisk(), 0);
devices.impella.on = false;
devices.ecmo.mode = "VV";
check("VV-ECMO 4 L/min, native 85%: SpO2", devices.spo2(85), 98.3, 0.1);
check("VV-ECMO doesn't flatten the pulse", devices.pulsatility(), 1.0);
devices.ecmo.on = false;                        // put the devices back
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  Impella P6: pulsatility` | `linear = nativeCO ÷ (nativeCO + device flow)`, then square it with a floor of 0.08. |
| `XX  VV-ECMO ... SpO2` (92 instead of 98) | You used the parallel (VA) mix for VV. VV uses `frac = flow ÷ CO`. |
| `XX  VV-ECMO doesn't flatten the pulse` | `arterialFlow()` must be 0 in VV mode. |
| `TypeError: this.flowTable is undefined` | `flow()` was written as an arrow function (`=>`). Arrow functions don't get their own `this`; use `flow() { ... }`. |
| MAP drops as support increases | You shrank the pulse pressure around DBP instead of around MAP. |

### Checkpoint

| device flow (L/min) | 0 | 2.0 | 3.2 | 4.3 | 6.0 |
|---|---|---|---|---|---|
| pulsatility | 1.00 | 0.479 | 0.342 | 0.261 | 0.184 |

VV-ECMO at 4.0 L/min, native SpO₂ 85, CO 4.5 → **≈98%**.

---

## Week 27B — Applying the devices to the monitor

**Goal:** a device panel that changes the arterial line, the pleth and the readouts.

**New ideas (JS):** nothing new in the language. This lesson connects the device model to everything else.

### The science: keeping the mean, shrinking the swing

Support flattens the pulse, but it doesn't lower mean pressure. So you want to keep MAP where it belongs, and shrink the swing around it. Two-thirds of the pulse pressure sits above MAP, and one-third below it, which is where the MAP ≈ DBP + PP/3 rule comes from. And the dicrotic notch fades as support rises, because the aortic valve opens less.

The pleth still means perfusion, and that stays true on support. On VA-ECMO with high flow, you may have a good SpO₂ and a small pleth, because the flow is non-pulsatile. So a poor pulse-ox signal on ECMO doesn't necessarily mean poor oxygenation.

### The big picture

```
onBeat(beat) ──► devices.pulsatility(), devices.mapOffset() ──► art.trigger(sys, dia, puls)
updateVitals ──► devices.spo2(P.spo2), devices.lvRisk() ──► the readouts
```

### Build it: the panel and the wiring 🔴

**`index.html`:** add a section with:

- Impella: a checkbox (`imp-on`) and a slider from 0 to 9 (`imp-level`, with `imp-level-out`).
- ECMO: a checkbox (`ecmo-on`), a select with VA and VV (`ecmo-mode`), and a flow slider from 0 to 6, in steps of 0.5 (`ecmo-flow`, with `ecmo-flow-out`).
- A slider for `P.nativeCO` from 1 to 6 (`native-co`, with `native-co-out`), bound with your `bindSlider`.
- Readouts: `v-pp` for pulse pressure, and `v-lv` for LV distension risk.

**`main.js`:** wire up the controls. In `onBeat`:

```js
const puls = devices.pulsatility();
const m = map() + devices.mapOffset();
const pp = (P.sbp - P.dbp) * puls * amp;
```

Then center the swing on the mean: `sys = m + 2 * pp / 3`, and `dia = m - pp / 3`. Trigger `art` with `puls` as `sharp`, so the notch fades as support rises. Trigger the pleth with `(0.7 * amp * Math.max(0.12, puls), 0, puls)`.

In `updateVitals`, show `devices.spo2(P.spo2)` rounded, the displayed pulse pressure, and the LV risk.

Lower `nativeCO` to 2.0, which is cardiogenic shock, and watch the same Impella level flatten the line much more.

<details>
<summary><b>Answer</b></summary>

```html
  <section class="controls">
    <label><input id="imp-on" type="checkbox"> Impella</label>
    <label>P-level <input id="imp-level" type="range" min="0" max="9" value="0"></label><span id="imp-level-out">0</span>
    <label><input id="ecmo-on" type="checkbox"> ECMO</label>
    <select id="ecmo-mode">
      <option value="VA">VA</option>
      <option value="VV">VV</option>
    </select>
    <label>Flow <input id="ecmo-flow" type="range" min="0" max="6" step="0.5" value="3"></label><span id="ecmo-flow-out">3</span>
    <label>Native CO <input id="native-co" type="range" min="1" max="6" step="0.5" value="4.5"></label><span id="native-co-out">4.5</span>
    <p>Pulse pressure <span id="v-pp">40</span> mmHg, LV distension risk <span id="v-lv">0</span></p>
  </section>
```

```js
import { Capno } from "./capno.js";
import { devices } from "./devices.js";
```

```js
bindSlider("native-co", "nativeCO");
byId("imp-on").addEventListener("change", e => { devices.impella.on = e.target.checked; });
byId("imp-level").addEventListener("input", e => {
  devices.impella.level = parseFloat(e.target.value);
  byId("imp-level-out").textContent = e.target.value;
});
byId("ecmo-on").addEventListener("change", e => { devices.ecmo.on = e.target.checked; });
byId("ecmo-mode").addEventListener("change", e => { devices.ecmo.mode = e.target.value; });
byId("ecmo-flow").addEventListener("input", e => {
  devices.ecmo.flow = parseFloat(e.target.value);
  byId("ecmo-flow-out").textContent = e.target.value;
});

```

```js
function onBeat(beat) {
  flashHeart();
  const amp = beat.ampMod ?? 1;                       // ?? = "use 1 if ampMod is missing"
  const puls = devices.pulsatility();
  const m = map() + devices.mapOffset();
  const pp = (P.sbp - P.dbp) * puls * amp;
  // keep the MEAN where it belongs, then shrink the swing around it
  art.trigger(m + 2 * pp / 3, m - pp / 3, puls);
  pleth.trigger(0.7 * amp * Math.max(0.12, puls), 0, puls);
}
```

```js
  byId("v-spo2").textContent = Math.round(devices.spo2(P.spo2));
  byId("v-pp").textContent = ((P.sbp - P.dbp) * devices.pulsatility()).toFixed(1);
  byId("v-lv").textContent = devices.lvRisk().toFixed(2);
```

</details>


Commit.

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

## Week 28 — IABP: counterpulsation timed off the ECG

**Goal:** a balloon that **inflates at the dicrotic notch** and **deflates on the R-wave**, giving the classic assisted waveform at 1:1 or 1:2.

**New ideas (JS):** adding behavior to an existing class through hooks, without rewriting it; event-driven timing.

### The science: counterpulsation

An intra-aortic balloon sits in the descending aorta, and works in opposition to the heart.

- **It inflates at the dicrotic notch,** just as diastole begins. This pushes blood back toward the coronary arteries and raises diastolic pressure, called **diastolic augmentation**. The augmented peak usually exceeds unassisted systole.
- **It deflates just before systole,** on the R-wave. This creates a sudden drop in pressure, lowering **assisted end-diastolic pressure** by 15–20 mmHg, so the next ejection faces less afterload. **Assisted systole** runs about 5 mmHg lower than unassisted.

Timing errors are what a clinician looks for on the trace: inflating too early or late, and deflating too early or late, each have a recognizable shape. At high heart rates, the R-wave comes soon after the notch, so the balloon barely has time to act, which you'll see at HR 150.

An earlier version of this project hung the balloon on a fixed-length pulse, and it only lowered end-diastolic pressure by about 7 mmHg. With the continuous `PulsePump`, it behaves properly.

**References:** *The Intra-aortic Balloon Pump: A Focused Review*, 2024, PMC11307388 · EMCrit IBCC, *Intra-aortic balloon pump*. emcrit.org/ibcc/iabp/ · LITFL, *IABP Trouble-shooting* · NCBI Bookshelf NBK543576 · *Project 3* textbook, Ex 6.2

### The big picture

The IABP is timed off the ECG, just like a real console:

```
R-wave ──► art.deflate()     "systole is coming: drop the pressure now"
           art.trigger(...)  "start a new pulse in 150 ms"
PulsePump.next(): after ~290 ms into a beat (the dicrotic notch) → inflate (add pressure)
```

You add a small `iabp` state object to `PulsePump`, one public hook (`deflate`), and a few lines in `next()`. Nothing else in the monitor changes.

Add an `iabp` term that `PulsePump.next()` adds to its output:

- **Inflate:** once `ms` passes the notch (about 290 ms), the term rises over about 40 ms to roughly 35 mmHg and then sags slowly, giving diastolic augmentation.
- **Deflate:** the next R-wave arrives about 150 ms *before* the next upstroke. On that R-wave, ramp the term from wherever it is down to about **−18 mmHg** over 120 ms. The next upstroke then starts from this lower pressure, which is the "assisted end-diastolic pressure".
- **Assisted systole:** on assisted beats, aim systole about 5 mmHg lower (less afterload).
- **Ratio:** assist every beat (1:1) or every other beat (1:2) using a beat counter.

### Learn it: adding a hook 🟢

A hook is a small method or check added to a class, which lets new behavior plug in while everything else stays as it was. Replace `scratch.js` with this:

```js
class Toaster {
  constructor() {
    this.heat = 0;
    this.turbo = { enabled: false, every: 1, count: 0, active: false };
  }

  startSlice() {
    const b = this.turbo;
    b.count++;
    b.active = b.enabled && (b.count % b.every === 0);
  }

  next() {
    let v = 10;
    if (this.turbo.active) v += 5;
    return v;
  }
}

const t = new Toaster();
t.startSlice();
console.log(t.next());

t.turbo.enabled = true;
t.turbo.every = 2;
const out = [];
for (let i = 0; i < 4; i++) {
  t.startSlice();
  out.push(t.next());
}
console.log(out.join(" "));
```

```text
10
15 10 15 10
```

When `enabled` is false, nothing changes, so older behavior is safe, and every old check still passes. `count % every === 0` is the same trick as bigeminy, and it's how you'll do a 1:2 ratio.

### Build it: the balloon 🔴

Add these to `PulsePump`:

**In the constructor:**

```js
this.iabp = { enabled: false, ratio: 1, count: 0, assisting: false, term: 0, deflating: null };
```

**A new method, `deflate()`,** which you'll call from `onBeat`, **before** `trigger()`. If the balloon is enabled and assisting, set `deflating` to `{ k: 0, from: b.term }`, to start the ramp down from the current term.

**In `next()`, when a new upstroke begins:** add one to `count`. `assisting` is `enabled && count % ratio === 0`. Reset `term` to 0 and `deflating` to `null`. On assisted beats, aim systole 5 mmHg lower.

**In `next()`, after computing `v`:**

- If deflating, add 1 to `k`, and ramp `term` from `from` down to −18, using `smoothstep(Math.min(1, k / samplesFor(120)))`.
- Otherwise, on assisted beats past 290 ms: `term = 35 · smoothstep(min(1, (ms − 290) / 40)) · exp(−max(0, ms − 330) / 600)`.
- Add `term` to `v`.

In `index.html`, add a checkbox (`iabp-on`) and a 1:1 / 1:2 select (`iabp-ratio`). In `main.js`, wire them up, and call `art.deflate()` first in `onBeat`.

<details>
<summary><b>Answer</b></summary>

```js
    this.t = 0;             // samples since this beat's upstroke began
    this.iabp = { enabled: false, ratio: 1, count: 0, assisting: false, term: 0, deflating: null };
```

```js
  // public hook: call from heart.onR(...) BEFORE trigger()
  deflate() {
    const b = this.iabp;
    if (!b.enabled || !b.assisting) return;
    b.deflating = { k: 0, from: b.term };         // start the ramp down from the current term
  }

```

```js
      const b = this.iabp;
      b.count++;
      b.assisting = b.enabled && (b.count % b.ratio === 0);
      b.term = 0;
      b.deflating = null;
      const aim = b.assisting ? p.sys - 5 : p.sys;
      this.beat = { base: this.value, sys: Math.max(aim, this.value + this.minRise), dia: p.dia, sharp: p.sharp };
```

```js
    const balloon = this.iabp;
    if (balloon.deflating) {
      balloon.deflating.k++;
      const u = smoothstep(Math.min(1, balloon.deflating.k / samplesFor(120)));
      balloon.term = balloon.deflating.from + (-18 - balloon.deflating.from) * u;
    } else if (balloon.assisting && ms >= 290) {
      balloon.term = 35 * smoothstep(Math.min(1, (ms - 290) / 40)) * Math.exp(-Math.max(0, ms - 330) / 600);
    }
    v += balloon.term;
    this.t++;
```

```html
    <label><input id="iabp-on" type="checkbox"> IABP</label>
    <select id="iabp-ratio">
      <option value="1">1:1</option>
      <option value="2">1:2</option>
    </select>
```

```js
byId("iabp-on").addEventListener("change", e => { art.iabp.enabled = e.target.checked; });
byId("iabp-ratio").addEventListener("change", e => { art.iabp.ratio = parseFloat(e.target.value); });

```

```js
  flashHeart();
  art.deflate();
```

</details>

There's a catch. `this.value` is now the pressure including the balloon term, and the next upstroke starts from there, which is what you want: it starts from the lowered pressure.

### Check it

Add these lines above the summary in `tests.js`:

```js
// --- Week 28 ---
for (const [hr, aug, edp] of [[60, 130.1, 63.0], [75, 130.1, 64.2]]) {
  const { out, rr } = runPump(hr, { iabp: true });
  const lastTwo = out.slice(-2 * rr);
  check(`IABP HR ${hr}: augmentation peak`, Math.max(...lastTwo), aug, 0.2);
  check(`IABP HR ${hr}: assisted end-diastolic`, out[rr * 7 + 37 - 1], edp, 0.2);
}
const fast = runPump(150, { iabp: true });
check("IABP HR 150: no augmentation (peak = assisted systole)", Math.max(...fast.out.slice(-2 * fast.rr)), 115.0, 0.2);
```


Use 1:2 to compare assisted and unassisted beats side by side. Then look at what happens at HR 150. When does the next R-wave arrive compared with the notch? Commit, and write a `DEVLOG.md` entry. The monitor is complete.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  IABP ... augmentation peak` (about 115) | Inflation never happens: `assisting` is false (the ratio test), or the `ms >= 290` condition is never reached. |
| `XX  assisted end-diastolic` (well above 63) | `deflate()` isn't being called on the R-wave, or it returns early because `assisting` is false. |
| The pressure drops but never comes back up | `term` isn't reset to 0 when the next upstroke starts. |
| 1:2 assists every beat | Count the beat *before* testing `count % ratio`. |
| Changes broke your Week 25 checks | With `iabp.enabled` false, nothing new should run. Reload `tests.html`: if the Week 25 lines turned `XX`, an IABP line is running when it shouldn't. |

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

You have three working projects. These lessons put them on one web page. All of it is optional, and each lesson is useful on its own.

Final layout of `index.html`:

```
┌────────────────────────── Monitor (Part 3) ─────────────────────────┐
│ ECG / ART / PLETH / CO2 sweeps                        HR BP SpO2 EtCO2 │
├──────────── Machine (Week 29) ───────────┬──── TCI (Week 30) ─────────┤
│ agent · dial · O2/air/N2O · MAC · FiO2   │ Cp/Ce chart from JSON      │
└──────────────────────────────────────────┴────────────────────────────┘
```

---

## Week 29A — Port the anesthesia machine to JavaScript

**Goal:** `machine.js`, a JS translation of your Part 2 Python, giving the same numbers.

**New ideas (JS):** class getters (`get cardiacOutput()`, JS's version of `@property`); `Object.values`, `Object.entries`; `.reduce`; checking that two languages give identical numbers.

**Read first:** [javascript.info: Getters and setters](https://javascript.info/property-accessors) · [Object.keys, values, entries](https://javascript.info/keys-values-entries)

### The science: the same model

There's nothing new here. It's Gas Man's model, which you built in Weeks 13–16. Two languages, one model and the same numbers is both the best possible check and the best way to learn a second language. If the JS and Python disagree, you've found a bug in one of them.

### The big picture

You already have a working anesthesia machine in Python. This week you **translate** it to JavaScript, so it can run live in the same page as the monitor:

```
machine/volatile.py (Python, checked)  ──translate line by line──►  web/js/machine.js (JavaScript)
tests.js: run 5 simulated minutes ──► must match the Python numbers to 3 decimals
```

Two languages, one model, the same numbers. That's both the best possible check and the best way to learn a second language.

### Learn it: getters and looping over objects 🟢

Replace `scratch.js` with this:

```js
class Shop {
  constructor() {
    this.stock = {
      tea: { price: 3, count: 2 },
      cake: { price: 5, count: 1 },
    };
  }

  get value() {
    return Object.values(this.stock).reduce((sum, item) => sum + item.price * item.count, 0);
  }

  list() {
    const out = [];
    for (const [name, item] of Object.entries(this.stock)) {
      out.push(`${name}:${item.count}`);
    }
    return out.join(" ");
  }
}

const s = new Shop();
console.log(s.value);
console.log(s.list());
```

```text
11
tea:2 cake:1
```

| Python | JavaScript |
|---|---|
| `@property` and `def value(self):` | `get value() {` |
| `d.values()` | `Object.values(d)` |
| `d.items()` | `Object.entries(d)` |
| `for name, item in d.items():` | `for (const [name, item] of Object.entries(d)) {` |
| `sum(x * 2 for x in a)` | `a.reduce((sum, x) => sum + x * 2, 0)` |

`.reduce` walks through an array keeping a running total, starting from the last input, here 0.

### Build it: `machine.js` 🔴

Create `web/js/machine.js`, importing `Compartment` from `math.js`. Keep your Python files open side by side.

**`AGENTS`:** four entries with the same numbers as `agents.py`, for example:

```js
sevoflurane: { name: "Sevoflurane", mac: 2.0, bloodGas: 0.65, lam: { VRG: 1.7, muscle: 3.1, fat: 48 } },
```

Name the N₂O key `nitrous_oxide`.

**`class VolatileModel`,** with a constructor taking `agent`, and these starting values: `comps` (the same three compartments as Python), `alveolar`, `circuit`, `dial`, `time`, `lastUptake` and `extraRate` all 0. Set `o2Flow` to 8, `airFlow` and `n2oFlow` to 0, `rr` to 14, `tv` to 0.5, `FRC` to 2.5, `deadSpace` to 0.3, `circuitFio2` to 0.95, `vSystem` to 7, and `vo2` to 0.25.

Then translate these, one at a time:

- Getters `freshGasFlow`, `minuteVentilation` and `cardiacOutput`
- `_mixedVenous()` and `_inspired()`, testing each against a hand-picked input
- `_updateFio2(dt)`, using `freshGasFio2`, which you also need to translate as a small exported function
- `step(dt)`: the same equations, in the same order as your Python
- `macValue()`: the alveolar value divided by the agent's MAC

**`class DualMachine`,** matching your `DualAgentModel`: `volatile`, `n2o`, `setFlows(o2, air, n2o)`, `step(dt)` with the second gas effect, and `totalMac()`.

**`macColor(mac)`:** returns `"red"` below 0.5, `"orange"` below 1.0, `"yellow"` below 1.3, and `"green"` otherwise.

<details>
<summary><b>Hint</b></summary>

`Object.entries(this.comps)` gives you `[name, comp]` pairs, and `this.agent.lam[name]` gives λ, which replaces your Python `_lambda_for`. Translate one helper at a time, in the same order as Week 14.

</details>
<details>
<summary><b>Answer</b></summary>

```js
import { Compartment } from "./math.js";

export const AGENTS = {
  sevoflurane: { name: "Sevoflurane", mac: 2.0, bloodGas: 0.65, lam: { VRG: 1.7, muscle: 3.1, fat: 48 } },
  isoflurane: { name: "Isoflurane", mac: 1.15, bloodGas: 1.46, lam: { VRG: 1.6, muscle: 2.9, fat: 45 } },
  desflurane: { name: "Desflurane", mac: 6.0, bloodGas: 0.42, lam: { VRG: 1.3, muscle: 2.0, fat: 27 } },
  nitrous_oxide: { name: "Nitrous oxide", mac: 104, bloodGas: 0.47, lam: { VRG: 1.1, muscle: 1.2, fat: 2.3 } },
};

export function freshGasFio2(o2, air, n2o) {
  const total = o2 + air + n2o;
  if (total <= 0) return 0;
  return (o2 * 1.0 + air * 0.21) / total;
}

export function macColor(mac) {
  if (mac < 0.5) return "red";
  if (mac < 1.0) return "orange";
  if (mac < 1.3) return "yellow";
  return "green";
}

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
    this.circuitFio2 = 0.95; this.vSystem = 7; this.vo2 = 0.25;
  }

  get freshGasFlow() { return this.o2Flow + this.airFlow + this.n2oFlow; }

  get minuteVentilation() { return this.rr * this.tv; }

  get cardiacOutput() {
    return Object.values(this.comps).reduce((sum, c) => sum + c.flow, 0);
  }

  _mixedVenous() {
    let total = 0;
    for (const [name, comp] of Object.entries(this.comps)) {
      total += comp.flow * comp.partialPressure(this.agent.lam[name]);
    }
    return total / this.cardiacOutput;
  }

  _inspired() {
    const mv = this.minuteVentilation;
    if (this.freshGasFlow >= mv) return this.dial;
    return (this.freshGasFlow * this.dial + (mv - this.freshGasFlow) * this.circuit) / mv;
  }

  _updateFio2(dt) {
    const fresh = freshGasFio2(this.o2Flow, this.airFlow, this.n2oFlow);
    const rate = (this.freshGasFlow * (fresh - this.circuitFio2) - this.vo2) / this.vSystem;
    this.circuitFio2 = Math.min(1, Math.max(0, this.circuitFio2 + rate * dt));
  }

  step(dt) {
    const VA = this.minuteVentilation * (1 - this.deadSpace);
    const cv = this._mixedVenous();
    const fi = this._inspired();
    this.lastUptake = this.cardiacOutput * this.agent.bloodGas * (this.alveolar - cv);
    const dFA = (VA * (fi - this.alveolar) - this.lastUptake) / this.FRC + this.extraRate;
    this.alveolar = Math.max(0, this.alveolar + dFA * dt);
    for (const [name, comp] of Object.entries(this.comps)) {
      comp.update(this.alveolar, this.agent.lam[name], dt);
    }
    this.circuit = this.alveolar;
    this.time += dt;
    this._updateFio2(dt);
  }

  macValue() {
    return this.alveolar / this.agent.mac;
  }
}

export class DualMachine {
  constructor(agent) {
    this.volatile = new VolatileModel(agent);
    this.n2o = new VolatileModel(AGENTS.nitrous_oxide);
  }

  setFlows(o2, air, n2o) {
    for (const m of [this.volatile, this.n2o]) {
      m.o2Flow = o2; m.airFlow = air; m.n2oFlow = n2o;
    }
    const total = o2 + air + n2o;
    this.n2o.dial = total > 0 ? 100 * n2o / total : 0;
  }

  step(dt) {
    this.n2o.step(dt);
    this.volatile.extraRate = this.volatile.alveolar * (Math.max(0, this.n2o.lastUptake) / 100) / this.volatile.FRC;
    this.volatile.step(dt);
  }

  totalMac() {
    return this.volatile.macValue() + this.n2o.macValue();
  }
}
```

</details>

### Check it

Add the import to the top of `tests.js`, and these lines above the summary:

```js
import { VolatileModel, DualMachine, AGENTS, macColor } from "./machine.js";
```

```js
// --- Week 29A ---
const machine = new VolatileModel(AGENTS.sevoflurane);
check("JS cardiac output", machine.cardiacOutput, 5.45);
machine.dial = 2.0;                               // o2Flow is 8 by default
for (let i = 0; i < 3000; i++) machine.step(0.1 / 60);   // 5 minutes
check("JS sevo FA at 5 min (Python: 1.549)", machine.alveolar, 1.549, 0.001);
check("JS VRG at 5 min (Python: 2.091)", machine.comps.VRG.concentration, 2.091, 0.001);

const dual = new DualMachine(AGENTS.sevoflurane);
dual.volatile.dial = 1.0;
dual.n2o.dial = 50;
for (let i = 0; i < 6000; i++) dual.step(0.1 / 60);      // 10 minutes
check("JS sevo FA with second gas (Python: 0.878)", dual.volatile.alveolar, 0.878, 0.005);
check("JS total MAC at 10 min (Python: 0.873)", dual.totalMac(), 0.873, 0.005);
check("MAC 0.8 is orange", macColor(0.8), "orange");
```


The two languages should agree to 3 decimals. Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  JS sevo FA` but close (like 1.55 vs 1.549) | A small difference in one equation. Print FA after the first step in both Python and JS and compare. |
| `got NaN` | A misspelled property (`this.alveolor`) or a missing `this.`. JS gives `NaN` instead of an error. |
| `XX  JS cardiac output` | The `reduce` starting value: `reduce((s, c) => s + c.flow, 0)`. |
| FA rises far too fast | The order of the five equations, exactly as in Python Week 14. |
| The panel freezes at high speed | You're taking one huge step per frame. Take many small `0.1/60` steps instead. |

### Checkpoint

Sevo 2%, 5 simulated minutes: FA **1.549** and VRG **2.091**, the same as your Python.

---

## Week 29B — The machine panel

**Goal:** the machine running live under the monitor, with a color-coded MAC display.

**New ideas (JS):** many small Euler steps per frame; setting a style from code; rebuilding an object when a choice changes.

### The science: why many small steps

Euler's method gets less accurate with larger steps, and with a large enough step it becomes unstable, which means the numbers blow up. It's the same point as Week 15's cautionary tale. So running the machine at 10× speed doesn't mean taking steps 10 times the size. It means taking 10 times as many small steps. The step stays at 0.1 seconds.

### The big picture

```
loop(now) ──► simulated minutes owed this frame = dt × speed ──► many machine.step(0.1/60)
updateVitals ──► MAC number with a color, FiO₂ with an alarm
```

### Build it: the panel 🔴

**`index.html`:** add a section with an agent `<select>` (`m-agent`), and number inputs for `m-dial` (default 2), `m-o2` (default 2), `m-air` (0) and `m-n2o` (0). Add a `m-speed` select of 1, 10, 30 and 60. Add readouts: `m-mac` (big), `m-et` and `m-fio2`.

**`main.js`:**

1. Import `DualMachine`, `AGENTS`, `freshGasFio2` and `macColor`. Make `let gasMachine = new DualMachine(AGENTS.sevoflurane)`.
2. Write a function `applyMachineControls()`, which reads the inputs, calls `setFlows`, and sets the volatile's dial. Attach it to every input's `"input"` event, and call it once at the start.
3. When the agent changes, make a new `DualMachine`, then apply the controls.
4. In `loop`, after working out `dt`, use the same "owing a fraction" trick as Week 22A. Add `(dt * speed) / 0.1` to a `machineCarry`, and while it's at least 1, subtract 1 and call `gasMachine.step(0.1 / 60)`. `dt` is in seconds, and each step covers 0.1 simulated seconds. Rounding instead would stall at 1×, where a frame is less than one step.
5. Write `updateMachinePanel()`, called from `drawAll`. It shows total MAC with its color from `macColor`, end-tidal agent, and circuit FiO₂, and toggles `.alarm` on the FiO₂ if it's under 25%.

<details>
<summary><b>Answer</b></summary>

```html
  <section class="controls" id="machine-panel">
    <h2>Machine</h2>
    <label>Agent
      <select id="m-agent">
        <option value="sevoflurane">Sevoflurane</option>
        <option value="desflurane">Desflurane</option>
        <option value="isoflurane">Isoflurane</option>
      </select>
    </label>
    <label>Dial % <input id="m-dial" type="number" min="0" max="18" step="0.1" value="2"></label>
    <label>O₂ <input id="m-o2" type="number" min="0" max="15" step="0.1" value="2"></label>
    <label>Air <input id="m-air" type="number" min="0" max="15" step="0.1" value="0"></label>
    <label>N₂O <input id="m-n2o" type="number" min="0" max="10" step="0.1" value="0"></label>
    <label>Speed
      <select id="m-speed">
        <option value="1">1×</option>
        <option value="10" selected>10×</option>
        <option value="30">30×</option>
        <option value="60">60×</option>
      </select>
    </label>
    <p>MAC <span id="m-mac" class="big">0.00</span>
       Et agent <span id="m-et">0.00</span> %
       FiO₂ <span id="m-fio2">95</span> %</p>
  </section>
```

```js
import { devices } from "./devices.js";
import { DualMachine, AGENTS, freshGasFio2, macColor } from "./machine.js";
```

```js
let gasMachine = new DualMachine(AGENTS.sevoflurane);

function applyMachineControls() {
  const o2 = parseFloat(byId("m-o2").value) || 0;
  const air = parseFloat(byId("m-air").value) || 0;
  const n2o = parseFloat(byId("m-n2o").value) || 0;
  gasMachine.setFlows(o2, air, n2o);
  gasMachine.volatile.dial = parseFloat(byId("m-dial").value) || 0;
}

for (const id of ["m-dial", "m-o2", "m-air", "m-n2o"]) {
  byId(id).addEventListener("input", applyMachineControls);
}
byId("m-agent").addEventListener("change", e => {
  gasMachine = new DualMachine(AGENTS[e.target.value]);
  applyMachineControls();
});
applyMachineControls();

function updateMachinePanel() {
  const mac = gasMachine.totalMac();
  const macEl = byId("m-mac");
  macEl.textContent = mac.toFixed(2);
  macEl.style.color = macColor(mac);
  byId("m-et").textContent = gasMachine.volatile.alveolar.toFixed(2);
  const fio2 = gasMachine.volatile.circuitFio2;
  byId("m-fio2").textContent = (fio2 * 100).toFixed(0);
  byId("m-fio2").classList.toggle("alarm", fio2 < 0.25);
}

```

```js
  updateVitals();
  updateMachinePanel();
}

let carry
```

```js
let machineCarry = 0;
```

```js
  lastT = now;
  machineCarry += (dt * parseFloat(byId("m-speed").value)) / 0.1;   // each step is 0.1 simulated seconds
  while (machineCarry >= 1) {
    machineCarry -= 1;
    gasMachine.step(0.1 / 60);
  }
```

</details>


`|| 0` falls back to 0 when an input is empty, because `parseFloat("")` gives `NaN`, and `NaN` counts as false. Without it, a single empty box would turn the whole model into `NaN`. Commit.

### Things to consider

- `freshGasFio2` isn't used by the panel yet. Add a `hypoxic mixture` warning with it, as in Week 18.

### Checkpoint

At 10×, with sevo 2% and O₂ 2 L/min, the MAC number climbs from red through orange. Set O₂ to 0.5 and N₂O to 1, and watch the FiO₂ fall and the alarm start.

---

## Week 30 — The TCI panel: Python writes JSON, JavaScript reads it

**Goal:** show the Part 1 simulations in the page, without rewriting them in JS.

**New ideas (JS):** `fetch`; `async`/`await` (waiting for a file without freezing the page); `createElement`.

**Read first:** [javascript.info: Promises, async/await](https://javascript.info/async) · [MDN: Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

### The science: looking at your own results

This panel lets you put context sensitivity and model differences side by side on one screen: a 5- versus 120-minute infusion, and Marsh versus Schnider. Put a Schnider run next to an Eleveld run, and you have a picture of what you read about in Week 6.

### The big picture

Part 1's TCI simulator stays in Python. JavaScript only **displays** its results:

```
Python: Simulation / Case ──save_sim_json──► web/data/*.json (plain text)
JavaScript: fetch("data/xxx.json") ──await──► an object ──► chart
```

JSON is the common language: Python writes it, JavaScript reads it.

### Learn it: waiting for a file 🟢

A file takes time to arrive. `await` waits for it without freezing the page. Make a test file, `web/data/pets.json`, containing `{"name": "Rex", "ages": [1, 2, 3]}`. Then replace `scratch.js` with this:

```js
async function load(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Couldn't load ${path}: ${res.status}`);
  return await res.json();
}

const pets = await load("data/pets.json");
console.log(pets.name, pets.ages.length);

try {
  await load("data/nothing.json");
} catch (err) {
  console.log(err.message);
}

const menu = document.getElementById("size");
const opt = document.createElement("option");
opt.value = opt.textContent = "giant";
menu.append(opt);
console.log(menu.options.length);
```

```text
Rex 3
Couldn't load data/nothing.json: 404
3
```

- `async function` marks a function that can wait. It returns a *promise*, a placeholder for a future value, and `await` gets the value out.
- In a module, you can use `await` at the top level too.
- `try`/`catch` is JS's `try`/`except`, and `throw` is `raise`.
- `createElement` builds a new element, and `.append` adds it to the page.

Delete `pets.json` when you're done.


### Build it: export the runs 🔴

In `tci/`, write `export_runs.py`, which uses your `save_sim_json` to write these to `../web/data/`, then writes `index.json`, listing the file names:

| File | Run |
|---|---|
| `roberts_70kg.json` | Roberts, 70 kg, Marsh |
| `marsh_manual.json` | Your Week 5 regimen, on Marsh, for the 35 yo reference adult |
| `schnider_manual.json` | The same, on Schnider |
| `eleveld_manual.json` | The same, on full Eleveld |
| `infusion_5min.json` | Marsh, Patient A: 100 mg, plus 10 mg/min for 5 min, 60 minutes total |
| `infusion_120min.json` | The same, with the infusion running 120 min, 180 minutes total |
| `remi_70kg.json` | Minto, Patient A: a 1 mcg/kg bolus, plus 0.1 mcg/kg/min, 60 minutes |

<details>
<summary><b>Answer</b></summary>

```python
import json

from dosing import apply_roberts, apply_rows, read_dose_table
from engine import Simulation
from export import save_sim_json
from patient import Patient
from pk_models import marsh_drug, schnider_drug, eleveld_drug, minto_drug

OUT = "../web/data/"

if __name__ == "__main__":
    a = Patient(40, 70, 170, "M")
    ref = Patient(35, 70, 170, "M")
    files = []

    def save(sim, name, label):
        sim.run()
        save_sim_json(sim, OUT + name, label=label)
        files.append(name)

    sim = Simulation(marsh_drug(a))
    apply_roberts(sim, a.weight)
    save(sim, "roberts_70kg.json", "Roberts, 70 kg, Marsh")

    rows = read_dose_table("cases/manual_propofol.csv")
    for model, name in [(marsh_drug, "marsh"), (schnider_drug, "schnider"), (eleveld_drug, "eleveld")]:
        sim = Simulation(model(ref), t_end=90)
        apply_rows(sim, rows, ref)
        save(sim, f"{name}_manual.json", f"Week 5 regimen on {name}")

    for minutes, total in [(5, 60), (120, 180)]:
        sim = Simulation(marsh_drug(a), t_end=total)
        sim.bolus(0, 100)
        sim.rate(0, 10)
        sim.rate(minutes, 0)
        save(sim, f"infusion_{minutes}min.json", f"{minutes}-min infusion, Marsh")

    sim = Simulation(minto_drug(a))
    sim.bolus(0, 70)
    sim.rate(0, 7)
    save(sim, "remi_70kg.json", "Remifentanil 1 mcg/kg + 0.1 mcg/kg/min, Minto")

    with open(OUT + "index.json", "w") as f:
        json.dump(files, f, indent=2)
    print(files)
```

</details>


### Build it: `tci_panel.js` 🔴

Create `web/js/tci_panel.js`, importing `valueToY` from `draw.js`, and export:

- **`loadRun(path)`,** as in the scratch file.
- **`peakOf(t, values)`** returns `{ peak, when }`.
- **`drawRun(canvas, run)`** paints the canvas black, sets the y-range from 0 to the highest `cp` or `ce`, and draws Cp in one color and Ce in another. x comes from `run.t`.
- **`setupTciPanel()`** finds a `<select id="tci-run">`, loads `data/index.json`, fills the menu using `createElement`, and on each change loads and draws that run, and shows the peak Ce and time-to-peak in `<span id="tci-peak">`.

Add the section to `index.html`, with the select, a `<canvas id="tci-chart" width="900" height="200">`, and the span. Call `setupTciPanel()` from `main.js`.

Should you compute the peak in JS, or have Python include it in the JSON? This answer computes it in JS, so that the file format stays simple. Decide for yourself, and note why in `DEVLOG.md`.

> **A library alternative.** [Chart.js](https://www.chartjs.org/docs/latest/) draws labeled charts with very little code, and you could use it in place of `drawRun`. It's worth doing as a stretch, because using other people's libraries is a skill too. This workbook's answer uses your own canvas code, so that every line stays yours.

<details>
<summary><b>Answer</b></summary>

```js
import { valueToY } from "./draw.js";

export async function loadRun(path) {
  const res = await fetch(path);                  // wait for the file to arrive
  if (!res.ok) throw new Error(`Couldn't load ${path}: ${res.status}`);
  return await res.json();                        // text -> JS object, the same shape you saved
}

export function peakOf(t, values) {
  let best = 0;
  values.forEach((v, i) => {
    if (v > values[best]) best = i;
  });
  return { peak: values[best], when: t[best] };
}

function drawLine(ctx, canvas, t, values, max, color) {
  ctx.strokeStyle = color;
  ctx.beginPath();
  values.forEach((v, i) => {
    const x = (t[i] / t[t.length - 1]) * canvas.width;
    const y = valueToY(v, 0, max, canvas.height);
    if (i === 0) {
      ctx.moveTo(x, y);
    } else {
      ctx.lineTo(x, y);
    }
  });
  ctx.stroke();
}

export function drawRun(canvas, run) {
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  const max = Math.max(...run.cp, ...run.ce) * 1.05;
  drawLine(ctx, canvas, run.t, run.cp, max, "#888");
  drawLine(ctx, canvas, run.t, run.ce, max, "#0f0");
}

export async function setupTciPanel() {
  const sel = document.getElementById("tci-run");
  const canvas = document.getElementById("tci-chart");
  const peakEl = document.getElementById("tci-peak");
  const files = await loadRun("data/index.json");
  for (const name of files) {
    const opt = document.createElement("option");
    opt.value = opt.textContent = name;
    sel.append(opt);
  }
  async function show() {
    const run = await loadRun(`data/${sel.value}`);
    drawRun(canvas, run);
    const { peak, when } = peakOf(run.t, run.ce);
    peakEl.textContent = `${run.label}: peak Ce ${peak.toFixed(2)} ${run.conc_unit} at ${when.toFixed(1)} min`;
  }
  sel.addEventListener("change", show);
  await show();
}
```

```html
  <section class="controls" id="tci-panel">
    <h2>TCI runs (from Python)</h2>
    <select id="tci-run"></select>
    <span id="tci-peak"></span>
    <canvas id="tci-chart" width="900" height="200"></canvas>
  </section>
```

```js
import { devices } from "./devices.js";
import { setupTciPanel, loadRun } from "./tci_panel.js";
```

```js
setupTciPanel();

```

</details>

### Check it

Add the import to the top of `tests.js`, and these lines above the summary. They read the actual file Python wrote.

```js
import { loadRun, peakOf } from "./tci_panel.js";
```

```js
// --- Week 30 ---
const roberts = await loadRun("data/roberts_70kg.json");
check("JSON: time points from Python", roberts.t.length, 361, 0);
check("JSON: Roberts Ce at 10 min (Week 4)", roberts.ce[60], 3.05, 0.05);
check("JSON: drug name", roberts.drug, "Propofol (Marsh)");
const schniderRun = await loadRun("data/schnider_manual.json");
check("JSON: Schnider peak Ce (Week 6)", peakOf(schniderRun.t, schniderRun.ce).peak, 8.62, 0.5);
```

```text
ALL OK
```


Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| The menu is empty | Open the console: the error names the file it couldn't load. Run `python export_runs.py` from inside `tci/`. |
| `Couldn't load data/index.json: 404` | The server must be started from inside `web/`, and the file must be in `web/data/`. |
| `Unexpected token '<'` | The server sent an error page instead of JSON. The path is wrong. |
| You get a `[object Promise]` | You forgot `await`. |
| `XX  JSON: Schnider peak Ce` is slightly off | This run uses 6 steps per minute, not the 60 from Week 6, so the peak is lower. Hence the wider tolerance. |

### Checkpoint

Choose `roberts_70kg.json`, and you should see the Week 4 curves (Ce **3.05** µg/mL at 10 min).

---

## Week 31A — The bridge: opioid MAC-sparing

**Goal:** connect the TCI and machine panels clinically.

**New ideas:** nothing new in the language. This lesson is about one clinical point, shown on one screen.

### The science: IV drugs have no MAC

Two *inhaled* agents add by MAC (Week 15). **IV drugs have no MAC.** Remifentanil doesn't add MAC. It **reduces how much volatile you need.** Lang and colleagues (1996) found about a 50% reduction in isoflurane MAC at about 1.37 ng/mL of remifentanil, with a ceiling of about 90%.

So raising the opioid can move a patient from "light" toward "surgical" **without touching the vaporizer**. That's the same synergy you saw in Week 9's propofol–opioid model, from another direction.

> Label it on screen: "Model of opioid MAC-sparing (Lang 1996). Fitted to published points, not a per-patient prediction."

**References:** Lang E, Kapila A, Shlugman D, Hoke JF, Sebel PS, Glass PSA. *Anesthesiology* 1996;85:721–8 · McEwan AI, Smith C, Dyar O, Goodman D, Glass PSA. *Anesthesiology* 1993;78:864–9

### The big picture

The capstone connects the two drug worlds:

```
TCI run (Python → JSON) ──remi Ce at the chosen minute──► macReduction(Ce) ──┐
machine panel ──volatile MAC──────────────────────────────────────────────────┴──► effective MAC = MAC ÷ (1 − reduction)
```

Opioids don't add MAC; they *lower how much volatile is needed*. Showing that on screen, without touching the vaporizer, is the clinical point of the whole project. Then you publish the page so anyone can use it.

### Build it: `bridge.js` 🔴

Create `web/js/bridge.js`, and export:

- **`macReduction(remiCe, emax = 0.9, ec50 = 1.096)`:** the saturating curve `reduction = Emax·Ce / (EC50 + Ce)`, fitted so that `macReduction(1.37)` = 0.5.
- **`effectiveMac(volatileMac, remiCe)`:** volatile MAC ÷ (1 − reduction).

<details>
<summary><b>Answer</b></summary>

```js
export function macReduction(remiCe, emax = 0.9, ec50 = 1.096) {
  return emax * remiCe / (ec50 + remiCe);
}

export function effectiveMac(volatileMac, remiCe) {
  return volatileMac / (1 - macReduction(remiCe));
}
```

</details>

### Check it

```js
import { macReduction } from "./bridge.js";
```

Add that import to the top of `tests.js`, and these lines above the summary:

```js
// --- Week 31 ---
check("remi 1.37 ng/mL halves MAC", macReduction(1.37), 0.5, 0.001);
check("0.8 MAC volatile + remi 1.37 = effective", 0.8 / (1 - macReduction(1.37)), 1.6, 0.01);
```


### Build it: effective MAC on the page 🔴

Add a slider to the machine panel (`m-minute`, 0–60), showing the minute, and a readout (`m-remi`). In `main.js`:

1. Load `data/remi_70kg.json` at the start with `loadRun`, and keep it in a variable.
2. Add a checkbox (`m-use-remi`). When it's on, read remi Ce at the chosen minute: the run has 6 samples per minute, so the index is `minute * 6`.
3. In `updateMachinePanel`, show the effective MAC with the same color scale, and add the label quoted above.

Raising remi should move the color toward green **without touching the dial**.

<details>
<summary><b>Answer</b></summary>

```html
    <label><input id="m-use-remi" type="checkbox"> Remifentanil</label>
    <label>At minute <input id="m-minute" type="range" min="0" max="60" value="30"></label>
    <span id="m-minute-out">30</span>
    <p class="note">Model of opioid MAC-sparing (Lang 1996). Fitted to published points, not a per-patient prediction.</p>
```

```html
       Remi <span id="m-remi">0.00</span> ng/mL
```

```js
import { setupTciPanel, loadRun } from "./tci_panel.js";
import { effectiveMac } from "./bridge.js";
```

```js
let remiRun = null;
loadRun("data/remi_70kg.json").then(run => { remiRun = run; });

function currentRemi() {
  if (!remiRun || !byId("m-use-remi").checked) return 0;
  const minute = parseFloat(byId("m-minute").value);
  byId("m-minute-out").textContent = minute;
  return remiRun.ce[minute * 6];
}

```

```js
  const remi = currentRemi();
  byId("m-remi").textContent = remi.toFixed(2);
  const mac = effectiveMac(gasMachine.totalMac(), remi);
```

</details>

```text
ALL OK
```

`.then(run => ...)` is another way of using a promise: "when this finishes, do that". Commit.

### If something goes wrong

| What you see | Where to look |
|---|---|
| `XX  remi 1.37 ng/mL halves MAC` | The formula: `emax * Ce / (ec50 + Ce)`. |
| Effective MAC goes *down* as remi goes up | You multiplied by the reduction instead of dividing by `(1 − reduction)`. |
| The live site shows a blank page | GitHub Pages serves `index.html` from the folder you chose. Check that the `web/` contents (not the folder above) are what's published, and that paths don't start with `/`. |
| The site works but the JSON doesn't load | The `data/` folder wasn't committed. |

### Checkpoint

`macReduction(1.37)` = **0.50**. With 0.8 MAC of volatile and remi at 1.37 ng/mL, the effective MAC is **1.6**.

---

## Week 31B — Put it online

**Goal:** a public web address for your simulator.

**New ideas:** GitHub; pushing a repository; GitHub Pages.

**Read first:** [GitHub Pages: creating a site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

### The big picture

Everything in `web/` runs in the browser, including the JSON files Python already wrote. No server has to run anything, so GitHub Pages can host it for free. The Streamlit apps are different, because they need Python running on a server, so they stay on your own computer.

### Build it: deploy

1. Make an account at [github.com](https://github.com), and create a new, empty repository.
2. Connect your project, and push it:

```bash
git remote add origin https://github.com/YOUR-NAME/anesthesia-sim.git
git branch -M main
git push -u origin main
```

3. On GitHub, go to **Settings → Pages**. Deploy from your branch. Pages can serve from the repository's root or from a `/docs` folder, so the simplest approach is to make a second repository that holds only the contents of `web/`, or rename `web/` to `docs/` and update your paths.
4. You get a live address to share. Open it, press F12, and make sure there are no red errors.

> **Keep the label on it.** Put "Teaching simulator. Not a medical device, and not for clinical decisions." somewhere on the page before you share it.

Your final `DEVLOG.md` entry: what you'd build next. Some ideas, using the papers behind this workbook:

- A hemodynamic panel for propofol from Su 2022
- A Gas Man-style circuit compartment, in place of the simple rebreathing rule
- Eleveld's BIS model, with an effect-site target suggested for a chosen BIS
- Capping the James lean body mass, the way commercial pumps do

### Checkpoint

Your page loads at a public address, `tests.html` there ends in `ALL OK`, and you typed every line of it.

---

# Appendices

## A. When you're stuck: a debugging checklist

1. **Read the whole error.** In Python, read the *last* line first, then the line in *your* file. In JS, click the file:line link in the console.
2. **Shrink it.** Copy the failing function into a scratch file and give it one fixed input.
3. **Print every intermediate.** `print(f"{A1=} {Cp=}")` in Python (the `=` prints the name too). `console.log({ A1, Cp })` in JS.
4. **Check units.** Minutes vs seconds, % vs fraction, mg vs µg. This is about a third of all bugs in this workbook.
5. **Check order.** Equations that depend on each other, and "record, then advance" vs "advance, then record".
6. **Check the check, too.** Occasionally the expected number is wrong. Every number here came from a reference run, but your settings (`dt`, `steps_per_min`) have to match.
7. **Walk away for 10 minutes.** Seriously.

## B. JavaScript traps that Python programmers hit

| Trap | What happens | Fix |
|---|---|---|
| `"75" + 5` | `"755"` | `parseFloat()` everything from the page |
| `==` | `0 == ""` is `true` | always use `===` |
| forgot `return` | function gives `undefined` | check every function returns |
| forgot `this.` in a class | `ReferenceError` or a silent global | always `this.` |
| forgot `await` | you get a Promise, not data | `await` inside an `async` function |
| math on `undefined` | `NaN` spreads silently | `console.log` inputs, and keep your `tests.js` checks |
| opening `index.html` directly | imports and fetch fail | `python -m http.server` |


## C. What changed from the earlier workbooks

**In this hand-typed edition:**

| Old | Problem | Now |
|---|---|---|
| Eleveld reference Q2 = 1.75 L/min | The journal's corrigendum gives 1.83 for the reference individual | 1.83, and Week 6B calculates it from the equations. Numbers in Weeks 6 and 11 were recalculated |
| Eleveld for the reference adult only | Couldn't show age, sex or obesity | Week 6B builds the full arterial PK model, alongside the simple version |
| Week 0: `ModuleNotFoundError` blamed on the wrong folder | Python looks in the running file's folder, so that isn't the cause | Correct explanation in Week 0, with the real folder rule for data files |
| Week 19 checkpoint said `ALL PASS` | The code prints `ALL OK` | `ALL OK` |
| Week 19 linked `style.css` before it existed | A confusing 404 for a beginner | Linked in Week 20A, when you create it |
| Week 25's `runPump` set `pump.iabp.enabled` | `pump.iabp` doesn't exist until Week 28, so the check crashed | `if (pump.iabp) ...` until the balloon arrives |
| `PulsePump`'s upstroke guard was fixed at 2 | 2 mmHg is fine for the arterial line, but it sent every pleth pulse off a 0-to-1 scale | A `minRise` option, in each pump's own units |
| Week 21's `pWave` and Week 19's | The same function could end up in two files | Moved to `ecg.js` in Week 21B |
| Starter code with `TODO`s | Someone else's structure | Every file typed by you, each idea practiced first in a scratch file |

**From the earlier workbooks to the original edition of this one:**

| Old | Problem | Now |
|---|---|---|
| Second gas: `alveolar *= 1 + uptake*0.01` per step | Timestep-dependent; sevo went to infinity in 3 min | A rate term `FA·U/FRC` inside dFA/dt (Week 15) |
| Decrement loop `sim.time < 60/60` | 1-minute cap, absolute clock; never ran after 30 min | Elapsed time from `t0`, true 60-minute cap (Week 17) |
| CO 5.0 while tissue flows sum to 5.45 | Inconsistent mass balance | `cardiac_output` is a property: the sum of flows (Week 14) |
| VRG MAC = tissue conc / MAC | Ignored λ; showed brain at 1.7 MAC when alveolar was 1 MAC | Partial pressure = C/λ first (Weeks 13–14) |
| Fixed 350 ms arterial pulse + flat hold | Flat diastole, 3 mmHg step, early notch, broke at high HR | Continuous `PulsePump` decay from the current pressure (Week 25) |
| IABP on the fixed-length pulse | EDP only ~7 mmHg lower; drew *early deflation* | Inflate at notch, deflate on R-wave (Week 28) |
| VV-ECMO SpO₂ mixed in parallel | 92% where ~98% is expected | VV in series, VA in parallel (Week 27) |
| T wave width 0.25 | 0.04 step at its edges | Edge-subtracted, rescaled T (Week 21) |
| Native CO fixed at 4.5 | Shock scenarios unrealistic | `P.nativeCO` is a control (Week 27) |
| Propofol–opioid interaction with illustrative Greco constants | Not a published surface | Bouillon 2004's published hierarchical model, with every opioid combined through MEAC (Week 9), as in StanpumpR |
| TCI part covered propofol and remifentanil only, one fixed regimen at a time | Not how real cases are dosed | Manual dose tables with redosing, 7 drugs, model overlays, a 10-second TCI controller with printable schedules, Streamlit app (Weeks 5–12) |
| Machine controls only in code | Hard to teach with | Streamlit machine with flowmeters, vaporizer, time-warp and low/high-flow comparison (Week 18) |

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
18. Shafer SL. *stanpumpR*. stanpumpr.io; source at github.com/StevenLShafer/stanpumpR. (Dose-table convention, drug library parameters, fat-free-mass scaling, opioid MEAC normalization, and the Bouillon interaction panel; read October 2026.)
19. Janmahasatian S, Duffull SB, Ash S, et al. Quantification of lean bodyweight. *Clin Pharmacokinet* 2005;44:1051–1065.
20. Minto CF, Schnider TW, Gregg KM, Henthorn TK, Shafer SL. Using the time of maximum effect site concentration to combine pharmacokinetics and pharmacodynamics. *Anesthesiology* 2003;99:324–333.
21. McClain DA, Hug CC Jr. Intravenous fentanyl kinetics. *Clin Pharmacol Ther* 1980;28:106–114.
22. Scott JC, Stanski DR. Decreased fentanyl and alfentanil dose requirements with age: a simultaneous pharmacokinetic and pharmacodynamic evaluation. *J Pharmacol Exp Ther* 1987;240:159–166.
23. Hudson RJ, Thomson IR, Cannon JE, et al. Pharmacokinetics of fentanyl in patients undergoing abdominal aortic surgery. *Anesthesiology* 1986;64:334–338.
24. Varvel JR, Shafer SL, Hwang SS, Coen PA, Stanski DR. Absorption characteristics of transdermally administered fentanyl. *Anesthesiology* 1989;70:928–934.
25. Shafer SL, Varvel JR, Aziz N, Scott JC. Pharmacokinetics of fentanyl administered by computer-controlled infusion pump. *Anesthesiology* 1990;73:1091–1102.
26. Shafer SL, Varvel JR. Pharmacokinetics, pharmacodynamics, and rational opioid selection. *Anesthesiology* 1991;74:53–63.
27. Gourlay GK, Kowalski SR, Plummer JL, et al. Fentanyl blood concentration–analgesic response relationship in the treatment of postoperative pain. *Anesth Analg* 1988;67:329–337.
28. Dyck JB, Maze M, Haack C, Vuorilehto L, Shafer SL. Computer-controlled infusion of intravenous dexmedetomidine hydrochloride in adult human volunteers. *Anesthesiology* 1993;78:821–828.
29. Colin PJ, Hannivoort LN, Eleveld DJ, et al. Dexmedetomidine pharmacodynamics in healthy volunteers: 1. Sedation. *Br J Anaesth* 2017;119:200–210.
30. Domino EF, Domino SE, Smith RE, et al. Ketamine kinetics in unmedicated and diazepam-premedicated subjects. *Clin Pharmacol Ther* 1984;36:645–653.
31. Mion G, Villevieille T. Ketamine pharmacology: an update (pharmacodynamics and molecular aspects, recent findings). *CNS Neurosci Ther* 2013;19:370–380.
32. Plaud B, Proost JH, Wierda JM, et al. Pharmacokinetics and pharmacodynamics of rocuronium at the vocal cords and the adductor pollicis in humans. *Clin Pharmacol Ther* 1995;58:185–191.
33. Cortínez LI, Nazar C, Muñoz HR. Estimation of the plasma effect-site equilibration rate constant (ke0) of rocuronium by the time of maximum effect. *Br J Anaesth* 2007;99:679–685.
34. Inturrisi CE, Colburn WA, Kaiko RF, Houde RW, Foley KM. Pharmacokinetics and pharmacodynamics of methadone in patients with chronic pain. *Clin Pharmacol Ther* 1987;41:392–401.
35. Kharasch ED, Hoffer C, Whittington D, Sheffels P. Role of hepatic and intestinal cytochrome P450 3A and 2B6 in the metabolism, disposition, and miotic effects of methadone. *Clin Pharmacol Ther* 2004;76:250–269.
36. Henthorn TK, Kharasch ED. Population pharmacokinetics of intravenous methadone enantiomers in adults: a comprehensive model. *Clin Pharmacol Ther* 2026;119:739–750. (StanpumpR's current methadone model; beyond this workbook.)
37. Shafer SL, Gregg KM. Algorithms to rapidly achieve and maintain stable drug concentrations at the site of drug effect with a computer-controlled infusion pump. *J Pharmacokinet Biopharm* 1992;20:147–169.
38. Absalom AR, Mani V, De Smet T, Struys MMRF. Pharmacokinetic models for propofol: defining and illuminating the devil in the detail. *Br J Anaesth* 2009;103:26–37.

### Part 2: Anesthesia machine and volatile agents
39. Eger EI, Saidman LJ, Brandstater B. Minimum alveolar anesthetic concentration: a standard of anesthetic potency. *Anesthesiology* 1965;26:756–763.
40. Eger EI II. The effect of inspired anesthetic concentration on the rate of rise of alveolar concentration. *Anesthesiology* 1963;24:153–157.
41. Eger EI II. *Anesthetic Uptake and Action*. Baltimore: Williams & Wilkins; 1974.
42. Epstein RM, Rackow H, Salanitre E, Wolf GL. Influence of the concentration effect on the uptake of anesthetic mixtures: the second gas effect. *Anesthesiology* 1964;25:364–371.
43. Stoelting RK, Eger EI II. An additional explanation for the second gas effect: a concentrating effect. *Anesthesiology* 1969;30:273–277.
44. Taheri S, Eger EI II. A demonstration of the concentration and second gas effects in humans anesthetized with nitrous oxide and desflurane. *Anesth Analg* 1999;89:774–780.
45. Korman B, Mapleson WW. Concentration and second gas effects: can the accepted explanation be improved? *Br J Anaesth* 1997;78:618–625.
46. Hendrickx JFA, Carette R, Lemmens HJM, De Wolf AM. Large volume N₂O uptake alone does not explain the second gas effect of N₂O on sevoflurane during constant inspired ventilation. *Br J Anaesth* 2006;96:391–395.
47. Yasuda N, Lockhart SH, Eger EI II, et al. Comparison of kinetics of sevoflurane and isoflurane in humans. *Anesth Analg* 1991;72:316–324.
48. Philip JH. Gas Man: an example of goal-oriented computer-assisted teaching which results in learning. *Int J Clin Monit Comput* 1986;3:165–173.
49. Philip JH. *Gas Man: Understanding Anesthesia Uptake and Distribution*. Med Man Simulations Inc. (gasmanweb.com).
50. Baum JA. *Low Flow Anaesthesia: The Theory and Practice of Low Flow, Minimal Flow and Closed System Anaesthesia*. 2nd ed. Butterworth-Heinemann; 2001.
51. Mapleson WW. The concept of the time constant applied to breathing systems and to the body.
52. Hendrickx JFA, De Wolf AM. The anaesthesia workstation: quo vadis? *Anesth Analg* 2018;127:671–675.
53. ISO 80601-2-13: Particular requirements for the basic safety and essential performance of an anaesthetic workstation (O₂:N₂O hypoxic guard).
54. Lang E, Kapila A, Shlugman D, Hoke JF, Sebel PS, Glass PSA. Reduction of isoflurane minimum alveolar concentration by remifentanil. *Anesthesiology* 1996;85:721–728.
55. McEwan AI, Smith C, Dyar O, Goodman D, Glass PSA. Isoflurane MAC reduction by fentanyl. *Anesthesiology* 1993;78:864–869.

### Part 3: Monitor waveforms and mechanical circulatory support
56. *Project 3: Medical Waveform Training Platform* textbook (`Project3_Waveform_Platform_Textbook.docx`). Exercise numbers are cited per week.
57. Stouffer GA. Arterial pressure (ch. 4). thoracickey.com/4-arterial-pressure/ (anacrotic limb, dicrotic notch at aortic valve closure, dicrotic wave from arterial recoil).
58. Deranged Physiology. *Normal arterial line waveforms*. derangedphysiology.com (MAP from the area under the curve is more accurate than the ⅓ estimate).
59. *Arterial Lines*. anaestheasier.com/arterial-lines/ (three components; incisura vs dicrotic notch).
60. *Broader applications of arterial pressure waveform analysis*. *BJA Education* 2017. bjaed.org (dicrotic notch about ⅓ down the descending limb).
61. *Unloading the Left Ventricle in Venoarterial ECMO*. *Circulation* 2022. doi:10.1161/CIRCULATIONAHA.122.062371.
62. *Left ventricular distension and venting strategies during VA-ECMO*. PMC6531683 (pulse pressure > 10 mmHg suggests the LV is still ejecting).
63. *Flow Optimization, Management, and Prevention of LV Distention during VA-ECMO*. IntechOpen; 2018 (ECPELLA pathophysiology).
64. *The Intra-aortic Balloon Pump: A Focused Review*. 2024. PMC11307388 (augmentation exceeds unassisted systole; assisted EDP 15–20 mmHg lower; assisted systole about 5 mmHg lower; sharp V at the notch).
65. EMCrit IBCC. *Intra-aortic balloon pump*. emcrit.org/ibcc/iabp/
66. LITFL. *IABP Trouble-shooting* (early and late inflation/deflation waveforms).
67. NCBI Bookshelf NBK543576 (figure: inflation at the dicrotic notch; augmentation above unassisted systole).
68. *Capnography and Pulse Oximetry*. StatPearls, NCBI Bookshelf NBK539754 (four capnogram phases; normal EtCO₂ 35–45 mmHg; SpO₂ from the red/infrared ratio, not trace height).
69. *Components of a time capnogram*. capnography.com (phase III up-slope, phase IV down-stroke).
70. LITFL. *Capnography Waveform Interpretation*.
71. NUEM Blog / EMS1: EtCO₂ falls with low cardiac output, pulmonary embolism and arrest.

### Added in this edition
73. Eleveld DJ, Colin P, Absalom AR, Struys MMRF. Corrigendum to "Pharmacokinetic-pharmacodynamic model for propofol for broad application in anaesthesia and sedation". *Br J Anaesth* 2018;121:519. (Reference Q2 is 1.83 L/min; recommends the supplementary NONMEM files for real implementations.)
74. Absalom AR, Mani V, De Smet T, Struys MMRF. Corrigendum. *Br J Anaesth* 2010;104:393. (Relabels the x-axis of Figure 6.)
75. Su H, Eleveld DJ, Struys MMRF, Colin PJ. Mechanism-based pharmacodynamic model for propofol haemodynamic effects in healthy volunteers. *Br J Anaesth* 2022;128:806–816.
76. Al-Rifai Z, Mulvey D. Principles of total intravenous anaesthesia: basic pharmacokinetics and model descriptions. *BJA Education* 2016;16:92–97.
77. Engbers F, Boveri H. From Schnider to Eleveld. TIVA Trainer blog; 2024. blog.tivatrainer.com/from-schnider-to-eleveld/
78. Cortínez LI, De la Fuente N, Eleveld DJ, et al. Performance of propofol target-controlled infusion models in the obese: pharmacokinetic and pharmacodynamic analysis. *Anesth Analg* 2014;119:302–310.
79. Gepts E, Camu F, Cockshott ID, Douglas EJ. Disposition of propofol administered as constant rate intravenous infusions in humans. *Anesth Analg* 1987;66:1256–1263.
80. Philip JH. *Workbook for Gas Man: a simulation and teaching tool*. Harvard Medical School; 2012.
81. McSharry PE, Clifford GD, Tarassenko L, Smith LA. A dynamical model for generating synthetic electrocardiogram signals. *IEEE Trans Biomed Eng* 2003;50:289–294.


## E. Learning resources

**Python**
- [The Python Tutorial](https://docs.python.org/3/tutorial/), especially §9 Classes
- [pytest: Get started](https://docs.pytest.org/en/stable/getting-started.html)
- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Matplotlib Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)
- [SciPy `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) and [`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
- [Streamlit: Get started](https://docs.streamlit.io/get-started/fundamentals/main-concepts), [`st.data_editor`](https://docs.streamlit.io/develop/api-reference/data/st.data_editor), [fragments](https://docs.streamlit.io/develop/concepts/architecture/fragments) and [caching](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [StanpumpR](https://stanpumpr.io), the tool Part 1 is modeled on
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
