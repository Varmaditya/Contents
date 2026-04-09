#include <stdio.h>
#define PI 3.14   // symbolic constant

int main() {
    const int days = 7;     // constant
    int age = 23;           // variable
    float height = 5.9;     // variable
    char grade = 'A';       // variable

    printf("PI = %.2f\n", PI);
    printf("Days in a week = %d\n", days);
    printf("Age = %d, Height = %.1f, Grade = %c\n", age, height, grade);

    return 0;
}
