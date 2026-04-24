# Program: Online Shopping System with Exception Handling

class OutOfStockError(Exception):
    pass


class PaymentError(Exception):
    pass


class Store:
    def __init__(self):
        self.products = {"laptop": 50000, "phone": 20000, "tablet": 15000}
        self.stock = {"laptop": 2, "phone": 3, "tablet": 1}
        self.cart = []

    def add_to_cart(self):
        try:
            item = input("Enter product name: ").lower()

            if item not in self.products:
                raise ValueError("Product not found!")

            if self.stock[item] == 0:
                raise OutOfStockError(f"{item} is out of stock!")

            self.cart.append(item)
            self.stock[item] -= 1

            print(item, "added to cart!")

        except ValueError as ve:
            print("Error:", ve)
        except OutOfStockError as oe:
            print("Error:", oe)

    def checkout(self):
        try:
            if not self.cart:
                raise Exception("Cart is empty!")

            total = sum(self.products[item] for item in self.cart)
            print("Total amount:", total)

            money = float(input("Enter payment amount: "))

            if money < total:
                raise PaymentError("Insufficient payment!")

            print("Payment successful! Order placed.")
            self.cart.clear()

        except ValueError:
            print("Invalid payment input!")
        except PaymentError as pe:
            print("Payment Error:", pe)
        except Exception as e:
            print("Error:", e)


store = Store()

while True:
    print("\n=== Store Menu ===")
    print("1. Add to Cart")
    print("2. Checkout")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        store.add_to_cart()
    elif choice == "2":
        store.checkout()
    elif choice == "3":
        break