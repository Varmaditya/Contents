// Program: Online Order Discount

import java.util.Scanner;

public class OrderDiscountCalculatorP26 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter order amount: ");
        double amount = sc.nextDouble();

        System.out.print("Premium member? (yes/no): ");
        String member = sc.next();

        double discount = 0;

        if (amount >= 5000) {
            discount = 20;
        } else if (amount >= 2000) {
            discount = 10;
        }

        if (member.equalsIgnoreCase("yes")) {
            discount = discount + 5;
        }

        System.out.println("Discount applied: " + discount + "%");
        System.out.println("Final price: ₹" + (amount - (amount * discount / 100)));

        sc.close();
    }
}
