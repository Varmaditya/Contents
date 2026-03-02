// Practice Program: Shopping Cart Discount System

import java.util.Scanner;

public class ShoppingCartP64 {

    static double calculateTotal(double price, int quantity) {
        return price * quantity;
    }

    static double applyDiscount(double total) {
        if (total >= 5000) return total * 0.80;
        else if (total >= 2000) return total * 0.90;
        else return total;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter product price: ");
        double price = sc.nextDouble();

        System.out.print("Enter quantity: ");
        int qty = sc.nextInt();

        double total = calculateTotal(price, qty);
        double finalAmount = applyDiscount(total);

        System.out.println("Final Bill: ₹" + finalAmount);

        sc.close();
    }
}