/*
Program: Smart Banking System
Description: Demonstrates basic Object-Oriented Programming by
creating a simple banking system with login, deposit,
withdrawal, balance inquiry and transaction history.
*/

#include <iostream>
using namespace std;

class BankAccount {
private:

    string accountHolder;
    int accountNumber;
    int pin;
    float balance;

    string transactions[10];
    int transactionCount;

public:

    BankAccount() {
        accountHolder = "Aditya";
        accountNumber = 1001;
        pin = 1234;
        balance = 10000;
        transactionCount = 0;
    }

    bool login() {
        int enteredPin;

        cout << "\nEnter ATM PIN: ";
        cin >> enteredPin;

        return enteredPin == pin;
    }

    void showAccount() {
        cout << "\n===== ACCOUNT DETAILS =====\n";
        cout << "Name    : " << accountHolder << endl;
        cout << "Account : " << accountNumber << endl;
        cout << "Balance : Rs." << balance << endl;
    }

    void deposit() {
        float amount;

        cout << "Enter Deposit Amount: ";
        cin >> amount;

        balance += amount;
        transactions[transactionCount++] = "Deposit : +" + to_string((int)amount);

        cout << "Amount Deposited Successfully.\n";
    }

    void withdraw() {
        float amount;

        cout << "Enter Withdrawal Amount: ";
        cin >> amount;

        if(amount <= balance) {
            balance -= amount;
            transactions[transactionCount++] = "Withdraw : -" + to_string((int)amount);

            cout << "Please Collect Your Cash.\n";
        } else {
            cout << "Insufficient Balance!\n";
        }
    }

    void miniStatement() {
        cout << "\n===== MINI STATEMENT =====\n";

        if(transactionCount == 0) {
            cout << "No Transactions Available.\n";
            return;
        }

        for(int i = 0; i < transactionCount; i++) {
            cout << i + 1 << ". "
                 << transactions[i]
                 << endl;
        }
    }
};

int main() {
    BankAccount customer;

    if(!customer.login()) {
        cout << "\nInvalid PIN!";
        return 0;
    }

    int choice;

    do {
        cout << "\n========== SMART BANK ==========\n";
        cout << "1. Account Details\n";
        cout << "2. Deposit Money\n";
        cout << "3. Withdraw Money\n";
        cout << "4. Mini Statement\n";
        cout << "5. Exit\n";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch(choice) {
            case 1:
                customer.showAccount();
                break;
            case 2:
                customer.deposit();
                break;
            case 3:
                customer.withdraw();
                break;
            case 4:
                customer.miniStatement();
                break;
            case 5:
                cout << "\nThank You For Banking With Us!\n";
                break;
            default:
                cout << "\nInvalid Choice!";
        }
    } while(choice != 5);

    return 0;
}
