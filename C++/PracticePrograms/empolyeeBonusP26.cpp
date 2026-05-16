/*
Program: Employee Bonus System
Description: Calculates employee bonus based on experience and performance rating.
*/

#include <iostream>
using namespace std;

int main() {
    int yearsOfExperience;
    int performanceRating;

    float bonusAmount;

    cout << "Enter years of experience: ";
    cin >> yearsOfExperience;

    cout << "Enter performance rating (1 to 5): ";
    cin >> performanceRating;

    if (yearsOfExperience >= 5) {
        if (performanceRating == 5) {
            bonusAmount = 50000;
        } else if (performanceRating >= 3) {
            bonusAmount = 25000;
        } else {
            bonusAmount = 10000;
        }
    } else {
        if (performanceRating >= 4) {
            bonusAmount = 15000;
        } else {
            bonusAmount = 5000;
        }
    }

    cout << "Bonus Amount = " << bonusAmount << endl;

    return 0;
}
