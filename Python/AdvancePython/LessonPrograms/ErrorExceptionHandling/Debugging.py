# DEBUGGING IN PYTHON (INTRODUCTION)
# ---------------------------------------------

print("\n===== LOGICAL BUG =====")

def area_of_circle(radius):
    return 2 * 3.14 * radius   # Wrong formula

print("Incorrect Area:", area_of_circle(5))


print("\n===== DEBUGGING USING PRINT =====")

def find_average(numbers):
    total = 0
    for num in numbers:
        print("Adding:", num)   # trace step
        total += num
    print("Total:", total)
    return total / len(numbers)

print("Average:", find_average([10, 20, 30]))


print("\n===== DEBUGGING DATA TYPES =====")

value = "10"
print("Value:", value)
print("Type:", type(value))


print("\n===== TYPE MISMATCH BUG =====")

a = 5
b = "5"

print("Type of a:", type(a))
print("Type of b:", type(b))
# print(a + b)  # TypeError


print("\n===== STEP-BY-STEP DEBUGGING =====")

def calculate_discount(price):
    print("Price:", price)
    discount = price * 0.1
    print("Discount:", discount)
    final = price - discount
    print("Final:", final)
    return final

print("Result:", calculate_discount(100))


print("\n===== DEBUGGER (pdb) =====")

print("""
Example usage:

import pdb

def test():
    x = 10
    pdb.set_trace()
    y = x + 5
    print(y)
""")
