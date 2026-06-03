#include <iostream>
using namespace std;

int main() {

    // Initializing a 2D array
    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // Displaying the 2D array
    cout << "Elements of 2D Array:\n";

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
