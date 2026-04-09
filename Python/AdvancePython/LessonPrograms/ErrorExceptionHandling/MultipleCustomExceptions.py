# MULTIPLE EXCEPTIONS, raise, CUSTOM EXCEPTIONS & ASSERTIONS
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== ADVANCED ERROR HANDLING =====")
print("""
In this chapter we will learn:

✔ Handling multiple exceptions
✔ Raising exceptions manually (raise)
✔ Creating custom exceptions
✔ Using assertions for validation

These concepts help in:
✔ Writing robust programs
✔ Validating inputs
✔ Controlling program flow
✔ Designing real-world systems
""")

# ---------------- Multiple Exceptions ----------------
print("\n===== MULTIPLE EXCEPTIONS =====")
print("""
We can handle multiple exceptions
in a single program.
""")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter numbers.")

print("""
Different errors are handled separately.
""")

# ---------------- Multiple Exceptions in Single Block ----------------
print("\n===== MULTIPLE EXCEPTIONS IN SINGLE BLOCK =====")
print("""
We can also handle multiple exceptions together.
""")

try:
    data = [1, 2, 3]
    index = int(input("Enter index: "))
    print("Value:", data[index])
except (IndexError, ValueError):
    print("Invalid input or index!")

# ---------------- Using raise ----------------
print("\n===== USING raise KEYWORD =====")
print("""
raise is used to manually trigger an exception.
""")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

try:
    print("Remaining Balance:", withdraw(5000, 7000))
except ValueError as e:
    print("Error:", e)

# ---------------- Custom Exceptions ----------------
print("\n===== CUSTOM EXCEPTIONS =====")
print("""
We can create our own exception classes
by inheriting from Exception.
""")

class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above!")
    print("Access granted")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except AgeError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Invalid input!")

print("""
Custom exceptions improve readability
and domain-specific error handling.
""")

# ---------------- Assertions ----------------
print("\n===== ASSERTIONS =====")
print("""
Assertions are used for debugging.

Syntax:
assert condition, message

If condition is False:
AssertionError is raised.
""")

def calculate_discount(price):
    assert price > 0, "Price must be positive!"
    return price * 0.9

try:
    print("Discounted Price:", calculate_discount(100))
    print("Discounted Price:", calculate_discount(-50))
except AssertionError as e:
    print("Assertion Error:", e)

print("""
Assertions are mainly used during development,
not for user-facing error handling.
""")

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

class InsufficientBalanceError(Exception):
    pass

def transfer_money(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive!")
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance!")
    return balance - amount

try:
    balance = 5000
    amount = int(input("Enter amount to transfer: "))
    balance = transfer_money(balance, amount)
    print("Transfer successful. Remaining balance:", balance)
except InsufficientBalanceError as e:
    print("Transaction Error:", e)
except ValueError as e:
    print("Input Error:", e)

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Use specific exceptions for clarity
✔ raise allows manual error generation
✔ Custom exceptions improve code design
✔ Assertions help in debugging
✔ Do not overuse assertions in production
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Multiple exceptions handle different errors
✔ raise is used to trigger exceptions manually
✔ Custom exceptions define domain-specific errors
✔ Assertions validate assumptions during development

These concepts are essential for:
✔ Real-world applications
✔ API design
✔ Data validation
✔ System reliability
""")