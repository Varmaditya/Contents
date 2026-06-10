#include<stdio.h>

int main(){
    int numberOfYear;
    float principleAmount, rateOfInterest, simpleInterest;

    printf("Enter Principle Amount: ");
    scanf("%f", &principleAmount);
    printf("Enter number of year: ");
    scanf("%d", &numberOfYear);
    printf("Enter Rate of Interest: ");
    scanf("%f", &rateOfInterest);

    simpleInterest = (principleAmount * numberOfYear * rateOfInterest) / 100;
    printf("Simple interest is %f\n", simpleInterest);

    return 0;
}
