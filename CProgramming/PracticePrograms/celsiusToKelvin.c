/* Converts a Celsius temperature to Kelvin */

#include <stdio.h>

#define SCALE_FACTOR 273.15

int main()
{
	float celsius, kelvin;

	printf("Enter the Temperature in Celcius : ");
	scanf("%f", &celsius);

	kelvin = celsius + SCALE_FACTOR;

	printf("Temperature in Kelvin is %.2f k\n", kelvin);
	return 0;
}
