#include <iostream>
using namespace std;

// Preprocessor constant
#define DAYS 7

int main() {

    // Declaration
    int age;
    float salary;
    char grade;

    // Assignment
    age = 21;
    salary = 55000.0;
    grade = 'A';

    // Initialization
    int year = 2025;
    float pi = 3.14;
    char section = 'B';

    // Constant using const
    const float PI = 3.14159;

    // Using variables
    cout << "Age: " << age << endl;
    cout << "Salary: " << salary << endl;
    cout << "Grade: " << grade << endl;

    cout << "Year: " << year << endl;
    cout << "Pi: " << pi << endl;
    cout << "Section: " << section << endl;

    // Using constants
    cout << "Days in a week (#define): " << DAYS << endl;
    cout << "Value of PI (const): " << PI << endl;

    return 0;
}