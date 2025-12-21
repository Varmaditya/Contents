/* Prints a countdown */

#include <stdio.h>

void printCount(int n) {
    printf("T minus %d and counting\n", n);
}

int main(void) {
    int i, n;
    printf("Enter the number to start countdown from: ");
    scanf("%d", &n);

    for (i = n; i > 0; --i) {
        printCount(i);
    }

    return 0;
}
