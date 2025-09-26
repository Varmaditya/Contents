# String Data Type

import sys

# Single-line string declaration
string_text = "Hello, Python!"
print("Single-line string value:", string_text)

# Multi-line string declaration
multi_line_string = """This is a
multi-line string example.
It can span multiple lines."""
print("\nMulti-line string value:\n", multi_line_string)

# Input
user_string = input("\nEnter a string: ")
print("You entered string:", user_string)

# Type checking
print("\nType of string_text:", type(string_text))
print("Type of multi_line_string:", type(multi_line_string))
print("Type of user_string:", type(user_string))

# Type casting
string_from_int = str(123)
string_from_float = str(45.67)
print("\nString from int:", string_from_int)
print("String from float:", string_from_float)

# Storage (memory size in bytes)
print("\nMemory size of string_text:", sys.getsizeof(string_text), "bytes")
print("Memory size of multi_line_string:", sys.getsizeof(multi_line_string), "bytes")
