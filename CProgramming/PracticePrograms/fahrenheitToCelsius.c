/* Converts a Fahrenheit temperature to Celsius */

#include <stdio.h>

#define FREEZING_PT 32.0f
#define SCALE_FACTOR (5.0f / 9.0f)

int main() {
  float fahrenheit, celsius;

  printf("Enter the Temperatue in Fahrenheit : ");
  scanf("%f", &fahrenheit);

  celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;

  printf("Temperature in Celsius is %.1f\n C", celsius);

  return 0;
}
