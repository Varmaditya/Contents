# MULTIPLE INHERITANCE & MRO IN PYTHON
# ---------------------------------------------

print("\n===== BASIC MULTIPLE INHERITANCE =====")

class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skills()   # Follows MRO

print("MRO of Child:", Child.__mro__)


print("\n===== CHANGING PARENT ORDER =====")

class Child2(Mother, Father):
    pass

child2 = Child2()
child2.skills()   # Different result

print("MRO of Child2:", Child2.mro())


print("\n===== super() WITH MULTIPLE INHERITANCE =====")

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(A):
    def show(self):
        print("Class C")
        super().show()

class D(B, C):
    def show(self):
        print("Class D")
        super().show()

d = D()
d.show()

print("MRO of D:", D.mro())