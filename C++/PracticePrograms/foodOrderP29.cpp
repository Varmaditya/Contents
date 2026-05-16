/*
Program: Food Ordering System
Description: Displays selected food item and calculates bill using switch statement.
*/

#include <iostream>
using namespace std;

int main() {
    int foodChoice;
    int quantity;

    float totalBill;

    cout << "------ MENU ------" << endl;
    cout << "1. Burger - 120" << endl;
    cout << "2. Pizza  - 250" << endl;
    cout << "3. Pasta  - 180" << endl;
    cout << "4. Coffee - 90" << endl;

    cout << "\nEnter food choice: ";
    cin >> foodChoice;

    cout << "Enter quantity: ";
    cin >> quantity;

    switch (foodChoice) {
        case 1:
            totalBill = 120 * quantity;
            cout << "Burger Ordered." << endl;
            break;
        case 2:
            totalBill = 250 * quantity;
            cout << "Pizza Ordered." << endl;
            break;
        case 3:
            totalBill = 180 * quantity;
            cout << "Pasta Ordered." << endl;
            break;
        case 4:
            totalBill = 90 * quantity;
            cout << "Coffee Ordered." << endl;
            break;
        default:
            totalBill = 0;
            cout << "Invalid Food Choice." << endl;
    }

    cout << "Total Bill = " << totalBill << endl;

    return 0;
}
