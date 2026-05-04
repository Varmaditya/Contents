#include <iostream>
using namespace std;

int main() {
    float fahrenheitTemperature;
    float celsiusTemperature;

    cout << "Enter temperature in Fahrenheit: ";
    cin >> fahrenheitTemperature;

    celsiusTemperature = (fahrenheitTemperature - 32) * (5.0 / 9.0);

    cout << "Temperature in Celsius = " << celsiusTemperature << endl;

    return 0;
}
