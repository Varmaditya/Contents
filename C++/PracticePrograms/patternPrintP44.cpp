/*
Program: Alphabet-Number Center Pyramid
Description: Prints centered pyramid with alphabets and numbers.
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
        for (int number = 1; number <= row; number++) {
            cout << number;
        }
        cout << endl;
    }

    return 0;
}
