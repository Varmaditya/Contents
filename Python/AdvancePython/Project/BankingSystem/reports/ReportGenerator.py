# reports/ReportGenerator.py

from storage.JSONStorage import JSONStorage

class ReportGenerator:

    CUSTOMER_FILE = "data/customers.json"
    ACCOUNT_FILE = "data/accounts.json"
    TRANSACTION_FILE = "data/transactions.json"
    LOAN_FILE = "data/loans.json"
    CARD_FILE = "data/cards.json"

    # CUSTOMER REPORT
    @staticmethod
    def customer_report():
        customers = JSONStorage.load_data( ReportGenerator.CUSTOMER_FILE)

        print("\n===== CUSTOMER REPORT =====")
        print("Total Customers:", len(customers))

    # ACCOUNT REPORT
    @staticmethod
    def account_report():
        accounts = JSONStorage.load_data(ReportGenerator.ACCOUNT_FILE)
        total_balance = 0

        for account in accounts:
            total_balance += account["balance"]

        print("\n===== ACCOUNT REPORT =====")
        print("Total Accounts:", len(accounts))
        print("Total Deposits: ₹", total_balance)

    # TRANSACTION REPORT
    @staticmethod
    def transaction_report():
        transactions = JSONStorage.load_data(ReportGenerator.TRANSACTION_FILE)
        total_amount = 0

        for transaction in transactions:
            total_amount += transaction["amount"]

        print("\n===== TRANSACTION REPORT =====")
        print("Total Transactions:", len(transactions))
        print("Total Transaction Amount: ₹", total_amount)

    # LOAN REPORT
    @staticmethod
    def loan_report():
        loans = JSONStorage.load_data(ReportGenerator.LOAN_FILE)
        approved = 0
        rejected = 0
        pending = 0
        total_amount = 0

        for loan in loans:
            total_amount += loan["amount"]

            if loan["status"] == "APPROVED":
                approved += 1
            elif loan["status"] == "REJECTED":
                rejected += 1
            else:
                pending += 1

        print("\n===== LOAN REPORT =====")
        print("Total Loans:", len(loans))
        print("Approved:", approved)
        print("Rejected:", rejected)
        print("Pending:", pending)

        print("Total Loan Amount: ₹", total_amount)

    # CARD REPORT
    @staticmethod
    def card_report():
        cards = JSONStorage.load_data(ReportGenerator.CARD_FILE)
        debit_cards = 0
        credit_cards = 0

        for card in cards:
            if card["card_type"] == "DEBIT":
                debit_cards += 1
            else:
                credit_cards += 1

        print("\n===== CARD REPORT =====")
        print("Total Cards:", len(cards))
        print("Debit Cards:", debit_cards)
        print("Credit Cards:", credit_cards)

    # HIGHEST BALANCE ACCOUNT
    @staticmethod
    def highest_balance_account():
        accounts = JSONStorage.load_data(ReportGenerator.ACCOUNT_FILE)
      
        if not accounts:
            print("No Accounts Found.")
            return

        highest = accounts[0]

        for account in accounts:
            if account["balance"] > highest["balance"]:
                highest = account

        print("\n===== HIGHEST BALANCE ACCOUNT =====")
        print("Account Number:", highest["account_no"])
        print("Customer ID:", highest["customer_id"])
        print("Balance: ₹", highest["balance"])

    # MOST ACTIVE ACCOUNT
    @staticmethod
    def most_active_account():
        transactions = JSONStorage.load_data(ReportGenerator.TRANSACTION_FILE)

        if not transactions:
            print("No Transactions Found.")
            return

        activity = {}

        for transaction in transactions:
            account_no = transaction["account_no"]
            activity[account_no] = (activity.get(account_no, 0) + 1)

        most_active = max(activity, key=activity.get)

        print("\n===== MOST ACTIVE ACCOUNT =====")
        print("Account Number:", most_active)
        print("Transactions:", activity[most_active])

    # SYSTEM OVERVIEW
    @staticmethod
    def system_overview():

        customers = JSONStorage.load_data( ReportGenerator.CUSTOMER_FILE)
        accounts = JSONStorage.load_data(ReportGenerator.ACCOUNT_FILE)
        transactions = JSONStorage.load_data(ReportGenerator.TRANSACTION_FILE)
        loans = JSONStorage.load_data(ReportGenerator.LOAN_FILE)
        cards = JSONStorage.load_data(ReportGenerator.CARD_FILE)

        print("\n" + "=" * 40)
        print("        BANK OVERVIEW")
        print("=" * 40)

        print("Customers:", len(customers))
        print("Accounts:", len(accounts))
        print("Transactions:", len(transactions))
        print("Loans:", len(loans))
        print("Cards:", len(cards))

    # ALL REPORTS
    @staticmethod
    def generate_all_reports():
        print("\n" + "=" * 50)
        print("        BANK REPORTS")
        print("=" * 50)

        ReportGenerator.customer_report()
        ReportGenerator.account_report()
        ReportGenerator.transaction_report()
        ReportGenerator.loan_report()
        ReportGenerator.card_report()
        ReportGenerator.highest_balance_account()
        ReportGenerator.most_active_account()
