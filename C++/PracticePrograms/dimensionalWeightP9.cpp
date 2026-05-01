#include <iostream>
using namespace std;

int main() {
    int boxLength, boxWidth, boxHeight;
    int volume, dimensionalWeight;

    cout << "Enter length of box: ";
    cin >> boxLength;

    cout << "Enter width of box: ";
    cin >> boxWidth;

    cout << "Enter height of box: ";
    cin >> boxHeight;

    volume = boxLength * boxWidth * boxHeight;

    dimensionalWeight = (volume + 165) / 166;

    cout << "\nVolume of Box = " << volume << endl;
    cout << "Dimensional Weight = " << dimensionalWeight << endl;

    return 0;
}
