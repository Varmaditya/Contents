# INTERFACES, ABSTRACT BASE CLASSES & DATACLASSES IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== INTERFACES, ABSTRACT BASE CLASSES & DATACLASSES =====")
print("""
In this chapter we will learn:

1️⃣ Interfaces (Python style)
2️⃣ Abstract Base Classes (ABC)
3️⃣ Dataclasses

These concepts help in:
✔ Designing structured systems
✔ Enforcing method rules
✔ Reducing boilerplate code
""")

# ---------------- Interfaces in Python ----------------
print("\n===== INTERFACES IN PYTHON =====")
print("""
Python does not have built-in interfaces
like Java or C++.

Instead, Python follows:
✔ Duck Typing
✔ Abstract Base Classes (ABC)

If an object implements required methods,
it behaves like an interface.
""")

class PaymentInterface:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentInterface):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UpiPayment(PaymentInterface):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

def process_payment(payment_method):
    payment_method.pay(1000)

card = CreditCardPayment()
upi = UpiPayment()

process_payment(card)
process_payment(upi)

print("""
Both classes implement pay() method.
They behave like an interface.
""")

# ---------------- Abstract Base Classes (ABC) ----------------
print("\n===== ABSTRACT BASE CLASSES (ABC) =====")
print("""
Abstract Base Classes allow us to:

✔ Force child classes to implement certain methods
✔ Prevent instantiation of incomplete classes

We use the abc module.
""")

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())

print("""
If a child class does not implement area(),
Python will raise an error.
""")

# ---------------- Dataclasses ----------------
print("\n===== DATACLASSES =====")
print("""
Dataclasses are used to create classes
that primarily store data.

They automatically generate:
✔ __init__()
✔ __repr__()
✔ __eq__()

Using @dataclass decorator.
""")

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: int

student1 = Student("Aditya", 21, 85)
student2 = Student("Sneha", 22, 90)

print("Student1:", student1)
print("Student2:", student2)

print("""
Dataclass automatically created:
✔ Constructor
✔ String representation
✔ Equality comparison
""")

print("Are students equal?", student1 == student2)

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

class LoggerInterface(ABC):

    @abstractmethod
    def log(self, message):
        pass

class FileLogger(LoggerInterface):
    def log(self, message):
        print("Logging to file:", message)

class ConsoleLogger(LoggerInterface):
    def log(self, message):
        print("Logging to console:", message)

def run_logger(logger: LoggerInterface):
    logger.log("System Started")

file_logger = FileLogger()
console_logger = ConsoleLogger()

run_logger(file_logger)
run_logger(console_logger)

print("""
Using ABC ensures all logger classes
implement log() method.
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Python uses duck typing for interfaces
✔ Abstract Base Classes enforce method implementation
✔ ABC prevents incomplete class usage
✔ Dataclasses reduce boilerplate code
✔ Interfaces & ABC improve system design
✔ Dataclasses simplify data storage classes

These concepts are important
for designing large and clean applications.
""")
