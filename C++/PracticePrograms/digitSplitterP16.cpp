#include <iostream>
using namespace std;

int main() {
    int number;

    int hundredsDigit;
    int tensDigit;
    int unitsDigit;

    cout << "Enter a 3-digit number: ";
    cin >> number;

    hundredsDigit = number / 100;
    tensDigit = (number / 10) % 10;
    unitsDigit = number % 10;

    cout << "\nHundreds = " << hundredsDigit << endl;
    cout << "Tens = " << tensDigit << endl;
    cout << "Units = " << unitsDigit << endl;

    return 0;
}
