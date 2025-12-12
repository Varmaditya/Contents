// Program: Student Result Evaluator

import java.util.Scanner;

public class StudentResultP9 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter marks for Subject 1: ");
        int m1 = sc.nextInt();

        System.out.print("Enter marks for Subject 2: ");
        int m2 = sc.nextInt();

        System.out.print("Enter marks for Subject 3: ");
        int m3 = sc.nextInt();

        boolean pass = (m1 >= 35) && (m2 >= 35) && (m3 >= 35);
        int total = m1 + m2 + m3;

        System.out.println("\nTotal Marks: " + total);
        System.out.println("Pass Status: " + pass);

        sc.close();
    }
}
