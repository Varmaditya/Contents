#Program: Calculate total cost of items in cart

print("===== SHOPPING CART TOTAL =====")

# (Item, Price) pairs
cart = [
    ("Shoes", 1200),
    ("T-shirt", 500),
    ("Jeans", 1500),
    ("Cap", 200)
]

total = 0  # accumulator

# Sum all prices
for item, price in cart:
    total += price

print("Total bill amount:", total)
