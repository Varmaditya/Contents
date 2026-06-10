#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    ptr = (int*) malloc(sizeof(int));
    *ptr = 100;

    printf("Value = %d\n", *ptr);
    free(ptr);

    return 0;
}
