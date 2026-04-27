#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    // -------- Basic Input using cin --------
    string name;
    int age;
    float marks;

    cout << "Enter your name (single word): ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Enter your marks: ";
    cin >> marks;

    // -------- Displaying Output --------
    cout << "\n--- Student Details ---\n";
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Marks: " << marks << endl;

    // -------- Calculation --------
    int nextAge = age + 1;
    cout << "Next year, you will be: " << nextAge << endl;

    // -------- getline() Example --------
    string fullName;

    cin.ignore(); // clear buffer before getline

    cout << "\nEnter your full name: ";
    getline(cin, fullName);

    cout << "Full Name: " << fullName << endl;

    // -------- Formatting Output --------
    float value = 3.14159;

    cout << "\nWithout formatting: " << value << endl;

    cout << "Using setprecision(3): "
         << setprecision(3) << value << endl;

    cout << "Using fixed and setprecision(2): "
         << fixed << setprecision(2) << value << endl;

    // -------- setw() Example --------
    cout << "\nUsing setw():\n";
    cout << setw(10) << 100 << endl;
    cout << setw(10) << 200 << endl;

    // -------- cerr Example --------
    cerr << "\nError: This is a sample error message\n";

    // -------- clog Example --------
    clog << "Log: Program executed successfully\n";

    return 0;
}
