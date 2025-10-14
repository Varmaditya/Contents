# Program: Identity Operators in Python

# ---------------- Introduction ----------------
print("\n===== IDENTITY OPERATORS IN PYTHON =====")

"""
Identity operators are used to compare the memory location of two objects.
Operators:
    'is'      → Returns True if both variables point to the same object
    'is not'  → Returns True if they point to different objects
Note:
    '==' compares values
    'is' compares object identity (memory address)
"""

# ---------------- Examples ----------------

# 1️⃣ Integers
a = 10
b = 10
print("a =", a, "b =", b)
print("a == b →", a == b)
print("a is b →", a is b)
print("a is not b →", a is not b)
print()

# 2️⃣ Strings
x = "hello"
y = "hello"
print("x =", x, "y =", y)
print("x == y →", x == y)
print("x is y →", x is y)  # True because strings are immutable and reused
print()

# 3️⃣ Lists (mutable objects)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 =", list1)
print("list2 =", list2)
print("list1 == list2 →", list1 == list2)  # same content
print("list1 is list2 →", list1 is list2)  # different objects in memory
print("list1 is not list2 →", list1 is not list2)
print()

# 4️⃣ None comparison
val = None
print("val is None →", val is None)
print("val is not None →", val is not None)
print()

# ---------------- Memory Example ----------------
print("===== MEMORY LOCATION CHECK =====")
num1 = 256
num2 = 256
num3 = 300
num4 = 300

print("id(num1):", id(num1))
print("id(num2):", id(num2))
print("id(num3):", id(num3))
print("id(num4):", id(num4))

print("num1 is num2 →", num1 is num2)
print("num3 is num4 →", num3 is num4)  # False (large ints not cached)
print()

print("""
Summary:
→ 'is' checks if both variables refer to the same object (same memory address).
→ '==' checks if both variables have the same value.
→ Use 'is' with None (val is None).
""")
