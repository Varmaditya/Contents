/*
Program: Character Type Counter
Description: Counts alphabets, digits, and spaces in a message.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {

    string message;

    int alphabetCount = 0;
    int digitCount = 0;
    int spaceCount = 0;

    cout << "Enter a message: ";
    getline(cin, message);

    for (int index = 0; index < message.length(); index++) {
        char currentCharacter = message[index];

        if ((currentCharacter >= 'A' && currentCharacter <= 'Z') || (currentCharacter >= 'a' && currentCharacter <= 'z')) {
            alphabetCount++;
        } else if (currentCharacter >= '0' && currentCharacter <= '9') {
            digitCount++;
        } else if (currentCharacter == ' ') {
            spaceCount++;
        }
    }

    cout << "\nAlphabets = " << alphabetCount << endl;
    cout << "Digits = " << digitCount << endl;
    cout << "Spaces = " << spaceCount << endl;

    return 0;
}
