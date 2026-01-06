// Program: Loan Approval Decision

import java.util.Scanner;

public class LoanApprovalP29 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Monthly income: ");
        double income = sc.nextDouble();

        System.out.print("Credit score: ");
        int score = sc.nextInt();

        System.out.print("Existing loans? (yes/no): ");
        String loans = sc.next();

        if (income >= 30000 && score >= 700) {
            if (loans.equalsIgnoreCase("no")) {
                System.out.println("Loan Approved");
            } else {
                System.out.println("Loan Pending Review");
            }
        } else {
            System.out.println("Loan Rejected");
        }

        sc.close();
    }
}
