# Assignment Operators in Python

# ---------------- Introduction ----------------
print("\n===== ASSIGNMENT OPERATORS IN PYTHON =====")

print("""
Assignment operators are used to assign values to variables.
Some operators combine arithmetic or bitwise operations with assignment.
They help write shorter and cleaner code.
""")

# ---------------- Simple Assignment ----------------
a = 10
print("Initial value assigned: a =", a)

# ---------------- Compound Assignments ----------------
print("\n===== ARITHMETIC ASSIGNMENT OPERATORS =====")

# Addition assignment
a += 5
print("After 'a += 5'  → a =", a)

# Subtraction assignment
a -= 3
print("After 'a -= 3'  → a =", a)

# Multiplication assignment
a *= 2
print("After 'a *= 2'  → a =", a)

# Division assignment
a /= 4
print("After 'a /= 4'  → a =", a)

# Modulus assignment
a %= 3
print("After 'a %= 3'  → a =", a)

# Floor Division assignment
a = 10
a //= 3
print("After 'a //= 3' → a =", a)

# Exponent assignment
a **= 2
print("After 'a **= 2' → a =", a)

# ---------------- Bitwise Assignment Operators ----------------
print("\n===== BITWISE ASSIGNMENT OPERATORS =====")
a = 5  # (binary: 0101)
print("Initial a =", a)

a &= 3   # (0101 & 0011 = 0001)
print("After 'a &= 3'  → a =", a)

a |= 2   # (0001 | 0010 = 0011)
print("After 'a |= 2'  → a =", a)

a ^= 1   # (0011 ^ 0001 = 0010)
print("After 'a ^= 1'  → a =", a)

a <<= 1  # (left shift: 0010 << 1 = 0100)
print("After 'a <<= 1' → a =", a)

a >>= 2  # (right shift: 0100 >> 2 = 0001)
print("After 'a >>= 2' → a =", a)

# ---------------- Example with User Input ----------------
print("\n===== USER INPUT EXAMPLE =====")
x = int(input("Enter a number: "))
print("You entered:", x)

x += 10
print("After adding 10 using 'x += 10' →", x)

x *= 2
print("After multiplying by 2 using 'x *= 2' →", x)

x //= 5
print("After floor dividing by 5 using 'x //= 5' →", x)

# ---------------- Summary ----------------
print("""
Summary:
1. '='   is simple assignment.
2. '+='  '-='  '*='  '/='  are arithmetic assignment operators.
3. '%='  '//='  '**=' perform modulus, floor division, and power assignments.
4. '&='  '|='  '^='  '<<='  '>>=' are bitwise assignment operators.

They help reduce code length.
Example:
    a = a + 5   →   a += 5
""")
