/*
Program: Alternating Number Triangle
Description: Prints alternating 0 and 1 triangle pattern.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = 1; row <= rows; row++) {

        for (int column = 1; column <= row; column++) {
            if ((row + column) % 2 == 0) {
                cout << "1 ";
            } else {
                cout << "0 ";
            }
        }

        cout << endl;
    }

    return 0;
}
