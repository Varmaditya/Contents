/*
Program: Shopping Cart System
Description: Calculates shopping bill from multiple products.
*/

#include <iostream>
using namespace std;

int main() {

    string productNames[5];
    float productPrices[5];

    float totalBill = 0;

    cout << "Enter Product Name and Price:\n";

    for(int index = 0; index < 5; index++) {

        cin >> productNames[index];
        cin >> productPrices[index];

        totalBill += productPrices[index];
    }

    cout << "\n----- CART -----\n";

    for(int index = 0; index < 5; index++) {

        cout << productNames[index]
             << " - ₹"
             << productPrices[index]
             << endl;
    }

    cout << "\nTotal Bill = ₹"
         << totalBill << endl;

    return 0;
}