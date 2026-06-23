# Program: Smart Calculator

def calculate(a: float, b: float, operation: str) -> float:
    """Performs calculation based on operation"""

    def add():
        return a + b

    def subtract():
        return a - b

    def multiply():
        return a * b

    def divide():
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if operation in operations:
        return operations[operation]()
    else:
        return "Invalid operation"


while True:
    print("\n=== Smart Calculator ===")
    print("1. Calculate")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        result = calculate(a, b, op)
        print("Result:", result)

    elif choice == "2":
        break

    else:
        print("Invalid choice!")