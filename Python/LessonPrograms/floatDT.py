# Float Data Type

import sys

# Declaration
float_number = 12.75

# Output
print("Float value:", float_number)

# Input
user_float = float(input("Enter a decimal number: "))
print("You entered float:", user_float)

# Type checking
print("Type of float_number:", type(float_number))

# Type casting
int_number = int(float_number)       # loses decimal part
string_number = str(float_number)
print("Float to int:", int_number)
print("Float to string:", string_number)

# Storage
print("Memory size of float_number:", sys.getsizeof(float_number), "bytes")

# Limit (uses double precision internally)
import sys
print("Max float value (sys.float_info.max):", sys.float_info.max)
