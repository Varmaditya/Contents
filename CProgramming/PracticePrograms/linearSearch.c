#include <stdio.h>

int main() {
    int n, i, x, c = 0;

    printf("ENTER SIZE OF ARRAY: ");
    scanf("%d", &n);

    int a[n];

    for(i=0; i<n; i++) {
        printf("ENTER ELEMENT %d: ", i + 1);
        scanf("%d",&a[i]);
    }

    printf("ENTER ELEMENT TO SEARCH: ");
    scanf("%d", &x);

    for(i=0; i<n; i++) {
        if(a[i] == x) {
            printf("\nFOUND AT INDEX: %d i.e. ELEMENT NUMBER: %d\n", i, i+1);
            c++;
            break;
        }
    }

    if(c == 0) {
        printf("\nELEMENT NOT FOUND\n");
    }

    return 1;
}
