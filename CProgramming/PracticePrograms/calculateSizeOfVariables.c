/* sizeof() operator in c is used to calculate the size of a variable
used inside the program and return the size in integer in the form
of memory bytes*/

#include<stdio.h>

int main()
{
    int a = 6;
    float b = 8.765f;
    long long int c = 15050603LL;
    double d = 78945.321654;
    char ch = 'X';    // Capital X

    printf("Size of a : %d Bytes\n" ,sizeof(a));
    printf("Size of b : %d Bytes\n" ,sizeof(b));
    printf("Size of c : %d Bytes\n" ,sizeof(c));
    printf("Size of d : %d Bytes\n" ,sizeof(d));
    printf("Size of X : %d Bytes\n",sizeof(ch));

    return 0;
}
