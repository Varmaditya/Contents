# Program to display product details and calculate total price

productName = input("Enter the product name: ")
productPrice = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity you want to buy: "))

total_cost = productPrice * quantity

print("\nProduct Summary:")
print("Product:", productName)
print("Price per unit:", productPrice)
print("Quantity:", quantity)
print("Total cost:", total_cost)
