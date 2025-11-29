# Program: Swap Two Variables using a Temporary Variable

print("===== SWAP TWO VARIABLES =====")

# Taking input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nBefore swapping: a =", a, ", b =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)
