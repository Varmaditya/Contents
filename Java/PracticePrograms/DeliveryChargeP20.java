// Program: Delivery Charge Estimator

import java.util.Scanner;

public class DeliveryChargeP20 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter distance in km: ");
        double distance = sc.nextDouble();

        double charge = (distance <= 5) ? 30 :
                (distance <= 10) ? 50 :
                        (distance <= 20) ? 80 : 120;

        System.out.println("Delivery Charge: ₹" + charge);

        sc.close();
    }
}
