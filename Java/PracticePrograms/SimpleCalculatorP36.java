// Program: Menu Driven Calculator

import java.util.Scanner;

public class SimpleCalculatorP36 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Modulus  6.Exit");
            System.out.print("Choose option: ");
            choice = sc.nextInt();

            if (choice >= 1 && choice <= 5) {
                System.out.print("Enter two numbers: ");
                int a = sc.nextInt();
                int b = sc.nextInt();

                if (choice == 1) {
                    System.out.println("Sum = " + (a + b));
                } else if (choice == 2) {
                    System.out.println("Difference = " + (a - b));
                } else if (choice == 3) {
                    System.out.println("Product = " + (a * b));
                } else if (choice == 4) {
                    if (b != 0) {
                        System.out.println("Quotient = " + (a / b));
                    } else {
                        System.out.println("Division by zero not allowed");
                    }
                } else if (choice == 5) {
                    if (b != 0) {
                        System.out.println("Remainder = " + (a % b));
                    } else {
                        System.out.println("Modulus by zero not allowed");
                    }
                }
            } else if (choice != 6) {
                System.out.println("Invalid option");
            }

        } while (choice != 6);

        System.out.println("Calculator closed");
        sc.close();
    }
}
