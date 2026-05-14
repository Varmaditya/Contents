# library.py

from storage import save_books, load_books
from book import Book

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = load_books(filename, Book)

    def add_book(self):
        title = input("Book title: ")
        author = input("Author: ")

        self.books.append(Book(title, author))

        print("Book added!")

    def show_books(self):
        if not self.books:
            print("Library empty!")
            return

        for book in self.books:
            book.display()

    def borrow_book(self):
        title = input("Enter book title: ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if not book.available:
                    print("Book already borrowed!")
                    return

                book.available = False
                print("Book borrowed!")
                return

        print("Book not found!")

    def save(self):
        save_books(self.filename, self.books)