// Practice Program: Parking Management System

import java.util.Scanner;

public class ParkingSystemP68 {

    static boolean validateVehicleType(String type) {
        return type.equalsIgnoreCase("car") ||
                type.equalsIgnoreCase("bike");
    }

    static int calculateCharge(String type, int hours) {

        if (type.equalsIgnoreCase("car"))
            return hours * 50;
        else
            return hours * 20;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int choice;
        int totalVehicles = 0;

        do {
            System.out.println("\n1.Park Vehicle  2.Exit");
            System.out.print("Choose option: ");
            choice = sc.nextInt();
            sc.nextLine();

            if (choice == 1) {

                System.out.print("Enter vehicle type (car/bike): ");
                String type = sc.nextLine();

                if (!validateVehicleType(type)) {
                    System.out.println("Invalid vehicle type");
                    continue;
                }

                System.out.print("Enter parking hours: ");
                int hours = sc.nextInt();

                int charge = calculateCharge(type, hours);

                System.out.println("Parking Charge: ₹" + charge);
                totalVehicles++;

                if (totalVehicles == 5) {
                    System.out.println("Parking Full");
                    break;
                }
            }

        } while (choice != 2);

        sc.close();
    }
}