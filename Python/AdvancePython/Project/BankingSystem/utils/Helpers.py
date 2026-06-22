# utils/Helpers.py

import random
from datetime import datetime


# GENERATE GENERAL ID
def generate_id(prefix):

    number = random.randint(
        1000,
        9999
    )

    return f"{prefix}{number}"


# GENERATE ACCOUNT NUMBER
def generate_account_no():

    number = random.randint(
        100000,
        999999
    )

    return f"ACC{number}"


# GENERATE CARD NUMBER
def generate_card_number():

    card_number = ""

    for _ in range(16):

        card_number += str(
            random.randint(0, 9)
        )

    return card_number


# GENERATE CVV
def generate_cvv():

    return str(
        random.randint(100, 999)
    )


# CURRENT DATE
def current_date():

    return datetime.now().strftime(
        "%d-%m-%Y"
    )


# CURRENT DATE & TIME
def current_datetime():

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )


# CURRENCY FORMAT
def format_currency(amount):

    return f"₹{amount:,.2f}"


# PRINT SECTION HEADING
def print_heading(title):

    print("\n" + "=" * 40)

    print(title.center(40))

    print("=" * 40)


# PRINT SUCCESS MESSAGE
def success(message):

    print(f"\n✓ {message}")


# PRINT ERROR MESSAGE
def error(message):

    print(f"\n✗ {message}")


# VALIDATE PHONE NUMBER
def validate_phone(phone):

    return (
        phone.isdigit()
        and len(phone) == 10
    )


# VALIDATE EMAIL
def validate_email(email):

    return (
        "@" in email
        and "." in email
    )


# PAUSE SCREEN
def pause():

    input(
        "\nPress Enter To Continue..."
    )