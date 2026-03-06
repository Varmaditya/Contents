// Program: Fibonacci Series

import java.util.Scanner;

public class FibonnaciSeriesP76 {

    static void generateFibonacci(int n) {

        int a = 0, b = 1;

        for (int i = 1; i <= n; i++) {

            System.out.print(a + " ");

            int next = a + b;
            a = b;
            b = next;
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of terms: ");
        int n = sc.nextInt();

        generateFibonacci(n);

        sc.close();
    }
}