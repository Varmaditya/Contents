// Program: Secure Login System

import java.util.Scanner;

public class LoginCheckerP58 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String correctUser = "Admin";
        String correctPass = "Java@123";

        int attempts = 0;
        boolean success = false;

        while (attempts < 3) {

            System.out.print("Username: ");
            String user = sc.nextLine();

            System.out.print("Password: ");
            String pass = sc.nextLine();

            if (user.equals(correctUser) && pass.equals(correctPass)) {
                success = true;
                break;
            } else {
                System.out.println("Invalid credentials");
            }

            attempts++;
        }

        if (success)
            System.out.println("Login Successful");
        else
            System.out.println("Account Locked");

        sc.close();
    }
}
