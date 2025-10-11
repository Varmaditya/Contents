# Logical Operators in Python

# ---------------- Introduction ----------------
print("\n===== LOGICAL OPERATORS IN PYTHON =====")

print("""
Logical operators are used to combine conditional (boolean) statements.
They return True or False depending on the result of the conditions.

There are three logical operators in Python:
1. and  → Returns True if both conditions are True
2. or   → Returns True if any one condition is True
3. not  → Reverses the result, returns True if condition is False
""")

# ---------------- Variable Declaration ----------------
a = 10
b = 20
c = 5

print("Values used:")
print("a =", a, ", b =", b, ", c =", c)
print("\n-------------------------------------------\n")

# ---------------- Logical AND ----------------
print("1️⃣ Logical AND (and) Operator:")
print("Example: (a > b) and (b > c)")
result = (a > b) and (b > c)
print("Result →", result)
print("Explanation: (10 > 20) is False and (20 > 5) is True → Final = False\n")

# ---------------- Logical OR ----------------
print("2️⃣ Logical OR (or) Operator:")
print("Example: (a > b) or (b > c)")
result = (a > b) or (b > c)
print("Result →", result)
print("Explanation: (10 > 20) is False or (20 > 5) is True → Final = True\n")

# ---------------- Logical NOT ----------------
print("3️⃣ Logical NOT (not) Operator:")
print("Example: not(a > b)")
result = not(a > b)
print("Result →", result)
print("Explanation: (a > b) is False → not(False) becomes True\n")

# ---------------- Combination Example ----------------
print("4️⃣ Combined Logical Expression:")
print("Example: (a > b) or (a < c) and (b > c)")
result = (a > b) or (a < c) and (b > c)
print("Result →", result)
print("Explanation: 'and' is evaluated first → (a < c) and (b > c) = True → False or True = True\n")

# ---------------- Logical with Boolean Variables ----------------
print("5️⃣ Using Logical Operators with Boolean Values:")
x = True
y = False

print("x =", x, ", y =", y)
print("x and y =", x and y)
print("x or y  =", x or y)
print("not x   =", not x)
print("not y   =", not y)

# ---------------- Input Example ----------------
print("\n===== USER INPUT EXAMPLE =====")
num = int(input("Enter a number: "))

if num > 0 and num < 10:
    print("Number is between 1 and 9.")
elif num <= 0 or num >= 10:
    print("Number is not in range 1-9.")
else:
    print("Invalid input.")

# ---------------- Summary ----------------
print("""
Summary:
→ Logical operators help combine multiple conditions.
→ 'and' requires all conditions to be True.
→ 'or' requires at least one condition to be True.
→ 'not' reverses the result (True becomes False and vice versa).

They are mostly used in decision-making and control statements.
Example:
    if age > 18 and citizen == True:
        print("Eligible to vote")
""")
