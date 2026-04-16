# MODULES IN PYTHON
# ---------------------------------------------

print("\n===== USING MODULE =====")

import math
print("Square root:", math.sqrt(16))


print("\n===== DIFFERENT IMPORT STYLES =====")

from math import sqrt
print("From import:", sqrt(25))

import math as m
print("Alias:", m.pi)


print("\n===== MULTIPLE IMPORT =====")

from math import sqrt, pi
print("Values:", sqrt(36), pi)


print("\n===== CUSTOM MODULE (CONCEPT) =====")
print("import calculator → calculator.add(2, 3)")


print("\n===== __name__ DEMO =====")

def test():
    print("Test function executed")

if __name__ == "__main__":
    print("Running directly")
    test()