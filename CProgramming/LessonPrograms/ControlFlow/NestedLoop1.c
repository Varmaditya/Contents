#include <stdio.h>

int main() {
    int i, j;

    for (i = 1; i <= 5; i++) {
        printf("\nMultiplication Table of %d\n", i);
        for (j = 1; j <= 10; j++) {
            printf("%d x %d = %d\n", i, j, i*j);
        }
    }
    return 0;
}

