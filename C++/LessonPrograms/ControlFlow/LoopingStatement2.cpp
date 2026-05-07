#include <iostream>
using namespace std;

int main() {

    // while loop example 1:
    // Printing numbers from 1 to 5
    int i = 1;

    cout << "Numbers from 1 to 5:\n";

    while (i <= 5) {
        cout << i << endl;
        i++;
    }

    // while loop example 2:
    // Countdown
    int count = 5;

    cout << "\nCountdown:\n";

    while (count >= 1) {
        cout << count << endl;
        count--;
    }

    return 0;
}

