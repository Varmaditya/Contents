// Program: Password Masking Simulation

import java.util.Scanner;

public class PasswordMaskingP24 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter username: ");
        String user = sc.nextLine();

        System.out.print("Enter password: ");
        String pass = sc.nextLine();

        System.out.println("\nLogin Details:");
        System.out.println("Username: " + user);
        System.out.println("Password: " + "*".repeat(pass.length()));

        sc.close();
    }
}
