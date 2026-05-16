/*
Program: Smart Calculator
Description: Performs arithmetic operations using switch statement.
*/

#include <iostream>
using namespace std;

int main() {
    float firstNumber;
    float secondNumber;
    char operation;

    cout << "Enter first number: ";
    cin >> firstNumber;

    cout << "Enter operation (+, -, *, /): ";
    cin >> operation;

    cout << "Enter second number: ";
    cin >> secondNumber;

    switch (operation) {
        case '+':
            cout << "Result = " << firstNumber + secondNumber << endl;
            break;
        case '-':
            cout << "Result = " << firstNumber - secondNumber << endl;
            break;
        case '*':
            cout << "Result = " << firstNumber * secondNumber << endl;
            break;
        case '/':
            cout << "Result = " << firstNumber / secondNumber << endl;
            break;
        default:
            cout << "Invalid Operation." << endl;
    }

    return 0;
}
