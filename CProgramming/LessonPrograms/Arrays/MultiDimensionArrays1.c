#include <stdio.h>

int main() {
    // Declaration + Initialization
    int matrix[2][3] = {
        {10, 20, 30},
        {40, 50, 60}
    };

    // Printing initialized values
    printf("Matrix elements are:\n");
    printf("%d %d %d\n", matrix[0][0], matrix[0][1], matrix[0][2]);
    printf("%d %d %d\n", matrix[1][0], matrix[1][1], matrix[1][2]);

    return 0;
}
