/*
Program: Hollow Pyramid Pattern
Description: Prints hollow star pyramid using nested loops.
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
            cout << " ";
        }

        for (int column = 1; column <= (2 * row - 1); column++) {
            if (column == 1 || column == (2 * row - 1) || row == rows) {
                cout << "*";
            } else {
                cout << " ";
            }
        }

        cout << endl;
    }

    return 0;
}
