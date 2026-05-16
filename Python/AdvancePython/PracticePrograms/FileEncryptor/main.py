# main.py for File Encryptor Program

from encryptor import Encryptor

tool = Encryptor()

while True:
    print("\n=== Secret Encryptor ===")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        filename = input("Enter filename: ")
        tool.encrypt_file(filename)

    elif choice == "2":
        filename = input("Enter filename: ")
        tool.decrypt_file(filename)

    else:
        break
