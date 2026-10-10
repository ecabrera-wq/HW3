# Part B answer: the debug print is moved inside the guard, so it only runs
# when this file is run directly (python projectile_skeleton_fixed.py),
# not when another script imports it.

if __name__ == "__main__":
    print(f"my name is {__name__}")
    # rest of the driver code here
