/*
Program: Movie Ticket Eligibility
Description: Checks ticket eligibility based on age category.
*/

#include <iostream>
using namespace std;

int main() {
    int customerAge;

    cout << "Enter customer age: ";
    cin >> customerAge;

    if (customerAge < 13) {
        cout << "Child Ticket Applicable." << endl;
    } else if (customerAge <= 59) {
        cout << "Adult Ticket Applicable." << endl;
    } else {
        cout << "Senior Citizen Ticket Applicable." << endl;
    }

    return 0;
}
