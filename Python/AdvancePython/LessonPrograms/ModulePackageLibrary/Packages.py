# PACKAGES IN PYTHON
# ---------------------------------------------

print("\n===== PACKAGE CONCEPT =====")
print("A package = folder of modules")


print("\n===== IMPORTING FROM PACKAGE =====")

print("from utils.math_utils import add")
print("OR")
print("import utils.math_utils")


print("\n===== USING IMPORTED FUNCTION =====")

# Simulating usage
def add(a, b):
    return a + b

print("Addition:", add(2, 3))


print("\n===== WHY PACKAGES =====")
print("""
✔ Organize code
✔ Group related modules
✔ Avoid confusion
""")


print("\n===== PROJECT STRUCTURE =====")
print("""
project/
    main.py
    utils/
        math_utils.py
        file_utils.py
""")