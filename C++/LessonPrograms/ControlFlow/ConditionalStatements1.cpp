#include <iostream>
using namespace std;

int main() {

    int age, num;

    // if statement example:
    cout << "Enter your age: ";
    cin >> age;

    // Checking condition
    if (age >= 18) {
        cout << "You are eligible to vote.";
    }

    // if-else statement example:
    cout << "Enter a number: ";
    cin >> num;

    // Checking even or odd
    if (num % 2 == 0) {
        cout << "The number is Even.";
    } else {
        cout << "The number is Odd.";
    }

    return 0;
}

