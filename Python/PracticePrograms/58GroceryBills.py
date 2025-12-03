# Program: Grocery Billing System

print("===== GROCERY BILLING SYSTEM =====")

cart = [
    ("Milk", 50, 2),
    ("Eggs", 6, 6),
    ("Rice", 60, 1),
    ("Chocolate", 40, 3)
]

totalBill = 0

print("Items Purchased:\n")

# item → (name, price_per_unit, quantity)
for item, price, qty in cart:
    cost = price * qty
    totalBill += cost

    print(f"{item}: {qty} pcs x ₹{price} = ₹{cost}")

print("\nTotal Bill Amount:", totalBill)
