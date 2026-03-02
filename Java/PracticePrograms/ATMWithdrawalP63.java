// Practice Program: ATM Withdrawal System

import java.util.Scanner;

public class ATMWithdrawalP63 {

    static boolean validateWithdrawal(double balance, double amount) {
        return amount > 0 && amount <= balance;
    }

    static double withdraw(double balance, double amount) {
        return balance - amount;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        double balance = 10000;

        System.out.print("Enter withdrawal amount: ");
        double amount = sc.nextDouble();

        if (validateWithdrawal(balance, amount)) {
            balance = withdraw(balance, amount);
            System.out.println("Remaining Balance: ₹" + balance);
        } else {
            System.out.println("Invalid transaction");
        }

        sc.close();
    }
}