#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str1[50] = "Aditya";

    // Reverse string manually
    int len = strlen(str1);
    for (int i = 0; i < len / 2; i++) {
        char temp = str1[i];
        str1[i] = str1[len - i - 1];
        str1[len - i - 1] = temp;
    }
    printf("Reversed string: %s\n", str1);

    // strchr() - find first occurrence of a character
    char text[] = "Welcome to C programming";
    char *ptr = strchr(text, 'C');
    if (ptr != NULL)
        printf("Character 'C' found at position: %ld\n", ptr - text);
    else
        printf("Character not found\n");

    // strstr() - find substring
    char sentence[] = "C is a powerful language";
    char *found = strstr(sentence, "powerful");
    if (found != NULL)
        printf("Substring found: %s\n", found);
    else
        printf("Substring not found\n");

    // strtok() - break string into tokens
    char fruits[] = "apple,banana,grapes";
    char *token = strtok(fruits, ",");
    printf("Fruits list:\n");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, ",");
    }

    // toupper() & tolower()
    char word[] = "HeLLo WoRLd";
    printf("Original: %s\n", word);
    for (int i = 0; word[i] != '\0'; i++)
        word[i] = toupper(word[i]);
    printf("Uppercase: %s\n", word);

    for (int i = 0; word[i] != '\0'; i++)
        word[i] = tolower(word[i]);
    printf("Lowercase: %s\n", word);

    return 0;
}
