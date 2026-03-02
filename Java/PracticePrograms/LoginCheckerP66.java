// Practice Program: Secure Login with Lock

import java.util.Scanner;

public class LoginCheckerP66 {

    static boolean authenticate(String user, String pass) {
        return user.equals("admin") && pass.equals("Java123");
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int attempts = 0;

        while (attempts < 3) {

            System.out.print("Username: ");
            String user = sc.nextLine();

            System.out.print("Password: ");
            String pass = sc.nextLine();

            if (authenticate(user, pass)) {
                System.out.println("Login Successful");
                break;
            } else {
                System.out.println("Invalid Credentials");
            }

            attempts++;

            if (attempts == 3) {
                System.out.println("Account Locked");
            }
        }

        sc.close();
    }
}