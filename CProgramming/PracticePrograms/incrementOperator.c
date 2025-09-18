// Increment operator

#include<stdio.h>
int main()
{
    int a= 5;
    int b, c, d;

    printf("Value of a = %d\n", a);

    b = ++a;
    c = a++;
    d = ++a;

    printf("Value of b using ++a = %d\n", b);
    printf("Value of c using a++ = %d\n", c);
    printf("Value of d using ++a = %d\n", d);

    return 0;
}

