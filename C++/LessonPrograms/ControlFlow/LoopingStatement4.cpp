#include <iostream>
using namespace std;

int main() {

    // nested loop example 1:
    // Printing square pattern
    cout << "Square Pattern:\n";

    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // nested loop example 2:
    // Multiplication table
    cout << "\nMultiplication Table:\n";

    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << i * j << "\t";
        }
        cout << endl;
    }

    return 0;
}
