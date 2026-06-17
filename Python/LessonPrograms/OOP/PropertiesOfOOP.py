# OOP PROPERTIES (FOUR PILLARS) IN PYTHON

print("\n===== OOP FOUR PILLARS DEMO =====")

# Encapsulation + Abstraction
class Employee:
    company_name = "Tech Solutions"   # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # Private Variable (Encapsulation)

    def get_salary(self):        # Abstraction (controlled access)
        return self.__salary

    def work(self):              # Method to be overridden
        print(self.name, "is working at", Employee.company_name)

# Inheritance + Polymorphism
class Manager(Employee):
    def work(self):              # Method Overriding (Polymorphism)
        print(self.name, "is managing the team at", Employee.company_name)

# Creating objects
emp = Employee("Ravi", 40000)
mgr = Manager("Sneha", 80000)

print("\n--- Work Behavior ---")
emp.work()
mgr.work()

print("\n--- Salary Access ---")
print("Employee Salary:", emp.get_salary())
print("Manager Salary:", mgr.get_salary())

print("\n--- Changing Class Variable ---")
Employee.company_name = "Global Tech"

emp.work()
mgr.work()

