// Program: Bio Data Form

import java.util.Scanner;

public class BioDataP3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        System.out.print("Enter your height (in cm): ");
        double height = sc.nextDouble();

        System.out.println("\n===== BIO DATA =====");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height + " cm");

        sc.close();
    }
}
