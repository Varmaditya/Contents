#include <iostream>
using namespace std;

// Parent Class
class Person {

public:

    string name;
    int age;

};

// Child Class
class Student : public Person {

public:

    int rollNo;

};

int main() {

    Student s1;

    // Inherited members
    s1.name = "Aditya";
    s1.age = 23;

    // Own member
    s1.rollNo = 101;

    cout << "Name: " << s1.name << endl;
    cout << "Age: " << s1.age << endl;
    cout << "Roll No: " << s1.rollNo << endl;

    return 0;
}