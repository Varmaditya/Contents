#include <stdio.h>

int main() {

    // Declaration
    int age;
    float salary;
    char grade;

    // Assignment
    age = 21;
    salary = 55000.0f;
    grade = 'A';

    // Initialization (declaration + value together)
    int year = 2025;
    float pi = 3.14f;
    char section = 'B';

    // Using and printing variables
    printf("Age: %d\n", age);
    printf("Salary: %.2f\n", salary);
    printf("Grade: %c\n", grade);

    printf("Year: %d\n", year);
    printf("Pi: %.2f\n", pi);
    printf("Section: %c\n", section);

    return 0;
}
