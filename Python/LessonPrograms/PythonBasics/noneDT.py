# Python Program: None Data Type

import sys

# ---------------- Declaration ----------------
empty_value = None   # Assigning None

# ---------------- Output ----------------
print("Value of empty_value:", empty_value)

# ---------------- Type Checking ----------------
print("Type of empty_value:", type(empty_value))

# ---------------- Comparison ----------------
# None is often used in checks
if empty_value is None:
    print("empty_value has no value (it's None)")

# ---------------- Input Example ----------------
# Note: Input from user always returns string, not None
# But we can demonstrate assigning None manually
user_input = input("Enter something (leave blank for None): ")
if user_input == "":
    user_value = None
else:
    user_value = user_input
print("You entered:", user_value, "| Type:", type(user_value))

# ---------------- Storage ----------------
print("Memory size of empty_value:", sys.getsizeof(empty_value), "bytes")
