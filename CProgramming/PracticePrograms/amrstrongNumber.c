/* Function to check Armstrong number*/

#include <stdio.h>
#include <math.h>

int isArmstrong(int n) {
    int temp = n, sum = 0, digits = 0;

    // Count digits
    while(temp != 0) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while(temp != 0) {
        int r = temp % 10;
        sum += pow(r, digits);  // r^digits
        temp /= 10;
    }

    if(sum == n)
        return 1;  // Armstrong
    else
        return 0;  // Not Armstrong
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if(isArmstrong(num))
        printf("%d is an Armstrong number", num);
    else
        printf("%d is NOT an Armstrong number", num);

    return 0;
}
