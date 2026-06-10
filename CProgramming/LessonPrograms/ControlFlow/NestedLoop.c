#include <stdio.h>

int main() {
    int i, j;

    for (i = 1; i <= 3; i++) {          // Outer loop → rows
        for (j = 1; j <= 5; j++) {      // Inner loop → columns
            printf("* ");
        }
        printf("\n"); // new line after each row
    }


    for (i = 1; i <= 5; i++) {
        printf("\nMultiplication Table of %d\n", i);
        for (j = 1; j <= 10; j++) {
            printf("%d x %d = %d\n", i, j, i*j);
        }
    }

    return 0;
}

