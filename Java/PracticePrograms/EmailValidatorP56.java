// Program: Advanced Email Validator

import java.util.Scanner;

public class EmailValidatorP56 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter email: ");
        String email = sc.nextLine();

        boolean valid = true;

        if (email.contains(" ")) valid = false;
        if (email.indexOf('@') != email.lastIndexOf('@')) valid = false;
        if (!email.contains("@")) valid = false;
        if (email.indexOf('.') < email.indexOf('@')) valid = false;
        if (email.length() < 8) valid = false;

        if (valid)
            System.out.println("Valid Email");
        else
            System.out.println("Invalid Email");

        sc.close();
    }
}
