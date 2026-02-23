# FUNCTION ANNOTATIONS IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== FUNCTION ANNOTATIONS IN PYTHON =====")
print("""
Function annotations are optional metadata added to:
✔ Function parameters
✔ Return values

Annotations describe what kind of data a function expects and returns.
They DO NOT enforce types at runtime.

Function annotations are widely used for:
✔ Code readability
✔ Documentation
✔ Static type checking
✔ IDE auto-completion
""")

# ---------------- Basic Annotation Syntax ----------------
print("\n===== BASIC FUNCTION ANNOTATION SYNTAX =====")
print("""
Syntax:

def function_name(param: type) -> return_type:
    pass
""")

def greet(name: str) -> str:
    return "Hello " + name

print(greet("Alice"))

# ---------------- Annotations Do Not Enforce Types ----------------
print("\n===== ANNOTATIONS DO NOT ENFORCE TYPES =====")

def add(a: int, b: int) -> int:
    return a + b

print("Correct usage:", add(10, 20))
print("Still works with strings:", add("Py", "thon"))

print("""
Python does not enforce annotations.
They are only hints, not rules.
""")

# ---------------- Accessing Annotations ----------------
print("\n===== ACCESSING FUNCTION ANNOTATIONS =====")

def calculate_area(length: float, width: float) -> float:
    return length * width

print("Annotations dictionary:")
print(calculate_area.__annotations__)

# ---------------- Using Multiple Annotation Types ----------------
print("\n===== MULTIPLE ANNOTATION TYPES =====")

def student_info(name: str, age: int, marks: list) -> dict:
    return {
        "name": name,
        "age": age,
        "marks": marks
    }

print(student_info("John", 21, [85, 90, 88]))

# ---------------- Using Custom Types in Annotations ----------------
print("\n===== CUSTOM TYPES IN ANNOTATIONS =====")

class User:
    pass

def get_user() -> User:
    return User()

user = get_user()
print("User object returned:", user)

# ---------------- Using Any Annotation ----------------
print("\n===== USING 'Any' ANNOTATION =====")

from typing import Any

def print_value(value: Any) -> None:
    print("Value:", value)

print_value(100)
print_value("Python")
print_value([1, 2, 3])

# ---------------- Using Union Annotation ----------------
print("\n===== USING UNION ANNOTATION =====")

from typing import Union

def square(value: Union[int, float]) -> Union[int, float]:
    return value * value

print("Square int:", square(5))
print("Square float:", square(4.5))

# ---------------- Default Values with Annotations ----------------
print("\n===== DEFAULT VALUES WITH ANNOTATIONS =====")

def connect(host: str = "localhost", port: int = 3306) -> str:
    return f"Connected to {host}:{port}"

print(connect())
print(connect("example.com", 8080))

# ---------------- Annotations with *args and **kwargs ----------------
print("\n===== ANNOTATIONS WITH *args AND **kwargs =====")

def total(*numbers: int) -> int:
    return sum(numbers)

print("Total:", total(10, 20, 30))

def show_details(**info: str) -> None:
    for key, value in info.items():
        print(key, ":", value)

show_details(name="Alice", city="Mumbai")

# ---------------- Practical Example: Data Validator ----------------
print("\n===== PRACTICAL EXAMPLE: DATA PROCESSING FUNCTION =====")

def process_payment(amount: float, currency: str) -> bool:
    """
    Processes a payment request.

    Parameters:
    amount (float): Payment amount
    currency (str): Currency type

    Returns:
    bool: Payment success status
    """
    print(f"Processing payment of {amount} {currency}")
    return True

print("Payment status:", process_payment(1500.50, "INR"))

# ---------------- Combining Docstrings & Annotations ----------------
print("\n===== DOCSTRINGS + ANNOTATIONS TOGETHER =====")

def calculate_salary(basic: float, bonus: float) -> float:
    """
    Calculates total salary.

    Parameters:
    basic (float): Basic salary
    bonus (float): Bonus amount

    Returns:
    float: Total salary
    """
    return basic + bonus

print("Total Salary:", calculate_salary(30000, 5000))

print("\nAnnotations:")
print(calculate_salary.__annotations__)

print("\nDocstring:")
print(calculate_salary.__doc__)

# ---------------- Why Annotations Matter ----------------
print("\n===== WHY FUNCTION ANNOTATIONS MATTER =====")
print("""
✔ Make code self-explanatory
✔ Improve collaboration in teams
✔ Enable static type checkers (mypy, pyright)
✔ Improve IDE suggestions
✔ Prepare code for large systems

Annotations become critical in:
✔ APIs
✔ Libraries
✔ Frameworks
✔ Enterprise applications
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Function annotations describe parameters and return values
✔ They do NOT enforce types at runtime
✔ Annotations are stored in __annotations__
✔ 'Any' and 'Union' allow flexible typing
✔ Annotations work with defaults, *args, **kwargs
✔ Combined with docstrings, annotations create professional code

This marks the completion of the FUNCTIONS chapter.
You are now fully prepared for advanced Python topics.
""")
