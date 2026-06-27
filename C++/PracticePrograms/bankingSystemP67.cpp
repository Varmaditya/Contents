/*
Program: ATM Banking System
Description: Demonstrates functions by simulating ATM operations like
login, balance inquiry, deposit and withdrawal.
*/

#include <iostream>
using namespace std;

int balance = 10000;
int pin = 1234;

bool login() {
    int enteredPin;

    cout << "Enter ATM PIN: ";
    cin >> enteredPin;

    if (enteredPin == pin) {
        cout << "\nLogin Successful!\n";
        return true;
    }

    cout << "\nInvalid PIN!\n";
    return false;
}

void showMenu() {
    cout << "\n====== ATM MENU ======\n";
    cout << "1. Check Balance\n";
    cout << "2. Deposit Money\n";
    cout << "3. Withdraw Money\n";
    cout << "4. Exit\n";
}

void checkBalance() {
    cout << "\nCurrent Balance : Rs." << balance << endl;
}

void depositMoney() {
    int amount;

    cout << "Enter Deposit Amount : ";
    cin >> amount;

    balance += amount;

    cout << "Deposit Successful!\n";
}

void withdrawMoney() {
    int amount;

    cout << "Enter Withdrawal Amount : ";
    cin >> amount;

    if (amount <= balance) {
        balance -= amount;
        cout << "Please Collect Cash.\n";
    } else {
        cout << "Insufficient Balance.\n";
    }
}

int main() {
    if (!login())
        return 0;

    int choice;

    do {
        showMenu();

        cout << "\nEnter Choice : ";
        cin >> choice;

        switch (choice) {
            case 1:
                checkBalance();
                break;
            case 2:
                depositMoney();
                break;
            case 3:
                withdrawMoney();
                break;
            case 4:
                cout << "\nThank You For Banking With Us!\n";
                break;
            default:
                cout << "\nInvalid Choice!\n";
        }
    } while (choice != 4);

    return 0;
}
