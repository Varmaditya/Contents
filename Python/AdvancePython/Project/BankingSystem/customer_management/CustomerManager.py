# customer_management/CustomerManager.py

from storage.JSONStorage import JSONStorage
from utils.Helpers import generate_id
from auth.AuthManager import AuthManager


class CustomerManager:

    FILE_NAME = "data/customers.json"

    # CREATE CUSTOMER
    @staticmethod
    def create_customer():

        print("\n===== CREATE CUSTOMER =====")

        name = input("Name: ")
        username = input("Username: ")

        if AuthManager.username_exists(username):

            print("Username already exists.")

            return

        password = input("Password: ")

        phone = input("Phone Number: ")

        if not phone.isdigit() or len(phone) != 10:

            print("Invalid Phone Number.")

            return

        email = input("Email: ")

        if "@" not in email:

            print("Invalid Email Address.")

            return

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        customer = {

            "user_id": generate_id("CUS"),
            "name": name,
            "username": username,
            "password": password,
            "phone": phone,
            "email": email
        }

        customers.append(customer)

        JSONStorage.save_data(
            CustomerManager.FILE_NAME,
            customers
        )

        print("\nCustomer Created Successfully!")

        print(
            "Customer ID:",
            customer["user_id"]
        )

    # VIEW ALL CUSTOMERS
    @staticmethod
    def view_customers():

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        if not customers:

            print("\nNo Customers Found.")

            return

        print("\n===== CUSTOMER LIST =====")

        for customer in customers:

            print(
                f"{customer['user_id']} | "
                f"{customer['name']} | "
                f"{customer['phone']}"
            )

    # SEARCH CUSTOMER
    @staticmethod
    def search_customer():

        customer_id = input(
            "Enter Customer ID: "
        )

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        for customer in customers:

            if customer["user_id"] == customer_id:

                print(
                    "\n===== CUSTOMER FOUND ====="
                )

                for key, value in customer.items():

                    print(
                        f"{key}: {value}"
                    )

                return

        print("Customer Not Found.")

    # UPDATE CUSTOMER
    @staticmethod
    def update_customer():

        customer_id = input(
            "Enter Customer ID: "
        )

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        for customer in customers:

            if customer["user_id"] == customer_id:

                print(
                    "\nLeave Blank To Skip"
                )

                name = input(
                    "New Name: "
                )

                phone = input(
                    "New Phone: "
                )

                email = input(
                    "New Email: "
                )

                if name:
                    customer["name"] = name

                if phone:
                    customer["phone"] = phone

                if email:
                    customer["email"] = email

                JSONStorage.save_data(
                    CustomerManager.FILE_NAME,
                    customers
                )

                print(
                    "Customer Updated Successfully."
                )

                return

        print("Customer Not Found.")

    # DELETE CUSTOMER
    @staticmethod
    def delete_customer():

        customer_id = input(
            "Enter Customer ID: "
        )

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        updated_customers = []

        deleted = False

        for customer in customers:

            if customer["user_id"] == customer_id:

                deleted = True

            else:

                updated_customers.append(
                    customer
                )

        JSONStorage.save_data(
            CustomerManager.FILE_NAME,
            updated_customers
        )

        if deleted:

            print(
                "Customer Deleted Successfully."
            )

        else:

            print("Customer Not Found.")

    # VIEW CUSTOMER PROFILE
    @staticmethod
    def view_customer_profile():

        username = input(
            "Enter Username: "
        )

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        for customer in customers:

            if customer["username"] == username:

                print(
                    "\n===== CUSTOMER PROFILE ====="
                )

                print(
                    "Customer ID:",
                    customer["user_id"]
                )

                print(
                    "Name:",
                    customer["name"]
                )

                print(
                    "Phone:",
                    customer["phone"]
                )

                print(
                    "Email:",
                    customer["email"]
                )

                return

        print("Customer Not Found.")

    # CUSTOMER STATISTICS
    @staticmethod
    def customer_statistics():

        customers = JSONStorage.load_data(
            CustomerManager.FILE_NAME
        )

        print(
            "\n===== CUSTOMER STATISTICS ====="
        )

        print(
            "Total Customers:",
            len(customers)
        )