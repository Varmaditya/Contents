#include <iostream>
using namespace std;

int main() {
    int years;
    float principal, rate, simpleInterest;

    cout << "Enter Principal Amount: ";
    cin >> principal;

    cout << "Enter Number of Years: ";
    cin >> years;

    cout << "Enter Rate of Interest: ";
    cin >> rate;

    simpleInterest = (principal * years * rate) / 100;

    cout << "Simple Interest = " << simpleInterest << endl;

    return 0;
}
