/*
Program: Lucky Number Search
Description: Searches for a lucky number in an array.
*/

#include <iostream>
using namespace std;

int main() {

    int luckyNumbers[10] =
    {7, 12, 25, 30, 45, 56, 68, 77, 89, 99};

    int searchNumber;

    bool found = false;

    cout << "Enter a number to search: ";
    cin >> searchNumber;

    for (int index = 0; index < 10; index++) {

        if (luckyNumbers[index] == searchNumber) {
            found = true;
        }
    }

    if (found) {
        cout << "Lucky Number Found!" << endl;
    }
    else {
        cout << "Lucky Number Not Found!" << endl;
    }

    return 0;
}