/*Program to check common element in two arrays*/

#include<stdio.h>

void main() {
    int i,j,n;

    printf("Enter the number of elements in an arrays: ");
    scanf("%d",&n);

    int a[n],b[n];

    printf("Enter the elements of 1st array: ");
    for(i=0;i<n;i++) {
        scanf("%d",&a[i]);
    }

    printf("Enter the elements of 2nd array: ");
    for(j=0;j<n;j++) {
        scanf("%d",&b[j]);
    }

    printf("The common numbers are: ");
    for(i=0; i<n; i++) {
        for(j=0;j<n;j++) {
            if(a[i]==b[j]) {
			   printf("%d\n", b[j]);
            }
        }
    }
}
