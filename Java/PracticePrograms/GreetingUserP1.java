// Program: Greeting User

import java.util.Scanner;

public class GreetingUserP1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.println("\nHello, \"" + name + "\"!");
        System.out.println("Welcome to Java Programming.\n");

        sc.close();
    }
}
