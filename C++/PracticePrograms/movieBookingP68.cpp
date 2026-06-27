/*
Program: Movie Ticket Booking System
Description: Books movie tickets and generates final bill using functions.
*/

#include <iostream>
using namespace std;

string movies[4] ={
    "Avengers",
    "Jawan",
    "Interstellar",
    "Bahubali"
};

int prices[4] ={250, 180, 300, 220};

void displayMovies() {
    cout << "\n======= NOW SHOWING =======\n";

    for (int i = 0; i < 4; i++) {
        cout << i + 1 << ". " << movies[i] << "  Rs." << prices[i] << endl;
    }
}

int calculateBill(int movieChoice, int tickets) {
    return prices[movieChoice - 1] * tickets;
}

void printTicket(int movieChoice, int tickets, int bill) {
    cout << "\n======= MOVIE TICKET =======\n";

    cout << "Movie : " << movies[movieChoice - 1] << endl;
    cout << "Tickets : " << tickets << endl;
    cout << "Total Bill : Rs." << bill << endl;
}

int main() {
    int choice;
    int tickets;

    displayMovies();

    cout << "\nChoose Movie : ";
    cin >> choice;

    cout << "Number of Tickets : ";
    cin >> tickets;

    int bill = calculateBill(choice, tickets);
    printTicket(choice, tickets, bill);

    return 0;
}
