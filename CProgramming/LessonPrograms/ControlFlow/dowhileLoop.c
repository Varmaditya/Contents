#include <stdio.h>

int main() {
    int i = 1;
	int n;

	printf("Enter last number you want: ");
	scanf("%d", &n);

    	// Using do-while loop
    do {
        printf("%d\n", i);
       	i++;
    } while (i <= n);

    return 0;
}
