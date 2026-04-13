#include <stdio.h>

int main() {
    // Declaring with initialization
    int marks[5] = {60, 70, 80, 90, 100};

    // Printing array directly using loop
    printf("Marks stored in array:\n");
    for (int i = 0; i < 5; i++) {
        printf("marks[%d] = %d\n", i, marks[i]);
    }

    return 0;
}
