#include <iostream>
using namespace std;

int main() {
    int totalSeconds;

    int hours;
    int minutes;
    int remainingSeconds;

    cout << "Enter total seconds: ";
    cin >> totalSeconds;

    hours = totalSeconds / 3600;
    minutes = (totalSeconds % 3600) / 60;
    remainingSeconds = totalSeconds % 60;

    cout << "\nHours = " << hours << endl;
    cout << "Minutes = " << minutes << endl;
    cout << "Seconds = " << remainingSeconds << endl;

    return 0;
}
