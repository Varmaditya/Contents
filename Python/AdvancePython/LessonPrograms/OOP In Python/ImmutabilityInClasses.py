# IMMUTABILITY IN CLASSES
# ---------------------------------------------

print("\n===== DEFAULT MUTABLE CLASS =====")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Aditya", 21)
print("Before:", p.age)

p.age = 25   # Modification allowed
print("After:", p.age)


print("\n===== IMMUTABLE USING PRIVATE ATTRIBUTES =====")

class SafePerson:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

sp = SafePerson("Sneha", 22)
print("Name:", sp.get_name())
print("Age:", sp.get_age())

# sp.__age = 30  # Not directly accessible


print("\n===== IMMUTABLE USING __setattr__ =====")

class FrozenPerson:
    def __init__(self, name, age):
        super().__setattr__("name", name)
        super().__setattr__("age", age)

    def __setattr__(self, key, value):
        raise AttributeError("Object is immutable")

fp = FrozenPerson("Ravi", 30)
print("Frozen Name:", fp.name)

try:
    fp.age = 35   # Attempt modification
except AttributeError as e:
    print("Error:", e)


print("\n===== IMMUTABLE DATACLASS =====")

from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    name: str
    marks: int

s1 = Student("Arjun", 90)
s2 = Student("Arjun", 90)

print("Student:", s1)
print("Are students equal?", s1 == s2)

# s1.marks = 95  # Would raise error
