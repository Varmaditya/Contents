/*
Program: Amazon Product Finder
Description: Searches product and calculates discounted price.
*/

#include <iostream>
using namespace std;

int main() {

    string products[5] = {"Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"};

    int prices[5] = {65000, 800, 1500, 12000, 25000};
    int discount[5] = {10, 5, 8, 12,15};

    string searchProduct;

    cout << "Enter Product Name: ";
    cin >> searchProduct;

    for(int index = 0; index < 5; index++) {
        if(searchProduct == products[index]) {

            int finalPrice = prices[index] - (prices[index] * discount[index] / 100);

            cout << "\nProduct Found\n";

            cout << "Price : $" << prices[index] << endl;
            cout << "Discount : " << discount[index] << "%" << endl;
            cout << "Final Price : $" << finalPrice << endl;
        }
    }

    return 0;
}
