#include <stdio.h>

// Function to print Fibonacci series
void fibonacci(int n) {
    int a = 0, b = 1, c;

    printf("Fibonacci Series: %d %d ", a, b);

    for(int i = 3; i <= n; i++) {
        c = a + b;
        printf("%d ", c);
        a = b;
        b = c;
    }
}

int main() {
    int n;

    printf("Enter number of terms: ");
    scanf("%d", &n);

    fibonacci(n);
    return 0;
}
