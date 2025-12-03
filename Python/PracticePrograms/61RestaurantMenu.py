# Program: Restaurant Order System

print("===== RESTAURANT ORDER SYSTEM =====")

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 150,
    "Coffee": 80
}

order = []      # will store (item, price)
total = 0

print("\nAvailable Menu:")
for item, price in menu.items():
    print(f"- {item}: ₹{price}")

print("\nEnter 'done' to finish ordering.\n")

# Taking multiple orders
while True:
    choice = input("Enter item to order: ").title()

    if choice == "Done":
        break

    if choice in menu:
        order.append((choice, menu[choice]))
        total += menu[choice]
        print(choice, "added to cart.")
    else:
        print("Item not available.")

# Display bill
print("\n===== BILL SUMMARY =====")
for item, price in order:
    print(f"{item}: ₹{price}")

print("Total Amount:", total)
