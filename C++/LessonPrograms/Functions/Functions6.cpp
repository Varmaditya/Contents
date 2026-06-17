#include <iostream>
using namespace std;

// Inline Function
inline int square(int num) {

    return num * num;

}

int main() {

    cout << "Square of 5 = "
         << square(5) << endl;

    cout << "Square of 10 = "
         << square(10) << endl;

    return 0;
}