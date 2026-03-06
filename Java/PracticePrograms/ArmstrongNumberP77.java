// Program: Armstrong Number Checker

import java.util.Scanner;

public class ArmstrongNumberP77 {

    static boolean isArmstrong(int num) {

        int original = num;
        int sum = 0;

        while (num > 0) {

            int digit = num % 10;
            sum += digit * digit * digit;
            num /= 10;
        }

        return sum == original;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number: ");
        int n = sc.nextInt();

        if (isArmstrong(n))
            System.out.println("Armstrong Number");
        else
            System.out.println("Not Armstrong");

        sc.close();
    }
}