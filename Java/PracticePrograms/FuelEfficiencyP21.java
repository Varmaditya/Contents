// Program: Fuel Efficiency Checker

import java.util.Scanner;

public class FuelEfficiencyP21 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter distance traveled (km): ");
        double dist = sc.nextDouble();

        System.out.print("Enter fuel used (liters): ");
        double fuel = sc.nextDouble();

        double mileage = dist / fuel;

        boolean efficient = mileage >= 15;

        System.out.println("Mileage: " + mileage);
        System.out.println("Fuel Efficient: " + efficient);

        sc.close();
    }
}
