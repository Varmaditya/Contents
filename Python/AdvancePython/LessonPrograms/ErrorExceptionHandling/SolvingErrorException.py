# TRY, EXCEPT, ELSE, FINALLY IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== TRY, EXCEPT, ELSE, FINALLY =====")
print("""
In real-world programs, errors are common.

Instead of letting the program crash,
we handle errors using:

✔ try
✔ except
✔ else
✔ finally

This makes programs:
✔ Stable
✔ User-friendly
✔ Robust
""")

# ---------------- Basic try-except ----------------
print("\n===== BASIC try-except =====")
print("""
Problem:
User enters 0 → division by zero error
""")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except:
    print("Error occurred! Cannot divide by zero or invalid input.")

print("""
Program does not crash.
Error is handled gracefully.
""")

# ---------------- Handling Specific Exceptions ----------------
print("\n===== HANDLING SPECIFIC EXCEPTIONS =====")
print("""
Problem:
User enters invalid input or zero
""")

try:
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

# ---------------- Using else Block ----------------
print("\n===== USING else BLOCK =====")
print("""
else runs only if no exception occurs.
""")

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except Exception as e:
    print("Error:", e)
else:
    print("Success! Result:", result)

# ---------------- Using finally Block ----------------
print("\n===== USING finally BLOCK =====")
print("""
finally block always executes.
Used for cleanup operations.
""")

try:
    print("Opening file...")
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing resources (if any).")

# ---------------- Multiple Exceptions in One Block ----------------
print("\n===== MULTIPLE EXCEPTIONS =====")
print("""
Handling multiple errors in a single program.
""")

try:
    data = [10, 20, 30]
    index = int(input("Enter index: "))
    print("Value:", data[index])
except IndexError:
    print("Index out of range!")
except ValueError:
    print("Invalid input! Enter a number.")

# ---------------- Practical Problem 1 ----------------
print("\n===== PRACTICAL PROBLEM 1 =====")
print("""
Problem:
Take two numbers from user and divide them safely.
""")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter numbers.")

# ---------------- Practical Problem 2 ----------------
print("\n===== PRACTICAL PROBLEM 2 =====")
print("""
Problem:
Access element from list safely.
""")

numbers = [5, 10, 15]

try:
    index = int(input("Enter index (0-2): "))
    print("Element:", numbers[index])
except IndexError:
    print("Index out of range!")
except ValueError:
    print("Invalid input!")

# ---------------- Practical Problem 3 ----------------
print("\n===== PRACTICAL PROBLEM 3 =====")
print("""
Problem:
Open a file safely.
""")

try:
    filename = input("Enter file name: ")
    f = open(filename, "r")
    print("File opened successfully.")
except FileNotFoundError:
    print("File does not exist!")
finally:
    print("File operation attempted.")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ try block contains risky code
✔ except handles errors
✔ else runs if no error occurs
✔ finally always runs
✔ Specific exceptions are better than generic except
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ try-except prevents program crashes
✔ Handle specific exceptions for clarity
✔ else executes when no error occurs
✔ finally always executes
✔ Used in real-world systems for reliability

Now you can build programs that handle errors safely.
""")