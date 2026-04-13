#include <stdio.h>

int main() {
    int marks[5];   // Array of size 5
    int i;

    // Taking input
    printf("Enter marks of 5 students:\n");
    for (i = 0; i < 5; i++) {
        printf("Enter mark for student %d: ", i + 1);
        scanf("%d", &marks[i]);   // input for array element
    }

    // Displaying output
    printf("\nMarks of 5 students are:\n");
    for (i = 0; i < 5; i++) {
        printf("marks[%d] = %d\n", i, marks[i]);
    }

    return 0;
}
