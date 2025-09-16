/* Converts a Kelvin temperature to Celsius */

#include <stdio.h>

#define SCALE_FACTOR 273.15

int main()
{
	float celsius, kelvin;

	printf("Enter the Temperature in Kelvin : ");
	scanf("%f", &kelvin);

	celsius = kelvin - SCALE_FACTOR;

	printf("Temperature in Celsius is %.2f C\n", celsius);
	return 0;
}
