/*Program to check if the number is perfect or not*/

#include<stdio.h>

int main () {
	int n, i, sum = 0;

	printf("Enter the value of n: ");
	scanf("%d", &n);

	for (i = 1; i < n; i++) {
		if (n % i == 0)
		sum = sum + i;
	}

	if (n == sum)
        printf("Entered no. is a perfect no.");
	else
        printf("Entered no. is not a perfect no.");

	return 0;
}
