# Conditional Statements in Python - IF Statement

# ---------------- Introduction ----------------
print("\n===== IF STATEMENT IN PYTHON =====")
print("""
Conditional statements allow a program to make decisions and
execute different code blocks based on certain conditions.

The simplest conditional statement is the 'if' statement.

SYNTAX:
if condition:
    statement(s)

→ The condition is checked first.
→ If the condition is True → the indented block runs.
→ If the condition is False → the block is skipped.
""")

# ---------------- Example 1: Basic IF Statement ----------------
print("\n---- Example 1: Checking eligibility for voting ----")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote. ✅")

print("Program continues after IF statement.\n")

# ---------------- Example 2: IF Statement with Comparison ----------------
print("---- Example 2: Checking temperature ----")
temperature = float(input("Enter current temperature (°C): "))

if temperature > 30:
    print("It's a hot day! ☀️")

print("Stay hydrated and stay safe.\n")

# ---------------- Example 3: IF with Boolean variable ----------------
print("---- Example 3: Using a Boolean condition ----")
is_student = True

if is_student:
    print("You are eligible for a student discount! 🎟️")

print("This message is always shown, outside the IF block.\n")

# ---------------- Example 4: Multiple IF Statements ----------------
print("---- Example 4: Multiple independent IF statements ----")
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A+")
if marks >= 75:
    print("Grade: A")
if marks >= 60:
    print("Grade: B")
if marks >= 40:
    print("Grade: C")
if marks < 40:
    print("Grade: Fail ❌")

print("Each IF is checked separately.\n")

# ---------------- Example 5: IF with Expressions ----------------
print("---- Example 5: Checking even number ----")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an Even number.")
if number % 2 != 0:
    print(number, "is an Odd number.")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
→ 'if' is the most basic conditional statement in Python.
→ It executes a block of code only if the condition is True.
→ Indentation (4 spaces or a Tab) defines the scope of the IF block.
→ Multiple independent IF statements can be used for multiple checks.
""")

