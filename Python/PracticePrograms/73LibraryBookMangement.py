# Program: Library Book Manager

print("===== LIBRARY BOOK MANAGER =====")

library = []

def add_book(title, author):
    library.append({"title": title, "author": author})

def search_book(keyword):
    return [book for book in library if keyword.lower() in book["title"].lower()]

def remove_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            return "Book removed."
    return "Book not found."

while True:
    print("\n1. Add Book\n2. Search Book\n3. Remove Book\n4. View Library\n5. Exit")
    choice = int(input("Choose option: "))

    if choice == 1:
        t = input("Book title: ")
        a = input("Author: ")
        add_book(t, a)

    elif choice == 2:
        key = input("Search keyword: ")
        result = search_book(key)
        print("Search Results:", result)

    elif choice == 3:
        t = input("Enter title to remove: ")
        print(remove_book(t))

    elif choice == 4:
        print("Library:", library)

    elif choice == 5:
        break
