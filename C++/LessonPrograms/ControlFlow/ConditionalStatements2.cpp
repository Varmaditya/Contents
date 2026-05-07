#include <iostream>
using namespace std;

int main() {

    int marks, num;

    // else-if ladder statement example:
    cout << "Enter your marks: ";
    cin >> marks;

    // Checking grades
    if (marks >= 90) {
        cout << "Grade A";
    } else if (marks >= 75) {
        cout << "Grade B";
    } else if (marks >= 50) {
        cout << "Grade C";
    } else {
        cout << "Fail";
    }

    // Nested if-else statement example:
    cout << "Enter a number: ";
    cin >> num;

    // Outer if
    if (num > 0) {
        // Inner if
        if (num % 2 == 0) {
            cout << "Positive Even Number";
        } else {
            cout << "Positive Odd Number";
        }
    } else {
        cout << "Number is Zero or Negative";
    }

    return 0;
}

