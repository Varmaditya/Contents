/*
Program: Metro Ticket System
Description: Calculates metro fare based on travel zone and passenger type.
*/

#include <iostream>
using namespace std;

int main() {
    int travelZone;
    char passengerType;

    float ticketFare;

    cout << "Enter travel zone (1-3): ";
    cin >> travelZone;

    cout << "Enter passenger type (A for Adult / C for Child): ";
    cin >> passengerType;

    switch (travelZone) {
        case 1:
            ticketFare = 30;
            break;
        case 2:
            ticketFare = 50;
            break;
        case 3:
            ticketFare = 80;
            break;
        default:
            ticketFare = 0;
            cout << "Invalid Zone." << endl;
    }

    if (passengerType == 'C') {
        ticketFare = ticketFare / 2;
    }

    cout << "Ticket Fare = " << ticketFare << endl;

    return 0;
}
