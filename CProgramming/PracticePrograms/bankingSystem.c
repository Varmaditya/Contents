#include <stdio.h>

// Structure to store account information
struct BankAccount {
    char name[50];
    float balance;
};

// Function to deposit money
void deposit(struct BankAccount *acc) {
    float amount;

    printf("Enter amount to deposit: ");
    scanf("%f", &amount);

    acc->balance += amount;

    printf("$%.2f deposited successfully.\n", amount);
}

// Function to withdraw money
void withdraw(struct BankAccount *acc) {
    float amount;

    printf("Enter amount to withdraw: ");
    scanf("%f", &amount);

    if(amount <= acc->balance) {
        acc->balance -= amount;
        printf("$%.2f withdrawn successfully.\n", amount);
    } else {
        printf("Insufficient Balance!\n");
    }
}

// Function to display account details
void showBalance(struct BankAccount acc) {
    printf("\nAccount Holder: %s\n", acc.name);
    printf("Current Balance: $%.2f\n", acc.balance);
}

int main() {

    struct BankAccount customer;
    int choice;

    printf("Enter Account Holder Name: ");
    scanf("%s", customer.name);

    customer.balance = 1000;

    do {
        printf("\n===== BANK MENU =====\n");
        printf("1. Deposit\n");
        printf("2. Withdraw\n");
        printf("3. Check Balance\n");
        printf("4. Exit\n");

        printf("Enter Choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                deposit(&customer);
                break;
            case 2:
                withdraw(&customer);
                break;
            case 3:
                showBalance(customer);
                break;
            case 4:
                printf("Thank You For Banking With Us.\n");
                break;
            default:
                printf("Invalid Choice!\n");
        }
    } while(choice != 4);

    return 0;
}
