#include <stdio.h>

int main() {
    int a = 10, b = 3, result;
    char ch = 'A';

    // Arithmetic Operators
    printf("Arithmetic: %d + %d = %d\n", a, b, a + b);

    // Relational Operators
    printf("Relational: %d > %d = %d\n", a, b, a > b);

    // Logical Operators
    printf("Logical: (%d > %d) && (%d < %d) = %d\n", a, b, a, 20, (a > b) && (a < 20));

    // Bitwise Operators
    printf("Bitwise: %d & %d = %d\n", a, b, a & b);

    // Assignment Operators
    result = a;
    result += b;
    printf("Assignment: result += b → %d\n", result);

    // Unary Operators
    printf("Unary: ++a = %d, --b = %d\n", ++a, --b);

    // Ternary Operator
    printf("Ternary: (a > b) ? a : b = %d\n", (a > b) ? a : b);

    // Miscellaneous
    printf("sizeof(int) = %zu\n", sizeof(int));
    printf("Character ch = %c, ASCII = %d\n", ch, ch);

    return 0;
}
