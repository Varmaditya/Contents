# Program: Using math Module
# Modules allow you to use pre-built mathematical functions in Python.

print("===== MODULE (math) DEMO =====")

import math

num = float(input("Enter a number: "))

print("\n--- Basic Operations ---")
print("Square Root:", math.sqrt(num))
print("Power (num^3):", math.pow(num, 3))
print("Ceil:", math.ceil(num))
print("Floor:", math.floor(num))

print("\n--- Advanced Math Functions ---")
print("Factorial (rounded number):", math.factorial(int(num)))
print("Log base e:", math.log(num))
print("Log base 10:", math.log10(num))
print("Sine:", math.sin(num))
print("Cosine:", math.cos(num))
print("Tangent:", math.tan(num))

print("\n--- Constants ---")
print("Pi:", math.pi)
print("Euler's number (e):", math.e)
