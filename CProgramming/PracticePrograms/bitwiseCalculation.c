#include <stdio.h>

int main()
{
    int a = 14, b = 7;

    printf("Bitwise NOT of a (~a): %d\n", ~a);
    printf("Bitwise NOT of b (~b): %d\n\n", ~b);

    printf("a & b = %d\n", a & b);

    printf("a | b = %d\n", a | b);

    printf("a ^ b = %d\n\n", a ^ b);

    printf("a << 1 = %d\n", a << 1);
    printf("b << 1 = %d\n\n", b << 1);

    printf("a >> 1 = %d\n", a >> 1);
    printf("b >> 1 = %d\n", b >> 1);

    return 0;
}
