#include <iostream>
using namespace std;

// Defining a class
class Student {

public:
    // Data Members
    string name;
    int age;
    float marks;

};

int main() {
    // Creating an object of Student class
    Student s1;

    // Assigning values to object members
    s1.name = "Aditya";
    s1.age = 23;
    s1.marks = 85.5;

    // Displaying object data
    cout << "Student Details\n";
    cout << "Name: " << s1.name << endl;
    cout << "Age: " << s1.age << endl;
    cout << "Marks: " << s1.marks << endl;

    return 0;
}