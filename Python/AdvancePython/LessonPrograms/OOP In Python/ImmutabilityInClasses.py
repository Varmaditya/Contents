# IMMUTABILITY IN CLASSES IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== IMMUTABILITY IN CLASSES =====")
print("""
Immutability means:
An object cannot be changed after it is created.

Immutable built-in types:
✔ int
✔ float
✔ str
✔ tuple

In OOP, we can design our own
immutable classes to prevent modification
after object creation.

Immutability helps in:
✔ Data safety
✔ Thread safety
✔ Predictable behavior
✔ Avoiding accidental changes
""")

# ---------------- Mutable Class Example ----------------
print("\n===== MUTABLE CLASS EXAMPLE =====")
print("""
By default, class objects are mutable.
Their attributes can be modified.
""")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Aditya", 21)

print("Before modification:", p.name, p.age)

p.age = 25   # modifying attribute

print("After modification:", p.name, p.age)

print("""
Attributes were modified successfully.
This class is mutable.
""")

# ---------------- Creating Immutable Class Using Private Attributes ----------------
print("\n===== IMMUTABLE CLASS USING PRIVATE ATTRIBUTES =====")
print("""
We can make attributes private
and provide only getter methods.
""")

class ImmutablePerson:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

ip = ImmutablePerson("Sneha", 22)

print("Name:", ip.get_name())
print("Age:", ip.get_age())

# ip.__age = 30   # Direct modification not allowed

print("""
Private attributes cannot be accessed directly.
Only getter methods are provided.
""")

# ---------------- Preventing Attribute Modification Using __setattr__ ----------------
print("\n===== IMMUTABILITY USING __setattr__ =====")
print("""
We can override __setattr__ to block
attribute changes after initialization.
""")

class FrozenPerson:
    def __init__(self, name, age):
        super().__setattr__("name", name)
        super().__setattr__("age", age)

    def __setattr__(self, key, value):
        raise AttributeError("Object is immutable")

fp = FrozenPerson("Ravi", 30)

print("Name:", fp.name)
print("Age:", fp.age)

# fp.age = 35   # This would raise an error

print("""
Attempting to modify attribute
will raise an AttributeError.
""")

# ---------------- Using Dataclass for Immutability ----------------
print("\n===== IMMUTABLE DATACLASS =====")
print("""
Dataclasses provide built-in support
for immutability using frozen=True.
""")

from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    name: str
    marks: int

student = Student("Arjun", 90)

print("Student:", student)

# student.marks = 95   # This would raise an error

print("""
frozen=True prevents modification
of attributes after creation.
""")

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

class BankAccount:
    def __init__(self, account_number, balance):
        super().__setattr__("account_number", account_number)
        super().__setattr__("balance", balance)

    def __setattr__(self, key, value):
        raise AttributeError("BankAccount object is immutable")

account = BankAccount("ACC123", 10000)

print("Account Number:", account.account_number)
print("Balance:", account.balance)

print("""
Bank account details cannot be modified.
This ensures financial data safety.
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Immutable objects cannot be changed after creation
✔ Normal classes are mutable by default
✔ Private attributes + getters improve safety
✔ Overriding __setattr__ enforces immutability
✔ Dataclass with frozen=True creates immutable class
✔ Immutability improves data integrity and safety

Immutability is useful in:
✔ Financial systems
✔ Configuration objects
✔ Thread-safe applications
✔ Large-scale system design
""")
