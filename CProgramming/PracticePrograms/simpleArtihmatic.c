#include<stdio.h>

int main(){
    int a, b, c;

    printf("Enter two numbers (eg.:5 8): ");
    scanf("%d %d", &a, &b);

    c = a + b;  // addition
    printf("The Sum is %d\n", c);

    c = a - b;  // substraction
    printf("The Difference is %d\n", c);

    c = a * b;  // multiplication
    printf("The Product is %d\n", c);

    c = a / b;  // division
    printf("The Division is %d\n", c);

    return 0;
}
