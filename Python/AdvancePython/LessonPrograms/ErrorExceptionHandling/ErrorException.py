# ERROR HANDLING & EXCEPTIONS IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== ERROR HANDLING & EXCEPTIONS =====")
print("""
Error Handling is the process of managing errors
so that programs do not crash unexpectedly.

An Exception is an error that occurs
during the execution of a program.

In real-world applications:
Errors are unavoidable.

Users can:
✔ Enter wrong input
✔ Access missing files
✔ Use invalid data

So instead of stopping the program,
we need a way to handle such situations.
""")

# ---------------- What is an Error ----------------
print("\n===== WHAT IS AN ERROR =====")
print("""
An error is any problem in a program
that prevents it from running correctly.

Errors can:
✔ Stop the program
✔ Produce incorrect output
✔ Crash the application
""")

# ---------------- Types of Errors ----------------
print("\n===== TYPES OF ERRORS =====")
print("""
There are mainly three types of errors:

1️⃣ Compile-Time Errors (Syntax Errors)
   - Errors in code structure
   - Detected before execution
   - Program will not run

2️⃣ Runtime Errors (Exceptions)
   - Occur during program execution
   - Program crashes while running

3️⃣ Logical Errors
   - Program runs successfully
   - But produces incorrect output
""")

# ---------------- Compile-Time Error Example ----------------
print("\n===== COMPILE-TIME (SYNTAX) ERROR EXAMPLE =====")
print("""
Example:
Missing colon in if statement

if True
    print("Hello")

This causes a SyntaxError.
Program will not execute.
""")

# ---------------- Runtime Error Example ----------------
print("\n===== RUNTIME ERROR (EXCEPTION) EXAMPLE =====")
print("""
Example:
Division by zero

print(10 / 0)

This causes:
ZeroDivisionError

Program crashes during execution.
""")

# ---------------- Logical Error Example ----------------
print("\n===== LOGICAL ERROR EXAMPLE =====")
print("""
Example:
Incorrect formula

def calculate_area(radius):
    return 2 * 3.14 * radius   # Wrong formula

Program runs successfully,
but gives incorrect result.
""")

# ---------------- What is an Exception ----------------
print("\n===== WHAT IS AN EXCEPTION =====")
print("""
An Exception is a runtime error
that occurs while the program is running.

It disrupts normal flow of the program.

Examples of common exceptions:
✔ ZeroDivisionError
✔ ValueError
✔ TypeError
✔ IndexError
✔ KeyError
✔ FileNotFoundError
""")

# ---------------- Examples of Exceptions ----------------
print("\n===== EXAMPLES OF EXCEPTIONS =====")

print("\n--- ZeroDivisionError ---")
print("10 / 0  → Division by zero")

print("\n--- ValueError ---")
print("int('abc') → Invalid conversion")

print("\n--- TypeError ---")
print("'2' + 3 → Invalid operation between types")

print("\n--- IndexError ---")
print("[1, 2, 3][5] → Index out of range")

print("\n--- KeyError ---")
print("{'a':1}['b'] → Key does not exist")

print("\n--- FileNotFoundError ---")
print("open('file.txt') → File not found")

# ---------------- Why Error Handling is Needed ----------------
print("\n===== WHY ERROR HANDLING IS NEEDED =====")
print("""
Without error handling:
✔ Program crashes immediately
✔ User gets no useful information
✔ System becomes unreliable

With proper handling:
✔ Program continues running
✔ User gets meaningful messages
✔ System becomes robust and user-friendly
""")

# ---------------- Real-World Examples ----------------
print("\n===== REAL-WORLD EXAMPLES =====")
print("""
1️⃣ ATM Machine
   - Wrong PIN entered
   - System should not crash
   - Should show: "Invalid PIN"

2️⃣ Login System
   - User enters wrong password
   - System should respond gracefully

3️⃣ File Processing System
   - File may not exist
   - System should handle missing file

4️⃣ E-commerce Website
   - Payment failure
   - System should not crash
   - Should show error message

5️⃣ Data Entry Forms
   - User enters text instead of number
   - System must validate input
""")

# ---------------- What Happens Without Handling ----------------
print("\n===== WITHOUT ERROR HANDLING =====")
print("""
Imagine a banking system crashes
just because of wrong input.

This leads to:
✔ Poor user experience
✔ Data loss
✔ System failure

Hence, handling errors is critical.
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Errors are problems in a program
✔ Compile-time errors stop execution before running
✔ Runtime errors (exceptions) occur during execution
✔ Logical errors give wrong results
✔ Errors can crash programs
✔ Real-world systems must handle errors
✔ Error handling improves reliability

Next chapter:
✔ try-except
✔ Handling multiple exceptions
✔ finally block
✔ Raising exceptions
""")