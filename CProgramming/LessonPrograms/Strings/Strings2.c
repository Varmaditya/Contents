#include <stdio.h>

int main() {
    char name[20];

    printf("Enter your name: ");
    scanf("%s", name);   // Will stop at space

    printf("Hello %s!\n", name);

    return 0;
}
