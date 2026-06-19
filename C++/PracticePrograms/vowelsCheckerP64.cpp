/*
Program: WhatsApp Message Scanner
Description: Counts vowels using string pointers.
*/

#include <iostream>
using namespace std;

int main() {

    string message;

    cout << "Enter Message:\n";

    getline(cin, message);

    char *messagePointer =
    &message[0];

    int vowelCount = 0;

    while(*messagePointer != '\0') {

        if(*messagePointer == 'a' ||
           *messagePointer == 'e' ||
           *messagePointer == 'i' ||
           *messagePointer == 'o' ||
           *messagePointer == 'u' ||

           *messagePointer == 'A' ||
           *messagePointer == 'E' ||
           *messagePointer == 'I' ||
           *messagePointer == 'O' ||
           *messagePointer == 'U') {

            vowelCount++;
        }

        messagePointer++;
    }

    cout << "\nVowels Found: "
         << vowelCount
         << endl;

    return 0;
}