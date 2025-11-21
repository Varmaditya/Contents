# FUNCTIONS IN PYTHON
# ---------------- Introduction ----------------
print("\n===== FUNCTIONS IN PYTHON =====")
print("""
A Function in Python is a reusable block of code that performs a specific task.
Functions help make code modular, clean, and maintainable.
Functions are defined using the 'def' keyword.
""")

# ---------------- Defining Functions ----------------
print("\n===== DEFINING FUNCTIONS =====")

print("\n--- Simple Function Definition ---")
def greet():
    print("Hello! This is a simple function.")

greet()

print("\n--- Function with Parameters (Positional Arguments) ---")
def add(a, b):
    print("Adding:", a, "+", b, "=", a + b)

add(10, 20)
add(3, 7)

# ---------------- Default & Keyword Arguments ----------------
print("\n===== DEFAULT & KEYWORD ARGUMENTS =====")

def student_info(name, course="Python", duration="3 months"):
    print("Name:", name)
    print("Course:", course)
    print("Duration:", duration)

print("\nCalling with Positional Arguments:")
student_info("John")

print("\nCalling with Keyword Arguments (order doesn't matter):")
student_info(course="Java", name="Janet", duration="4 months")

# ---------------- Variable-Length Arguments ----------------
print("\n===== VARIABLE-LENGTH ARGUMENTS (*args, **kwargs) =====")

print("\n--- *args Example (accepts many positional values) ---")
def total_sum(*args):
    print("Numbers received:", args)
    print("Sum =", sum(args))

total_sum(10, 20, 30, 40)
total_sum(5, 15)

print("\n--- **kwargs Example (accepts many key-value pairs) ---")
def details(**kwargs):
    print("Details received:", kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)

details(name="John", age=23, country="India")

# ---------------- Return Statement ----------------
print("\n===== RETURN STATEMENT =====")

def multiply(x, y):
    result = x * y
    return result

val = multiply(6, 7)
print("Returned Value:", val)

# ---------------- Scope of Variables (Local vs Global) ----------------
print("\n===== SCOPE OF VARIABLES =====")

x = 100  # global variable

def show_scope():
    x = 50  # local variable
    print("Inside function (local x):", x)

show_scope()
print("Outside function (global x):", x)

print("\n--- Using global keyword to modify global variable ---")
y = 30

def change_global():
    global y
    y = 99
    print("Inside function modified y:", y)

change_global()
print("Outside function modified y:", y)

# ---------------- Built-in Functions ----------------
print("\n===== BUILT-IN FUNCTIONS =====")

nums = [10, 50, 20, 5, 40]

print("List:", nums)
print("Length:", len(nums))
print("Type:", type(nums))
print("Sum:", sum(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sorted:", sorted(nums))
print("Range example (1 to 5):", list(range(1, 6)))

# ---------------- Iterating with Functions ----------------
print("\n===== USING FUNCTIONS WITH LOOPS =====")

def square(n):
    return n * n

print("Squares from 1 to 5:")
for i in range(1, 6):
    print(i, "->", square(i))

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE: STUDENT MARKS SYSTEM =====")

def calculate_average(*marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

def student_report(name, *marks, **extra):
    print("\nReport for:", name)
    print("Marks:", marks)
    print("Average:", calculate_average(*marks))
    print("Extra Info:", extra)

student_report("John", 85, 90, 95, city="Delhi", course="Computer Engineering")

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We covered:
✔ Defining functions with def
✔ Positional, keyword, and default arguments
✔ Variable-length arguments (*args and **kwargs)
✔ Return statement and returning values
✔ Local vs global variables (with global keyword)
✔ Common built-in functions (len, sum, max, min, range, sorted)
✔ Practical example using multiple concepts together

Functions help in code reusability, modularity, and cleaner program design.
""")
