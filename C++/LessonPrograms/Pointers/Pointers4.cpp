#include <iostream>
using namespace std;

int main() {
    int salary = 25000;
    int *ptr = &salary;

    cout << "Before Change: " << salary << endl;

    // Changing value through pointer
    *ptr = 30000;

    cout << "After Change: " << salary << endl;

    return 0;
}
