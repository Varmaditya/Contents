// Program: Job Application Screening

import java.util.Scanner;

public class JobApplicationScreeningP27 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter age: ");
        int age = sc.nextInt();

        System.out.print("Years of experience: ");
        int exp = sc.nextInt();

        System.out.print("Degree (yes/no): ");
        String degree = sc.next();

        if (age >= 21 && age <= 35) {
            if (exp >= 2 && degree.equalsIgnoreCase("yes")) {
                System.out.println("Eligible for interview");
            } else {
                System.out.println("Not eligible: Skill criteria not met");
            }
        } else {
            System.out.println("Not eligible: Age criteria failed");
        }

        sc.close();
    }
}
