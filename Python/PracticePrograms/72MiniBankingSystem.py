# Program: Mini Banking System

print("===== MINI BANKING SYSTEM =====")

accounts = {
    "Jash": 5000,
    "Rohit": 3000,
    "Neha": 7000
}

def deposit(user, amount):
    accounts[user] += amount
    return f"{amount} added. New Balance = {accounts[user]}"

def withdraw(user, amount):
    if amount > accounts[user]:
        return "Insufficient balance."
    accounts[user] -= amount
    return f"Withdrawn {amount}. New Balance = {accounts[user]}"

def transfer(src, dst, amount):
    if amount > accounts[src]:
        return "Not enough balance to transfer."
    accounts[src] -= amount
    accounts[dst] += amount
    return f"Transferred {amount} to {dst}"

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Exit")
    ch = int(input("Choose: "))

    if ch == 4:
        break

    user = input("Enter username: ").title()

    if user not in accounts:
        print("User not found.")
        continue

    if ch == 1:
        amt = float(input("Amount: "))
        print(deposit(user, amt))

    elif ch == 2:
        amt = float(input("Amount: "))
        print(withdraw(user, amt))

    elif ch == 3:
        dst = input("Transfer to: ").title()
        amt = float(input("Amount: "))
        print(transfer(user, dst, amt))
