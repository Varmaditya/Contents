# Program: Find Costliest Product (With User Input)

print("===== COSTLIEST PRODUCT FINDER =====")

products = {}  # empty dictionary

count = int(input("How many products do you want to enter? "))

# Taking product inputs
for i in range(count):
    name = input(f"Enter product name {i+1}: ").title()
    price = float(input(f"Enter price of {name}: "))
    products[name] = price

# Find max price
maxPrice = max(products.values())

# Find product with max price
for name, price in products.items():
    if price == maxPrice:
        print("\nCostliest Product:", name, "-", price)
