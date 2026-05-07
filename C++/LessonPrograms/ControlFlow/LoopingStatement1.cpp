#include <iostream>
using namespace std;

int main() {

    // for loop example 1:
    // Printing numbers from 1 to 5
    cout << "Numbers from 1 to 5:\n";

    for (int i = 1; i <= 5; i++) {
        cout << i << endl;
    }

    // for loop example 2:
    // Printing even numbers
    cout << "\nEven numbers from 2 to 10:\n";

    for (int i = 2; i <= 10; i += 2) {
        cout << i << endl;
    }

    return 0;
}

