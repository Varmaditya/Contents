#include <stdio.h>

void add(int a, int b) {
    a = a + b;
    printf("Sum inside function: %d\n", a);
}

int main() {
    int x = 5, y = 10;
    add(x, y);
    printf("Values after function: x = %d, y = %d\n", x, y);
    return 0;
}
