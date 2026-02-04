# CLOSURES & DOCSTRINGS IN PYTHON
# ---------------------------------------------

print("\n===== BASIC CLOSURE =====")

def multiplier(factor):
    """Returns a function that multiplies a number by factor."""
    def multiply(num):
        return num * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print("Double of 5:", double(5))
print("Triple of 5:", triple(5))

print("\nEach returned function remembers its own 'factor' value.")

print("\n===== STATE PRESERVING CLOSURE =====")

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c1 = counter()
c2 = counter()

print("Counter 1:", c1())
print("Counter 1:", c1())
print("Counter 2:", c2())

print("\nEach closure maintains its own separate state.")

print("\n===== DOCSTRING EXAMPLE =====")

def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int): first number
    b (int): second number
    """
    return a + b

print("Addition result:", add(10, 20))

print("\nAccessing docstring using __doc__:")
print(add.__doc__)

print("\nUsing help() to view documentation:")
help(add)
