#include<stdio.h>

int main(){
    int a, b, c;

    printf("Please enter two numbers : ");
    scanf("%d %d", &a, &b);//ok

    c = a + b;//addition
    printf("The Sum is %d\n", c);

    c = a - b;//substraction
    printf("The Difference is %d\n", c);

    c = a * b;//multiplication
    printf("The Product is %d\n", c);

    c = a / b;
    printf("The Division is %d\n", c);
    return 0;
}
