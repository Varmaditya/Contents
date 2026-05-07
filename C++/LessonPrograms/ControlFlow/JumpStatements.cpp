#include <iostream>
using namespace std;

int main() {

    // -------- break Statement --------
    cout << "Break Statement:\n";

    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            break;
        }
        cout << i << " ";
    }

    // -------- continue Statement --------
    cout << "\n\nContinue Statement:\n";

    for (int i = 1; i <= 5; i++) {
        if (i == 3) {
            continue;
        }
        cout << i << " ";
    }

    // -------- goto Statement --------
    cout << "\n\nGoto Statement:\n";

    goto message;

    cout << "This line will be skipped\n";
    cout << "This line will be skipped\n";
    cout << "This line will be skipped\n";

message:
    cout << "Control jumped using goto";

    // -------- return Statement --------
    cout << "\n\nReturn Statement:\n";

    int num = -5;

    if (num < 0) {
        cout << "Negative number detected. Program ending...\n";
        return 0;
    }

    cout << "This line will not execute";

    return 0;
}
