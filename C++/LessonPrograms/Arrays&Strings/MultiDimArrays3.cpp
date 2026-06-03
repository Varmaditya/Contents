#include <iostream>
using namespace std;

int main() {

    int matrix[2][3];

    // Taking input
    cout << "Enter elements for 2D array:\n";

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> matrix[i][j];
        }
    }

    // Displaying output
    cout << "\nElements of the 2D Array:\n";

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
