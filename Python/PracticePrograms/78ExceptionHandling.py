# Program: Safe Divider (Exception Handling)
# Exception handling helps prevent program crashes when errors occur.

print("===== EXCEPTION HANDLING DEMO =====")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result =", a / b)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input, please enter numbers only.")

# Program continues smoothly even if error happens.
