// Program: Subscription Plan Selector

import java.util.Scanner;

public class SubscriptionPlanP31 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plan type (basic/standard/premium): ");
        String plan = sc.nextLine();

        double price = switch (plan.toLowerCase()) {
            case "basic" -> 199;
            case "standard" -> 399;
            case "premium" -> 599;
            default -> 0;
        };

        if (price > 0) {
            System.out.println("Selected plan price: ₹" + price);
        } else {
            System.out.println("Invalid plan selected");
        }

        sc.close();
    }
}
