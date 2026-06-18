#include <iostream>
using namespace std;

int main() {
    int num = 100;

    // Pointer storing address of num
    int *ptr = &num;

    cout << "Value of num: " << num << endl;
    cout << "Address stored in ptr: " << ptr << endl;

    return 0;
}
