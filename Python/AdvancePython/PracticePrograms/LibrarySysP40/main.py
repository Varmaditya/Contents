# main.py for library system

from library import Library

library = Library("books.txt")

while True:
    print("\n=== Digital Library ===")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.save()
        print("Library saved!")
        break