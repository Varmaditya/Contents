# COMMON DUNDER (MAGIC) METHODS IN PYTHON
# ---------------------------------------------

print("\n===== DUNDER METHODS DEMO =====")

class Product:

    # Constructor → Initializes object attributes
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Controls what print(object) displays
    def __str__(self):
        return f"{self.name} costs ₹{self.price}"

    # Official representation (used for debugging)
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    # Enables + operator between objects
    def __add__(self, other):
        return Product(self.name + " & " + other.name,
                       self.price + other.price)

    # Enables == comparison between objects
    def __eq__(self, other):
        return self.price == other.price

    # Enables len(object)
    def __len__(self):
        return len(self.name)

    # Makes object callable like a function
    def __call__(self, discount):
        return self.price - discount


# Creating objects
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 2000)

print("\n__str__ →", p1)
print("__repr__ →", repr(p1))

print("\n__add__ →", p1 + p2)

print("\n__eq__ →", p1 == p2)

print("\n__len__ → Length of product name:", len(p1))

print("\n__call__ → Price after discount:", p1(5000))