#include <stdio.h>

int main() {
    int choice;
    float num1, num2, result;

    printf("===== Simple Calculator =====\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Modulus\n");
    printf("Enter your choice (1–5): ");
    scanf("%d", &choice);

    // For modulus, we’ll use int inputs, so read accordingly
    if (choice >= 1 && choice <= 5) {
        printf("Enter two numbers: ");
        scanf("%f %f", &num1, &num2);
    }

    switch (choice) {
        case 1:
            result = num1 + num2;
            printf("Result = %.2f\n", result);
            break;
        case 2:
            result = num1 - num2;
            printf("Result = %.2f\n", result);
            break;
        case 3:
            result = num1 * num2;
            printf("Result = %.2f\n", result);
            break;
        case 4:
            if (num2 != 0)
                printf("Result = %.2f\n", num1 / num2);
            else
                printf("Error! Division by zero not allowed.\n");
            break;
        case 5:
            // Modulus only makes sense for integers
            printf("Result = %d\n", (int)num1 % (int)num2);
            break;
        default:
            printf("Invalid choice! Please enter between 1 and 5.\n");
    }

    return 0;
}
