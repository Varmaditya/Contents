#include <stdio.h>

int main() {
    int num, reverse = 0, remainder;

    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0) {
      remainder = num % 10;
      reverse = reverse * 10 + remainder;
      num = num / 10;
    }

    printf("Reverse of the number is : %d\n", reverse);

    return 0;
}
