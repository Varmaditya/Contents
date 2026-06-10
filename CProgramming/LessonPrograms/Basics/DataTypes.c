#include <stdio.h>

int main() {
    char letter = 'A';                   // char
    int age = 23;                        // int
    float pi = 3.14159;                  // float
    double big = 123456.789012345;       // double

    printf("char: %c\n", letter);
    printf("int: %d\n", age);
    printf("float: %.5f\n", pi);
    printf("double: %.12lf\n", big);

    unsigned int u_age = 40000;          // unsigned int
    short int s_num = -30000;            // short int
    unsigned short int us_num = 60000;   // unsigned short int
    long int population = 2000000000;    // long int
    unsigned long int u_population = 4000000000; // unsigned long int
    unsigned char u_char = 250;          // unsigned char
    long double huge = 3.141592653589793238L; // long double

    printf("unsigned int: %u\n", u_age);
    printf("short int: %d\n", s_num);
    printf("unsigned short int: %u\n", us_num);
    printf("long int: %ld\n", population);
    printf("unsigned long int: %lu\n", u_population);
    printf("unsigned char: %u\n", u_char);
    printf("long double: %.18Lf\n", huge);

    return 0;
}
