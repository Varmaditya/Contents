# Program: Calculate Total Bill with Discount

print("===== TOTAL BILL CALCULATOR =====")

# Taking inputs
product_name = input("Enter product name: ")
price = float(input("Enter price of one item: ₹"))
quantity = int(input("Enter quantity: "))

# Calculating total price
total = price * quantity

# Applying discount (10% discount if total > 1000)
discount = 0.10 * total
final_amount = total - discount

print(f"\nProduct: {product_name}")
print(f"Total Price (before discount): ₹{total}")
print("Discount applied (10%): ₹", discount)
print("Final Bill Amount: ₹", final_amount)
