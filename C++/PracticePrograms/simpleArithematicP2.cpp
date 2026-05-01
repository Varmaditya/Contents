#include <iostream>
using namespace std;

int main() {
    int a, b, c;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    c = a + b;
    cout << "Sum = " << c << endl;

    c = a - b;
    cout << "Difference = " << c << endl;

    c = a * b;
    cout << "Product = " << c << endl;

    c = a / b;
    cout << "Division = " << c << endl;

    return 0;
}
