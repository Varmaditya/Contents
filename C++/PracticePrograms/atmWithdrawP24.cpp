/*
Program: Smart ATM Security System
Description: Allows withdrawal only if PIN is correct and balance is sufficient.
*/

#include <iostream>
using namespace std;

int main() {
    int enteredPin;
    float accountBalance;
    float withdrawalAmount;

    cout << "Enter ATM PIN: ";
    cin >> enteredPin;

    if (enteredPin == 1234) {
        cout << "Enter account balance: ";
        cin >> accountBalance;

        cout << "Enter withdrawal amount: ";
        cin >> withdrawalAmount;

        if (withdrawalAmount <= accountBalance) {
            cout << "Withdrawal Successful." << endl;
            cout << "Remaining Balance = "
                 << accountBalance - withdrawalAmount << endl;
        } else {
            cout << "Insufficient Balance." << endl;
        }

    } else {
        cout << "Incorrect PIN." << endl;
    }

    return 0;
}
