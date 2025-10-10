# Relational (Comparison) Operators in Python

# ---------------- Introduction ----------------
print("\n===== RELATIONAL (COMPARISON) OPERATORS IN PYTHON =====")

print("""
These operators are used to compare two values.
They always return a Boolean value:
True  -> if the condition is satisfied
False -> if the condition is not satisfied
""")

# ---------------- Variable Declaration ----------------
a = 10
b = 20

print("Values used for comparison:")
print("a =", a)
print("b =", b)
print("\n---------------- OPERATIONS ----------------\n")

# 1️. Equal to (==)
print("1. Equal to (==)")
print("   Expression: a == b →", a == b)
print("   Meaning   : Returns True if both values are equal.\n")

# 2️. Not equal to (!=)
print("2. Not equal to (!=)")
print("   Expression: a != b →", a != b)
print("   Meaning   : Returns True if both values are NOT equal.\n")

# 3️. Greater than (>)
print("3. Greater than (>)")
print("   Expression: a > b →", a > b)
print("   Meaning   : Returns True if left value is greater.\n")

# 4️. Less than (<)
print("4. Less than (<)")
print("   Expression: a < b →", a < b)
print("   Meaning   : Returns True if left value is smaller.\n")

# 5️. Greater than or equal to (>=)
print("5. Greater than or equal to (>=)")
print("   Expression: a >= b →", a >= b)
print("   Meaning   : Returns True if left value is greater or equal.\n")

# 6️. Less than or equal to (<=)
print("6. Less than or equal to (<=)")
print("   Expression: a <= b →", a <= b)
print("   Meaning   : Returns True if left value is smaller or equal.\n")

# ---------------- Input Example ----------------
print("---------- USER INPUT EXAMPLE ----------")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"{x} == {y} → {x == y}")
print(f"{x} != {y} → {x != y}")
print(f"{x} > {y}  → {x > y}")
print(f"{x} < {y}  → {x < y}")
print(f"{x} >= {y} → {x >= y}")
print(f"{x} <= {y} → {x <= y}")

# ---------------- Practical Notes ----------------
print("""
Notes:
- Comparison operators return True or False (Boolean values).
- They are commonly used in decision making (e.g., if statements).
- Works with numbers, strings, and other comparable data types.

Example with strings:
   "apple" == "apple" → True
   "apple" < "banana" → True (because 'a' comes before 'b' alphabetically)
""")

# String Example
print("\nString Comparison Example:")
print("'apple' == 'apple' →", "apple" == "apple")
print("'apple' < 'banana' →", "apple" < "banana")
print("'cat' > 'bat' →", "cat" > "bat")
