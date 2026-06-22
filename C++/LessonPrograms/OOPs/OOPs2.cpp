#include <iostream>
using namespace std;

// Defining a class
class Employee {

public:

    // Data Members
    string name;
    int salary;

    // Member Function
    void display() {
        cout << "\nEmployee Details\n";
        cout << "Name: " << name << endl;
        cout << "Salary: " << salary << endl;
    }
};

int main() {
    // Creating object
    Employee emp1;

    // Assigning values
    emp1.name = "Rahul";
    emp1.salary = 45000;

    // Calling member function
    emp1.display();

    return 0;
}