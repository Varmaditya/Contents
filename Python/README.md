# Conditional Statements in Python - Short-hand if / Conditional Expressions
# ---------------- Introduction ----------------
print("\n===== SHORT-HAND IF / CONDITIONAL EXPRESSIONS IN PYTHON =====")
print("""
Python allows writing conditional statements in a single line using **short-hand if** or **conditional expressions**.
This helps make the code more compact and readable when only one statement needs to be executed.

TYPES:
1️⃣ Single-line if statement
2️⃣ Single-line if-else statement (Ternary Expression)
3️⃣ Nested short-hand if (multiple inline conditions)
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

# ---------------- Example 3: Checking Even or Odd ----------------
print("\n---- Example 3: Even or Odd Check ----")
num = int(input("Enter a number: "))
print("Even") if num % 2 == 0 else print("Odd")

# ---------------- Example 4: Voting Eligibility ----------------
print("\n---- Example 4: Voting Eligibility ----")
age = int(input("Enter your age: "))
print("Eligible to vote ✅") if age >= 18 else print("Not eligible ❌")

# ---------------- Example 5: Positive, Negative, or Zero (Nested Short-hand) ----------------
print("\n---- Example 5: Nested Short-hand Example ----")
number = int(input("Enter a number: "))
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
print("The number is:", result)

# ---------------- Example 6: Compare Two Numbers ----------------
print("\n---- Example 6: Comparing Two Numbers ----")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"{x} is greater") if x > y else print(f"{y} is greater") if y > x else print("Both are equal")

# ---------------- Example 7: Grade Evaluation ----------------
print("\n---- Example 7: Quick Grade Evaluation ----")
marks = int(input("Enter your marks (0-100): "))
grade = "A" if marks >= 85 else "B" if marks >= 70 else "C" if marks >= 50 else "F"
print("Your grade is:", grade)

# ---------------- Example 8: Check Discount Eligibility ----------------
print("\n---- Example 8: Discount Eligibility ----")
purchase = float(input("Enter total purchase amount: ₹"))
discount = "Discount Applied 🎉" if purchase > 1000 else "No Discount 😔"
print(discount)

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

print("Next, we’ll begin Looping Statements starting with the WHILE loop! 🔁")
