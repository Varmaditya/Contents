// Program: Password Strength Analyzer

import java.util.Scanner;

public class PasswordStrengthP57 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter password: ");
        String password = sc.nextLine();

        boolean upper = false, lower = false, digit = false, special = false;

        for (int i = 0; i < password.length(); i++) {
            char letter = password.charAt(i);

            if (Character.isUpperCase(letter)) upper = true;
            else if (Character.isLowerCase(letter)) lower = true;
            else if (Character.isDigit(letter)) digit = true;
            else special = true;
        }

        if (password.length() >= 8 && upper && lower && digit && special)
            System.out.println("Strong Password");
        else
            System.out.println("Weak Password");

        sc.close();
    }
}
