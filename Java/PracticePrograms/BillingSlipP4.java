// Program: Simple Billing Slip

import java.util.Scanner;

public class BillingSlipP4 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter item name: ");
        String item = sc.nextLine();

        System.out.print("Enter item price: ");
        double price = sc.nextDouble();

        System.out.print("Enter quantity: ");
        int qty = sc.nextInt();

        double total = price * qty;

        System.out.println("\n===== BILL RECEIPT =====");
        System.out.println("Item: " + item);
        System.out.println("Quantity: " + qty);
        System.out.println("Price per item: " + price);
        System.out.println("Total Amount: " + total);

        sc.close();
    }
}
