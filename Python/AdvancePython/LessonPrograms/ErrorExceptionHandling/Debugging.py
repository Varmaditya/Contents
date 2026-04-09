# DEBUGGING IN PYTHON (INTRODUCTION)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== DEBUGGING IN PYTHON =====")
print("""
Debugging is the process of:
✔ Finding errors (bugs)
✔ Understanding why they occur
✔ Fixing them

A bug is simply a mistake in the program.

Debugging helps in:
✔ Identifying problems
✔ Improving program correctness
✔ Writing reliable code
""")

# ---------------- Types of Bugs ----------------
print("\n===== TYPES OF BUGS =====")
print("""
1️⃣ Syntax Errors
   - Code will not run

2️⃣ Runtime Errors
   - Program crashes during execution

3️⃣ Logical Errors
   - Program runs but gives wrong output
""")

# ---------------- Example of Logical Bug ----------------
print("\n===== EXAMPLE OF LOGICAL BUG =====")
print("""
Problem:
Program calculates area incorrectly
""")

def area_of_circle(radius):
    return 2 * 3.14 * radius   # Wrong formula

print("Calculated Area:", area_of_circle(5))

print("""
Bug:
Formula is incorrect.

Correct formula should be:
π * r * r
""")

# ---------------- Debugging Using Print Statements ----------------
print("\n===== DEBUGGING USING PRINT STATEMENTS =====")
print("""
One of the simplest debugging methods:
Print intermediate values.
""")

def find_average(numbers):
    total = 0
    for num in numbers:
        print("Adding:", num)
        total += num
    print("Total:", total)
    return total / len(numbers)

print("Average:", find_average([10, 20, 30]))

# ---------------- Debugging Input Issues ----------------
print("\n===== DEBUGGING INPUT ISSUES =====")
print("""
Problem:
User enters wrong input type.
""")

value = "10"
print("Value:", value)
print("Type:", type(value))

print("""
Understanding data type helps identify bugs.
""")

# ---------------- Using type() for Debugging ----------------
print("\n===== USING type() FOR DEBUGGING =====")

a = 5
b = "5"

print("Type of a:", type(a))
print("Type of b:", type(b))

print("""
Even if values look similar,
types may be different.
""")

# ---------------- Using Logging Style Debugging ----------------
print("\n===== STEP-BY-STEP DEBUGGING =====")
print("""
Break program into steps
and verify each step.
""")

def calculate_discount(price):
    print("Received price:", price)

    discount = price * 0.1
    print("Calculated discount:", discount)

    final_price = price - discount
    print("Final price:", final_price)

    return final_price

print("Result:", calculate_discount(100))

# ---------------- Introduction to Debugger (pdb) ----------------
print("\n===== INTRODUCTION TO PYTHON DEBUGGER (pdb) =====")
print("""
Python provides a built-in debugger called pdb.

Basic usage:
import pdb
pdb.set_trace()

This pauses execution and allows:
✔ Step-by-step execution
✔ Checking variable values
✔ Understanding flow
""")

print("""
Example (not executed here):

import pdb

def test():
    x = 10
    pdb.set_trace()
    y = x + 5
    print(y)
""")

# ---------------- Common Debugging Strategies ----------------
print("\n===== COMMON DEBUGGING STRATEGIES =====")
print("""
✔ Read error messages carefully
✔ Use print() to trace values
✔ Check variable types
✔ Break problem into smaller parts
✔ Test with simple inputs first
✔ Reproduce the error consistently
""")

# ---------------- Real-World Debugging Scenario ----------------
print("\n===== REAL-WORLD DEBUGGING SCENARIO =====")
print("""
Example:
E-commerce cart shows wrong total.

Steps to debug:
✔ Check item prices
✔ Check calculation logic
✔ Print intermediate values
✔ Verify input data
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Debugging is a skill, not a tool
✔ Errors are normal in programming
✔ Good programmers debug efficiently
✔ Always test edge cases
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Debugging means finding and fixing bugs
✔ Bugs can be syntax, runtime, or logical
✔ Print statements help trace execution
✔ type() helps identify data issues
✔ pdb allows step-by-step debugging
✔ Debugging improves code quality

Debugging is essential for every programmer.
""")