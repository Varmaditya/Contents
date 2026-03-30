# DECORATORS IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== DECORATORS IN PYTHON =====")
print("""
Decorators are functions that modify the behavior
of other functions without changing their code.

They are built using:
✔ Functions as first-class objects
✔ Nested functions
✔ Closures

Decorators are widely used in:
✔ Logging
✔ Authentication
✔ Caching
✔ Frameworks (Django, Flask)
""")

# ---------------- Why Decorators Exist ----------------
print("\n===== WHY DECORATORS EXIST =====")
print("""
Problem:
We often want to add extra functionality
to multiple functions.

Example:
✔ Logging
✔ Timing
✔ Access control

Without decorators:
We would repeat code again and again.

Decorators solve this by wrapping functions.
""")

def greet():
    print("Hello!")

def greet_with_log():
    print("Function started")
    greet()
    print("Function ended")

greet_with_log()

print("""
This approach is not reusable.
Decorators solve this problem.
""")

# ---------------- Basic Function Decorator ----------------
print("\n===== BASIC FUNCTION DECORATOR =====")

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

def say_hello():
    print("Hello, World!")

decorated_func = my_decorator(say_hello)
decorated_func()

print("""
Decorator wraps the original function
and adds extra behavior.
""")

# ---------------- Using @ Decorator Syntax ----------------
print("\n===== USING @ DECORATOR SYNTAX =====")

def log_decorator(func):
    def wrapper():
        print("Logging: Function started")
        func()
        print("Logging: Function ended")
    return wrapper

@log_decorator
def greet_user():
    print("Welcome User!")

greet_user()

print("""
@decorator is syntactic sugar for:
greet_user = log_decorator(greet_user)
""")

# ---------------- Decorator with Arguments ----------------
print("\n===== DECORATOR WITH ARGUMENTS =====")

def repeat_decorator(func):
    def wrapper():
        for i in range(3):
            func()
    return wrapper

@repeat_decorator
def say_hi():
    print("Hi!")

say_hi()

print("""
Decorator repeats function execution.
""")

# ---------------- Decorator Handling Function Arguments ----------------
print("\n===== DECORATOR HANDLING ARGUMENTS =====")

def argument_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments received:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@argument_decorator
def add(a, b):
    return a + b

print("Result:", add(5, 10))

# ---------------- Decorator with Parameters ----------------
print("\n===== DECORATOR WITH PARAMETERS =====")
print("""
Here, decorator itself takes arguments.
""")

def repeat_times(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_times(2)
def greet_again():
    print("Hello again!")

greet_again()

# ---------------- Real-World Example ----------------
print("\n===== REAL-WORLD EXAMPLE =====")

def login_required(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to dashboard,", user)

dashboard("admin")
dashboard("guest")

print("""
Decorator checks access before running function.
""")

# ---------------- Timing Decorator Example ----------------
print("\n===== TIMING DECORATOR EXAMPLE =====")

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    print("Task completed")

slow_function()

# ---------------- Common Mistakes ----------------
print("\n===== COMMON MISTAKES =====")
print("""
✔ Not returning wrapper function
✔ Not handling arguments (*args, **kwargs)
✔ Losing original function metadata
✔ Forgetting return value inside wrapper
""")

# ---------------- Fixing Metadata Issue ----------------
print("\n===== FIXING METADATA ISSUE =====")

from functools import wraps

def better_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def sample():
    """This is a sample function"""
    print("Running sample")

print("Function Name:", sample.__name__)
print("Docstring:", sample.__doc__)

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Decorators modify function behavior
✔ Built using closures
✔ @ syntax simplifies usage
✔ Can accept arguments
✔ Used in real-world systems
✔ wraps() preserves metadata

Decorators are heavily used in:
✔ Web frameworks
✔ Authentication systems
✔ Logging and monitoring
✔ Performance optimization
""")
