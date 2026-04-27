#include <iostream>
using namespace std;

int main() {

    // -------- Type Casting --------

    int a = 10, b = 3;

    // Without type casting
    float result1 = a / b;
    cout << "Without Type Casting: " << result1 << endl;

    // With type casting
    float result2 = (float)a / b;
    cout << "With Type Casting: " << result2 << endl;

    // Explicit type casting
    float x = 5.7;
    int y = (int)x;
    cout << "Float to Int: " << y << endl;

    // -------- Type Modifiers --------

    short int smallNum = 100;
    long int bigNum = 2000000000;

    unsigned int positiveNum = 40000;
    signed int negativeNum = -200;

    unsigned char ch = 250;

    // Displaying modified types
    cout << "Short int: " << smallNum << endl;
    cout << "Long int: " << bigNum << endl;
    cout << "Unsigned int: " << positiveNum << endl;
    cout << "Signed int: " << negativeNum << endl;
    cout << "Unsigned char: " << (int)ch << endl;

    return 0;
}
