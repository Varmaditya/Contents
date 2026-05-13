# main.py for password manager program

from vault import Vault
from generator import generate_password

vault = Vault()

while True:
    print("\n=== Password Manager ===")
    print("1. Generate Password")
    print("2. View Saved Passwords")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        site = input("Website name: ")

        pwd = generate_password()

        vault.save(site, pwd)

        print("Generated Password:", pwd)

    elif choice == "2":
        vault.show()

    else:
        break