# DECORATORS IN PYTHON
# ---------------------------------------------

print("\n===== BASIC DECORATOR =====")

def log_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@log_decorator
def greet():
    print("Hello!")

greet()


print("\n===== DECORATOR WITH ARGUMENTS =====")

def arg_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        return func(*args, **kwargs)
    return wrapper

@arg_decorator
def add(a, b):
    return a + b

print("Result:", add(5, 10))


print("\n===== DECORATOR WITH PARAMETERS =====")

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(2)
def say_hi():
    print("Hi!")

say_hi()


print("\n===== USING wraps (BEST PRACTICE) =====")

from functools import wraps

def safe_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@safe_decorator
def sample():
    """Sample function"""
    return "Done"

print("Function Name:", sample.__name__)
print("Doc:", sample.__doc__)
