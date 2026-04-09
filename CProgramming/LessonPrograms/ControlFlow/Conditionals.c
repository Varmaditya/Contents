#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    // Example of 'if'
    if (num > 0) {
        printf("The number is positive.\n");
    }

    // Example of 'if-else'
    if (num % 2 == 0) {
        printf("The number is Even.\n");
    } else {
        printf("The number is Odd.\n");
    }

    return 0;
}
