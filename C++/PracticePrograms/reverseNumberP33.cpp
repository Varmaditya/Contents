/*
Program: Reverse Number Generator
Description: Reverses a given number using while loop.
*/

#include <iostream>
using namespace std;

int main() {
    int originalNumber;
    int reversedNumber = 0;

    int lastDigit;

    cout << "Enter a number: ";
    cin >> originalNumber;

    while (originalNumber > 0) {
        lastDigit = originalNumber % 10;
        reversedNumber = (reversedNumber * 10) + lastDigit;
        originalNumber = originalNumber / 10;
    }

    cout << "\nReversed Number = " << reversedNumber << endl;

    return 0;
}
