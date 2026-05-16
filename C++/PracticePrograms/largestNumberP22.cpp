/*
Program: Largest Number Checker
*/

#include <iostream>
using namespace std;

int main() {
    int firstNumber;
    int secondNumber;

    cout << "Enter two numbers: ";
    cin >> firstNumber >> secondNumber;

    if (firstNumber > secondNumber) {
        cout << firstNumber << " is larger." << endl;
    } else if (secondNumber > firstNumber) {
        cout << secondNumber << " is larger." << endl;
    } else {
        cout << "Both numbers are equal." << endl;
    }

    return 0;
}
