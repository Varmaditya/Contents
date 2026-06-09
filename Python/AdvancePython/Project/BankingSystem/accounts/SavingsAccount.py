# accounts/SavingsAccount.py

from accounts.Account import Account


class SavingsAccount(Account):

    INTEREST_RATE = 4

    def __init__(self, account_no, customer_id, balance=0):

        super().__init__(account_no, customer_id, balance)

        self.account_type = "SAVINGS"

    # CALCULATE INTEREST
    def calculate_interest(self):

        return (
            self.balance *
            self.INTEREST_RATE
        ) / 100

    # CONVERT TO DICTIONARY
    def to_dict(self):

        return {
            "account_no": self.account_no,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance
        }