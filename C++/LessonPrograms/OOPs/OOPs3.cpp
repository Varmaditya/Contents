#include <iostream>
using namespace std;

class Student {

public:

    // Accessible everywhere
    string name;

private:

    // Accessible only inside the class
    int marks;

protected:

    // Accessible inside class and derived classes
    int rollNo;

public:

    // Public member function
    void setData() {

        // Private and protected members
        // can be accessed inside the class

        marks = 90;
        rollNo = 101;

    }

    void displayData() {

        cout << "Name: " << name << endl;
        cout << "Marks: " << marks << endl;
        cout << "Roll No: " << rollNo << endl;

    }

};

int main() {

    Student s1;

    // Public member can be accessed directly
    s1.name = "Aman";

    // Setting values using member function
    s1.setData();

    // Displaying data
    s1.displayData();

    /*
    The following statements will cause errors:

    s1.marks = 90;     // Private member
    s1.rollNo = 101;   // Protected member
    */

    return 0;
}