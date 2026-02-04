# NESTED FUNCTIONS & FUNCTIONS AS FIRST-CLASS OBJECTS
# ---------------------------------------------------

print("\n===== NESTED FUNCTIONS =====")

def outer():
    message = "Hello"

    def inner():
        print("Inner says:", message)

    inner()

outer()

print("\n===== RETURNING A NESTED FUNCTION =====")

def multiplier(factor):
    def multiply(num):
        return num * factor
    return multiply

double = multiplier(2)
print("Double of 5:", double(5))

print("\n===== FUNCTIONS AS FIRST-CLASS OBJECTS =====")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Assigning function to variable
operation = add
print("Using variable:", operation(10, 5))

# Passing function as argument
def calculate(x, y, func):
    return func(x, y)

print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subtract))

# Returning function based on condition
def select_operation(choice):
    if choice == "add":
        return add
    else:
        return subtract

func = select_operation("sub")
print("Selected operation:", func(20, 8))
