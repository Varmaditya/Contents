#include <stdio.h>

int main(void) {

    int n = 123;
    long int L = 2000000000L;
    float f = 3.14159f;
    double d = 2.718281828;
    char ch = 'C';
    char name[] = "Ada";

    // Printing different data types
    printf("int: %d\n", n);
    printf("long: %ld\n", L);
    printf("float: %f\n", f);
    printf("double: %lf\n", d);
    printf("char: %c\n", ch);
    printf("string: %s\n", name);

    // Width and precision
    printf("pi (2 decimals): %.2f\n", f);
    printf("n right-aligned width 6: |%6d|\n", n);
    printf("n left-aligned width 6 : |%-6d|\n", n);

    // Printing expressions
    printf("2 + 3 = %d\n", 2 + 3);
    printf("Area 7 x 5 = %d\n", 7 * 5);

    return 0;
}
