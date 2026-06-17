#include <iostream>
using namespace std;

// Function returning an integer
int add(int a, int b) {

    return a + b;

}

int main() {

    int result;

    result = add(10, 20);

    cout << "Sum = " << result << endl;

    return 0;
}