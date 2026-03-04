// Program: Password Strength Checker

import java.util.Scanner;

public class PasswordStrenghtCheckP74 {

    static boolean hasUpper(String pass) {

        for (char c : pass.toCharArray())
            if (Character.isUpperCase(c))
                return true;

        return false;
    }

    static boolean hasLower(String pass) {

        for (char c : pass.toCharArray())
            if (Character.isLowerCase(c))
                return true;

        return false;
    }

    static boolean hasDigit(String pass) {

        for (char c : pass.toCharArray())
            if (Character.isDigit(c))
                return true;

        return false;
    }

    static boolean hasSpecial(String pass) {

        String special = "!@#$%^&*";

        for (char c : pass.toCharArray())
            if (special.indexOf(c) != -1)
                return true;

        return false;
    }

    static boolean isCommonPassword(String pass) {

        String[] common = {"password", "123456", "admin", "qwerty"};

        for (String p : common)
            if (pass.equalsIgnoreCase(p))
                return true;

        return false;
    }

    static int calculateStrength(String pass) {

        int score = 0;

        if (pass.length() >= 8) score++;

        if (hasUpper(pass)) score++;

        if (hasLower(pass)) score++;

        if (hasDigit(pass)) score++;

        if (hasSpecial(pass)) score++;

        if (isCommonPassword(pass))
            score = 0;

        return score;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter password: ");
        String password = sc.nextLine();

        int strength = calculateStrength(password);

        if (strength >= 4)
            System.out.println("Strong Password");
        else if (strength >= 2)
            System.out.println("Medium Password");
        else
            System.out.println("Weak Password");

        sc.close();
    }
}