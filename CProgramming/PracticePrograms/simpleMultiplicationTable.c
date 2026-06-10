#include <stdio.h>

int main() {
    int num, i = 1;

    printf("Enter a number to calculate table of: \n");
    scanf("%d", &num);

	for(i = 1; i <= 10; i++) {
		printf("%d x %d = %d \n", i, num, num * i);
	}

	return 0;
}
