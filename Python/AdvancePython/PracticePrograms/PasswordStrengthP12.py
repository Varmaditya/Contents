# Program: Password Strength Checker

def check_password(password: str) -> str:
    """
    Checks strength of password.

    Rules:
    ✔ Length > 6
    ✔ Contains number
    ✔ Contains uppercase
    """

    has_number = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_upper = True

    if len(password) > 6 and has_number and has_upper:
        return "Strong Password"
    elif len(password) > 4:
        return "Medium Password"
    else:
        return "Weak Password"


while True:
    pwd = input("Enter password (or 'exit'): ")

    if pwd == "exit":
        break

    print(check_password(pwd))