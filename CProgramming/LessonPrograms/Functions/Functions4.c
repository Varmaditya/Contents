#include <stdio.h>

// Function Declaration
void findSquare();

int main() {
    // Function Call
    findSquare();
    return 0;
}

// Function Definition
void findSquare() {
    int num, square;
    printf("Enter a number: ");
    scanf("%d", &num);

    square = num * num;
    printf("Square of %d is %d\n", num, square);
}
