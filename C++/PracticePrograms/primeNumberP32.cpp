/*
Program: Prime Number Checker
Description: Checks whether a number is prime or not using loop.
*/

#include <iostream>
using namespace std;

int main() {
    int number;
    int divisorCount = 0;

    cout << "Enter a number: ";
    cin >> number;

    for (int divisor = 1; divisor <= number; divisor++) {
        if (number % divisor == 0) {
            divisorCount++;
        }
    }

    if (divisorCount == 2) {
        cout << "\nPrime Number." << endl;
    } else {
        cout << "\nNot a Prime Number." << endl;
    }

    return 0;
}
