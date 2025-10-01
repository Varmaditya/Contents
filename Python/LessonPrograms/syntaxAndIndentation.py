# Python Syntax & Indentation
# This program explains the rules of syntax and indentation in Python

# ---------------- BASIC SYNTAX ----------------
# Python programs are written using statements.
# Each statement usually goes on a new line.

print("Hello, World!")   # Example of a simple Python statement

# Multiple statements can be written on the same line using ;
x = 10; y = 20; print("x:", x, "y:", y)

# ---------------- INDENTATION ----------------
# Indentation (spaces at the beginning of a line) defines code blocks in Python.
# Unlike other languages (C, Java) that use { }, Python uses indentation.

age = 18
if age >= 18:   # Correct indentation
    print("\nYou are an adult.")    # 4 spaces indentation
    print("You can vote.")
else:
    print("You are a minor.")

# ❌ Wrong indentation (would cause an IndentationError if uncommented):
# if age >= 18:
# print("This will cause an error")

# ---------------- INDENTATION LEVELS ----------------
# Nested blocks require extra indentation
number = 10
if number > 0:
    print("\nNumber is positive")
    if number % 2 == 0:
        print("It is also even")  # More indentation for nested block
    else:
        print("It is odd")
else:
    print("Number is negative")

# ---------------- INDENTATION CONSISTENCY ----------------
# Always use the SAME number of spaces (PEP 8 recommends 4).
# Mixing tabs and spaces causes errors.

# ---------------- COMMENTS ----------------
# Single-line comment using #
"""
This is a multi-line comment
written inside triple quotes.
"""

# ---------------- LINE CONTINUATION ----------------
# If a statement is too long, use \ to continue on next line
long_variable_name = 100 + 200 + 300 + \
                     400 + 500
print("\nLine continuation result:", long_variable_name)

# Parentheses, brackets, and braces allow implicit line continuation
numbers = [
    1, 2, 3,
    4, 5, 6
]
print("Numbers list:", numbers)

# ---------------- WHITESPACE IMPORTANCE ----------------
# Extra spaces around operators or inside brackets don't affect execution
value = ( 1 + 2 )
print("\nExtra spaces example:", value)

# ---------------- EMPTY BLOCK ----------------
# If you want an empty block, use 'pass' (placeholder statement)
print("\nUsing pass for empty block:")
if True:
    pass  # does nothing, prevents error for empty block

# ---------------- INDENTATION SUMMARY ----------------
# 1. Indentation defines code blocks
# 2. Standard is 4 spaces
# 3. Consistency is important (tabs vs spaces)
# 4. Nested blocks need extra indentation
