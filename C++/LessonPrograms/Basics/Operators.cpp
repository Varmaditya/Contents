#include <iostream>
using namespace std;

int main() {

    int a = 10, b = 5;

    // -------- Arithmetic Operators --------
    cout << "Arithmetic Operators:\n";
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    cout << "a / b = " << a / b << endl;
    cout << "a % b = " << a % b << endl;

    // -------- Relational Operators --------
    cout << "\nRelational Operators:\n";
    cout << "a > b: " << (a > b) << endl;
    cout << "a < b: " << (a < b) << endl;
    cout << "a == b: " << (a == b) << endl;
    cout << "a != b: " << (a != b) << endl;

    // -------- Logical Operators --------
    cout << "\nLogical Operators:\n";
    cout << "(a > 5 && b < 10): " << (a > 5 && b < 10) << endl;
    cout << "(a < 5 || b < 10): " << (a < 5 || b < 10) << endl;
    cout << "!(a > b): " << !(a > b) << endl;

    // -------- Assignment Operators --------
    cout << "\nAssignment Operators:\n";
    int x = 10;
    x += 5;
    cout << "x += 5: " << x << endl;

    x -= 3;
    cout << "x -= 3: " << x << endl;

    x *= 2;
    cout << "x *= 2: " << x << endl;

    x /= 4;
    cout << "x /= 4: " << x << endl;

    // -------- Increment / Decrement --------
    cout << "\nIncrement / Decrement:\n";
    int y = 5;
    cout << "y = " << y << endl;
    cout << "y++ = " << y++ << endl;  // post-increment
    cout << "After y++: " << y << endl;

    cout << "++y = " << ++y << endl;  // pre-increment
    cout << "After ++y: " << y << endl;

    // -------- Bitwise Operators --------
    cout << "\nBitwise Operators:\n";
    cout << "a & b = " << (a & b) << endl;
    cout << "a | b = " << (a | b) << endl;
    cout << "a ^ b = " << (a ^ b) << endl;
    cout << "~a = " << (~a) << endl;
    cout << "a << 1 = " << (a << 1) << endl;
    cout << "a >> 1 = " << (a >> 1) << endl;

    // -------- Conditional (Ternary) Operator --------
    cout << "\nTernary Operator:\n";
    int max = (a > b) ? a : b;
    cout << "Max of a and b: " << max << endl;

    // -------- sizeof Operator --------
    cout << "\nSizeof Operator:\n";
    cout << "Size of int: " << sizeof(a) << " bytes" << endl;
    cout << "Size of float: " << sizeof(float) << " bytes" << endl;

    // -------- Comma Operator --------
    cout << "\nComma Operator:\n";
    int m;
    m = (a = 3, b = 4, a + b);
    cout << "Result using comma operator: " << m << endl;

    // -------- Address-of Operator --------
    cout << "\nAddress-of Operator:\n";
    cout << "Address of a: " << &a << endl;

    return 0;
}
