# Conditional Statements in Python - Nested IF-ELSE Statement

# ---------------- Introduction ----------------
print("\n===== NESTED IF-ELSE STATEMENT IN PYTHON =====")
print("""
A nested if-else means placing one if-else statement inside another.

It is used when we need to check multiple related conditions.

SYNTAX:
if condition1:
    if condition2:
        statement(s)
    else:
        statement(s)
else:
    statement(s)

→ The inner if-else is executed only when the outer condition is True.
→ Indentation is important to show hierarchy of conditions.
""")

# ---------------- Example 1: Checking Grade Based on Marks ----------------
print("\n---- Example 1: Grading System ----")
marks = int(input("Enter your marks (0-100): "))

if marks >= 40:
    print("You have passed the exam! ✅")
    if marks >= 90:
        print("Excellent! Grade: A+ 🏆")
    elif marks >= 75:
        print("Very Good! Grade: A")
    elif marks >= 60:
        print("Good Job! Grade: B")
    else:
        print("You passed with Grade: C")
else:
    print("Sorry, you failed. Better luck next time. ❌")

# ---------------- Example 2: Temperature and Weather Check ----------------
print("\n---- Example 2: Checking temperature range ----")
temperature = float(input("Enter temperature (°C): "))

if temperature >= 0:
    print("Temperature is above freezing.")
    if temperature > 35:
        print("It's very hot outside! ☀️")
    else:
        print("Normal temperature.")
else:
    print("It's freezing cold! ❄️")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
→ Nested if-else means one if-else inside another.
→ Used when multiple related conditions must be checked.
→ The inner block runs only if the outer condition is True.
→ Indentation defines which block belongs to which condition.
""")

print("Next, we'll study the 'if-elif-else' ladder for multiple separate conditions!")
