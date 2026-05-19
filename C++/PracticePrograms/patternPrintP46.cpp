/*
Program: Checkerboard Pattern
Description: Prints checkerboard style pattern using conditionals.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = 1; row <= rows; row++) {
        for (int column = 1; column <= rows; column++) {
            if ((row + column) % 2 == 0) {
                cout << "X ";
            } else {
                cout << "O ";
            }
        }
        cout << endl;
    }

    return 0;
}
