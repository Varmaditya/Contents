/*
Program: Right Triangle Star Pattern
Description: Prints right triangle star pattern using nested loops.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = 1; row <= rows; row++) {
        for (int star = 1; star <= row; star++) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
