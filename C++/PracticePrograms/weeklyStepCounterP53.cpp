/*
Program: Weekly Step Counter
Description: Stores daily walking steps and finds total steps walked.
*/

#include <iostream>
using namespace std;

int main() {

    int dailySteps[7];
    int totalSteps = 0;

    cout << "Enter steps walked for 7 days:\n";

    for(int day = 0; day < 7; day++) {
        cin >> dailySteps[day];
    }

    for(int day = 0; day < 7; day++) {
        totalSteps += dailySteps[day];
    }

    cout << "\nTotal Steps Walked = "
         << totalSteps << endl;

    return 0;
}