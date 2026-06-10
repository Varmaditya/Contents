#include <stdio.h>

int main() {
    int i, n;

    // Using for loop to print numbers
    for (i = 1; i <= 10; i++) {
        printf("%d\n", i);
    }

    // Using for loop to print table
    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++){
        printf("%10d%10d\n", i, i * i);
    }

    return 0;
}
