#include <iostream>
using namespace std;

void changeValue(int num) {

    cout << "Inside Function Before Change: "
         << num << endl;

    num = 100;

    cout << "Inside Function After Change: "
         << num << endl;

}

int main() {

    int value = 50;

    cout << "Before Function Call: "
         << value << endl;

    changeValue(value);

    cout << "After Function Call: "
         << value << endl;

    return 0;
}