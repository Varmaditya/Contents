# ERROR HANDLING & EXCEPTIONS (INTRODUCTION)
# ---------------------------------------------

print("\n===== SYNTAX ERROR =====")

# Syntax Error Example (commented to avoid crash)
print("Example: if True print('Hello')")
print("Reason: Missing colon → SyntaxError")


print("\n===== RUNTIME ERRORS (EXCEPTIONS) =====")

# Examples (not executed to prevent crash)
print("ZeroDivisionError → 10 / 0")
print("ValueError → int('abc')")
print("TypeError → '2' + 3")
print("IndexError → [1, 2, 3][5]")
print("KeyError → {'a':1}['b']")
print("FileNotFoundError → open('file.txt')")


print("\n===== ACTUAL RUNTIME ERROR (COMMENTED) =====")

# Uncomment to see crash
# print(10 / 0)


print("\n===== LOGICAL ERROR =====")

def calculate_area(radius):
    return 2 * 3.14 * radius   # Wrong formula

print("Incorrect Area for radius 5:", calculate_area(5))


print("\n===== REAL-WORLD SCENARIOS =====")

print("1. ATM → Wrong PIN entered")
print("2. Login → Wrong password")
print("3. File System → File not found")
print("4. Input → Text instead of number")


print("\n===== PROGRAM BEHAVIOR =====")

print("""
✔ Syntax errors → Program does not start
✔ Runtime errors → Program crashes during execution
✔ Logical errors → Program runs but gives wrong result
✔ Errors are common in real-world systems
""")
