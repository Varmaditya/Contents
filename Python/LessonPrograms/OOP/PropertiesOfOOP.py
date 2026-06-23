# OOP PROPERTIES (FOUR PILLARS) IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== OOP PROPERTIES (FOUR PILLARS) =====")
print("""
Object Oriented Programming is built on four major principles:

1️⃣ Encapsulation
2️⃣ Abstraction
3️⃣ Inheritance
4️⃣ Polymorphism

These principles make code:
✔ Secure
✔ Reusable
✔ Scalable
✔ Maintainable
""")

# ======================================================
# 1️⃣ ENCAPSULATION
# ======================================================

print("\n===== 1️⃣ ENCAPSULATION =====")
print("""
Encapsulation means:
✔ Binding data and methods together inside a class
✔ Restricting direct access to internal data

It protects object integrity.
""")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Aditya", 5000)

account.deposit(1000)
account.withdraw(2000)

print("Balance (using method):", account.get_balance())

# print(account.__balance)  # This would cause an error

print("""
Private variables use double underscore (__).
They cannot be accessed directly outside the class.
""")

# ======================================================
# 2️⃣ ABSTRACTION
# ======================================================

print("\n===== 2️⃣ ABSTRACTION =====")
print("""
Abstraction means:
✔ Hiding internal implementation details
✔ Showing only essential features

Users interact with methods
without knowing internal logic.
""")

class CoffeeMachine:
    def make_coffee(self):
        self.__boil_water()
        self.__brew_coffee()
        print("Coffee is ready!")

    def __boil_water(self):
        print("Boiling water...")

    def __brew_coffee(self):
        print("Brewing coffee...")

machine = CoffeeMachine()
machine.make_coffee()

print("""
User only calls make_coffee().
Internal steps are hidden.
""")

# ======================================================
# 3️⃣ INHERITANCE
# ======================================================

print("\n===== 3️⃣ INHERITANCE =====")
print("""
Inheritance allows one class to inherit
properties and methods of another class.

It promotes code reuse.
""")

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()

print("""
Dog inherited the speak() method from Animal.
""")

# ======================================================
# 4️⃣ POLYMORPHISM
# ======================================================

print("\n===== 4️⃣ POLYMORPHISM =====")
print("""
Polymorphism means:
✔ Same method name
✔ Different behavior

Commonly achieved using method overriding.
""")

class Bird:
    def fly(self):
        print("Bird flies in the sky")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

bird = Bird()
penguin = Penguin()

bird.fly()
penguin.fly()

print("""
Both classes have fly() method,
but behavior is different.
""")

# ======================================================
# PRACTICAL COMBINED EXAMPLE
# ======================================================

print("\n===== PRACTICAL COMBINED EXAMPLE =====")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # encapsulation

    def get_salary(self):
        return self.__salary

    def work(self):
        print(self.name, "is working")

class Manager(Employee):
    def work(self):
        print(self.name, "is managing the team")

emp = Employee("Ravi", 40000)
mgr = Manager("Sneha", 80000)

emp.work()
mgr.work()

print("Employee Salary:", emp.get_salary())
print("Manager Salary:", mgr.get_salary())

print("""
In this example:
✔ Encapsulation: __salary is private
✔ Inheritance: Manager inherits Employee
✔ Polymorphism: work() behaves differently
✔ Abstraction: Salary accessed via method
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Encapsulation protects data
✔ Abstraction hides implementation details
✔ Inheritance promotes code reuse
✔ Polymorphism allows flexible behavior

These four pillars form the foundation
of powerful object-oriented systems.
""")
