// Practice Program 10: Restaurant Billing System

import java.util.Scanner;

public class RestaruantBillingP69 {

    static double calculateItemCost(String item, int qty) {

        double price = 0;

        if (item.equalsIgnoreCase("pizza")) price = 250;
        else if (item.equalsIgnoreCase("burger")) price = 120;
        else if (item.equalsIgnoreCase("pasta")) price = 180;
        else {
            System.out.println("Invalid item");
            return 0;
        }

        return price * qty;
    }

    static double applyGST(double total) {
        return total * 1.05;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        double total = 0;
        String choice;

        do {
            System.out.print("Enter item name: ");
            String item = sc.nextLine();

            System.out.print("Enter quantity: ");
            int qty = sc.nextInt();
            sc.nextLine();

            total += calculateItemCost(item, qty);

            System.out.print("Add more items? (yes/no): ");
            choice = sc.nextLine();

        } while (choice.equalsIgnoreCase("yes"));

        total = applyGST(total);

        System.out.println("Final Bill (with GST): ₹" + total);
        sc.close();
    }
}