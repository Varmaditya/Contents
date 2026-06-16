# loans/Loan.py

from datetime import datetime


class Loan:

    def __init__(
        self,
        loan_id,
        customer_id,
        loan_type,
        amount
    ):

        self.loan_id = loan_id
        self.customer_id = customer_id
        self.loan_type = loan_type
        self.amount = amount

        self.status = "PENDING"

        self.applied_on = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    # CONVERT OBJECT TO DICTIONARY
    def to_dict(self):

        return {
            "loan_id": self.loan_id,
            "customer_id": self.customer_id,
            "loan_type": self.loan_type,
            "amount": self.amount,
            "status": self.status,
            "applied_on": self.applied_on
        }

    # STRING REPRESENTATION
    def __str__(self):

        return (
            f"{self.loan_id} | "
            f"{self.loan_type} | "
            f"₹{self.amount} | "
            f"{self.status}"
        )