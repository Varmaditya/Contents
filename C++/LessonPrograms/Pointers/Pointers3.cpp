#include <iostream>
using namespace std;

int main() {
    int marks = 95;
    int *ptr = &marks;

    cout << "Value of marks: " << marks << endl;
    cout << "Address of marks: " << ptr << endl;
    cout << "Value using pointer: " << *ptr << endl;

    return 0;
}
