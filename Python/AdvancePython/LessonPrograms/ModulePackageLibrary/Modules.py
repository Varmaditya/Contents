# MODULES IN PYTHON (DETAILED)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== MODULES IN PYTHON =====")
print("""
A module is a Python file (.py file)
that contains code.

Modules help:
✔ Organize code
✔ Reuse code
✔ Avoid repetition

Example:
calculator.py, file_utils.py
""")

# ---------------- Creating Your Own Module ----------------
print("\n===== CREATING YOUR OWN MODULE =====")
print("""
Example: calculator.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
""")

print("""
This file can now be reused
in other programs.
""")

# ---------------- Importing Modules ----------------
print("\n===== IMPORTING MODULES =====")

print("""
Different import styles:
""")

# Style 1: import module
import math
print("Using import math:", math.sqrt(16))

# Style 2: from module import function
from math import sqrt
print("Using from import:", sqrt(25))

# Style 3: aliasing
import math as m
print("Using alias:", m.pi)

# Style 4: import multiple items
from math import sqrt, pi
print("Multiple import:", sqrt(36), pi)

print("""
Import styles give flexibility
in how we use modules.
""")

# ---------------- Why Different Import Styles ----------------
print("\n===== WHY DIFFERENT IMPORT STYLES =====")
print("""
✔ import module → clear but longer
✔ from module → shorter
✔ alias → avoids long names
✔ selective import → only needed functions
""")

# ---------------- Using Custom Module (Concept) ----------------
print("\n===== USING CUSTOM MODULE =====")
print("""
Assume we created calculator.py

We can use it like:

import calculator
calculator.add(2, 3)

OR

from calculator import add
add(2, 3)
""")

# ---------------- __name__ == "__main__" ----------------
print("\n===== __name__ == '__main__' =====")
print("""
Every Python file has a special variable:
__name__

If file is run directly:
__name__ = '__main__'

If file is imported:
__name__ = module name
""")

print("""
Example:

if __name__ == "__main__":
    print("Running directly")
""")

print("""
Purpose:
✔ Prevent certain code from running on import
✔ Used for testing modules
""")

# Demonstration
def test_function():
    print("This is a test function")

if __name__ == "__main__":
    print("This file is running directly")
    test_function()

# ---------------- Practical Use Case ----------------
print("\n===== PRACTICAL USE CASE =====")
print("""
Split program into modules:

main.py → main logic
math_utils.py → calculations
file_utils.py → file handling

This makes code:
✔ Clean
✔ Reusable
✔ Easy to maintain
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Module = Python file
✔ import brings module into program
✔ Multiple import styles available
✔ __name__ controls execution behavior

Modules are the first step
towards organized programming.
""")