/*
Program: Length of Message
Description: Finds total number of characters in a message.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string message;

    cout << "Enter a message: ";
    getline(cin, message);

    int messageLength = 0;

    while (message[messageLength] != '\0') {
        messageLength++;
    }

    cout << "\nLength of Message = " << messageLength << endl;

    return 0;
}
