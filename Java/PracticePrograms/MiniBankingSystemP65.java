// Practice Program: Mini Banking System

import java.util.Scanner;

public class MiniBankingSystemP65 {

    static double deposit(double balance, double amount) {
        return balance + amount;
    }

    static double withdraw(double balance, double amount) {
        if (amount <= balance)
            return balance - amount;
        else
            return balance;
    }

    static void display(double balance) {
        System.out.println("Current Balance: ₹" + balance);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        double balance = 5000;
        int choice;

        do {
            System.out.println("\n1.Deposit  2.Withdraw  3.Check Balance  4.Exit");
            System.out.print("Choose option: ");
            choice = sc.nextInt();

            if (choice == 1) {
                System.out.print("Enter amount: ");
                balance = deposit(balance, sc.nextDouble());
            }
            else if (choice == 2) {
                System.out.print("Enter amount: ");
                balance = withdraw(balance, sc.nextDouble());
            }
            else if (choice == 3) {
                display(balance);
            }

        } while (choice != 4);

        sc.close();
    }
}