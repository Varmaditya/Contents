# INTERFACES & DATACLASSES IN PYTHON
# ---------------------------------------------

print("\n===== INTERFACE USING DUCK TYPING =====")

class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

def process_payment(method):
    method.pay(1000)

process_payment(CreditCard())
process_payment(UPI())


print("\n===== INTERFACE USING ABSTRACT BASE CLASS =====")

from abc import ABC, abstractmethod

class PaymentInterface(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class DebitCard(PaymentInterface):
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")

debit = DebitCard()
debit.pay(2000)


print("\n===== DATACLASS EXAMPLE =====")

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: int

s1 = Student("Aditya", 21, 85)
s2 = Student("Sneha", 22, 90)

print("Student 1:", s1)
print("Are students equal?", s1 == s2)
