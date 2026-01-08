// Program: Password Strength Checker

import java.util.Scanner;

public class PasswordStrengthCheckerP34 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter password: ");
        String pass = sc.nextLine();

        int digits = 0;

        for (int i = 0; i < pass.length(); i++) {
            if (pass.charAt(i) >= '0' && pass.charAt(i) <= '9') {
                digits++;
            }
        }

        if (digits >= 2 && pass.length() >= 8) {
            System.out.println("Strong password");
        } else {
            System.out.println("Weak password");
        }

        sc.close();
    }
}
