# Python Program: Data types
import sys

# Integer
integer_var = 10
print("Integer value:", integer_var, " Type:", type(integer_var))

# Float
float_var = 3.14
print("Float value:", float_var, " Type:", type(float_var))

# Complex
complex_var = 2 + 5j
print("Complex value:", complex_var, " Type:", type(complex_var))

# String
string_var = "Hello Python"
print("String value:", string_var, " Type:", type(string_var))

# Boolean
bool_var = True
print("Boolean value:", bool_var, " Type:", type(bool_var))

# NoneType
none_var = None
print("None value:", none_var, " Type:", type(none_var))

# List
list_var = [1, 2, 3]
print("List value:", list_var, " Type:", type(list_var))

# Tuple
tuple_var = (1, 2, 3)
print("Tuple value:", tuple_var, " Type:", type(tuple_var))

# Set
set_var = {1, 2, 3}
print("Set value:", set_var, " Type:", type(set_var))

# Dictionary
dict_var = {"one": 1, "two": 2}
print("Dictionary value:", dict_var, " Type:", type(dict_var))


#--------------Extras--------------------#
#The order by “smallest to largest” in memory terms generally looks like:
#None < Bool < Int < Float < Complex < String
# Data Types: Storage Size and Limits

print("----- Data Types in Python (Smallest to Largest) -----\n")

# Boolean
print("Storage:", sys.getsizeof(bool_var), "bytes")
print("Range: Only True / False\n")

# Integer
print("Storage:", sys.getsizeof(int_var), "bytes")
print("Range: Unlimited (only limited by memory)\n")

# Float
print("Storage:", sys.getsizeof(float_var), "bytes")
print("Range:", sys.float_info.min, "to", sys.float_info.max, "\n")

# Complex
print("Storage:", sys.getsizeof(complex_var), "bytes")
print("Range: No fixed limit for real/imag parts (they are floats)\n")

# String
print("Storage:", sys.getsizeof(string_var), "bytes")
print("Range: Depends on length of string (no fixed max size)\n")

# None
print("Storage:", sys.getsizeof(none_var), "bytes")
print("Range: Represents no value\n")
