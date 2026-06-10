#include <stdio.h>

void countdown(int n) {
    if (n == 0) {      // Base Case
        return;
    }

    printf("%d\n", n);
    countdown(n - 1);  // Recursive Call
}

int main() {
    countdown(5);

    return 0;
}
