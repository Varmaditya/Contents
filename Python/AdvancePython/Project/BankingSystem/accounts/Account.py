# accounts/Account.py

class Account:

    def __init__(self, account_no, customer_id, balance=0):

        self.account_no = account_no
        self.customer_id = customer_id
        self.balance = balance

    # DEPOSIT MONEY
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be positive."
            )

        self.balance += amount

    # WITHDRAW MONEY
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be positive."
            )

        if amount > self.balance:
            raise ValueError(
                "Insufficient Balance."
            )

        self.balance -= amount

    # CHECK BALANCE
    def get_balance(self):

        return self.balance

    # CONVERT TO DICTIONARY
    def to_dict(self):

        return {
            "account_no": self.account_no,
            "customer_id": self.customer_id,
            "balance": self.balance
        }

    # STRING REPRESENTATION
    def __str__(self):

        return (
            f"{self.account_no} | "
            f"Balance: ₹{self.balance}"
        )