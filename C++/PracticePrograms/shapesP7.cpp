#include <iostream>
using namespace std;

int main() {
    // Square
    float squareSide, squareArea;

    cout << "Enter side of square: ";
    cin >> squareSide;

    squareArea = squareSide * squareSide;

    cout << "Area of Square = " << squareArea << endl;

    // Triangle
    float triangleBase, triangleHeight, triangleArea;

    cout << "\nEnter base of triangle: ";
    cin >> triangleBase;

    cout << "Enter height of triangle: ";
    cin >> triangleHeight;

    triangleArea = 0.5 * triangleBase * triangleHeight;

    cout << "Area of Triangle = " << triangleArea << endl;

    // Rectangle
    float rectangleLength, rectangleWidth, rectangleArea;

    cout << "\nEnter length of rectangle: ";
    cin >> rectangleLength;

    cout << "Enter width of rectangle: ";
    cin >> rectangleWidth;

    rectangleArea = rectangleLength * rectangleWidth;

    cout << "Area of Rectangle = " << rectangleArea << endl;

    return 0;
}
