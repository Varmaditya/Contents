#include <iostream>
using namespace std;

int main() {
    float celsiusTemperature, fahrenheitTemperature;

    cout << "Enter temperature in Celsius: ";
    cin >> celsiusTemperature;

    fahrenheitTemperature = (9.0 / 5.0) * celsiusTemperature + 32;

    cout << "Temperature in Fahrenheit = " << fahrenheitTemperature << endl;

    return 0;
}
