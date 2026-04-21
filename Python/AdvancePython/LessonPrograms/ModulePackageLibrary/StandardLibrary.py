# PYTHON STANDARD LIBRARY (CORE MODULES - DETAILED)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== PYTHON STANDARD LIBRARY =====")
print("""
Python provides a large collection of built-in modules
called the Standard Library.

These modules help us:
✔ Solve common problems
✔ Avoid writing code from scratch
✔ Build real-world applications

Rule:
👉 Don't reinvent the wheel
""")

# ---------------- pip (External Libraries) ----------------
print("\n===== pip (EXTERNAL LIBRARIES) =====")
print("""
pip is used to install external libraries.

Command:
pip install library_name

Use when:
✔ Feature not available in standard library
✔ Working with APIs, ML, Web apps

Example:
pip install requests
""")

# ======================================================
# os MODULE
# ======================================================

print("\n===== os MODULE =====")
print("""
WHAT:
Used for interacting with Operating System

WHEN:
✔ File & folder operations
✔ Automation scripts
✔ System utilities
""")

import os

# Example 1: Current directory
print("\n--- Example 1: Current Directory ---")
print(os.getcwd())

# Example 2: List files
print("\n--- Example 2: List Files ---")
print(os.listdir())

# Example 3: Create directory
print("\n--- Example 3: Create Folder ---")
os.makedirs("demo_folder", exist_ok=True)
print("Folder created")

# ======================================================
# sys MODULE
# ======================================================

print("\n===== sys MODULE =====")
print("""
WHAT:
Used for system-level operations

WHEN:
✔ Command-line arguments
✔ System configuration
✔ Script control
""")

import sys

# Example 1: Python version
print("\n--- Example 1: Python Version ---")
print(sys.version)

# Example 2: Arguments
print("\n--- Example 2: Command-line Arguments ---")
print(sys.argv)

# Example 3: Exit program
print("\n--- Example 3: Exit Example ---")
print("Program continues... (sys.exit() not called)")

# ======================================================
# math MODULE
# ======================================================

print("\n===== math MODULE =====")
print("""
WHAT:
Provides mathematical functions

WHEN:
✔ Calculations
✔ Scientific programs
✔ Geometry
""")

import math

# Example 1: Square root
print("\n--- Example 1: Square Root ---")
print(math.sqrt(36))

# Example 2: Factorial
print("\n--- Example 2: Factorial ---")
print(math.factorial(5))

# Example 3: Trigonometry
print("\n--- Example 3: Cosine ---")
print(math.cos(0))

# ======================================================
# random MODULE
# ======================================================

print("\n===== random MODULE =====")
print("""
WHAT:
Generates random values

WHEN:
✔ Games
✔ Simulations
✔ Random selection
""")

import random

# Example 1: Random number
print("\n--- Example 1: Random Integer ---")
print(random.randint(1, 10))

# Example 2: Random choice
print("\n--- Example 2: Random Choice ---")
print(random.choice(["apple", "banana", "mango"]))

# Example 3: Shuffle list
print("\n--- Example 3: Shuffle List ---")
data = [1, 2, 3, 4]
random.shuffle(data)
print(data)

# ======================================================
# datetime MODULE
# ======================================================

print("\n===== datetime MODULE =====")
print("""
WHAT:
Handles date and time

WHEN:
✔ Logging
✔ Scheduling
✔ Time-based operations
""")

import datetime

# Example 1: Current time
print("\n--- Example 1: Current Time ---")
now = datetime.datetime.now()
print(now)

# Example 2: Specific date
print("\n--- Example 2: Create Date ---")
d = datetime.datetime(2025, 1, 1)
print(d)

# Example 3: Date difference
print("\n--- Example 3: Date Difference ---")
delta = now - d
print(delta)

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ os → system & files
✔ sys → system control
✔ math → calculations
✔ random → randomness
✔ datetime → time handling

These are core tools for real-world programming.
""")