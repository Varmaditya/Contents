# Program: Calculate Total Bill with Discount

print("===== TOTAL BILL CALCULATOR =====")

# Taking inputs
productName = input("Enter product name: ")
price = float(input("Enter price of one item: ₹"))
quantity = int(input("Enter quantity: "))

# Calculating total price
total = price * quantity

# Applying discount (10% discount if total > 1000)
discount = 0.10 * total
finalAmount = total - discount

print(f"\nProduct: {productName}")
print(f"Total Price (before discount): ₹{total}")
print("Discount applied (10%): ₹", discount)
print("Final Bill Amount: ₹", finalAmount)
