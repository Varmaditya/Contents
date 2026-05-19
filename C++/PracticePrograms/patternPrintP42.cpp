/*
Program: Palindromic Number Pattern
Description: Prints palindromic number pyramid pattern.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = 1; row <= rows; row++) {
        for (int space = 1; space <= rows - row; space++) {
            cout << "  ";
        }
        for (int number = row; number >= 1; number--) {
            cout << number << " ";
        }
        for (int number = 2; number <= row; number++) {
            cout << number << " ";
        }
        cout << endl;
    }

    return 0;
}
