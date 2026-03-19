# METHOD OVERRIDING & super() IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== METHOD OVERRIDING IN PYTHON =====")
print("""
Method Overriding occurs when a child class
provides its own implementation of a method
that is already defined in the parent class.

It is one of the key concepts of Polymorphism.

Conditions for Method Overriding:
✔ Inheritance must exist
✔ Method name must be same
✔ Parameters must be same
""")

# ---------------- Basic Method Overriding ----------------
print("\n===== BASIC METHOD OVERRIDING =====")

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.speak()
dog.speak()

print("""
Dog class overrides the speak() method
of Animal class.
""")

# ---------------- Method Overriding with Same Signature ----------------
print("\n===== METHOD OVERRIDING WITH SAME PARAMETERS =====")

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key ignition")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self start button")

v = Vehicle()
c = Car()
b = Bike()

v.start()
c.start()
b.start()

print("""
All classes have start() method,
but behavior is different.
This is Polymorphism using Method Overriding.
""")

# ---------------- Using super() ----------------
print("\n===== USING super() FUNCTION =====")
print("""
super() is used to call the parent class method
from the child class.

It helps:
✔ Extend parent functionality
✔ Avoid rewriting parent code
""")

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)   # calling parent constructor
        self.grade = grade

    def display(self):
        super().display()        # calling parent method
        print("Grade:", self.grade)

student = Student("Aditya", "A")

student.display()

print("""
super().__init__() calls parent constructor.
super().display() calls parent method.
""")

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", self.calculate_bonus())

class Manager(Employee):
    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        return base_bonus + 5000   # extra bonus for manager

manager = Manager("Sneha", 80000)

manager.display()

print("""
Manager overrides calculate_bonus()
but still uses parent logic via super().
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Method Overriding requires inheritance
✔ Method signature should be same
✔ super() calls parent class method
✔ Overriding enables runtime polymorphism
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Method Overriding allows child class
   to redefine parent method
✔ It supports Polymorphism
✔ super() is used to call parent class methods
✔ Helps extend functionality without duplication

Method Overriding is widely used in:
✔ Framework development
✔ GUI applications
✔ Enterprise systems
✔ API design
""")
