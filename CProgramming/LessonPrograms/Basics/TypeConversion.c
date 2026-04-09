#include <stdio.h>

int main() {
    int a = 5, b = 2;
    float f = 3.5;
    double d = 7.89;

    // Automatic Type Conversion
    float autoResult = a + f;    // int 'a' automatically promoted to float
    double mixResult = f + d;    // float promoted to double

    printf("Automatic Conversion:\n");
    printf("a + f = %.2f  (int promoted to float)\n", autoResult);
    printf("f + d = %.2lf (float promoted to double)\n\n", mixResult);

    // Manual Type Conversion (Type Casting)
    int intResult = (int)f;      // float to int (fractional part lost)
    float preciseDivision = (float)a / b;  // manual cast ensures float division
    double forcedCast = (double)a / b;     // ensures double division

    printf("Manual Conversion (Type Casting):\n");
    printf("Casting float f=3.5 to int: %d\n", intResult);
    printf("Casting int to float before division: %.2f\n", preciseDivision);
    printf("Casting int to double before division: %.4lf\n", forcedCast);

    return 0;
}
