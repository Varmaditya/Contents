// Program: Student Information Card

import java.util.Scanner;

public class StudentCardP2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter student name: ");
        String name = sc.nextLine();

        System.out.print("Enter course name: ");
        String course = sc.nextLine();

        System.out.print("Enter roll number: ");
        int roll = sc.nextInt();

        System.out.println("\n===== STUDENT INFORMATION CARD =====");
        System.out.println("Name: " + name);
        System.out.println("Course: " + course);
        System.out.println("Roll Number: " + roll);

        sc.close();
    }
}
