#include <iostream>
using namespace std;

int main() {

    int numbers[3] = {10, 20, 30};     // Integer array
    float prices[3] = {99.5, 150.75, 200.25};    // Float array
    char grades[3] = {'A', 'B', 'C'};    // Character array
    bool status[3] = {true, false, true};    // Boolean array
    string names[3] = {"Aditya", "Rahul", "Aman"};    // String array


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
