#include <stdio.h>

int main() {
    // Declaration and initialization of float array
    float prices[4] = {10.5, 20.75, 30.0, 45.99};

    printf("Prices stored in float array:\n");
    for (int i = 0; i < 4; i++) {
        printf("prices[%d] = %.2f\n", i, prices[i]);
    }

    // Character array (like a string)
    char vowels[5] = {'a', 'e', 'i', 'o', 'u'};

    printf("Vowels stored in char array:\n");
    for (int i = 0; i < 5; i++) {
        printf("vowels[%d] = %c\n", i, vowels[i]);
    }

    // Double array with larger precision
    double salary[3] = {25000.50, 30000.75, 45000.99};

    printf("Salaries stored in double array:\n");
    for (int i = 0; i < 3; i++) {
        printf("salary[%d] = %.2lf\n", i, salary[i]);
    }

    return 0;
}
