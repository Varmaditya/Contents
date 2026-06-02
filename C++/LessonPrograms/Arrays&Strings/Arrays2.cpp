#include <iostream>
using namespace std;

int main() {

    // Integer array
    int numbers[3] = {10, 20, 30};

    // Float array
    float prices[3] = {99.5, 150.75, 200.25};

    // Character array
    char grades[3] = {'A', 'B', 'C'};

    // Boolean array
    bool status[3] = {true, false, true};

    // String array
    string names[3] = {"Aditya", "Rahul", "Aman"};

    // Displaying integer array
    cout << "Integer Array:\n";

    for (int i = 0; i < 3; i++) {
        cout << numbers[i] << endl;
    }

    // Displaying float array
    cout << "\nFloat Array:\n";

    for (int i = 0; i < 3; i++) {
        cout << prices[i] << endl;
    }

    // Displaying character array
    cout << "\nCharacter Array:\n";

    for (int i = 0; i < 3; i++) {
        cout << grades[i] << endl;
    }

    // Displaying boolean array
    cout << "\nBoolean Array:\n";

    for (int i = 0; i < 3; i++) {
        cout << status[i] << endl;
    }

    // Displaying string array
    cout << "\nString Array:\n";

    for (int i = 0; i < 3; i++) {
        cout << names[i] << endl;
    }

    return 0;
}