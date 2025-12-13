// Program: E-Commerce Checkout Calculator

import java.util.Scanner;

public class CheckoutCalculatorP23 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter product price: ");
        double price = sc.nextDouble();

        System.out.print("Enter quantity: ");
        int qty = sc.nextInt();

        double subtotal = price * qty;
        double gst = subtotal * 0.18;
        double total = subtotal + gst;

        System.out.println("\nSubtotal: " + subtotal);
        System.out.println("GST (18%): " + gst);
        System.out.println("Total Amount: " + total);

        sc.close();
    }
}
