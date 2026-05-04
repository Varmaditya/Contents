#include <iostream>
using namespace std;

int main() {
    float celsiusTemperature;
    float kelvinTemperature;

    cout << "Enter temperature in Celsius: ";
    cin >> celsiusTemperature;

    kelvinTemperature = celsiusTemperature + 273.15;

    cout << "Temperature in Kelvin = " << kelvinTemperature << endl;

    return 0;
}
