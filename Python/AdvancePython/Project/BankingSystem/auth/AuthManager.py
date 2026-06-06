from storage.jsonStorage import JSONStorage


class AuthManager:

    ADMIN_FILE = "data/admins.json"
    EMPLOYEE_FILE = "data/employees.json"
    CUSTOMER_FILE = "data/customers.json"

    # LOGIN
    @staticmethod
    def login():
        print("\n===== LOGIN =====")

        username = input("Username: ")
        password = input("Password: ")

        # Check Admin Login
        admins = JSONStorage.load_data(AuthManager.ADMIN_FILE)

        for admin in admins:
            if admin["username"] == username and admin["password"] == password:
                print(f"\nWelcome Admin {admin['name']}")
                return "ADMIN", admin

        # Check Employee Login
        employees = JSONStorage.load_data(AuthManager.EMPLOYEE_FILE)

        for employee in employees:
            if employee["username"] == username and employee["password"] == password:
                print(f"\nWelcome Employee {employee['name']}")
                return "EMPLOYEE", employee

        # Check Customer Login
        customers = JSONStorage.load_data(AuthManager.CUSTOMER_FILE)

        for customer in customers:
            if customer["username"] == username and customer["password"] == password:
                print(f"\nWelcome {customer['name']}")
                return "CUSTOMER", customer

        print("\nInvalid Username or Password")

        return None, None


    # CHECK USERNAME EXISTS
    @staticmethod
    def username_exists(username):
        admins = JSONStorage.load_data(AuthManager.ADMIN_FILE)
        employees = JSONStorage.load_data(AuthManager.EMPLOYEE_FILE)
        customers = JSONStorage.load_data(AuthManager.CUSTOMER_FILE)
        all_users = admins + employees + customers

        for user in all_users:
            if user["username"] == username:
                return True

        return False

    # CHANGE CUSTOMER PASSWORD
    @staticmethod
    def change_customer_password():
        username = input("Username: ")
        customers = JSONStorage.load_data(AuthManager.CUSTOMER_FILE)

        for customer in customers:
            if customer["username"] == username:
                current_password = input("Current Password: ")

                if customer["password"] != current_password:
                    print("Incorrect Password")
                    return

                new_password = input("New Password: ")
                customer["password"] = new_password

                JSONStorage.save_data(AuthManager.CUSTOMER_FILE, customers)
                print("Password Changed Successfully")

                return

        print("Customer Not Found")


    # GET CUSTOMER BY USERNAME
    @staticmethod
    def get_customer(username):
        customers = JSONStorage.load_data(AuthManager.CUSTOMER_FILE)

        for customer in customers:
            if customer["username"] == username:
                return customer

        return None
