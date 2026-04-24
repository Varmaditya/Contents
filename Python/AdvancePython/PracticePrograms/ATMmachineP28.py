# Program: ATM Machine with Exception Handling

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                raise ValueError("Amount must be positive!")

            if amount > self.balance:
                raise Exception("Insufficient funds!")

            self.balance -= amount
            print("Withdrawn:", amount)

        except ValueError as ve:
            print("Error:", ve)

        except Exception as e:
            print("Error:", e)

    def show_balance(self):
        print("Balance:", self.balance)


atm = ATM(1000)

while True:
    print("\n=== ATM ===")
    print("1. Withdraw")
    print("2. Balance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        atm.withdraw()
    elif choice == "2":
        atm.show_balance()
    elif choice == "3":
        break