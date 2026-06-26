/*
Program: Smart Restaurant Billing System
Description: Uses multiple functions to prepare a restaurant bill.
*/

#include <iostream>
#include <iomanip>
using namespace std;

// Display menu
void displayMenu() {
    cout << "=========== MENU ===========" << endl;
    cout << "1. Burger    ₹120" << endl;
    cout << "2. Pizza     ₹250" << endl;
    cout << "3. Pasta     ₹180" << endl;
    cout << "4. Coffee    ₹90" << endl;
    cout << "============================" << endl;
l
}

// Calculate bill
int calculateBill(int price, int quantity) {
    return price * quantity;
}

// Apply discount
float applyDiscount(float totalBill) {
    if(totalBill >= 500)
        return totalBill * 0.10;

    return 0;
}

// Print receipt
void printReceipt(float totalBill,
                  float discount,
                  float finalBill) {
    cout << "\n========= RECEIPT =========\n";

    cout << "Total Bill : ₹"  << totalBill << endl;
    cout << "Discount : ₹" << discount << endl;
    cout << "Final Bill : ₹" << finalBill << endl;
}

int main() {
    int prices[4]={120,250,180,90};

    int foodChoice;
    int quantity;

    displayMenu();

    cout<<"Choose Food : ";
    cin>>foodChoice;

    cout<<"Quantity : ";
    cin>>quantity;

    float totalBill =
    calculateBill(prices[foodChoice-1],quantity);

    float discount =
    applyDiscount(totalBill);

    printReceipt(totalBill, discount, totalBill-discount);
}