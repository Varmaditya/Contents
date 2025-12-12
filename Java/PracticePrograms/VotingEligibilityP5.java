// Program: Voting Eligibility Checker

import java.util.Scanner;

public class VotingEligibilityP5 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        boolean eligible = age >= 18;

        System.out.println("Eligible to vote: " + eligible);

        sc.close();
    }
}
