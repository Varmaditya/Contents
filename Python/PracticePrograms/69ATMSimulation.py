# Program: ATM Menu System

print("===== ATM SYSTEM =====")

balance = 5000

def check_balance():
    print("Current Balance:", balance)

def deposit(amount):
    return amount

def withdraw(amount):
    if amount > balance:
        print("Insufficient balance.")
        return 0
    return -amount

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = int(input("Choose option: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        amt = float(input("Amount to deposit: "))
        balance += deposit(amt)
        print("Deposit successful.")

    elif choice == 3:
        amt = float(input("Amount to withdraw: "))
        balance += withdraw(amt)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid option.")
