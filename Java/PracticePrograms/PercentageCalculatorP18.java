// Program: Percentage Calculator

import java.util.Scanner;

public class PercentageCalculatorP18 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter obtained marks: ");
        double obtained = sc.nextDouble();

        System.out.print("Enter total marks: ");
        double total = sc.nextDouble();

        double percent = (obtained / total) * 100;

        System.out.println("Percentage: " + percent);

        sc.close();
    }
}
