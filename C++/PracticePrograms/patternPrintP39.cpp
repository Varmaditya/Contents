/*
Program: Inverted Triangle Pattern
Description: Prints inverted triangle using nested loops.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = rows; row >= 1; row--) {
        for (int star = 1; star <= row; star++) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
