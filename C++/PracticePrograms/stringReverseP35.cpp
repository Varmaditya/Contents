/*
Program: Reverse a Given String
Description: Reverses a message using loop.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string message;

    cout << "Enter a message: ";
    getline(cin, message);

    cout << "\nReversed Message:\n";

    for (int index = message.length() - 1; index >= 0; index--) {
        cout << message[index];
    }

    return 0;
}
