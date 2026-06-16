/*
Program: Password Security Scanner
Description: Evaluates password strength.
*/

#include <iostream>
using namespace std;

int main() {

    string password;

    bool hasDigit = false;
    bool hasSpecialCharacter = false;

    cout << "Enter Password: ";
    cin >> password;

    for(int index = 0; index < password.length(); index++) {

        if(password[index] >= '0' && password[index] <= '9') {
            hasDigit = true;
        }

        if(password[index] == '@' || password[index] == '#' || password[index] == '$' || password[index] == '!') {
            hasSpecialCharacter = true;
        }
    }

    if(password.length() >= 8 && hasDigit && hasSpecialCharacter) {
        cout << "\nStrong Password";
    } else {
        cout << "\nWeak Password";
    }

    return 0;
}
