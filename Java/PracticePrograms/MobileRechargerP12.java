// Program: Mobile Recharge Validator

import java.util.Scanner;

public class MobileRechargerP12 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter recharge amount: ");
        int amount = sc.nextInt();

        boolean valid = (amount == 99) || (amount == 199) || (amount == 399);

        System.out.println("Is valid recharge plan: " + valid);

        sc.close();
    }
}
