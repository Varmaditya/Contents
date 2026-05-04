#include <iostream>
using namespace std;

int main() {
    float distanceInKilometers;

    float distanceInMeters;
    float distanceInCentimeters;
    float distanceInFeet;
    float distanceInInches;

    cout << "Enter distance in kilometers: ";
    cin >> distanceInKilometers;

    distanceInMeters = distanceInKilometers * 1000;
    distanceInCentimeters = distanceInKilometers * 100000;
    distanceInFeet = distanceInKilometers * 3280.84;
    distanceInInches = distanceInKilometers * 39370.1;

    cout << "\nDistance in Meters = " << distanceInMeters << endl;
    cout << "Distance in Centimeters = " << distanceInCentimeters << endl;
    cout << "Distance in Feet = " << distanceInFeet << endl;
    cout << "Distance in Inches = " << distanceInInches << endl;

    return 0;
}
