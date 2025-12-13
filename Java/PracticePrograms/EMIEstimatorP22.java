// Program: Simple EMI Estimator

import java.util.Scanner;

public class EMIEstimatorP22 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter loan amount: ");
        double loan = sc.nextDouble();

        System.out.print("Enter interest rate (%): ");
        double rate = sc.nextDouble();

        System.out.print("Enter months: ");
        int months = sc.nextInt();

        double interest = (loan * rate * months) / (12 * 100);
        double emi = (loan + interest) / months;

        System.out.println("Estimated EMI: " + emi);

        sc.close();
    }
}
