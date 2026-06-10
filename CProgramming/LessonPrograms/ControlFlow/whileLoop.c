#include <stdio.h>

int main() {
    int n, i, sum = 0, digit;

    //while loop for digit count
    printf("Enter a number: ");
    scanf("%d", &n);

    while (n > 0) {
        digit = n % 10;   // get last digit
        sum += digit;     // add to sum
        n = n / 10;       // remove last digit
    }

    printf("Sum of digits = %d\n", sum);

    //while loop for table
    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);

    i = 1;
    while (i <= n) {
        printf("%10d%10d\n", i, i * i);
        i++;
    }

    return 0;
}
