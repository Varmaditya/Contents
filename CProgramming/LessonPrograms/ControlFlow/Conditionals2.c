#include <stdio.h>

int main() {
    int marks;
    printf("Enter your marks (0-100): ");
    scanf("%d", &marks);

    // Example of if - else if - else
    if (marks >= 90) {
        printf("Grade: A\n");
    } else if (marks >= 75) {
        printf("Grade: B\n");
    } else if (marks >= 50) {
        printf("Grade: C\n");
    } else {
        printf("Grade: Fail\n");
    }

    // Example of nested if
    if (marks >= 50) {
        if (marks >= 90) {
            printf("Excellent performance!\n");
        } else {
            printf("You passed, keep improving.\n");
        }
    } else {
        printf("You need to work harder.\n");
    }

    return 0;
}
