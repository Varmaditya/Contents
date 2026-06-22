#include <iostream>
using namespace std;

class Student {

private:

    int marks;

public:

    // Setter Function
    void setMarks(int m) {
        marks = m;
    }

    // Getter Function
    int getMarks() {
        return marks;
    }

};

int main() {
    Student s1;

    // Setting value using public function
    s1.setMarks(85);

    cout << "Marks: "  << s1.getMarks();

    return 0;
}