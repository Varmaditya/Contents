# main.py

from auth.AuthManager import AuthManager
from customer_management.CustomerManager import CustomerManager
from accounts.AccountManager import AccountManager


# ADMIN DASHBOARD
def admin_dashboard(admin):
    while True:
        print("\n" + "=" * 40)
        print("        ADMIN DASHBOARD")
        print("=" * 40)

        print(f"Welcome, {admin['name']}")

        print("\n1. View Bank Statistics")
        print("2. Employee Management")
        print("3. Logout")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            print("\nStatistics Module Coming Soon...")
        elif choice == "2":
            print("\nEmployee Module Coming Soon...")
        elif choice == "3":
            print("\nLogging Out...")
            break
        else:
            print("Invalid Choice.")

# EMPLOYEE DASHBOARD
def employee_dashboard(employee):
    while True:
        print("\n" + "=" * 40)
        print("      EMPLOYEE DASHBOARD")
        print("=" * 40)

        print(f"Logged In: {employee['name']}")

        print("\n--- CUSTOMER MANAGEMENT ---")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")

        print("\n--- ACCOUNT MANAGEMENT ---")
        print("6. Create Account")
        print("7. View Accounts")
        print("8. Search Account")
        print("9. Deposit Money")
        print("10. Withdraw Money")
        print("11. Check Balance")
        print("12. Delete Account")

        print("\n--- SYSTEM ---")
        print("13. Logout")

        choice = input("\nEnter Choice: ")

        # ---------------- CUSTOMER ----------------
        if choice == "1":
            CustomerManager.create_customer()
        elif choice == "2":
            CustomerManager.view_customers()
        elif choice == "3":
            CustomerManager.search_customer()
        elif choice == "4":
            CustomerManager.update_customer()
        elif choice == "5":
            CustomerManager.delete_customer()

        # ---------------- ACCOUNT ----------------
        elif choice == "6":
            AccountManager.create_account()
        elif choice == "7":
            AccountManager.view_accounts()
        elif choice == "8":
            AccountManager.search_account()
        elif choice == "9":
            AccountManager.deposit_money()
        elif choice == "10":
            AccountManager.withdraw_money()
        elif choice == "11":
            AccountManager.check_balance()
        elif choice == "12":
            AccountManager.delete_account()
        elif choice == "13":
            print("\nLogging Out...")
            break
        else:
            print("Invalid Choice.")


# CUSTOMER DASHBOARD
def customer_dashboard(customer):
    while True:
        print("\n" + "=" * 40)
        print("      CUSTOMER DASHBOARD")
        print("=" * 40)

        print(f"Welcome, {customer['name']}")

        print("\n1. View Profile")
        print("2. My Accounts")
        print("3. Transaction History")
        print("4. Apply Loan")
        print("5. Logout")

        choice = input("\nEnter Choice: ")
        if choice == "1":
            print("\nProfile Module Coming Soon...")
        elif choice == "2":
            print("\nAccounts Module Coming Soon...")
        elif choice == "3":
            print("\nTransaction Module Coming Soon...")
        elif choice == "4":
            print("\nLoan Module Coming Soon...")
        elif choice == "5":
            print("\nLogging Out...")
            break
        else:
            print("Invalid Choice.")


# MAIN APPLICATION
def main():
    while True:
        print("\n" + "=" * 50)
        print("      DIGITAL BANKING SYSTEM")
        print("=" * 50)

        print("1. Login")
        print("2. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            role, user = AuthManager.login()
            if role == "ADMIN":
                admin_dashboard(user)
            elif role == "EMPLOYEE":
                employee_dashboard(user)
            elif role == "CUSTOMER":
                customer_dashboard(user)
            else:
                print("\nInvalid Username or Password.")
        elif choice == "2":
            print("\nThank You For Using Digital Banking System.")
            break
        else:
            print("Invalid Choice.")

# PROGRAM ENTRY POINT
if __name__ == "__main__":

    main()
