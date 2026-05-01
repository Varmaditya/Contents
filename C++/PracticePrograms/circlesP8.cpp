#include <iostream>
using namespace std;

int main() {
    float radius;
    float areaOfCircle;
    float circumferenceOfCircle;

    cout << "Enter radius of circle: ";
    cin >> radius;

    areaOfCircle = 3.14 * radius * radius;
    circumferenceOfCircle = 2 * 3.14 * radius;

    cout << "\nArea of Circle = " << areaOfCircle << endl;
    cout << "Circumference of Circle = " << circumferenceOfCircle << endl;

    return 0;
}
