/*
Program: Login Attempt System
Description: Repeatedly asks for password until correct password is entered.
*/

#include <iostream>
using namespace std;

int main() {
    string enteredPassword;

    while (enteredPassword != "cpp@123") {
        cout << "Enter Password: ";
        cin >> enteredPassword;

        if (enteredPassword != "cpp@123") {
            cout << "Wrong Password. Try Again.\n" << endl;
        }
    }

    cout << "\nLogin Successful!" << endl;

    return 0;
}
