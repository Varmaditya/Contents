// Program: Factorial Calculator

import java.util.Scanner;

public class FactorialNumberP79 {

    static long factorial(int n) {

        long fact = 1;

        for (int i = 1; i <= n; i++)
            fact *= i;

        return fact;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number: ");
        int n = sc.nextInt();

        System.out.println("Factorial: " + factorial(n));

        sc.close();
    }
}