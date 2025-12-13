// Program: Grade Calculator

import java.util.Scanner;

public class GradeCalculatorP13 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int marks = sc.nextInt();

        String grade = (marks >= 90) ? "A+" :
                (marks >= 75) ? "A" :
                        (marks >= 60) ? "B" :
                                (marks >= 50) ? "C" : "D";

        System.out.println("Grade: " + grade);

        sc.close();
    }
}
