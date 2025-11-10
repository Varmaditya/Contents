# Python Program: Constants

# Variables
name = "Alice"
age = 21
height = 5.6

print("Variable - Name:", name)
print("Variable - Age:", age)
print("Variable - Height:", height)

# Constants (using naming convention)
PI = 3.14159
GRAVITY = 9.8
APP_NAME = "MyApp"

print("\nConstant - PI:", PI)
print("Constant - GRAVITY:", GRAVITY)
print("Constant - APP_NAME:", APP_NAME)

# Modifying constants (not recommended)
PI = 3.14
print("\n(After modifying PI) PI:", PI, "-> Not recommended!")






"""

# Python Program: Variables and Constants
# This program explains Variables and Constants in Python

# ---------------- VARIABLES ----------------
# Variables are used to store data values.
# Python does not require explicit type declaration.

# Declaration
name = "Alice"
age = 21
height = 5.6

print("Variable - Name:", name)
print("Variable - Age:", age)
print("Variable - Height:", height)

# ---------------- CONSTANTS ----------------
# Python does not have built-in constant types.
# By convention, we use UPPERCASE variable names for constants.

PI = 3.14159       # Constant for value of Pi
GRAVITY = 9.8      # Constant for gravitational acceleration
APP_NAME = "MyApp" # Constant for application name

print("\nConstant - PI:", PI)
print("Constant - GRAVITY:", GRAVITY)
print("Constant - APP_NAME:", APP_NAME)

# Technically constants CAN be changed in Python (not enforced),
# but by convention we DO NOT change them.
PI = 3.14   # ❌ This should not be done
print("\n(After modifying PI) PI:", PI, " -> Not recommended!")

# Best practice: treat uppercase names as constants and do not modify them.

"""
