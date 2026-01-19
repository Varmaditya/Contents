// Program: Monthly Expense Tracker

import java.util.Scanner;

public class ExpenseTrackerP50 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double[] expenses = new double[6];
        double total = 0;

        for (int i = 0; i < expenses.length; i++) {
            System.out.print("Enter expense for day " + (i + 1) + ": ");
            expenses[i] = sc.nextDouble();
            total += expenses[i];
        }

        double avg = total / expenses.length;

        System.out.println("Total expense: ₹" + total);
        System.out.println("Average daily expense: ₹" + avg);

        sc.close();
    }
}
