# Conditional Statements in Python - IF-ELIF-ELSE Ladder

# ---------------- Introduction ----------------
print("\n===== IF-ELIF-ELSE LADDER IN PYTHON =====")
print("""
The 'if-elif-else' ladder is used when we need to check **multiple conditions**
and execute only one block of code among many possible choices.

SYNTAX:
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)

→ The conditions are checked one by one from top to bottom.
→ As soon as one condition is True, its block runs and the rest are skipped.
→ If none of the conditions are True, the 'else' block executes.
""")

# ---------------- Example 1: Grading System ----------------
print("\n---- Example 1: Student Grading ----")
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A+ 🏆 Excellent Performance!")
elif marks >= 75:
    print("Grade: A 👍 Very Good!")
elif marks >= 60:
    print("Grade: B 🙂 Good Job!")
elif marks >= 40:
    print("Grade: C 😐 Passed.")
else:
    print("Grade: F ❌ Failed. Try again!")

# ---------------- Example 2: Checking Temperature Range ----------------
print("\n---- Example 2: Temperature Check ----")
temperature = float(input("Enter temperature in °C: "))

if temperature > 35:
    print("It's too hot! ☀️")
elif temperature > 25:
    print("It's a warm day 🌤️")
elif temperature > 15:
    print("It's pleasant outside 🌸")
elif temperature > 5:
    print("It's a bit cold ❄️")
else:
    print("It's freezing! 🧣")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
→ The 'if-elif-else' ladder is used when multiple conditions are to be checked.
→ Only one condition's block executes (the first one that is True).
→ If none of the conditions are True, the 'else' block runs.
→ Helps write clean and structured decision-making code.
""")

