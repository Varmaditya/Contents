// Program: Restaurant Menu Billing

import java.util.Scanner;

public class RestaurantBillP30 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Menu:");
        System.out.println("1. Burger - ₹150");
        System.out.println("2. Pizza  - ₹250");
        System.out.println("3. Pasta  - ₹200");

        System.out.print("Enter item number: ");
        int choice = sc.nextInt();

        System.out.print("Enter quantity: ");
        int qty = sc.nextInt();

        int price;

        switch (choice) {
            case 1:
                price = 150;
                break;
            case 2:
                price = 250;
                break;
            case 3:
                price = 200;
                break;
            default:
                System.out.println("Invalid item selected");
                sc.close();
                return;
        }

        System.out.println("Total Bill: ₹" + (price * qty));
        sc.close();
    }
}
