# Looping Statements in Python - WHILE LOOP

# ---------------- Introduction ----------------
print("\n===== WHILE LOOP IN PYTHON =====")
print("""
A 'loop' is used to execute a block of code multiple times until a certain condition is False.
The 'while' loop in Python repeats a block of code **as long as the condition is True**.

It is used when the number of iterations is **not known in advance**.

SYNTAX:
while condition:
    # code block

→ The condition is checked before each iteration.
→ The code block runs while the condition remains True.
→ If the condition is False at the start, the loop does not execute even once.
""")

# ---------------- Example 1: Basic While Loop ----------------
print("\n---- Example 1: Print numbers from 1 to 5 ----")
i = 1
while i <= 5:
    print("Number:", i)
    i += 1   # increment step
print("Loop completed successfully.\n")

# ---------------- Example 2: Countdown Example ----------------
print("---- Example 2: Countdown Timer ----")
count = 5
while count >= 1:
    print("Countdown:", count)
    count -= 1
print("Blast off!\n")

# ---------------- Example 3: Taking Input until a Condition ----------------
print("---- Example 3: Asking user for input until condition met ----")
password = ""
while password != "python":
    password = input("Enter the password: ")
print("Access granted ✅\n")

# ---------------- Example 4: While loop for Sum of N Natural Numbers ----------------
print("---- Example 4: Calculate Sum of Natural Numbers ----")
n = int(input("Enter a number: "))
i = 1
sum_n = 0
while i <= n:
    sum_n += i
    i += 1
print("Sum of first", n, "numbers is:", sum_n, "\n")

# ---------------- Example 5: While loop for Even Numbers ----------------
print("---- Example 5: Display Even Numbers ----")
num = 1
limit = int(input("Enter limit: "))
while num <= limit:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
print("\nDisplayed all even numbers successfully.\n")

# ---------------- Example 6: Real-life Example - Bank Balance Countdown ----------------
print("---- Example 6: Simple Bank Balance Simulation ----")
balance = 1000
withdraw = 200
while balance > 0:
    print("Current Balance: ₹", balance)
    balance -= withdraw
print("Balance is now ₹0. Transaction complete.\n")

# ---------------- Example 7: While Loop with Multiple Variables ----------------
print("---- Example 7: Two Variables Changing in While Loop ----")
a = 1
b = 5
while a <= 5 and b <= 9:
    print(f"a = {a}, b = {b}")
    a += 1
    b += 1
print("Loop ended when condition became False.\n")

# ---------------- Summary ----------------
print("===== SUMMARY =====")
print("""
→ while → executes code repeatedly while condition is True
→ Condition is checked before every iteration
→ Variable inside loop must be updated, or loop becomes infinite
→ Used when number of repetitions is not known in advance

Example:
    i = 1
    while i <= 5:
        print(i)
        i += 1
""")
