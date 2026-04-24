# Program: Shopping Cart System

cart = []

def add_item():
    item = input("Enter item: ")
    cart.append(item)
    print("Item added!")

def view_cart():
    print("\nYour Cart:")
    for item in cart:
        print("-", item)

def remove_item():
    item = input("Enter item to remove: ")

    if item in cart:
        cart.remove(item)
        print("Item removed!")
    else:
        print("Item not found!")


while True:
    print("\n=== Shopping Cart ===")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")