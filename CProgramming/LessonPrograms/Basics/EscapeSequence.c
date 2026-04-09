#include <stdio.h>

int main() {
    printf("Demonstrating Escape Sequences in C\n\n");

    printf("1. Newline -> Hello\\nWorld:\n");
    printf("Hello\nWorld\n\n");

    printf("2. Tab -> Hello\\tWorld:\n");
    printf("Hello\t World\n\n");

    printf("3. Backspace -> Helloo\\bWorld:\n");
    printf("Helloo\b World\n\n");

    printf("4. Carriage Return -> Hello World\\rHi:\n");
    printf("Hello World\rHioo\n\n");

    printf("5. Backslash -> \\\\:\n");
    printf("\\\n\n");

    printf("6. Single Quote -> \\\':\n");
    printf("\'\n\n");

    printf("7. Double Quote -> \\\" :\n");
    printf("\"\n\n");

    printf("8. Alert -> \\a:\n");
    printf("\a\n"); // may beep if supported

    return 0;
}
