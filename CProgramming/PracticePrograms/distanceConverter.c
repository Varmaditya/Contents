#include<stdio.h>
#include<conio.h>

void main() {
    float km, mt, inch, ft, cm;

    printf("Enter the distance between two cities in kilometers : ");
    scanf("%f", &km);

    mt = km * 1000;
    ft = mt * 3.33;
    cm = mt * 100;
    inch = ft * 12;

    printf("The distance in meters is = %.2f mts.\n", mt);
    printf("The distance in feets is = %.2f ft.\n", ft);
    printf("The distance in centimeters is = %.2f cms.\n", cm);
    printf("The distance in inchs is = %.2f inches.\n", inch);
}
