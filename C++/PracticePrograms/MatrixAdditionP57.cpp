/*
Program: Matrix Addition Calculator
Description: Adds two matrices and displays result.
*/

#include <iostream>
using namespace std;

int main() {

    int firstMatrix[3][3];
    int secondMatrix[3][3];
    int resultMatrix[3][3];

    cout << "Enter First Matrix:\n";

    for(int row = 0; row < 3; row++) {

        for(int column = 0; column < 3; column++) {

            cin >> firstMatrix[row][column];
        }
    }

    cout << "\nEnter Second Matrix:\n";

    for(int row = 0; row < 3; row++) {

        for(int column = 0; column < 3; column++) {

            cin >> secondMatrix[row][column];
        }
    }

    for(int row = 0; row < 3; row++) {

        for(int column = 0; column < 3; column++) {

            resultMatrix[row][column] =
            firstMatrix[row][column] +
            secondMatrix[row][column];
        }
    }

    cout << "\nResult Matrix\n\n";

    for(int row = 0; row < 3; row++) {

        for(int column = 0; column < 3; column++) {

            cout << resultMatrix[row][column]
                 << " ";
        }

        cout << endl;
    }

    return 0;
}