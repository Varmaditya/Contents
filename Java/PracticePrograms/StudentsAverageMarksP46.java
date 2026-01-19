// Program: Student Marks Average

import java.util.Scanner;

public class StudentsAverageMarksP46 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] marks = new int[5];
        int sum = 0;

        for (int i = 0; i < marks.length; i++) {
            System.out.print("Enter marks of student " + (i + 1) + ": ");
            marks[i] = sc.nextInt();
            sum += marks[i];
        }

        double avg = sum / (double) marks.length;
        System.out.println("Average Marks: " + avg);

        sc.close();
    }
}
