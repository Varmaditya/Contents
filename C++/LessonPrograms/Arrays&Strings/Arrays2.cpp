#include <iostream>
using namespace std;

int main() {

    int numbers[5];

    // Taking input into array
    cout << "Enter 5 numbers:\n";

    for (int i = 0; i < 5; i++) {
        cin >> numbers[i];
    }

    // Displaying array elements
    cout << "\nElements in the array are:\n";

    for (int i = 0; i < 5; i++) {
        cout << "numbers[" << i << "] = " << numbers[i] << endl;
    }

    return 0;
}
