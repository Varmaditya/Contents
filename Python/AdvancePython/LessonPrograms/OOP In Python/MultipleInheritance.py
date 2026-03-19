# MULTIPLE INHERITANCE, MRO, CLASS METHODS & STATIC METHODS
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== MULTIPLE INHERITANCE, MRO, CLASS METHODS & STATIC METHODS =====")
print("""
In this chapter we will learn:

1️⃣ Multiple Inheritance
2️⃣ Method Resolution Order (MRO)
3️⃣ super() in Multiple Inheritance
4️⃣ Class Methods
5️⃣ Static Methods

These concepts are important for designing
flexible and scalable object-oriented systems.
""")

# ---------------- Multiple Inheritance ----------------
print("\n===== MULTIPLE INHERITANCE =====")
print("""
Multiple Inheritance means:
A class can inherit from more than one parent class.

Syntax:
class Child(Parent1, Parent2):
    pass

This allows combining behaviors
from multiple parent classes.
""")

class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def cooking(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skills()
child.cooking()

print("""
Child inherits methods from both parents.
""")

# ---------------- Method Resolution Order (MRO) ----------------
print("\n===== METHOD RESOLUTION ORDER (MRO) =====")
print("""
MRO determines the order in which
Python searches for methods.

If multiple parents have same method,
Python follows MRO to decide which one to execute.
""")

class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()

print("MRO of C:", C.mro())

print("""
Since A appears before B,
A.show() is executed.
""")

# ---------------- Changing Parent Order ----------------
print("\n===== CHANGING PARENT ORDER =====")

class D(B, A):
    pass

obj2 = D()
obj2.show()

print("MRO of D:", D.mro())

print("""
Now B appears first,
so B.show() is executed.
""")

# ---------------- Using super() ----------------
print("\n===== USING super() WITH MULTIPLE INHERITANCE =====")
print("""
super() follows MRO order.
It calls the next class in MRO chain.
""")

class X:
    def display(self):
        print("Class X")

class Y(X):
    def display(self):
        print("Class Y")
        super().display()

class Z(X):
    def display(self):
        print("Class Z")
        super().display()

class Final(Y, Z):
    def display(self):
        print("Class Final")
        super().display()

f = Final()
f.display()

print("MRO of Final:", Final.mro())

print("""
Execution order follows MRO.
""")

# ---------------- Diamond Problem ----------------
print("\n===== DIAMOND PROBLEM =====")
print("""
Diamond Structure:

        A
       / \
      B   C
       \ /
        D

Python solves this using MRO (C3 Linearization).
It ensures each class is executed only once.
""")

# ---------------- Class Methods ----------------
print("\n===== CLASS METHODS =====")
print("""
Class methods:
✔ Work with class variables
✔ Use 'cls' parameter
✔ Defined using @classmethod
""")

class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

emp1 = Employee("Aditya")
emp2 = Employee("Sneha")

print("Company Name:", Employee.company_name)

Employee.change_company("GlobalTech")

print("Company Name After Change:", emp1.company_name)

# ---------------- Static Methods ----------------
print("\n===== STATIC METHODS =====")
print("""
Static methods:
✔ Do not use self
✔ Do not use cls
✔ Utility functions inside class
✔ Defined using @staticmethod
""")

class MathUtility:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print("Addition:", MathUtility.add(5, 3))
print("Multiplication:", MathUtility.multiply(4, 6))

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Multiple Inheritance allows inheriting from multiple classes
✔ MRO decides method lookup order
✔ Parent order affects behavior
✔ super() follows MRO chain
✔ Diamond problem solved using MRO
✔ Class methods modify class variables
✔ Static methods are utility methods

These are important concepts
for advanced object-oriented programming.
""")
