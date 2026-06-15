# transactions/Transaction.py

from datetime import datetime


class Transaction:

    def __init__(
        self,
        transaction_id,
        account_no,
        transaction_type,
        amount
    ):

        self.transaction_id = transaction_id
        self.account_no = account_no
        self.transaction_type = transaction_type
        self.amount = amount

        self.date_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    # CONVERT OBJECT TO DICTIONARY
    def to_dict(self):

        return {
            "transaction_id": self.transaction_id,
            "account_no": self.account_no,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "date_time": self.date_time
        }

    # STRING REPRESENTATION
    def __str__(self):

        return (
            f"{self.transaction_id} | "
            f"{self.transaction_type} | "
            f"₹{self.amount}"
        )