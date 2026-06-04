#include <iostream>
#include <string>
using namespace std;

int main() {

    // Variables for student information
    string fullName;
    string city;

    // Taking string input
    cout << "Enter your full name: ";
    getline(cin, fullName);

    cout << "Enter your city: ";
    getline(cin, city);

    // Displaying information
    cout << "\n--- Student Information ---\n";

    cout << "Name: " << fullName << endl;
    cout << "City: " << city << endl;

    return 0;
}