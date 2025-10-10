# Arithmetic Operators in Python

# ---------------- Introduction ----------------
print("\n===== ARITHMETIC OPERATORS IN PYTHON =====")
print("""
Arithmetic operators are used to perform mathematical operations
like addition, subtraction, multiplication, division, etc.
""")

# ---------------- Variable Declaration ----------------
a = 15
b = 4

print("Values used for demonstration:")
print("a =", a)
print("b =", b)
print("\n---------------- OPERATIONS ----------------\n")

# 1️. Addition (+)
add_result = a + b
print("1. Addition (+)")
print("   Expression: a + b =", add_result)
print("   Meaning   : Adds two numbers.\n")

# 2. Subtraction (-)
sub_result = a - b
print("2. Subtraction (-)")
print("   Expression: a - b =", sub_result)
print("   Meaning   : Subtracts right operand from left.\n")

# 3️. Multiplication (*)
mul_result = a * b
print("3. Multiplication (*)")
print("   Expression: a * b =", mul_result)
print("   Meaning   : Multiplies two numbers.\n")

# 4️. Division (/)
div_result = a / b
print("4. Division (/)")
print("   Expression: a / b =", div_result)
print("   Meaning   : Divides left by right, always returns float.\n")

# 5️. Floor Division (//)
floor_result = a // b
print("5. Floor Division (//)")
print("   Expression: a // b =", floor_result)
print("   Meaning   : Divides and returns only integer part (floor value).\n")

# 6️. Modulus (%)
mod_result = a % b
print("6. Modulus (%)")
print("   Expression: a % b =", mod_result)
print("   Meaning   : Returns remainder of division.\n")

# 7. Exponent (**)
exp_result = a ** b
print("7. Exponent (**)")
print("   Expression: a ** b =", exp_result)
print("   Meaning   : Raises a to the power of b (a^b).\n")

# ---------------- Input Example ----------------
print("---------- USER INPUT EXAMPLE ----------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Modulus: {num1 % num2}")
print(f"Exponent: {num1 ** num2}")
