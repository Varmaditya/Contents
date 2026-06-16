# cards/Card.py

from datetime import datetime


class Card:

    def __init__(
        self,
        card_number,
        customer_id,
        card_type,
        expiry_date
    ):

        self.card_number = card_number
        self.customer_id = customer_id
        self.card_type = card_type
        self.expiry_date = expiry_date

        self.status = "ACTIVE"

        self.issued_on = datetime.now().strftime(
            "%d-%m-%Y"
        )

    # CONVERT OBJECT TO DICTIONARY
    def to_dict(self):

        return {
            "card_number": self.card_number,
            "customer_id": self.customer_id,
            "card_type": self.card_type,
            "expiry_date": self.expiry_date,
            "status": self.status,
            "issued_on": self.issued_on
        }

    # STRING REPRESENTATION
    def __str__(self):

        return (
            f"{self.card_number} | "
            f"{self.card_type} | "
            f"{self.status}"
        )