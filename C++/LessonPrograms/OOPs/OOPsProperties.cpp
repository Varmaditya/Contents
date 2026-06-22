#include <iostream>
using namespace std;

// Parent Class
class Person {

protected:

    string name;

public:

    void setName(string n) {
        name = n;
    }

};

// Child Class
class Student : public Person {

private:

    int marks;

public:

    void setMarks(int m) {
        marks = m;
    }

    void display() {
        cout << "Name: " << name << endl;
        cout << "Marks: " << marks << endl;
    }

};

int main() {

    Student s1;

    s1.setName("Aditya");
    s1.setMarks(90);

    s1.display();

    return 0;
}