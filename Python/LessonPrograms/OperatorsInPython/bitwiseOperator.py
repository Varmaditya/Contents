# Bitwise Operators in Python

# ---------------- Introduction ----------------
print("\n===== BITWISE OPERATORS IN PYTHON =====")

print("""
Bitwise operators are used to perform operations at the binary (bit) level.
They only work on integers.
Each bit (0 or 1) of the number is compared or shifted according to the operator.
""")

# ---------------- Variable Declaration ----------------
a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("Values used:")
print("a =", a, "→ Binary:", format(a, '04b'))
print("b =", b, "→ Binary:", format(b, '04b'))
print("\n-------------------------------------------\n")

# 1️⃣ Bitwise AND (&)
print("1. Bitwise AND (&)")
print("   Operation: 0101 & 0011")
result = a & b
print("   Result Binary:", format(result, '04b'), "→ Decimal:", result)
print("   Explanation: Only bits that are 1 in BOTH numbers remain 1.\n")

# 2️⃣ Bitwise OR (|)
print("2. Bitwise OR (|)")
print("   Operation: 0101 | 0011")
result = a | b
print("   Result Binary:", format(result, '04b'), "→ Decimal:", result)
print("   Explanation: Bits that are 1 in ANY number become 1.\n")

# 3️⃣ Bitwise XOR (^)
print("3. Bitwise XOR (^)")
print("   Operation: 0101 ^ 0011")
result = a ^ b
print("   Result Binary:", format(result, '04b'), "→ Decimal:", result)
print("   Explanation: Bits that are DIFFERENT become 1.\n")

# 4️⃣ Bitwise NOT (~)
print("4. Bitwise NOT (~)")
print("   Operation: ~0101")
result = ~a
print("   Result Binary:", format(result & 0xff, '08b'), "→ Decimal:", result)
print("   Explanation: Inverts bits (1→0 and 0→1). Note: Result is negative due to 2’s complement.\n")

# 5️⃣ Bitwise Left Shift (<<)
print("5. Bitwise Left Shift (<<)")
print("   Operation: 0101 << 1")
result = a << 1
print("   Result Binary:", format(result, '04b'), "→ Decimal:", result)
print("   Explanation: Shifts bits left by 1 place (adds a 0 on the right).\n")

# 6️⃣ Bitwise Right Shift (>>)
print("6. Bitwise Right Shift (>>)")
print("   Operation: 0101 >> 1")
result = a >> 1
print("   Result Binary:", format(result, '04b'), "→ Decimal:", result)
print("   Explanation: Shifts bits right by 1 place (drops the rightmost bit).\n")

# ---------------- Input Example ----------------
print("===== USER INPUT EXAMPLE =====")
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

print("\nBitwise Results:")
print(f"{x} & {y} = {x & y}")
print(f"{x} | {y} = {x | y}")
print(f"{x} ^ {y} = {x ^ y}")
print(f"~{x} = {~x}")
print(f"{x} << 1 = {x << 1}")
print(f"{x} >> 1 = {x >> 1}")

# ---------------- Summary ----------------
print("""
Summary:
→ Bitwise operators work on binary representation of integers.
→ They are faster and used in low-level programming, graphics, networking, etc.

List of Bitwise Operators:
&   → AND
|   → OR
^   → XOR
~   → NOT
<<  → Left Shift
>>  → Right Shift
""")
