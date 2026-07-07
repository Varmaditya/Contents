/*
Program: Smart Library Management System
Description: Basic OOP project using classes, objects, arrays,
strings, loops and conditionals.
*/

#include <iostream>
#include <iomanip>
using namespace std;

class Book{
public:
    int id, year;
    string title, author, category;
    bool available;
};

class Library{
    Book books[20];
    int count;

public:
    Library() {
        count=10;
        books[0] = {101, 2013, "C++ Primer", "Lippman", "Programming", true};
        books[1] = {102, 2008, "Clean Code", "Martin", "Programming", true};
        books[2] = {103, 1997, "Harry Potter", "Rowling", "Fantasy", true};
        books[3] = {104, 2018, "Atomic Habits", "James Clear", "Self Help", true};
        books[4] = {105, 1980, "Cosmos", "Carl Sagan", "Science", true};
        books[5] = {106, 2013, "The Alchemist", "Paulo Coelho", "Fiction", true};
        books[6] = {107, 2023, "Jawan Script", "Atlee", "Cinema", true};
        books[7] = {108, 2019, "The Silent Patient", "Alex Michaelides", "Thriller", true};
        books[8] = {109, 2020, "Python Crash Course", "Eric Matthes", "Programming", true};
        books[9] = {110, 2022, "Ikigai", "Garcia", "Self Help", true};
    }

    void menu(){
        cout << "\n======= BOOKVERSE LIBRARY =======\n";
        cout << "1.View Books\n2.Search Book\n3.Borrow Book\n4.Return Book\n";
        cout << "5.Add Book\n6.Remove Book\n7.Recommend Category\n8.Statistics\n9.Exit\n";
    }

    void viewBooks() {
        cout << "\n";
        cout << left
             << setw(8)  << "ID"
             << setw(30) << "Title"
             << setw(20) << "Author"
             << setw(18) << "Category"
             << setw(12) << "Status"
             << endl;
        cout << string(88, '-') << endl;

        for(int i = 0; i < count; i++) {
            cout << left
                 << setw(8)  << books[i].id
                 << setw(30) << books[i].title
                 << setw(20) << books[i].author
                 << setw(18) << books[i].category
                 << setw(12) << (books[i].available ? "Available" : "Borrowed")
                 << endl;
        }
    }

    void searchBook() {
        string key;
        cout << "Enter Title: ";
        cin.ignore();
        getline(cin, key);

        for(int i = 0; i < count; i++) {
            if(books[i].title == key){
                cout << "\nFound!\nAuthor: " << books[i].author<< "\nCategory: " << books[i].category
                    << "\nStatus: " << (books[i].available ? "Available" : "Borrowed")<< "\n";
                return;
            }
        }

        cout << "Book Not Found!\n";
    }

    void borrowBook() {
        int id;
        cout << "Enter Book ID: ";
        cin >> id;

        for(int i = 0 ; i < count; i++) {
            if(books[i].id == id){
                if(books[i].available){
                    books[i].available = false;
                    cout << "Book Borrowed Successfully!\n";
                }else
                    cout << "Book Already Borrowed!\n";
                return;
            }
        }

        cout << "Invalid Book ID!\n";
    }

    void returnBook() {
        int id;
        cout << "Enter Book ID: ";
        cin >> id;

        for(int i = 0; i < count; i++) {
            if(books[i].id == id){
                books[i].available = true;
                cout << "Book Returned Successfully!\n";
                return;
            }
        }

        cout << "Invalid Book ID!\n";
    }

    void addBook() {
        if(count >= 20){
            cout << "Library Full!\n";
            return;
        }

        cout << "ID: ";
        cin>>books[count].id;
        cin.ignore();

        cout << "Title: ";
        getline(cin,books[count].title);

        cout << "Author: ";
        getline(cin,books[count].author);

        cout << "Category: ";
        getline(cin,books[count].category);

        cout << "Year: ";
        cin>>books[count].year;

        books[count].available = true;
        count++;

        cout << "Book Added!\n";
    }

    void removeBook() {
        int id;
        cout << "Enter Book ID: ";
        cin >> id;

        for(int i = 0; i < count; i++) {
            if(books[i].id == id){
                for(int j = i; j < count - 1; j++)
                    books[j] = books[j + 1];

                count--;
                cout << "Book Removed!\n";
                return;
            }
        }

        cout << "Book Not Found!\n";
    }

    void recommend() {
        string cat;
        cout << "Enter Category: ";
        cin.ignore();
        getline(cin, cat);
        cout << "\nRecommended Books\n";

        for(int i = 0; i < count; i++)
            if(books[i].category == cat)
                cout << "- " << books[i].title << " by " << books[i].author << "\n";
    }

    void statistics() {
        int available = 0;

        for(int i = 0; i < count ; i++)
            if(books[i].available)
                available++;

        cout << "\nTotal Books : " << count;
        cout << "\nAvailable   : " << available;
        cout << "\nBorrowed    : " << count-available << "\n";
    }
};

int main() {
    Library library;
    int choice;

    do {
        library.menu();
        cout << "\nEnter Choice: ";
        cin >> choice;

        switch(choice) {
            case 1:
                library.viewBooks();
                break;
            case 2:
                library.searchBook();
                break;
            case 3:
                library.borrowBook();
                break;
            case 4:
                library.returnBook();
                break;
            case 5:
                library.addBook();
                break;
            case 6:
                library.removeBook();
                break;
            case 7:
                library.recommend();
                break;
            case 8:
                library.statistics();
                break;
            case 9:
                cout<<"\nThank you for visiting BookVerse!\n";
                break;
            default:
                cout<<"Invalid Choice!\n";
        }
    } while(choice != 9);

    return 0;
}
