#include <iostream>
using namespace std;

// Recursive Function
int sum(int n) {
    // Base Case
    if (n == 1) {
        return 1;
    }

    // Recursive Case
    return n + sum(n - 1);
}

int main() {
    int num;

    cout << "Enter a number: ";
    cin >> num;
    cout << "Sum = " << sum(num);

    return 0;
}
