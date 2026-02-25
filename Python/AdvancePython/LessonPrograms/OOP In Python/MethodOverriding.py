# METHOD OVERRIDING & super() IN PYTHON
# ---------------------------------------------

print("\n===== BASIC METHOD OVERRIDING =====")

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   # Overriding parent method
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.speak()
dog.speak()

print("\n===== USING super() =====")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def display(self):
        print("Name:", self.name)
        print("Bonus:", self.calculate_bonus())

class Manager(Employee):
    def calculate_bonus(self):
        base = super().calculate_bonus()   # call parent method
        return base + 5000

mgr = Manager("Sneha", 80000)
mgr.display()