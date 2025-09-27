# Python Variables Demo
# This program shows how variables work in Python
# Only basics: declaration, naming rules, reassignment, and output

# Rule 1: Variables store data values
name = "Alice"
age = 21
height = 5.4

print("Name:", name)
print("Age:", age)
print("Height:", height)

# Rule 2: Variables can be reassigned (no need to declare type explicitly)
age = 22   # changed from 21
print("\nAfter reassignment, Age:", age)

# Rule 3: Variable names must start with a letter or underscore
_valid_name = "This is valid"
print("\nValid variable name example:", _valid_name)

# Rule 4: Variable names cannot start with a number or use special symbols
# ❌ 2name = "Not allowed"
# ❌ my-name = "Not allowed"
# ✔ my_name = "Allowed"
my_name = "Alice Smith"
print("Variable with underscore:", my_name)

# Rule 5: Variables are case-sensitive
city = "Mumbai"
City = "Delhi"
print("\ncity:", city)
print("City:", City)

# Rule 6: Multiple variables can be declared in one line
x, y, z = 10, 20, 30
print("\nMultiple variables -> x:", x, " y:", y, " z:", z)

# Rule 7: Same value to multiple variables
a = b = c = "Python"
print("Same value assigned -> a:", a, " b:", b, " c:", c)
