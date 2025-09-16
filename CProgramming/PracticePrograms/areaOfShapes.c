#include <stdio.h>

void main() {
    float area;
    float side; //For sqaure
    float base, height; //For triangle
    float length, breadth; //For rectangle

    //Area of sqaure
    printf("Enter the side of square in cms: ");
    scanf("%f",&side);
    area = side * side;
    printf("Area of square with sides %.2f cms is %f\n", side, area);

    //Area of Triangle
    printf("Enter the base of triangle in cms : ");
    scanf("%f",&base);
    printf("Enter the height of triangle in cms : ");
    scanf("%f",&height);
    area = 0.5 * base * height;
    printf("Area is of triangle with base %.2fcms and height %.2fcms is %fcms\n", base, height, area);

    //Area of Rectangle
    printf("Enter the length of rectanlge in cms : ");
    scanf("%f", &length);
    printf("Enter the breadth of rectangle in cms : ");
    scanf("%f", &breadth);
    area = length * breadth;
    printf("The area of rectangle with lenght %.2fcms and breadth %.2fcms is %fcms\n", length, breadth, area);
}
