# Program: Simple Contact Book

contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")

    contacts[name] = number
    print("Contact added!")

def view_contacts():
    print("\nAll Contacts:")
    for name, number in contacts.items():
        print(name, "->", number)

def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Number:", contacts[name])
    else:
        print("Contact not found!")


while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")