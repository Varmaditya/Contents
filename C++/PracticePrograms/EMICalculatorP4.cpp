#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float principal, rate, time, emi;

    cout << "Enter Principal Amount: ";
    cin >> principal;

    cout << "Enter Rate of Interest: ";
    cin >> rate;

    cout << "Enter Time (in years): ";
    cin >> time;

    rate = rate / (12 * 100);
    time = time * 12;

    emi = (principal * rate * pow(1 + rate, time)) / (pow(1 + rate, time) - 1);

    cout << "Monthly EMI = " << emi << endl;

    return 0;
}
