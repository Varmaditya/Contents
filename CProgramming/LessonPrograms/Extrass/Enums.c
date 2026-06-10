#include <stdio.h>

enum Day {
    MONDAY,
    TUESDAY,
    WEDNESDAY
};

int main() {
    enum Day today = TUESDAY;
    printf("Today = %d\n", today);

    return 0;
}
