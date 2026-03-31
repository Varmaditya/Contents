# MULTIPLE & CUSTOM EXCEPTION HANDLING
# ---------------------------------------------

print("\n===== MULTIPLE EXCEPTIONS =====")

try:
    a = int("10")
    b = int("0")
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")


print("\n===== MULTIPLE EXCEPTIONS IN ONE BLOCK =====")

try:
    data = [1, 2, 3]
    print(data[5])
except (IndexError, ValueError):
    print("Invalid index or value!")


print("\n===== USING raise =====")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

try:
    print(withdraw(5000, 7000))
except ValueError as e:
    print("Error:", e)


print("\n===== CUSTOM EXCEPTION =====")

class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18+")
    return "Access granted"

try:
    print(check_age(16))
except AgeError as e:
    print("Custom Error:", e)


print("\n===== ASSERTION =====")

def calculate_discount(price):
    assert price > 0, "Price must be positive!"
    return price * 0.9

try:
    print(calculate_discount(-50))
except AssertionError as e:
    print("Assertion Error:", e)
