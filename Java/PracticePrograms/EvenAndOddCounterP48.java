// Program: Even and Odd Counter

import java.util.Scanner;

public class EvenAndOddCounterP48 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] nums = new int[10];
        int even = 0, odd = 0;

        for (int i = 0; i < nums.length; i++) {
            System.out.print("Enter number: ");
            nums[i] = sc.nextInt();

            if (nums[i] % 2 == 0)
                even++;
            else
                odd++;
        }

        System.out.println("Even numbers: " + even);
        System.out.println("Odd numbers: " + odd);

        sc.close();
    }
}
