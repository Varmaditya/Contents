# loans/LoanManager.py

from datetime import datetime

from storage.JSONStorage import JSONStorage
from utils.Helpers import generate_id


class LoanManager:

    FILE_NAME = "data/loans.json"

    # APPLY LOAN
    @staticmethod
    def apply_loan():

        print("\n===== APPLY LOAN =====")

        customer_id = input("Customer ID: ")

        print("\nLoan Types")
        print("1. Home Loan")
        print("2. Personal Loan")
        print("3. Education Loan")
        print("4. Vehicle Loan")

        choice = input("\nChoose Loan Type: ")

        loan_types = {
            "1": "HOME",
            "2": "PERSONAL",
            "3": "EDUCATION",
            "4": "VEHICLE"
        }

        if choice not in loan_types:

            print("Invalid Loan Type.")

            return

        try:

            amount = float(input("Loan Amount: "))

            if amount <= 0:

                print("Invalid Amount.")

                return

        except ValueError:

            print("Invalid Amount.")

            return

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        loan = {
            "loan_id": generate_id("LOAN"),
            "customer_id": customer_id,
            "loan_type": loan_types[choice],
            "amount": amount,
            "status": "PENDING",
            "applied_on": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }

        loans.append(loan)

        JSONStorage.save_data(
            LoanManager.FILE_NAME,
            loans
        )

        print("\nLoan Application Submitted.")

        print("Loan ID:", loan["loan_id"])

    # VIEW ALL LOANS
    @staticmethod
    def view_loans():

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        if not loans:

            print("No Loans Found.")

            return

        print("\n===== LOAN LIST =====")

        for loan in loans:

            print(
                f"{loan['loan_id']} | "
                f"{loan['customer_id']} | "
                f"{loan['loan_type']} | "
                f"₹{loan['amount']} | "
                f"{loan['status']}"
            )

    # SEARCH LOAN
    @staticmethod
    def search_loan():

        loan_id = input("Loan ID: ")

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        for loan in loans:

            if loan["loan_id"] == loan_id:

                print("\n===== LOAN DETAILS =====")

                for key, value in loan.items():

                    print(f"{key}: {value}")

                return

        print("Loan Not Found.")

    # APPROVE LOAN
    @staticmethod
    def approve_loan():

        loan_id = input("Loan ID: ")

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        for loan in loans:

            if loan["loan_id"] == loan_id:

                if loan["status"] == "APPROVED":

                    print(
                        "Loan Already Approved."
                    )

                    return

                loan["status"] = "APPROVED"

                loan["approved_on"] = datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                JSONStorage.save_data(
                    LoanManager.FILE_NAME,
                    loans
                )

                print(
                    "Loan Approved Successfully."
                )

                return

        print("Loan Not Found.")

    # REJECT LOAN
    @staticmethod
    def reject_loan():

        loan_id = input("Loan ID: ")

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        for loan in loans:

            if loan["loan_id"] == loan_id:

                if loan["status"] == "REJECTED":

                    print(
                        "Loan Already Rejected."
                    )

                    return

                loan["status"] = "REJECTED"

                loan["rejected_on"] = datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                JSONStorage.save_data(
                    LoanManager.FILE_NAME,
                    loans
                )

                print(
                    "Loan Rejected Successfully."
                )

                return

        print("Loan Not Found.")

    # VIEW CUSTOMER LOANS
    @staticmethod
    def customer_loans():

        customer_id = input(
            "Customer ID: "
        )

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        found = False

        print(
            "\n===== CUSTOMER LOANS ====="
        )

        for loan in loans:

            if loan["customer_id"] == customer_id:

                found = True

                print(
                    f"{loan['loan_id']} | "
                    f"{loan['loan_type']} | "
                    f"₹{loan['amount']} | "
                    f"{loan['status']}"
                )

        if not found:

            print(
                "No Loans Found."
            )

    # LOAN STATISTICS
    @staticmethod
    def loan_statistics():

        loans = JSONStorage.load_data(
            LoanManager.FILE_NAME
        )

        total_loans = len(loans)

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

        print("\n===== LOAN STATISTICS =====")

        print("Total Loans:", total_loans)
        print("Approved:", approved)
        print("Rejected:", rejected)
        print("Pending:", pending)

        print(
            "Total Loan Amount: ₹",
            total_amount
        )