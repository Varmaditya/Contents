# CLASS METHODS & STATIC METHODS IN PYTHON
# ---------------------------------------------

print("\n===== CLASS METHOD DEMO =====")

class Employee:
    company_name = "TechCorp"   # Class Variable

    def __init__(self, name):
        self.name = name

    # Class Method → modifies class variable
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Company:", Employee.company_name)


emp1 = Employee("Aditya")
emp2 = Employee("Sneha")

emp1.display()
print()

# Changing class variable using class method
Employee.change_company("GlobalTech")

emp2.display()


print("\n===== STATIC METHOD DEMO =====")

class MathUtility:

    # Static Method → utility function
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("Addition:", MathUtility.add(5, 3))
print("Multiplication:", MathUtility.multiply(4, 6))
