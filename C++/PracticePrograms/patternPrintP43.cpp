/*
Program: Alphabet Diamond Pattern
Description: Prints alphabet diamond using nested loops.
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
        for (char alphabet = 'A'; alphabet < 'A' + row; alphabet++) {
            cout << alphabet;
        }
        for (char alphabet = 'A' + row - 2; alphabet >= 'A'; alphabet--) {
            cout << alphabet;
        }
        cout << endl;
    }

    for (int row = rows - 1; row >= 1; row--) {
        for (int space = 1; space <= rows - row; space++) {
            cout << " ";
        }
        for (char alphabet = 'A'; alphabet < 'A' + row; alphabet++) {
            cout << alphabet;
        }
        for (char alphabet = 'A' + row - 2; alphabet >= 'A'; alphabet--) {
            cout << alphabet;
        }
        cout << endl;
    }

    return 0;
}
