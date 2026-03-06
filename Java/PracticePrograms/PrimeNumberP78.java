// Program: Prime Number Checker

import java.util.Scanner;

public class PrimeNumberP78 {

    static boolean isPrime(int num) {

        if (num <= 1)
            return false;

        for (int i = 2; i <= num / 2; i++)
            if (num % i == 0)
                return false;

        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number: ");
        int n = sc.nextInt();

        if (isPrime(n))
            System.out.println("Prime Number");
        else
            System.out.println("Not Prime");

        sc.close();
    }
}