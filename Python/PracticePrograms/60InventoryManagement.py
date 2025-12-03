# Program: Inventory Management System

print("===== INVENTORY MANAGEMENT =====")

inventory = {
    "Shoes": 10,
    "Jeans": 5,
    "T-shirts": 20,
    "Caps": 2
}

print("Current Stock:\n", inventory)

item = input("\nEnter item to purchase: ").title()
qty = int(input("Enter quantity needed: "))

# Check stock availability
if item in inventory:
    if qty <= inventory[item]:
        inventory[item] -= qty
        print("\nOrder Confirmed!")
        print("Remaining Stock:", inventory[item])
    else:
        print("\nOnly", inventory[item], "pcs available. Cannot fulfil order.")
else:
    print("\nItem not found in inventory.")
