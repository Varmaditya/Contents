# Program: Simple Student Class (Introduction to OOP)
# OOP (Object-Oriented Programming) is an advanced topic where
# code is organized into "classes" and "objects".

print("===== STUDENT CLASS DEMO =====")

class Student:
    def __init__(self, name, marks):
        self.name = name        # instance variable
        self.marks = marks

    def display(self):          # method (function inside class)
        print("Name:", self.name)
        print("Marks:", self.marks)

# Creating objects
s1 = Student("Asha", 85)
s2 = Student("Rohit", 92)

s1.display()
s2.display()
