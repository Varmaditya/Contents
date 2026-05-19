/*
Program: Factorial Calculator
Description: Calculates factorial of a number using for loop.
*/

#include <iostream>
using namespace std;

int main() {
    int number;
    long long factorial = 1;

    cout << "Enter a number: ";
    cin >> number;

    for (int counter = 1; counter <= number; counter++) {
        factorial = factorial * counter;
    }

    cout << "\nFactorial = " << factorial << endl;

    return 0;
}
