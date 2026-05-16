/*
Program: simple Login System
*/

#include <iostream>
using namespace std;

int main() {
    string enteredPassword;

    cout << "Enter password: ";
    cin >> enteredPassword;

    if (enteredPassword == "cpp123") {
        cout << "Login Successful." << endl;
    } else {
        cout << "Incorrect Password." << endl;
    }

    return 0;
}
