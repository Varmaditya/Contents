#include <iostream>
#include <cstdio>
using namespace std;

int main() {

    // -------- scanf and printf --------
    int age;
    float marks;

    printf("Enter age: ");
    scanf("%d", &age);

    printf("Enter marks: ");
    scanf("%f", &marks);

    printf("Age = %d\n", age);
    printf("Marks = %.2f\n", marks);

    // -------- getchar and putchar --------
    char ch;

    printf("\nEnter a character: ");
    getchar(); // to consume leftover newline
    ch = getchar();

    printf("You entered: ");
    putchar(ch);
    printf("\n");

    // -------- puts --------
    puts("\nThis is a string using puts");

    return 0;
}
