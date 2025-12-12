// Program: Salary Breakdown Calculator

import java.util.Scanner;

public class SalaryCalculatorP7 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter basic salary: ");
        double basic = sc.nextDouble();

        double hra = basic * 0.20;      // 20% HRA
        double da = basic * 0.10;       // 10% DA
        double pf = basic * 0.05;       // 5% PF deduction

        double gross = basic + hra + da;
        double net = gross - pf;

        System.out.println("\n===== SALARY SLIP =====");
        System.out.println("Basic Salary: " + basic);
        System.out.println("HRA (20%): " + hra);
        System.out.println("DA (10%): " + da);
        System.out.println("PF Deducted: " + pf);
        System.out.println("Gross Salary: " + gross);
        System.out.println("Net Salary: " + net);

        sc.close();
    }
}
