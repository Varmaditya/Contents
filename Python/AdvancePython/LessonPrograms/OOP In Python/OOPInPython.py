# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== INTRODUCTION TO OBJECT ORIENTED PROGRAMMING (OOP) =====")
print("""
Object Oriented Programming (OOP) is a programming paradigm
based on the concept of objects.

An object represents a real-world entity.

Examples:
✔ Student
✔ Car
✔ Bank Account
✔ Employee

OOP helps:
✔ Organize code logically
✔ Group related data and behavior
✔ Improve reusability
✔ Make large systems manageable
""")

# ---------------- OOP Core Components ----------------
print("\n===== OOP CORE COMPONENTS =====")
print("""
The main components of OOP are:

1️⃣ Class
   - Blueprint or template for creating objects

2️⃣ Object
   - Instance of a class

3️⃣ Attributes
   - Variables that store data inside a class
   - Two types:
       ✔ Instance Variables
       ✔ Class Variables

4️⃣ Methods
   - Functions defined inside a class
   - Used to define object behavior
""")

# ---------------- OOP Properties (Four Pillars) ----------------
print("\n===== OOP PROPERTIES (FOUR PILLARS) =====")
print("""
OOP is based on four major principles:

1️⃣ Encapsulation
   - Binding data and methods together
   - Restricting direct access to data

2️⃣ Abstraction
   - Hiding internal implementation details
   - Showing only essential features

3️⃣ Inheritance
   - One class acquiring properties of another class

4️⃣ Polymorphism
   - Same method behaving differently
   - Example: method overriding

In this chapter, we focus on the basic structure of OOP.
Advanced properties will be covered in next chapters.
""")

# ---------------- What is a Class ----------------
print("\n===== WHAT IS A CLASS? =====")
print("""
A Class is a blueprint or template for creating objects.

Think of:
Class  → Blueprint of a building
Object → Actual building constructed from blueprint
""")

class Student:
    pass

print("Empty class Student created successfully.")

# ---------------- What is an Object ----------------
print("\n===== WHAT IS AN OBJECT? =====")

student1 = Student()
student2 = Student()

print("Student1 object:", student1)
print("Student2 object:", student2)

print("""
Objects are instances of a class.
Each object has its own memory location.
""")

# ---------------- __init__ Method (Constructor) ----------------
print("\n===== __init__ METHOD (CONSTRUCTOR) =====")
print("""
__init__ is a special method called automatically
when an object is created.

It is used to initialize instance variables.
""")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print("Person1 Name:", person1.name)
print("Person1 Age:", person1.age)
print("Person2 Name:", person2.name)
print("Person2 Age:", person2.age)

# ---------------- Instance Variables ----------------
print("\n===== INSTANCE VARIABLES =====")
print("""
Instance variables belong to each object individually.
Each object stores its own copy.
""")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "City")

print("Car1:", car1.brand, car1.model)
print("Car2:", car2.brand, car2.model)

# ---------------- Class Variables ----------------
print("\n===== CLASS VARIABLES =====")
print("""
Class variables are shared among all objects
of the class.
""")

class Company:
    company_name = "Tech Solutions"   # class variable

    def __init__(self, employee_name):
        self.employee_name = employee_name

emp1 = Company("Rahul")
emp2 = Company("Sneha")

print("Employee1 Company:", emp1.company_name)
print("Employee2 Company:", emp2.company_name)

print("\nChanging class variable...")

Company.company_name = "Global Tech"

print("Employee1 Company:", emp1.company_name)
print("Employee2 Company:", emp2.company_name)

# ---------------- Instance Methods ----------------
print("\n===== INSTANCE METHODS =====")
print("""
Instance methods:
✔ Defined inside class
✔ Work with instance variables
✔ Always take 'self' as first parameter
""")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited. New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn. Remaining balance:", self.balance)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Owner:", self.owner)
        print("Current Balance:", self.balance)

account1 = BankAccount("Aditya", 5000)

account1.display_balance()
account1.deposit(2000)
account1.withdraw(3000)
account1.withdraw(10000)

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE: STUDENT RECORD SYSTEM =====")

class StudentRecord:
    school_name = "Bright Future School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display_report(self):
        print("\nSchool:", StudentRecord.school_name)
        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())

studentA = StudentRecord("Arjun", [85, 90, 88])
studentB = StudentRecord("Meera", [75, 80, 79])

studentA.display_report()
studentB.display_report()

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ OOP is based on objects
✔ Class is a blueprint
✔ Object is an instance of class
✔ Attributes store data
✔ Methods define behavior
✔ __init__ initializes object data
✔ Instance variables belong to objects
✔ Class variables are shared
✔ OOP has four pillars:
   Encapsulation, Abstraction, Inheritance, Polymorphism

This forms the foundation of OOP in Python.
Next topics:
✔ Encapsulation
✔ Inheritance
✔ Polymorphism
✔ Abstraction
""")