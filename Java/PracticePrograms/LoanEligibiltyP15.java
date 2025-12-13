// Program: Loan Eligibility Checker

import java.util.Scanner;

public class LoanEligibiltyP15 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter monthly income: ");
        double income = sc.nextDouble();

        System.out.print("Enter credit score: ");
        int score = sc.nextInt();

        boolean eligible = (income >= 25000) && (score >= 700);

        System.out.println("Loan Eligibility: " + eligible);

        sc.close();
    }
}
