#include <iostream>
using namespace std;

// Recursive Function
void countDown(int n) {

    // Base Case
    if (n == 0) {

        return;

    }

    cout << n << " ";

    // Recursive Call
    countDown(n - 1);

}

int main() {

    int num;

    cout << "Enter a number: ";
    cin >> num;

    cout << "Countdown: ";

    countDown(num);

    return 0;
}