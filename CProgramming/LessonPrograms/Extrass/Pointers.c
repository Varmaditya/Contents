#include <stdio.h>

int main() {
    int age = 23;
    int *ptr = &age;    // ptr stores address of age

    printf("Value of age: %d\n", age);
    printf("Address of age: %p\n", (void*)&age);
    printf("Value through pointer: %d\n", *ptr);

    return 0;
}
