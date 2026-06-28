/*
Program: Email Validator
Description: Checks whether an email address is valid.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {

    string emailAddress;

    cout << "Enter Email Address: ";
    cin >> emailAddress;

    if(emailAddress.find('@') != string::npos && emailAddress.find('.') != string::npos) {
        cout << "\n✅ Valid Email Address";
    } else {
        cout << "\n❌ Invalid Email Address";
    }

    return 0;
}
