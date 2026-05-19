/*
Program: Sum of Given Integers
Description: Calculates sum of numbers entered by user.
*/

#include <iostream>
using namespace std;

int main() {
    int totalNumbers;
    int currentNumber;

    int sum = 0;

    cout << "How many numbers do you want to add? ";
    cin >> totalNumbers;

    for (int counter = 1; counter <= totalNumbers; counter++) {
        cout << "Enter Number " << counter << ": ";
        cin >> currentNumber;
        sum += currentNumber;
    }

    cout << "\nTotal Sum = " << sum << endl;

    return 0;
}
