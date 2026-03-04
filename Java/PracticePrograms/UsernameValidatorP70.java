// Practice Program: Username Validator

import java.util.Scanner;

public class UsernameValidatorP70 {

    static boolean usernameExists(String[] users, String name) {

        for (String u : users)
            if (u.equalsIgnoreCase(name))
                return true;

        return false;
    }

    static void printUsers(String[] users) {

        System.out.println("Registered Users:");

        for (String u : users)
            System.out.println(u);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] users = {"amit", "rahul", "neha", "sara"};

        printUsers(users);

        System.out.print("Enter username to search: ");
        String name = sc.nextLine();

        if (usernameExists(users, name))
            System.out.println("User Found");
        else
            System.out.println("User Not Found");

        sc.close();
    }
}