# Conditional Statements in Python - Short-hand if / Conditional Expressions

# ---------------- Introduction ----------------
print("\n===== SHORT-HAND IF / CONDITIONAL EXPRESSIONS IN PYTHON =====")
print("""
Python allows writing conditional statements in a single line using **short-hand if** or **conditional expressions**.
This helps make the code more compact and readable when only one statement needs to be executed.

TYPES:
1. Single-line if statement
2. Single-line if-else statement (Ternary Expression)
3. Nested short-hand if (multiple inline conditions)
""")

# ---------------- Syntax ----------------
print("""
SYNTAX:

1. Single-line if:
   statement_if_true  if condition

2. Single-line if-else (Ternary Expression):
   value_if_true  if condition  else  value_if_false

3. Nested short-hand if:
   value1 if condition1 else value2 if condition2 else value3
""")

# ---------------- Example 1: Single-line if ----------------
print("\n---- Example 1: Single-line if ----")
x = 10
if x > 5: print("x is greater than 5")   # Simple one-line if
print("This line runs always.")          # Normal statement

# ---------------- Example 2: Short-hand if-else ----------------
print("\n---- Example 2: Short-hand if-else (Ternary Expression) ----")
a = 7
b = 12
max_value = a if a > b else b
print("Maximum value is:", max_value)

# ---------------- Example 3: Nested Short-hand ----------------
print("\n---- Example 3: Nested Short-hand  ----")
number = int(input("Enter a number: "))
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
print("The number is:", result)

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✅ Short-hand if and conditional expressions make simple decisions concise.
✅ Best used for quick decisions or assignments.
✅ Avoid overusing nested short-hands — use normal if-else for complex logic.

Examples:
→ print("Even") if num%2==0 else print("Odd")
→ result = "Pass" if marks>=40 else "Fail"
→ category = "Child" if age<13 else "Teen" if age<20 else "Adult"
""")

