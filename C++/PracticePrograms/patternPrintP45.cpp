/*
Program: Number Box Border Pattern
Description: Prints box pattern with numbers on borders.
*/

#include <iostream>
using namespace std;

int main() {

    int size;

    cout << "Enter size: ";
    cin >> size;

    cout << endl;

    for (int row = 1; row <= size; row++) {
        for (int column = 1; column <= size; column++) {
            if (row == 1 || row == size ||
                column == 1 || column == size) {
                cout << column << " ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }

    return 0;
}
