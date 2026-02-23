# CLOSURES & DOCSTRINGS IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== CLOSURES & DOCSTRINGS IN PYTHON =====")
print("""
This chapter covers two powerful Python concepts:

1️⃣ Closures
   - Functions that remember variables from their enclosing scope
   - Built using nested functions + returning functions

2️⃣ Docstrings
   - Special strings used to document functions, modules, and classes
   - Help users understand what a function does

These concepts are heavily used in:
✔ Decorators
✔ Libraries & frameworks
✔ Professional Python code
""")

# ======================================================
# CLOSURES
# ======================================================

print("\n===== WHAT IS A CLOSURE? =====")
print("""
A closure is a function that:
✔ Is defined inside another function
✔ Uses variables from the outer function
✔ Remembers those variables even after the outer function finishes

Closures are created when:
✔ A nested function is returned
✔ The inner function uses enclosing variables
""")

# ---------------- Basic Closure Example ----------------
print("\n===== BASIC CLOSURE EXAMPLE =====")

def outer_function():
    message = "Hello from outer function"

    def inner_function():
        print(message)

    return inner_function

my_func = outer_function()
my_func()   # inner function still remembers 'message'

print("""
Even though outer_function() has finished,
inner_function() still remembers the variable 'message'.
""")

# ---------------- Closure with Parameters ----------------
print("\n===== CLOSURE WITH PARAMETERS =====")

def power_generator(power):
    def calculate(number):
        return number ** power
    return calculate

square = power_generator(2)
cube = power_generator(3)

print("Square of 5:", square(5))
print("Cube of 4:", cube(4))

print("""
The inner function 'calculate' remembers the value of 'power'.
Each returned function has its own memory.
""")

# ---------------- Why Closures Are Useful ----------------
print("\n===== WHY USE CLOSURES? =====")
print("""
Closures allow us to:
✔ Customize function behavior
✔ Avoid global variables
✔ Preserve state safely
✔ Write cleaner, reusable code
""")

# ---------------- Practical Closure Example: Counter ----------------
print("\n===== PRACTICAL EXAMPLE: COUNTER USING CLOSURE =====")

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

my_counter = counter()
print("Counter:", my_counter())
print("Counter:", my_counter())
print("Counter:", my_counter())

print("""
The variable 'count' is preserved across function calls
without using global variables.
""")

# ======================================================
# DOCSTRINGS
# ======================================================

print("\n===== DOCSTRINGS IN PYTHON =====")
print("""
A docstring is a string literal used to document:
✔ Functions
✔ Classes
✔ Modules

Docstrings are written using triple quotes.
They can be accessed using the __doc__ attribute or help().
""")

# ---------------- Function Docstring Example ----------------
print("\n===== FUNCTION DOCSTRING EXAMPLE =====")

def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Sum of a and b
    """
    return a + b

print("Result:", add(10, 20))
print("\nDocstring of add():")
print(add.__doc__)

# ---------------- Using help() with Docstrings ----------------
print("\n===== USING help() FUNCTION =====")
print("Help on add() function:")
help(add)

# ---------------- Docstring in Closure ----------------
print("\n===== DOCSTRING IN CLOSURE =====")

def salary_calculator(tax_rate):
    """
    Creates a salary calculation function with a fixed tax rate.

    Parameters:
    tax_rate (float): Tax percentage to deduct

    Returns:
    function: A function that calculates net salary
    """

    def calculate_salary(amount):
        """
        Calculates net salary after tax deduction.

        Parameters:
        amount (float): Gross salary

        Returns:
        float: Net salary after tax
        """
        return amount - (amount * tax_rate)

    return calculate_salary

calc = salary_calculator(0.10)
print("Net Salary:", calc(50000))

print("\nOuter function docstring:")
print(salary_calculator.__doc__)

print("\nInner function docstring:")
print(calc.__doc__)

# ---------------- Real-World Example: Access Control ----------------
print("\n===== REAL-WORLD EXAMPLE: ACCESS CONTROL USING CLOSURE =====")

def login_required(role):
    """
    Creates a role-based access checker.

    Parameters:
    role (str): Required role to access a feature

    Returns:
    function: Access checking function
    """

    def access(user_role):
        """
        Checks whether the user has required access.

        Parameters:
        user_role (str): Role of the user

        Returns:
        str: Access result
        """
        if user_role == role:
            return "Access Granted"
        return "Access Denied"

    return access

admin_access = login_required("admin")
print(admin_access("admin"))
print(admin_access("guest"))

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Closures are functions that remember enclosing variables
✔ Closures avoid global variables
✔ Closures preserve state across function calls
✔ Docstrings document functions, classes, and modules
✔ Docstrings improve readability and maintainability
✔ help() and __doc__ use docstrings

Closures + Docstrings form the backbone of:
✔ Decorators
✔ Frameworks
✔ Clean, professional Python code
""")
