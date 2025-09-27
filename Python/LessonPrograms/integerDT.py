# Integer Data Type

import sys

# Declaration
integer_number = 100

# Output
print("Integer value:", integer_number)

# Input (user entered number is converted to int)
user_integer = int(input("Enter an integer: "))
print("You entered integer:", user_integer)

# Type checking
print("Type of integer_number:", type(integer_number))

# Type casting
float_number = float(integer_number)
string_number = str(integer_number)
print("Integer to float:", float_number)
print("Integer to string:", string_number)

# Storage (memory size in bytes)
print("Memory size of integer_number:", sys.getsizeof(integer_number), "bytes")

# Integer has unlimited precision in Python (no fixed max limit)
big_integer = 10**100   # very large integer
print("Big integer:", big_integer)
print("Type of big_integer:", type(big_integer))
