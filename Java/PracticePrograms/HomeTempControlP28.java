// Program: Smart Home Temperature Control

import java.util.Scanner;

public class HomeTempControlP28 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter room temperature: ");
        double temp = sc.nextDouble();

        System.out.print("Season (summer/winter): ");
        String season = sc.next();

        if (season.equalsIgnoreCase("summer")) {
            if (temp > 30) {
                System.out.println("AC ON");
            } else {
                System.out.println("AC OFF");
            }
        } else if (season.equalsIgnoreCase("winter")) {
            if (temp < 18) {
                System.out.println("Heater ON");
            } else {
                System.out.println("Heater OFF");
            }
        } else {
            System.out.println("Invalid season");
        }

        sc.close();
    }
}
