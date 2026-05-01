#include <iostream>
using namespace std;

int main() {
    float basic, hra, da, gross;

    cout << "Enter Basic Salary: ";
    cin >> basic;

    hra = 0.40 * basic;
    da = 0.50 * basic;

    gross = basic + hra + da;

    cout << "Gross Salary = " << gross << endl;

    return 0;
}
