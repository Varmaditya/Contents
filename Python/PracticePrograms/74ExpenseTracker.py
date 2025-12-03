# Program: Expense Tracker

print("===== EXPENSE TRACKER =====")

expenses = {}

def add_expense(day, amount):
    if day not in expenses:
        expenses[day] = []
    expenses[day].append(amount)

def total_expense(day):
    return sum(expenses.get(day, []))

def monthly_summary():
    for day, exp_list in expenses.items():
        print(f"{day}: Total = {sum(exp_list)}  | Entries = {len(exp_list)}")

while True:
    print("\n1. Add Expense\n2. View Day Total\n3. Monthly Summary\n4. Exit")
    ch = int(input("Choose: "))

    if ch == 1:
        day = input("Enter day (e.g., Mon, Tue): ").title()
        amt = float(input("Amount spent: "))
        add_expense(day, amt)

    elif ch == 2:
        day = input("Enter day: ").title()
        print("Total spent:", total_expense(day))

    elif ch == 3:
        monthly_summary()

    elif ch == 4:
        break
