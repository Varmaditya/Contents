// Practice Program: Even or Odd Checker using Method

import java.util.Scanner;

public class EvenOddMethodP62 {

    // Method to check even or odd
    static void checkEvenOdd(int num) {
        if (num % 2 == 0)
            System.out.println("Number is Even");
        else
            System.out.println("Number is Odd");
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        // Calling method
        checkEvenOdd(number);

        sc.close();
    }
}