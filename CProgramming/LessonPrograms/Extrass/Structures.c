#include <stdio.h>

struct Student {
    char name[20];
    int age;
    float marks;
};

int main() {

    struct Student s1 = {"Aditya", 23, 89.5};

    printf("Name: %s\n", s1.name);
    printf("Age: %d\n", s1.age);
    printf("Marks: %.1f\n", s1.marks);

    return 0;
}
