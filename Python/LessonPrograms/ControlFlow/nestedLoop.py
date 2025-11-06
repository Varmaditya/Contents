# Looping Statements in Python - NESTED LOOPS

# ---------------- Introduction ----------------
print("\n===== NESTED LOOPS IN PYTHON =====")
print("""
A *nested loop* means placing one loop inside another.
The **outer loop** runs first, and for each iteration of the outer loop,
the **inner loop** runs completely.

It is commonly used in pattern printing, working with multi-dimensional data,
and performing repeated actions for combinations of values.

SYNTAX:
for variable1 in sequence1:
    for variable2 in sequence2:
        # code block

→ Outer loop → Controls the number of major repetitions.
→ Inner loop → Executes completely for every iteration of the outer loop.
""")

# ---------------- Example 1: Basic Nested For Loop ----------------
print("\n---- Example 1: Basic Nested For Loop ----")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop i = {i}, Inner loop j = {j}")
    print("----- Inner loop completed -----\n")
print("Nested for loop execution completed.\n")

# ---------------- Example 2: Multiplication Table (1 to 3) ----------------
print("---- Example 2: Multiplication Tables from 1 to 3 ----")
for i in range(1, 4):  # Outer loop for table number
    print(f"\nMultiplication Table for {i}:")
    for j in range(1, 11):  # Inner loop for multiplier
        print(f"{i} x {j} = {i*j}")
print("\nAll tables printed successfully.\n")

# ---------------- Example 3: Pattern Printing (Stars) ----------------
print("---- Example 3: Right-Angled Triangle Pattern ----")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print("Star pattern printed successfully.\n")

# ---------------- Example 4: Nested While Loop ----------------
print("---- Example 4: Nested While Loop Example ----")
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"Outer i = {i}, Inner j = {j}")
        j += 1
    i += 1
    print("Completed one full inner loop cycle.\n")
print("Nested while loop execution done.\n")

# ---------------- Example 5: Nested Loop with Lists ----------------
print("---- Example 5: Display Student Marks ----")
students = ["Alice", "Bob"]
subjects = ["Math", "Science", "English"]

for name in students:
    print(f"\nMarks for {name}:")
    for subject in subjects:
        marks = int(input(f"Enter marks in {subject}: "))
        print(f"{subject}: {marks}")
print("\nAll student data collected successfully.\n")

# ---------------- Example 6: Nested Loop with 2D List ----------------
print("---- Example 6: Traversing a 2D List ----")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix Elements:")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
print("Matrix traversal completed.\n")

# ---------------- Example 7: Real-life Example - Shopping Cart ----------------
print("---- Example 7: Shopping Cart Items ----")
categories = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Vegetables": ["Tomato", "Potato", "Carrot"]
}

for category, items in categories.items():
    print(f"\nCategory: {category}")
    for item in items:
        print(" -", item)
print("\nShopping cart displayed successfully.\n")

# ---------------- Example 8: Nested Loop with range() and conditions ----------------
print("---- Example 8: Display Even Numbers in a Range ----")
for i in range(1, 4):
    print(f"\nRange Set {i}:")
    for j in range(1, 11):
        if j % 2 == 0:
            print(j, end=" ")
    print()
print("\nNested loop with condition example completed.\n")

# ---------------- Example 9: Nested Loop for Combination Generation ----------------
print("---- Example 9: Generating Combinations ----")
colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"Product Variant: {color} - {size}")
print("\nAll product combinations generated successfully.\n")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
→ Nested loops → loops inside loops (can be for-for, while-while, for-while, etc.)
→ Inner loop → runs completely for each iteration of the outer loop
→ Common uses:
   • Pattern printing
   • 2D data (lists, matrices)
   • Generating combinations
   • Working with multiple sequences
→ Be careful! Nested loops increase time complexity.

Example Summary:
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
""")