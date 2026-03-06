// Program: Palindrome Checker (Number and String)

import java.util.Scanner;

public class PalindromP80 {

    // Method to check palindrome number
    static boolean isNumberPalindrome(int num) {

        int original = num;
        int reverse = 0;

        while (num > 0) {

            int digit = num % 10;
            reverse = reverse * 10 + digit;
            num = num / 10;
        }

        return original == reverse;
    }

    // Method to check palindrome string
    static boolean isStringPalindrome(String text) {

        int start = 0;
        int end = text.length() - 1;

        while (start < end) {

            if (text.charAt(start) != text.charAt(end))
                return false;

            start++;
            end--;
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // -------- Number Palindrome --------
        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        if (isNumberPalindrome(number))
            System.out.println("Number is Palindrome");
        else
            System.out.println("Number is NOT Palindrome");

        sc.nextLine(); // clear buffer


        // -------- String Palindrome --------
        System.out.print("\nEnter a string: ");
        String word = sc.nextLine();

        if (isStringPalindrome(word))
            System.out.println("String is Palindrome");
        else
            System.out.println("String is NOT Palindrome");

        sc.close();
    }
}