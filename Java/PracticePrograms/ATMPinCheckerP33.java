// Program: ATM PIN Retry System

import java.util.Scanner;

public class ATMPinCheckerP33 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        final int CORRECT_PIN = 1234;
        int attempts = 0;

        while (attempts < 3) {
            System.out.print("Enter PIN: ");
            int pin = sc.nextInt();

            if (pin == CORRECT_PIN) {
                System.out.println("Access granted");
                break;
            } else {
                System.out.println("Incorrect PIN");
            }
            attempts++;
        }

        if (attempts == 3) {
            System.out.println("Card blocked");
        }

        sc.close();
    }
}
