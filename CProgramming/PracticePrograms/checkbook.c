#include <stdio.h>

int main() {
    int cmd;
    float balance = 0.0f, credit, debit;

    printf("*** BANK CHECKBOOK ***\n");
    printf("Commands: \n1.Clear \n1.Credit \n2.Debit \n");
    printf("3.Balance \n4.Exit\n\n");

    for (;;) {
        printf("Enter command: ");
        scanf("%d", &cmd);

        switch (cmd) {
            case 1:
                balance = 0.0f;
                break;
            case 2:
                printf("Enter amount of credit: ");
                scanf("%f", &credit);
                balance += credit;
                break;
            case 3:
                printf("Enter amount of debit: ");
                scanf("%f", &debit);
                balance -= debit;
                break;
            case 4:
                printf("Current balance: $%.2f\n", balance);
                break;
            case 5:
                return 0;
            default:
                printf("Commands: \n0=clear \n1=credit \n2=debit \n");
                printf("3=balance \n4=exit\n\n");
                break;
        }
    }
}
