# Program: Simple Calculator

print("===== SIMPLE CALCULATOR =====")

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid operator"

while(True):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    print("Result =", calculate(num1, num2, operator), "\n")
    quit = input("Do you want to exit? (y/n): ")
    if quit == "y": break
    print()
