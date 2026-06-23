# Program: Secret Message Vault

class Vault:
    def __init__(self, filename):
        self.filename = filename

    def save_message(self):
        message = input("Enter secret message: ")

        # simple "encryption" by reversing text
        encrypted = message[::-1]

        with open(self.filename, "a") as file:
            file.write(encrypted + "\n")

        print("Message stored securely!")

    def read_messages(self):
        try:
            with open(self.filename, "r") as file:
                print("\nSecret Messages:")
                for line in file:
                    decrypted = line.strip()[::-1]
                    print("-", decrypted)
        except FileNotFoundError:
            print("No messages found!")


vault = Vault("vault.txt")

while True:
    print("\n=== Secret Vault ===")
    print("1. Save Message")
    print("2. Read Messages")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        vault.save_message()
    elif choice == "2":
        vault.read_messages()
    else:
        break