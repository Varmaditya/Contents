#include <iostream>
using namespace std;

// Function Declaration
void greet();

int main() {

    cout << "Inside main()\n";

    // Function Call
    greet();

    cout << "Back to main()\n";

    return 0;
}

// Function Definition
void greet() {

    cout << "Welcome to C++ Functions!\n";

}