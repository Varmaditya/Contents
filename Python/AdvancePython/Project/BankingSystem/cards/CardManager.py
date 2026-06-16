# cards/CardManager.py

import random

from datetime import datetime
from datetime import timedelta

from storage.JSONStorage import JSONStorage


class CardManager:

    FILE_NAME = "data/cards.json"

    # GENERATE CARD NUMBER
    @staticmethod
    def generate_card_number():

        number = ""

        for _ in range(16):

            number += str(
                random.randint(0, 9)
            )

        return number

    # GENERATE CVV
    @staticmethod
    def generate_cvv():

        return str(
            random.randint(100, 999)
        )

    # ISSUE CARD
    @staticmethod
    def issue_card():

        print("\n===== ISSUE CARD =====")

        customer_id = input(
            "Customer ID: "
        )

        print("\n1. Debit Card")
        print("2. Credit Card")

        choice = input(
            "\nChoose Card Type: "
        )

        if choice == "1":

            card_type = "DEBIT"

        elif choice == "2":

            card_type = "CREDIT"

        else:

            print("Invalid Choice.")

            return

        expiry_date = (
            datetime.now() +
            timedelta(days=1825)
        ).strftime("%m/%Y")

        card = {

            "card_number": CardManager.generate_card_number(),

            "customer_id": customer_id,

            "card_type": card_type,

            "cvv": CardManager.generate_cvv(),

            "expiry_date": expiry_date,

            "status": "ACTIVE",

            "issued_on": datetime.now().strftime(
                "%d-%m-%Y"
            )
        }

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        cards.append(card)

        JSONStorage.save_data(
            CardManager.FILE_NAME,
            cards
        )

        print("\nCard Issued Successfully")

        print(
            "Card Number:",
            card["card_number"]
        )

    # VIEW ALL CARDS
    @staticmethod
    def view_cards():

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        if not cards:

            print("No Cards Found.")

            return

        print("\n===== CARD LIST =====")

        for card in cards:

            print(
                f"{card['card_number']} | "
                f"{card['customer_id']} | "
                f"{card['card_type']} | "
                f"{card['status']}"
            )

    # SEARCH CARD
    @staticmethod
    def search_card():

        card_number = input(
            "Card Number: "
        )

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        for card in cards:

            if card["card_number"] == card_number:

                print("\n===== CARD DETAILS =====")

                for key, value in card.items():

                    print(f"{key}: {value}")

                return

        print("Card Not Found.")

    # BLOCK CARD
    @staticmethod
    def block_card():

        card_number = input(
            "Card Number: "
        )

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        for card in cards:

            if card["card_number"] == card_number:

                card["status"] = "BLOCKED"

                JSONStorage.save_data(
                    CardManager.FILE_NAME,
                    cards
                )

                print(
                    "Card Blocked Successfully."
                )

                return

        print("Card Not Found.")

    # UNBLOCK CARD
    @staticmethod
    def unblock_card():

        card_number = input(
            "Card Number: "
        )

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        for card in cards:

            if card["card_number"] == card_number:

                card["status"] = "ACTIVE"

                JSONStorage.save_data(
                    CardManager.FILE_NAME,
                    cards
                )

                print(
                    "Card Activated Successfully."
                )

                return

        print("Card Not Found.")

    # CUSTOMER CARDS
    @staticmethod
    def customer_cards():

        customer_id = input(
            "Customer ID: "
        )

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        found = False

        print(
            "\n===== CUSTOMER CARDS ====="
        )

        for card in cards:

            if card["customer_id"] == customer_id:

                found = True

                print(
                    f"{card['card_number']} | "
                    f"{card['card_type']} | "
                    f"{card['status']}"
                )

        if not found:

            print("No Cards Found.")

    # CARD STATISTICS
    @staticmethod
    def card_statistics():

        cards = JSONStorage.load_data(
            CardManager.FILE_NAME
        )

        total_cards = len(cards)

        debit_cards = 0
        credit_cards = 0

        active_cards = 0
        blocked_cards = 0

        for card in cards:

            if card["card_type"] == "DEBIT":
                debit_cards += 1
            else:
                credit_cards += 1

            if card["status"] == "ACTIVE":
                active_cards += 1
            else:
                blocked_cards += 1

        print("\n===== CARD STATISTICS =====")

        print("Total Cards:", total_cards)
        print("Debit Cards:", debit_cards)
        print("Credit Cards:", credit_cards)

        print("Active Cards:", active_cards)
        print("Blocked Cards:", blocked_cards)