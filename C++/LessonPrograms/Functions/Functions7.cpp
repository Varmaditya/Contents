#include <iostream>
using namespace std;

// Function with default argument
void greet(string name = "Guest") {

    cout << "Welcome "
         << name << endl;

}

int main() {

    // Uses default value
    greet();

    // Uses supplied value
    greet("Aditya");

    greet("Rahul");

    return 0;
}