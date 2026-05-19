/*
Program: Floyd's Triangle
Description: Prints Floyd's number pattern using nested loops.
*/

#include <iostream>
using namespace std;

int main() {

    int rows;
    int currentNumber = 1;

    cout << "Enter number of rows: ";
    cin >> rows;

    cout << endl;

    for (int row = 1; row <= rows; row++) {
        for (int column = 1; column <= row; column++) {
            cout << currentNumber << " ";
            currentNumber++;
        }
        cout << endl;
    }

    return 0;
}
