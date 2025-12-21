/*Program to show linear search*/

#include<stdio.h>

int main() {
    int n, i, x, c = 0;

    printf("ENTER SIZE OF ARRAY: ");
    scanf("%d", &n);

    int a[n];

    for(i=0;i<n;i++) {
        scanf("%d",&a[i]);
    }

    printf("ENTER ELEMENT TO SEARCH\n");
    scanf("%d",&x);

    for(i=0;i<n;i++) {
        if(a[i]==x) {
            printf("FOUND AT INDEX: %d i.e. ELEMENT NUMBER: %d", i, i+1);
            c++;
            break;
        }
    }

    if(c==0) {
        printf("ELEMENT NOT FOUND");
    }

    return 1;
}
