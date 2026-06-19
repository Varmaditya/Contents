/*
Program: String Encryption System
Description: Encrypts a message using pointer manipulation.
*/

#include <iostream>
using namespace std;

int main() {

    string message;

    cout << "Enter Message: ";
    getline(cin, message);

    char *characterPointer =
    &message[0];

    while(*characterPointer != '\0') {

        *characterPointer =
        *characterPointer + 3;

        characterPointer++;
    }

    cout << "\nEncrypted Message:\n";

    cout << message;

    return 0;
}