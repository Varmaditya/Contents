#include <iostream>
using namespace std;

class Calculator {

public:

    // Function 1
    int add(int a, int b) {
        return a + b;
    }

    // Function 2
    float add(float a, float b) {
        return a + b;
    }

};

int main() {

    Calculator calc;

    cout << "Integer Addition: " << calc.add(10, 20) << endl;

    cout << "Float Addition: " << calc.add(10.5f, 20.5f) << endl;

    return 0;
}