# accounts/AccountManager.py

from storage.JSONStorage import JSONStorage
from utils.Helpers import generate_account_no


class AccountManager:

    FILE_NAME = "data/accounts.json"

    # CREATE ACCOUNT
    @staticmethod
    def create_account():

        print("\n===== CREATE ACCOUNT =====")

        customer_id = input("Customer ID: ")

        account_type = input(
            "Account Type (SAVINGS/CURRENT): "
        ).upper()

        try:

            initial_balance = float(
                input("Initial Deposit: ")
            )

        except ValueError:

            print("Invalid Amount.")

            return

        account = {
            "account_no": generate_account_no(),
            "customer_id": customer_id,
            "account_type": account_type,
            "balance": initial_balance
        }

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        accounts.append(account)

        JSONStorage.save_data(
            AccountManager.FILE_NAME,
            accounts
        )

        print("\nAccount Created Successfully!")

        print(
            "Account Number:",
            account["account_no"]
        )

    # VIEW ACCOUNTS
    @staticmethod
    def view_accounts():

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        if not accounts:

            print("No Accounts Found.")

            return

        print("\n===== ACCOUNT LIST =====")

        for account in accounts:

            print(
                f"{account['account_no']} | "
                f"{account['customer_id']} | "
                f"{account['account_type']} | "
                f"₹{account['balance']}"
            )

    # SEARCH ACCOUNT
    @staticmethod
    def search_account():

        account_no = input(
            "Enter Account Number: "
        )

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        for account in accounts:

            if account["account_no"] == account_no:

                print(
                    "\n===== ACCOUNT FOUND ====="
                )

                for key, value in account.items():

                    print(
                        f"{key}: {value}"
                    )

                return

        print("Account Not Found.")

    # DEPOSIT MONEY
    @staticmethod
    def deposit_money():

        account_no = input(
            "Account Number: "
        )

        try:

            amount = float(
                input("Deposit Amount: ")
            )

        except ValueError:

            print("Invalid Amount.")

            return

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        for account in accounts:

            if account["account_no"] == account_no:

                account["balance"] += amount

                JSONStorage.save_data(
                    AccountManager.FILE_NAME,
                    accounts
                )

                print(
                    "Deposit Successful."
                )

                print(
                    "Updated Balance:",
                    account["balance"]
                )

                return

        print("Account Not Found.")

    # WITHDRAW MONEY
    @staticmethod
    def withdraw_money():

        account_no = input(
            "Account Number: "
        )

        try:

            amount = float(
                input("Withdraw Amount: ")
            )

        except ValueError:

            print("Invalid Amount.")

            return

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        for account in accounts:

            if account["account_no"] == account_no:

                if amount > account["balance"]:

                    print(
                        "Insufficient Balance."
                    )

                    return

                account["balance"] -= amount

                JSONStorage.save_data(
                    AccountManager.FILE_NAME,
                    accounts
                )

                print(
                    "Withdrawal Successful."
                )

                print(
                    "Updated Balance:",
                    account["balance"]
                )

                return

        print("Account Not Found.")

    # CHECK BALANCE
    @staticmethod
    def check_balance():

        account_no = input(
            "Account Number: "
        )

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        for account in accounts:

            if account["account_no"] == account_no:

                print(
                    f"\nCurrent Balance: ₹{account['balance']}"
                )

                return

        print("Account Not Found.")

    # DELETE ACCOUNT
    @staticmethod
    def delete_account():

        account_no = input(
            "Account Number: "
        )

        accounts = JSONStorage.load_data(
            AccountManager.FILE_NAME
        )

        updated_accounts = []

        deleted = False

        for account in accounts:

            if account["account_no"] == account_no:

                deleted = True

            else:

                updated_accounts.append(
                    account
                )

        JSONStorage.save_data(
            AccountManager.FILE_NAME,
            updated_accounts
        )

        if deleted:

            print(
                "Account Deleted Successfully."
            )

        else:

            print("Account Not Found.")