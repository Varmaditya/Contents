# Program: Digital Diary

class Diary:
    def __init__(self, filename):
        self.filename = filename

    def write_entry(self):
        entry = input("Write your diary entry: ")

        with open(self.filename, "a") as file:
            file.write(entry + "\n")

        print("Entry saved!")

    def read_entries(self):
        try:
            with open(self.filename, "r") as file:
                print("\nYour Diary:")
                print(file.read())
        except FileNotFoundError:
            print("No diary entries found!")


diary = Diary("diary.txt")

while True:
    print("\n=== Digital Diary ===")
    print("1. Write Entry")
    print("2. Read Entries")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        diary.write_entry()
    elif choice == "2":
        diary.read_entries()
    elif choice == "3":
        break