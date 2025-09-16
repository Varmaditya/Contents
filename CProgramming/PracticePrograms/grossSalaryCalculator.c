#include<stdio.h>

void main() {
    float basic,hra,da,gross;

    printf("Enter the Basic Salary : $");
    scanf("%f", &basic);

    hra = 40 * basic / 100;
    da = 50 * basic / 100;
    gross = basic + hra + da;

    printf("Gross Salary is $%f", gross);
}
