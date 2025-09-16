/* Converts a Celsius temperature to Fahrenheit */

#include<stdio.h>

#define FREEZING_PT 32.0f
#define SCALE_FACTOR (5.0f / 9.0f)

int main() {
    float celsius,fahrenheit;

    printf("Enter the Temperature in Celcius : ");
    scanf("%f",&celsius);

    fahrenheit = SCALE_FACTOR * celsius + FREEZING_PT;

    printf("Temperature in Fahernheit is %.1f", fahrenheit);
}
