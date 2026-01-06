// Program: Ride Fare Calculator

import java.util.Scanner;

public class RideFareCalculatorP25 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter distance (km): ");
        double distance = sc.nextDouble();

        System.out.print("Peak hours? (yes/no): ");
        String peak = sc.next();

        double fare;

        if (distance <= 5) {
            fare = 50;
        } else if (distance <= 15) {
            fare = 100;
        } else {
            fare = 150;
        }

        if (peak.equalsIgnoreCase("yes")) {
            fare = fare + 30;
        }

        System.out.println("Total Fare: ₹" + fare);
        sc.close();
    }
}
