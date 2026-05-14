# storage.py

def save_books(filename, books):
    with open(filename, "w") as file:
        for book in books:
            file.write(f"{book.title},{book.author},{book.available}\n")


def load_books(filename, Book):
    books = []

    try:
        with open(filename, "r") as file:
            for line in file:
                title, author, available = line.strip().split(",")

                book = Book(title, author)

                if available == "False":
                    book.available = False

                books.append(book)

    except FileNotFoundError:
        print("No saved library data found.")

    return books