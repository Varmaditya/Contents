# MODULES, PACKAGES & STANDARD LIBRARY (INTRODUCTION)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== MODULES, PACKAGES & STANDARD LIBRARY =====")
print("""
Till now, we have written programs in a single file.

But real-world applications are:
✔ Large
✔ Complex
✔ Multi-file systems

To manage this, Python provides:
✔ Modules
✔ Packages
✔ Standard Library

This helps in writing:
✔ Organized code
✔ Reusable code
✔ Maintainable applications
""")

# ---------------- What is a Module ----------------
print("\n===== WHAT IS A MODULE =====")
print("""
A module is simply a Python file (.py file).

Example:
math.py
file_utils.py
calculator.py

A module contains:
✔ Functions
✔ Variables
✔ Classes

Purpose:
✔ Organize code
✔ Reuse code
""")

# Example (concept)
print("\n--- Example Module Content ---")
print("""
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
""")

# ---------------- Why Modules are Needed ----------------
print("\n===== WHY MODULES ARE NEEDED =====")
print("""
Without modules:
✔ Code becomes too long
✔ Difficult to manage
✔ Hard to reuse

With modules:
✔ Code is divided into parts
✔ Easy to maintain
✔ Easy to reuse
""")

# ---------------- Using a Module ----------------
print("\n===== USING A MODULE =====")
print("""
We use 'import' to use a module.

Example:
import math
""")

import math

print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)

print("""
Here:
✔ math is a module
✔ sqrt() and pi are its features
""")

# ---------------- What is a Package ----------------
print("\n===== WHAT IS A PACKAGE =====")
print("""
A package is a folder containing multiple modules.

Example structure:

project/
    main.py
    utils/
        file_utils.py
        math_utils.py

Purpose:
✔ Group related modules together
✔ Organize large projects
""")

# ---------------- Why Packages are Needed ----------------
print("\n===== WHY PACKAGES ARE NEEDED =====")
print("""
In large applications:

✔ Many modules exist
✔ Need logical grouping

Packages help:
✔ Organize modules
✔ Avoid naming conflicts
✔ Improve readability
""")

# ---------------- Standard Library ----------------
print("\n===== PYTHON STANDARD LIBRARY =====")
print("""
Python comes with built-in modules called
Standard Library.

Examples:
✔ math → mathematical functions
✔ random → random values
✔ datetime → date and time
✔ os → operating system interaction
✔ json → JSON handling
✔ csv → CSV handling

We already used:
✔ csv
✔ json
✔ pathlib
""")

# Example usage
import random

print("Random number:", random.randint(1, 10))

# ---------------- Don’t Reinvent the Wheel ----------------
print("\n===== DON'T REINVENT THE WHEEL =====")
print("""
Instead of writing everything from scratch:

✔ Use existing modules
✔ Use standard library

Example:
Instead of writing your own square root:
Use math.sqrt()

Benefits:
✔ Saves time
✔ Reduces errors
✔ Improves efficiency
""")

# ---------------- Turning Scripts into Organized Code ----------------
print("\n===== TURNING SCRIPTS INTO ORGANIZED CODE =====")
print("""
Earlier:
One file → all code

Now:
Split into modules:

main.py → main logic
file_utils.py → file operations
math_utils.py → calculations

Benefits:
✔ Clean structure
✔ Easy debugging
✔ Reusability
""")

# ---------------- Practical Demonstration ----------------
print("\n===== PRACTICAL DEMONSTRATION =====")

print("""
We already used modules:

✔ import csv
✔ import json
✔ from pathlib import Path

These are all modules from Python library.

Now you understand:
✔ Where they come from
✔ Why we use them
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Module = single Python file
✔ Package = folder of modules
✔ Standard library = built-in modules
✔ import is used to access modules
✔ Reuse code instead of rewriting
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Modules help organize code
✔ Packages group related modules
✔ Standard library provides ready tools
✔ import is used to access modules
✔ Avoid reinventing the wheel

This is the foundation for:
✔ Large applications
✔ Clean code architecture
✔ Professional Python development
""")