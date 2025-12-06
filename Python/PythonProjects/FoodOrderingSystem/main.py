# FOOD ORDERING SYSTEM (CONSOLE PROJECT)

import datetime

# ---------------- Configuration ----------------

TAX_RATE = 0.12  # 12% GST

MENU = {
    "Pizzas": {
        1: ("Margherita", 250),
        2: ("Farmhouse", 320),
        3: ("Pepperoni", 350),
    },
    "Burgers": {
        4: ("Veg Burger", 150),
        5: ("Cheese Burger", 180),
        6: ("Chicken Burger", 220),
    },
    "Drinks": {
        7: ("Coke", 60),
        8: ("Lemonade", 80),
        9: ("Cold Coffee", 120),
    },
    "Desserts": {
        10: ("Brownie", 140),
        11: ("Ice Cream", 90),
        12: ("Cheesecake", 180),
    }
}

COUPONS = {
    "SAVE50": {"type": "flat", "value": 50},    # flat ₹50 off
    "NEW10": {"type": "percent", "value": 10},  # 10% off
    "FEST20": {"type": "percent", "value": 20}  # 20% off
}


# ---------------- Helper Functions ----------------

def print_header():
    print("\n" + "=" * 40)
    print("        FOOD ORDERING SYSTEM        ")
    print("=" * 40)


def display_menu():
    print("\n===== MENU =====")
    for category, items in MENU.items():
        print(f"\n-- {category} --")
        for code, (name, price) in items.items():
            print(f"{code}. {name} - ₹{price}")

def find_item_by_code(code):
    """Return (name, price) given item code, else None."""
    for items in MENU.values():
        if code in items:
            return items[code]
    return None

def display_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n===== YOUR CART =====")
    print("{:<4} {:<20} {:<8} {:<8}".format("No.", "Item", "Qty", "Total"))
    print("-" * 40)
    for idx, item in enumerate(cart, start=1):
        name = item["name"]
        qty = item["quantity"]
        price = item["price"]
        lineTotal = qty * price
        print(f"{idx:<4} {name:<20} {qty:<8} ₹{lineTotal:<8}")
    print("-" * 40)

def calculate_subtotal(cart):
    return sum(item["price"] * item["quantity"] for item in cart)

def apply_coupon(subtotal, code):
    """Return (discount_amount, coupon_used)."""
    if not code:
        return 0, None

    code = code.upper()
    if code not in COUPONS:
        print("Invalid coupon code. No discount applied.")
        return 0, None

    coupon = COUPONS[code]
    if coupon["type"] == "flat":
        discount = coupon["value"]
    else:  # percent
        discount = (coupon["value"] / 100) * subtotal

    # Avoid negative totals
    discount = min(discount, subtotal)

    print(f"Coupon '{code}' applied. Discount: ₹{int(discount)}")
    return int(discount), code

def save_bill_to_file(cart, subtotal, taxAmount, discount, total, coupon_code):
    now = datetime.datetime.now()
    filename = f"bill_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("===== FOOD ORDERING SYSTEM - BILL =====\n")
        f.write(f"Date & Time: {now}\n")
        f.write("-" * 40 + "\n")
        f.write("{:<4} {:<20} {:<8} {:<8}\n".format("No.", "Item", "Qty", "Total"))
        f.write("-" * 40 + "\n")

        for idx, item in enumerate(cart, start=1):
            name = item["name"]
            qty = item["quantity"]
            price = item["price"]
            lineTotal = qty * price
            f.write(f"{idx:<4} {name:<20} {qty:<8} ₹{lineTotal:<8}\n")

        f.write("-" * 40 + "\n")
        f.write(f"Subtotal: ₹{subtotal}\n")
        f.write(f"GST @ {int(TAX_RATE * 100)}%: ₹{taxAmount}\n")
        if coupon_code:
            f.write(f"Coupon ({coupon_code}) Discount: -₹{discount}\n")
        f.write(f"Grand Total: ₹{total}\n")
        f.write("Thank you for ordering with us!\n")

    print(f"\nBill saved as '{filename}'")


# ---------------- Main Flow ----------------

def main():
    cart = []
    print_header()

    while True:
        print("\n1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_menu()

        elif choice == "2":
            display_menu()
            try:
                code = int(input("\nEnter item code to add: "))
                item = find_item_by_code(code)
                if item is None:
                    print("Invalid item code.")
                    continue

                name, price = item
                qty = int(input(f"Enter quantity for {name}: "))
                if qty <= 0:
                    print("Quantity must be positive.")
                    continue

                # Check if item already in cart -> update quantity
                for cItem in cart:
                    if cItem["name"] == name:
                        cItem["quantity"] += qty
                        break
                else:
                    cart.append({"name": name, "price": price, "quantity": qty})

                print(f"{qty} x {name} added to cart.")

            except ValueError:
                print("Please enter valid numeric values.")

        elif choice == "3":
            display_cart(cart)

        elif choice == "4":
            if not cart:
                print("\nYour cart is empty. Add items before checkout.")
                continue

            # Show order summary
            display_cart(cart)
            subtotal = calculate_subtotal(cart)
            taxAmount = int(subtotal * TAX_RATE)
            print(f"\nSubtotal: ₹{subtotal}")
            print(f"GST @ {int(TAX_RATE * 100)}%: ₹{taxAmount}")

            # Apply coupon
            couponInput = input("Enter coupon code (or press Enter to skip): ").strip()
            discount, couponUsed = apply_coupon(subtotal, couponInput)

            total = subtotal + taxAmount - discount
            total = int(total)

            print("\n===== ORDER SUMMARY =====")
            print(f"Subtotal: ₹{subtotal}")
            print(f"GST: ₹{taxAmount}")
            if couponUsed:
                print(f"Coupon ({couponUsed}) Discount: -₹{discount}")
            print(f"Grand Total: ₹{total}")

            confirm = input("\nConfirm order? (y/n): ").strip().lower()
            if confirm == "y":
                print("\nOrder confirmed! 🎉")
                saveChoice = input("Do you want to save the bill to a file? (y/n): ").strip().lower()
                if saveChoice == "y":
                    save_bill_to_file(cart, subtotal, taxAmount, discount, total, couponUsed)
                print("Thank you for ordering. Visit again!")
                break
            else:
                print("Order cancelled. You can continue modifying your cart.")

        elif choice == "5":
            print("\nExiting... Thank you!")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


# Run the program
if __name__ == "__main__":
    main()
