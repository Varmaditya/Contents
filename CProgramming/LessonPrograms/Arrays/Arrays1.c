#include <stdio.h>

int main() {
    // Declaration of an integer array
    int numbers[5];

    // Initializing array elements one by one
    numbers[0] = 10;
    numbers[1] = 20;
    numbers[2] = 30;
    numbers[3] = 40;
    numbers[4] = 50;

    // Printing all elements
    printf("Array elements are:\n");
    for (int i = 0; i < 5; i++) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }

    return 0;
}
