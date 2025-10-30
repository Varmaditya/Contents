# Conditional Statements in Python - IF-ELSE Statement

# ---------------- Introduction ----------------
print("\n===== IF-ELSE STATEMENT IN PYTHON =====")
print("""
The 'if-else' statement allows us to perform one action when a condition is True,
and another action when the condition is False.

SYNTAX:
if condition:
    statement(s)     # executed if condition is True
else:
    statement(s)     # executed if condition is False

Only one of the two blocks will execute based on the condition.
""")

# ---------------- Example 1: Even or Odd Check ----------------
print("\n---- Example 1: Checking whether a number is even or odd ----")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an EVEN number.")
else:
    print(number, "is an ODD number.")

# ---------------- Example 2: Voting Eligibility ----------------
print("\n---- Example 2: Checking voting eligibility ----")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote. ✅")
else:
    print("You are NOT eligible to vote yet. ❌")

# ---------------- Example 3: Comparing Two Numbers ----------------
print("\n---- Example 3: Comparing two numbers ----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The first number", a, "is greater than the second number", b)
else:
    print("The second number", b, "is greater than or equal to", a)

# ---------------- Example 4: Checking Password Match ----------------
print("\n---- Example 4: Simple password check ----")
password = input("Enter password: ")

if password == "python123":
    print("Access Granted ✅")
else:
    print("Access Denied ❌ Wrong Password.")

# ---------------- Example 5: Boolean Condition Example ----------------
print("\n---- Example 5: Boolean condition ----")
is_student = False

if is_student:
    print("Welcome student! Enjoy your course discount.")
else:
    print("Hello guest! Please register to get student benefits.")

# ---------------- Example 6: Temperature Check ----------------
print("\n---- Example 6: Checking hot or cold weather ----")
temperature = float(input("Enter today's temperature (°C): "))

if temperature > 25:
    print("It's a warm day ☀️")
else:
    print("It's a cool day 🌤️")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
→ The 'if-else' statement is used for two-way decision making.
→ 'if' block executes when condition is True.
→ 'else' block executes when condition is False.
→ Only one block runs at a time.
→ Indentation defines which statements belong to each block.
""")

print("Next, we'll learn about the 'if-elif-else' ladder for multiple conditions!")
