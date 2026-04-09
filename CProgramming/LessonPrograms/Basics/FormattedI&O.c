#include <stdio.h>

int main() {
    int roll;
    float marks;
    char grade;

    // Taking input using scanf (formatted input)
    printf("Enter Roll Number: ");
    scanf("%d", &roll);

    printf("Enter Marks: ");
    scanf("%f", &marks);

    printf("Enter Grade: ");
    scanf(" %c", &grade);  // Notice space before %c to handle newline issues

    // Displaying output using printf (formatted output)
    printf("\n--- Student Details ---\n");
    printf("Roll Number: %d\n", roll);
    printf("Marks: %.2f\n", marks);
    printf("Grade: %c\n", grade);

    return 0;
}
