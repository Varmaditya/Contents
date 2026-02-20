# NESTED FUNCTIONS & FUNCTIONS AS FIRST-CLASS OBJECTS
# ---------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== NESTED FUNCTIONS & FIRST-CLASS FUNCTIONS =====")
print("""
In Python:
✔ Functions can be defined inside other functions (Nested Functions)
✔ Functions are treated like variables (First-Class Objects)

This means functions can be:
✔ Assigned to variables
✔ Passed as arguments to other functions
✔ Returned from functions
✔ Stored in data structures

These concepts are the foundation of:
✔ Closures
✔ Decorators
✔ Callbacks
✔ Functional Programming
""")

# ---------------- Nested Functions ----------------
print("\n===== NESTED FUNCTIONS =====")
print("""
A nested function is a function defined inside another function.
The inner function can access variables from the outer function.
""")

def outer_function():
    print("Inside outer function")

    def inner_function():
        print("Inside inner function")

    inner_function()   # calling inner function

outer_function()

# ---------------- Nested Function with Enclosing Variable ----------------
print("\n===== NESTED FUNCTION WITH ENCLOSING VARIABLES =====")

def greet_person(name):
    greeting = "Hello"

    def greet():
        print(greeting, name)

    greet()

greet_person("Alice")

print("""
The inner function can access variables from the enclosing function.
This follows the LEGB rule.
""")

# ---------------- Returning a Nested Function ----------------
print("\n===== RETURNING A NESTED FUNCTION =====")

def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print("Double of 5:", double(5))
print("Triple of 5:", triple(5))

print("""
The inner function remembers the value of 'factor'
even after the outer function has finished execution.
This behavior leads to closures.
""")

# ---------------- Functions as First-Class Objects ----------------
print("\n===== FUNCTIONS AS FIRST-CLASS OBJECTS =====")
print("""
In Python, functions behave like any other object.
They can be stored, passed, and returned.
""")

# ---------------- Assigning Function to a Variable ----------------
print("\n===== ASSIGNING FUNCTION TO A VARIABLE =====")

def add(a, b):
    return a + b

operation = add   # function assigned to variable
print("Result using variable:", operation(10, 20))

# ---------------- Passing Function as Argument ----------------
print("\n===== PASSING FUNCTION AS ARGUMENT =====")

def calculate(a, b, func):
    print("Result:", func(a, b))

def subtract(x, y):
    return x - y

calculate(20, 10, add)
calculate(20, 10, subtract)

print("""
Functions passed as arguments are commonly used in:
✔ Callbacks
✔ Event handling
✔ Strategy selection
""")

# ---------------- Returning Function from Another Function ----------------
print("\n===== RETURNING FUNCTION FROM FUNCTION =====")

def operation_selector(choice):
    def add_op(x, y):
        return x + y

    def mul_op(x, y):
        return x * y

    if choice == "add":
        return add_op
    else:
        return mul_op

func = operation_selector("mul")
print("Selected operation result:", func(4, 5))

# ---------------- Storing Functions in Data Structures ----------------
print("\n===== STORING FUNCTIONS IN DATA STRUCTURES =====")

def square(n):
    return n * n

def cube(n):
    return n ** 3

functions = [square, cube]

for f in functions:
    print("Result:", f(3))

print("""
Storing functions allows dynamic execution of behavior.
""")

# ---------------- Practical Example: Message Formatter ----------------
print("\n===== PRACTICAL EXAMPLE: MESSAGE FORMATTER =====")

def formatter(style):
    def uppercase(text):
        return text.upper()

    def lowercase(text):
        return text.lower()

    def titlecase(text):
        return text.title()

    if style == "upper":
        return uppercase
    elif style == "lower":
        return lowercase
    else:
        return titlecase

format_text = formatter("upper")
print(format_text("python programming is powerful"))

format_text = formatter("title")
print(format_text("python programming is powerful"))

# ---------------- Real-World Analogy ----------------
print("\n===== REAL-WORLD ANALOGY =====")
print("""
Think of functions as tools.
You can:
✔ Hand a tool to someone (pass as argument)
✔ Put tools in a toolbox (data structure)
✔ Choose a tool based on task (return function)
✔ Build tools inside tools (nested functions)
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Nested functions are functions inside functions
✔ Inner functions can access enclosing variables
✔ Functions can be assigned to variables
✔ Functions can be passed as arguments
✔ Functions can be returned from functions
✔ Functions can be stored in data structures

These concepts are ESSENTIAL for:
✔ Closures
✔ Decorators
✔ Functional programming
✔ Clean, flexible system design

This chapter unlocks advanced Python thinking.
""")