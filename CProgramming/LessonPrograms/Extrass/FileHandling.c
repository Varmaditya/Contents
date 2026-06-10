#include <stdio.h>

int main() {
    FILE *file = fopen("notes.txt", "w");

    fprintf(file, "Learning C Programming");
    fclose(file);
    printf("Data written to file.");

    return 0;
}
