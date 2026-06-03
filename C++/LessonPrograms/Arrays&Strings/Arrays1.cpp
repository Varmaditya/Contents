#include <iostream>
using namespace std;

int main() {

    // Declaring an array
    int marks[5];

    // Initializing array elements
    marks[0] = 90;
    marks[1] = 85;
    marks[2] = 78;
    marks[3] = 92;
    marks[4] = 88;

    // Displaying array elements
    cout << "Marks stored in array:\n";

    for (int i = 0; i < 5; i++) {
        cout << "marks[" << i << "] = " << marks[i] << endl;
    }

    return 0;
}
