/*
Program: Count Vowels in a String
Description: Counts total vowels present in a message.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {

    string message;

    int vowelCount = 0;

    cout << "Enter a message: ";
    getline(cin, message);

    for (int index = 0; index < message.length(); index++) {
        char currentCharacter = message[index];

        if (currentCharacter == 'a' || currentCharacter == 'e' ||
            currentCharacter == 'i' || currentCharacter == 'o' ||
            currentCharacter == 'u' || currentCharacter == 'A' ||
            currentCharacter == 'E' || currentCharacter == 'I' ||
            currentCharacter == 'O' || currentCharacter == 'U') {
            vowelCount++;
        }
    }

    cout << "\nTotal Vowels = " << vowelCount << endl;

    return 0;
}
