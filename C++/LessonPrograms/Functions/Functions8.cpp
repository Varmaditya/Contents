#include <iostream>
using namespace std;

// Function Declarations
void displayLine();
int add(int a, int b);
int multiply(int a, int b);

int main() {

    displayLine();

    cout << "Addition = "
         << add(10, 20) << endl;

    cout << "Multiplication = "
         << multiply(10, 20) << endl;

    displayLine();

    return 0;
}

// Function Definitions
void displayLine() {

    cout << "---------------------\n";

}

int add(int a, int b) {

    return a + b;

}

int multiply(int a, int b) {

    return a * b;

}