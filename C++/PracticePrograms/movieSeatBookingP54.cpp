/*
Program: Movie Theater Seat Booking System
Description: Allows users to book seats and view seat availability.
*/

#include <iostream>
using namespace std;

int main() {

    int seats[10] = {0};
    int seatNumber;

    cout << "Available Seats:\n";

    for(int index = 0; index < 10; index++) {
        cout << "Seat " << index + 1 << " : ";

        if(seats[index] == 0)
            cout << "Available";
        else
            cout << "Booked";

        cout << endl;
    }

    cout << "\nEnter Seat Number to Book: ";
    cin >> seatNumber;

    seats[seatNumber - 1] = 1;

    cout << "\nUpdated Seat Status:\n";

    for(int index = 0; index < 10; index++) {
        cout << "Seat " << index + 1 << " : ";

        if(seats[index] == 0)
            cout << "Available";
        else
            cout << "Booked";

        cout << endl;
    }

    return 0;
}
