#include <iostream>
using namespace std;

int main() {
    float timeInHours;

    float timeInMinutes;
    float timeInSeconds;

    cout << "Enter time in hours: ";
    cin >> timeInHours;

    timeInMinutes = timeInHours * 60;
    timeInSeconds = timeInHours * 3600;

    cout << "\nTime in Minutes = " << timeInMinutes << endl;
    cout << "Time in Seconds = " << timeInSeconds << endl;

    return 0;
}
