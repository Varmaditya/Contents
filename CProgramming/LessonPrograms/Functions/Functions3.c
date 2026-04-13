#include <stdio.h>

void swap(int *a, int *b) {   // using pointers
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y);   // passing addresses
    printf("After swap: x = %d, y = %d\n", x, y);
    return 0;
}
