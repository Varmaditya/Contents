#include <stdio.h>
#include <string.h>

#define MAX_BOOKS 100

// Structure to store book information
struct Book{
    int id;
    char title[50];
    char author[50];
    int available;
};

struct Book library[MAX_BOOKS];
int count = 0;

// Function: Add Book
void addBook() {
    printf("\nEnter Book ID: ");
    scanf("%d", &library[count].id);

    printf("Enter Book Title: ");
    scanf(" %[^\n]", library[count].title);

    printf("Enter Author Name: ");
    scanf(" %[^\n]", library[count].author);

    library[count].available = 1;
    count++;

    printf("\nBook Added Successfully!\n");
}

// Function: Display Books
void displayBooks() {
    int i;

    if(count == 0) {
        printf("\nNo Books Available.\n");
        return;
    }

    printf("\n-----------------------------\n");

    for(i=0;i<count;i++) {
        printf("Book ID   : %d\n", library[i].id);
        printf("Title     : %s\n", library[i].title);
        printf("Author    : %s\n", library[i].author);

        if(library[i].available)
            printf("Status    : Available\n");
        else
            printf("Status    : Issued\n");

        printf("-----------------------------\n");
    }
}

// Function: Search Book
void searchBook(){
    int id, i;

    printf("Enter Book ID to Search: ");
    scanf("%d",&id);

    for(i=0;i<count;i++) {
        if(library[i].id == id) {
            printf("\nBook Found!\n");

            printf("Book ID : %d\n", library[i].id);
            printf("Title   : %s\n", library[i].title);
            printf("Author  : %s\n", library[i].author);

            return;
        }
    }

    printf("Book Not Found!\n");
}


// Function: Issue Book
void issueBook() {
    int id, i;

    printf("Enter Book ID to Issue: ");
    scanf("%d",&id);

    for(i=0;i<count;i++) {
        if(library[i].id == id) {
            if(library[i].available) {
                library[i].available = 0;
                printf("Book Issued Successfully!\n");
            } else {
                printf("Book Already Issued!\n");
            }

            return;
        }
    }

    printf("Book Not Found!\n");
}

// Function: Return Book
void returnBook(){
    int id, i;

    printf("Enter Book ID to Return: ");
    scanf("%d",&id);

    for(i=0;i<count;i++) {
        if(library[i].id == id) {
            library[i].available = 1;
            printf("Book Returned Successfully!\n");

            return;
        }
    }

    printf("Book Not Found!\n");
}

// Main Function
int main() {
    int choice;

    do {
        printf("\n========== LIBRARY MANAGEMENT ==========\n");
        printf("1. Add Book\n");
        printf("2. Display Books\n");
        printf("3. Search Book\n");
        printf("4. Issue Book\n");
        printf("5. Return Book\n");
        printf("6. Exit\n");

        printf("Enter Choice: ");
        scanf("%d",&choice);

        switch(choice) {
            case 1:
                addBook();
                break;
            case 2:
                displayBooks();
                break;
            case 3:
                searchBook();
                break;
            case 4:
                issueBook();
                break;
            case 5:
                returnBook();
                break;
            case 6:
                printf("Thank You!\n");
                break;
            default:
                printf("Invalid Choice!\n");
        }

    } while(choice != 6);

    return 0;
}
