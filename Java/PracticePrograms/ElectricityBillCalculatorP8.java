// Program: Electricity Bill Calculation

import java.util.Scanner;

public class ElectricityBillCalculatorP8 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter total units consumed: ");
        int units = sc.nextInt();

        double bill = (units <= 100) ? units * 4.5 :
                (units <= 300) ? (100 * 4.5) + (units - 100) * 6.0 :
                        (100 * 4.5) + (200 * 6.0) + (units - 300) * 8.0;

        System.out.println("Total Electricity Bill: ₹" + bill);

        sc.close();
    }
}
