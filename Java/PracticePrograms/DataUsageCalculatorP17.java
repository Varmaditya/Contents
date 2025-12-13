// Program: Mobile Data Usage Calculator

import java.util.Scanner;

public class DataUsageCalculatorP17 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter total data (GB): ");
        double total = sc.nextDouble();

        System.out.print("Enter used data (GB): ");
        double used = sc.nextDouble();

        double remaining = total - used;

        System.out.println("Remaining Data: " + remaining + " GB");

        sc.close();
    }
}
