#include <stdio.h>

// Function Declaration
int findMax(int a, int b);

int main() {
    int x, y, max;
    printf("Enter two numbers: ");
    scanf("%d %d", &x, &y);

    // Function Call and storing return value
    max = findMax(x, y);
    printf("The maximum number is: %d\n", max);

    return 0;
}

// Function Definition
int findMax(int a, int b) {
    if(a > b)
        return a;   // return larger number
    else
        return b;
}
