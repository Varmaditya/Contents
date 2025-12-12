// Program: Discount Calculator

import java.util.Scanner;

public class DiscountCalculatorP10 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter purchase amount: ");
        double amount = sc.nextDouble();

        double discount = (amount > 5000) ? amount * 0.20 :
                (amount > 2000) ? amount * 0.10 : 0;

        double finalAmount = amount - discount;

        System.out.println("\nOriginal Amount: " + amount);
        System.out.println("Discount: " + discount);
        System.out.println("Final Payable Amount: " + finalAmount);

        sc.close();
    }
}
