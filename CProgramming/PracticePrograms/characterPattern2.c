#include <stdio.h>

int main() {
    int n, i, j, space;

    printf("Enter number of rows (e.g., 5): ");
    scanf("%d", &n);

    // Upper half
    for(i = 1; i <= n; i++) {
        for(space = 1; space <= n - i; space++) {
            printf(" ");
        }
        char ch = 'A';
        for(j = 1; j <= i; j++) {
            printf("%c", ch);
            ch++;
        }
        ch -= 2;
        for(j = 1; j < i; j++) {
            printf("%c", ch);
            ch--;
        }
        printf("\n");
    }

    // Lower half
    for(i = n - 1; i >= 1; i--) {
        for(space = 1; space <= n - i; space++) {
            printf(" ");
        }
        char ch = 'A';
        for(j = 1; j <= i; j++) {
            printf("%c", ch);
            ch++;
        }
        ch -= 2;
        for(j = 1; j < i; j++) {
            printf("%c", ch);
            ch--;
        }
        printf("\n");
    }

    return 0;
}
