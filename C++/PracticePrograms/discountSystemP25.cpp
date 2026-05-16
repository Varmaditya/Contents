/*
Program: Online Shopping Discount System
Description: Calculates discount based on shopping amount using else-if ladder.
*/

#include <iostream>
using namespace std;

int main() {
    float shoppingAmount;
    float discount;
    float finalAmount;

    cout << "Enter shopping amount: ";
    cin >> shoppingAmount;

    if (shoppingAmount >= 5000) {
        discount = shoppingAmount * 0.30;
    } else if (shoppingAmount >= 3000) {
        discount = shoppingAmount * 0.20;
    } else if (shoppingAmount >= 1000) {
        discount = shoppingAmount * 0.10;
    } else {
        discount = 0;
    }

    finalAmount = shoppingAmount - discount;

    cout << "\nDiscount = " << discount << endl;
    cout << "Final Amount = " << finalAmount << endl;

    return 0;
}
