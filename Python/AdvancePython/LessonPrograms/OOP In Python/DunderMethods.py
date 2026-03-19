# COMMON DUNDER (MAGIC) METHODS IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== COMMON DUNDER (MAGIC) METHODS =====")
print("""
Dunder methods (Double UNDERSCORE methods)
are special methods in Python.

They start and end with double underscores:
Example:
__init__, __str__, __repr__, __len__, __add__, etc.

They are also called Magic Methods.

These methods allow objects to:
✔ Customize built-in behavior
✔ Work with operators (+, -, len, print)
✔ Define object representation
""")

# ---------------- __init__ ----------------
print("\n===== __init__ METHOD =====")
print("""
__init__ is a constructor.
It runs automatically when an object is created.
It initializes object attributes.
""")

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Aditya")
print("Person Name:", p.name)

# ---------------- __str__ ----------------
print("\n===== __str__ METHOD =====")
print("""
__str__ defines what is printed
when we use print(object).
""")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

s = Student("Ravi", 85)
print(s)

# ---------------- __repr__ ----------------
print("\n===== __repr__ METHOD =====")
print("""
__repr__ provides official string representation.
Used mainly for debugging.
""")

class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book('{self.title}')"

b = Book("Python Basics")
print(b)

# ---------------- __len__ ----------------
print("\n===== __len__ METHOD =====")
print("""
__len__ allows object to work with len().
""")

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

playlist = Playlist(["Song1", "Song2", "Song3"])
print("Number of songs:", len(playlist))

# ---------------- __add__ ----------------
print("\n===== __add__ METHOD =====")
print("""
__add__ allows objects to use + operator.
""")

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

n1 = Number(10)
n2 = Number(20)
result = n1 + n2

print("Addition Result:", result)

# ---------------- __eq__ ----------------
print("\n===== __eq__ METHOD =====")
print("""
__eq__ defines behavior of == operator.
""")

class User:
    def __init__(self, username):
        self.username = username

    def __eq__(self, other):
        return self.username == other.username

u1 = User("admin")
u2 = User("admin")

print("Are users equal?", u1 == u2)

# ---------------- __call__ ----------------
print("\n===== __call__ METHOD =====")
print("""
__call__ allows an object to be called like a function.
""")

class Greeter:
    def __init__(self, message):
        self.message = message

    def __call__(self, name):
        print(self.message, name)

g = Greeter("Hello")
g("Aditya")

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __add__(self, item):
        self.items.append(item)
        return self

    def __str__(self):
        return f"Cart Items: {self.items}"

cart = ShoppingCart()
cart + "Laptop"
cart + "Mouse"

print(cart)
print("Total Items:", len(cart))

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Dunder methods customize object behavior
✔ They integrate objects with Python built-ins
✔ Used heavily in frameworks and libraries
✔ Important for advanced OOP design
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ __init__ initializes object
✔ __str__ controls print()
✔ __repr__ controls official representation
✔ __len__ enables len()
✔ __add__ enables + operator
✔ __eq__ enables == comparison
✔ __call__ allows object to behave like function

Dunder methods make objects powerful
and integrate them with Python language features.
""")
