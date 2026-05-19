/*
Program: Number Triangle Pattern
Description: Prints increasing number triangle pattern.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = 1; row <= rows; row++) {
        for (int number = 1; number <= row; number++) {
            cout << number << " ";
        }
        cout << endl;
    }

    return 0;
}
