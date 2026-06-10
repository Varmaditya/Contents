#include <stdio.h>

// Function to calculate factorial
int factorial(int n) {
    int fact = 1;

    for(int i = 1; i <= n; i++) {
        fact *= i;  // multiply fact by each number up to n
    }

    return fact;
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    printf("Factorial of %d = %d", num, factorial(num));

    return 0;
}
