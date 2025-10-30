# Control Flow in Python

# ---------------- Introduction ----------------
print("\n===== CONTROL FLOW IN PYTHON =====")
print("""
Control flow refers to the order in which individual statements,
instructions, or function calls are executed in a program.

By default, Python executes code from top to bottom, but using
control statements we can change this order to:
1. Make decisions
2. Repeat certain actions
3. Jump between statements
""")

# ---------------- Types of Control Flow Statements ----------------
print("Types of Control Flow Statements in Python:")
print("1. Conditional Statements → if, elif, else")
print("2. Looping Statements     → for, while")
print("3. Jump Statements        → break, continue, pass")

# ---------------- Example Variables ----------------
print("\nLet's define some example variables for demonstration:")
temperature = 30
count = 3
weather = "sunny"

print("Temperature =", temperature)
print("Count =", count)
print("Weather =", weather)

# ---------------- Conditional Example ----------------
print("\n---- Conditional Statement Example ----")
print("Checking weather condition using if-elif-else:")

if weather == "sunny":
    print("It's a bright day! Wear sunglasses. 😎")
elif weather == "rainy":
    print("Carry an umbrella! ☔")
else:
    print("Stay warm and cozy! ❄️")

# ---------------- Looping Example ----------------
print("\n---- Looping Statement Example ----")
print("Using a 'for' loop to print numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")

print("\nUsing a 'while' loop to count down from 3:")
while count > 0:
    print(count, end=" ")
    count -= 1

# ---------------- Jump Statements Example ----------------
print("\n\n---- Jump Statement Example ----")
print("Demonstrating 'break', 'continue', and 'pass' in a loop:")

for i in range(1, 6):
    if i == 2:
        print("Skipping number 2 using continue.")
        continue
    if i == 4:
        print("Breaking loop at number 4 using break.")
        break
    print("Number:", i)

# Using pass (does nothing, placeholder for future code)
for j in range(3):
    pass  # Placeholder statement
print("Used 'pass' inside loop without any operation.")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
Control Flow helps manage how your program executes statements.

1. Conditional Statements → For making decisions.
2. Looping Statements     → For repeating tasks.
3. Jump Statements        → For skipping or breaking loops.

We'll study each type in detail next!
""")
