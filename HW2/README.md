# HW2: Tracing the Rails

## The Problem

You are given three Python files that import each other in a chain. `conductor.py` imports `train.py`, and `train.py` imports `station.py`.

**station.py**
```python
print(f"[station] __name__ is {__name__}")

def announce():
    print(f"[station.announce] __name__ is {__name__}")

if __name__ == "__main__":
    print("[station] Running as main!")
    announce()
```

**train.py**
```python
import station

print(f"[train] __name__ is {__name__}")

def depart():
    print(f"[train.depart] __name__ is {__name__}")
    station.announce()

if __name__ == "__main__":
    print("[train] Running as main!")
    depart()
```

**conductor.py**
```python
import train

print(f"[conductor] __name__ is {__name__}")

if __name__ == "__main__":
    print("[conductor] Running as main!")
    train.depart()
```

**Part A:** Without running any code, write out the exact output, in order, for each of these commands:
1. `python station.py`
2. `python train.py`
3. `python conductor.py`

**Part B:** Suppose a file called `projectile_skeleton.py` has this line at the top level, outside any function and outside the `if __name__ == "__main__":` block:

```python
print(f"my name is {__name__}")
```

A second file, `quadratic_equation_solver.py`, starts with `import projectile_skeleton`. Explain what this line prints and when, if you run `python quadratic_equation_solver.py`. Is this likely intentional? Rewrite `projectile_skeleton.py` so the line no longer prints when the file is imported by another script.

## What This Question Assesses

This question checks whether a student really understands what `__name__` is and when the `if __name__ == "__main__":` guard runs. A common misconception is that `__name__` depends on which function is calling, when it is actually set once, when the module is loaded, based on whether the file was run directly or imported.

The hardest part is `python conductor.py`. Students have to trace the order of execution across three files instead of reading one file top to bottom. They also have to see that `station` and `train` keep their own names (`"station"` and `"train"`) even though they are being used by `conductor`, and that `train.depart()` prints `"train"` instead of `"__main__"` because `train.py` was never run directly. Most students get the single file case right but slip on the multi level import. By working through it, they learn that imports run a module's top level code immediately, and that the guard exists to keep demo or test code from running when a file is reused as a library.

Part B connects the idea to a realistic bug. An unguarded print in a module pollutes the output of every script that imports it.

## Answer Key

The three files are included in this folder ([`station.py`](station.py), [`train.py`](train.py), [`conductor.py`](conductor.py)), so you can run them to check the answers below.

**Part A**

`python station.py`
```
[station] __name__ is __main__
[station] Running as main!
[station.announce] __name__ is __main__
```

`python train.py`
```
[station] __name__ is station
[train] __name__ is __main__
[train] Running as main!
[train.depart] __name__ is __main__
[station.announce] __name__ is station
```

`python conductor.py`
```
[station] __name__ is station
[train] __name__ is train
[conductor] __name__ is __main__
[conductor] Running as main!
[train.depart] __name__ is train
[station.announce] __name__ is station
```

**Part B**

The line has no guard, so it runs every time `projectile_skeleton.py` is loaded, including when it is imported. When you run `python quadratic_equation_solver.py`, the `import projectile_skeleton` statement runs first and prints `my name is projectile_skeleton` before the solver asks for any input. This is almost certainly leftover debugging output, not intentional.

Fix: move the print inside the guard so it only runs when the file is run directly. See [`projectile_skeleton_fixed.py`](projectile_skeleton_fixed.py).

```python
if __name__ == "__main__":
    print(f"my name is {__name__}")
    # rest of the driver code here
```
