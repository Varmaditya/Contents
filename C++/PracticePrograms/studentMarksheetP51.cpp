/*
Program: Classroom Marks Analyzer
Description: Stores marks of students and calculates total, average, highest, and lowest marks.
*/

#include <iostream>
using namespace std;

int main() {

    int studentMarks[5];

    int totalMarks = 0;
    int highestMarks;
    int lowestMarks;

    cout << "Enter marks of 5 students:\n";

    for (int index = 0; index < 5; index++) {
        cin >> studentMarks[index];
    }

    highestMarks = studentMarks[0];
    lowestMarks = studentMarks[0];

    for (int index = 0; index < 5; index++) {

        totalMarks += studentMarks[index];

        if (studentMarks[index] > highestMarks) {
            highestMarks = studentMarks[index];
        }

        if (studentMarks[index] < lowestMarks) {
            lowestMarks = studentMarks[index];
        }
    }

    cout << "\nTotal Marks = " << totalMarks << endl;
    cout << "Average Marks = " << totalMarks / 5.0 << endl;
    cout << "Highest Marks = " << highestMarks << endl;
    cout << "Lowest Marks = " << lowestMarks << endl;

    return 0;
}