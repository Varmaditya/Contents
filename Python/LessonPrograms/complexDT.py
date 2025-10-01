# Python Program: Complex Data Type

import sys

# Declaration
complex_number = 3 + 4j

# Output
print("Complex value:", complex_number)

# Input
user_complex = complex(input("Enter a complex number (example: 2+3j): "))
print("You entered complex number:", user_complex)

# Type checking
print("Type of complex_number:", type(complex_number))

# Type casting
complex_from_int = complex(5)
complex_from_float = complex(2.5)
print("Complex from int:", complex_from_int)
print("Complex from float:", complex_from_float)

# Storage
print("Memory size of complex_number:", sys.getsizeof(complex_number), "bytes")
