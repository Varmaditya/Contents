# FUNCTION ANNOTATIONS IN PYTHON
# ---------------------------------------------

print("\n===== BASIC FUNCTION ANNOTATION =====")

def greet(name: str) -> str:
    return "Hello " + name

print(greet("Alice"))

print("\n===== ANNOTATIONS ARE NOT ENFORCED =====")

def add(a: int, b: int) -> int:
    return a + b

print("With integers:", add(10, 20))
print("With strings:", add("Py", "thon"))

print("\n===== ACCESSING ANNOTATIONS =====")

def area(length: float, width: float) -> float:
    return length * width

print("Annotations:", area.__annotations__)

print("\n===== DEFAULT VALUES + ANNOTATIONS =====")

def connect(host: str = "localhost", port: int = 3306) -> str:
    return f"Connected to {host}:{port}"

print(connect())
print(connect("example.com", 8080))

print("\n===== *args ANNOTATION =====")

def total(*nums: int) -> int:
    return sum(nums)

print("Total:", total(10, 20, 30))

print("\n===== ANNOTATIONS + DOCSTRING =====")

def calculate_salary(basic: float, bonus: float) -> float:
    """
    Calculates total salary.
    """
    return basic + bonus

print("Salary:", calculate_salary(30000, 5000))
print("Annotations:", calculate_salary.__annotations__)
