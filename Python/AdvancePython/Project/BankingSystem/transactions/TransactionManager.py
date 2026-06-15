# transactions/TransactionManager.py

from datetime import datetime

from storage.JSONStorage import JSONStorage
from utils.Helpers import generate_id


class TransactionManager:

    TRANSACTION_FILE = "data/transactions.json"
    ACCOUNT_FILE = "data/accounts.json"

    # RECORD TRANSACTION
    @staticmethod
    def record_transaction(
        account_no,
        transaction_type,
        amount
    ):

        transactions = JSONStorage.load_data(
            TransactionManager.TRANSACTION_FILE
        )

        transaction = {

            "transaction_id": generate_id("TXN"),

            "account_no": account_no,

            "transaction_type": transaction_type,

            "amount": amount,

            "date_time": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }

        transactions.append(transaction)

        JSONStorage.save_data(
            TransactionManager.TRANSACTION_FILE,
            transactions
        )

    # TRANSFER MONEY
    @staticmethod
    def transfer_money():

        print("\n===== TRANSFER MONEY =====")

        sender = input(
            "From Account Number: "
        )

        receiver = input(
            "To Account Number: "
        )

        try:

            amount = float(
                input("Amount: ")
            )

        except ValueError:

            print("Invalid Amount.")

            return

        accounts = JSONStorage.load_data(
            TransactionManager.ACCOUNT_FILE
        )

        sender_account = None
        receiver_account = None

        for account in accounts:

            if account["account_no"] == sender:

                sender_account = account

            elif account["account_no"] == receiver:

                receiver_account = account

        if sender_account is None:

            print("Sender Account Not Found.")

            return

        if receiver_account is None:

            print("Receiver Account Not Found.")

            return

        if amount > sender_account["balance"]:

            print("Insufficient Balance.")

            return

        sender_account["balance"] -= amount

        receiver_account["balance"] += amount

        JSONStorage.save_data(
            TransactionManager.ACCOUNT_FILE,
            accounts
        )

        TransactionManager.record_transaction(
            sender,
            "TRANSFER OUT",
            amount
        )

        TransactionManager.record_transaction(
            receiver,
            "TRANSFER IN",
            amount
        )

        print("\nTransfer Successful.")

    # VIEW TRANSACTION HISTORY
    @staticmethod
    def view_transaction_history():

        account_no = input(
            "Account Number: "
        )

        transactions = JSONStorage.load_data(
            TransactionManager.TRANSACTION_FILE
        )

        found = False

        print(
            "\n===== TRANSACTION HISTORY ====="
        )

        for transaction in transactions:

            if transaction["account_no"] == account_no:

                found = True

                print(
                    f"{transaction['transaction_id']} | "
                    f"{transaction['transaction_type']} | "
                    f"₹{transaction['amount']} | "
                    f"{transaction['date_time']}"
                )

        if not found:

            print("No Transactions Found.")

    # MINI STATEMENT
    @staticmethod
    def mini_statement():

        account_no = input(
            "Account Number: "
        )

        transactions = JSONStorage.load_data(
            TransactionManager.TRANSACTION_FILE
        )

        account_transactions = []

        for transaction in transactions:

            if transaction["account_no"] == account_no:

                account_transactions.append(
                    transaction
                )

        if not account_transactions:

            print("No Transactions Found.")

            return

        print("\n===== MINI STATEMENT =====")

        for transaction in account_transactions[-5:]:

            print(
                f"{transaction['transaction_type']} | "
                f"₹{transaction['amount']} | "
                f"{transaction['date_time']}"
            )

    # VIEW ALL TRANSACTIONS
    @staticmethod
    def view_all_transactions():

        transactions = JSONStorage.load_data(
            TransactionManager.TRANSACTION_FILE
        )

        if not transactions:

            print(
                "No Transactions Found."
            )

            return

        print(
            "\n===== ALL TRANSACTIONS ====="
        )

        for transaction in transactions:

            print(
                f"{transaction['transaction_id']} | "
                f"{transaction['account_no']} | "
                f"{transaction['transaction_type']} | "
                f"₹{transaction['amount']}"
            )

    # ACCOUNT STATEMENT
    @staticmethod
    def account_statement():

        account_no = input(
            "Account Number: "
        )

        transactions = JSONStorage.load_data(
            TransactionManager.TRANSACTION_FILE
        )

        print(
            "\n===== ACCOUNT STATEMENT ====="
        )

        print(
            "Account Number:",
            account_no
        )

        print("-" * 60)

        total_transactions = 0

        for transaction in transactions:

            if transaction["account_no"] == account_no:

                total_transactions += 1

                print(
                    f"{transaction['date_time']} | "
                    f"{transaction['transaction_type']} | "
                    f"₹{transaction['amount']}"
                )

        print("-" * 60)

        print(
            "Total Transactions:",
            total_transactions
        )