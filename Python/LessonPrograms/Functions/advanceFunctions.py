# ADVANCED-BASIC FUNCTION TOPICS (LAMBDAS, MAP, FILTER, REDUCE)
# ---------------- Introduction ----------------
print("\n===== MORE FUNCTION TOPICS (BEGINNER LEVEL) =====")
print("""
These are additional basic concepts related to functions that help write 
short, clean and efficient code. These include:
1. Lambda Functions
2. map()
3. filter()
4. reduce()

All these tools work with functions and are commonly used in data processing.
""")

# ---------------- Lambda (Anonymous Functions) ----------------
print("\n===== LAMBDA (ANONYMOUS FUNCTIONS) =====")
print("""
A lambda function is a small anonymous (nameless) function written in one line.
Syntax:
    lambda arguments: expression
Used when the function is very simple and used only once.
""")

# simple lambda
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))

# lambda with two arguments
add = lambda a, b: a + b
print("10 + 20 using lambda:", add(10, 20))

# lambda inside another function
def apply_twice(func, value):
    return func(func(value))

print("Apply square twice on 2:", apply_twice(lambda x: x * x, 2))


# ---------------- map() Function ----------------
print("\n===== map() FUNCTION =====")
print("""
map(function, iterable)
Applies a function to every element in an iterable (list, tuple, etc.)
and returns a map object (which we convert to list).
""")

numbers = [1, 2, 3, 4, 5]

# using map with lambda
mapped = list(map(lambda x: x * 2, numbers))
print("Original list:", numbers)
print("After map (*2):", mapped)


# ---------------- filter() Function ----------------
print("\n===== filter() FUNCTION =====")
print("""
filter(function, iterable)
Keeps only the elements for which the function returns True.
""")

# filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", evens)


# ---------------- reduce() Function ----------------
print("\n===== reduce() FUNCTION =====")
print("""
reduce(function, iterable)
Repeatedly applies the function to elements of iterable and reduces 
them to a single value (like cumulative result).
Example: adding all numbers.
""")

from functools import reduce

# reduce to sum all numbers
total = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", total)

# reduce to find maximum
max_value = reduce(lambda a, b: a if a > b else b, numbers)
print("Max using reduce:", max_value)


# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE: PROCESSING SCORES =====")

scores = [45, 67, 89, 32, 78, 90, 55]

print("Scores:", scores)

# 1. Add +5 bonus marks to each score
bonus_scores = list(map(lambda x: x + 5, scores))
print("After +5 bonus:", bonus_scores)

# 2. Filter only passing students (>= 50)
passing = list(filter(lambda x: x >= 50, bonus_scores))
print("Students who passed (>=50):", passing)

# 3. Total of passing students
total_pass = reduce(lambda a, b: a + b, passing)
print("Total marks of passed students:", total_pass)


# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We covered:
✔ Lambda Functions (quick one-line functions)
✔ map() to apply function to all items
✔ filter() to select items based on condition
✔ reduce() to reduce list into a single value
✔ Practical example of processing marks

These are the remaining basic topics related to functions in Python.
""")
