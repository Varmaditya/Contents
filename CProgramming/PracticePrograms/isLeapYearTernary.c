#include <stdio.h>

int main() {
    int y;

    printf("Please input a year and I will tell you if it's a leap year: ");
    scanf("%d",&y);

    //Using ternary operator
    (((y % 100 != 0) && (y % 4 == 0)) || (y % 400 == 0)) ?
        printf("Your input (%d) is a leap year.",y) :
        printf("Your input (%d) is NOT a leap year.",y);

    return 0;
}
