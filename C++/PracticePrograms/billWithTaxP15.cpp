#include <iostream>
using namespace std;

int main() {
    float productPrice;
    float taxRate;

    float taxAmount;
    float totalBill;

    cout << "Enter product price: ";
    cin >> productPrice;

    cout << "Enter tax rate (%): ";
    cin >> taxRate;

    taxAmount = (productPrice * taxRate) / 100;
    totalBill = productPrice + taxAmount;

    cout << "\nTax Amount = " << taxAmount << endl;
    cout << "Total Bill = " << totalBill << endl;

    return 0;
}
