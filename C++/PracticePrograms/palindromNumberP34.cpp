/*
Program: Palindrome Number Checker
Description: Checks whether a number is palindrome or not.
*/

#include <iostream>
using namespace std;

int main() {
    int originalNumber;
    int temporaryNumber;
    int reversedNumber = 0;

    int lastDigit;

    cout << "Enter a number: ";
    cin >> originalNumber;

    temporaryNumber = originalNumber;

    while (temporaryNumber > 0) {
        lastDigit = temporaryNumber % 10;
        reversedNumber = (reversedNumber * 10) + lastDigit;
        temporaryNumber = temporaryNumber / 10;
    }

    if (originalNumber == reversedNumber) {
        cout << "\nPalindrome Number." << endl;
    } else {
        cout << "\nNot a Palindrome Number." << endl;
    }

    return 0;
}
