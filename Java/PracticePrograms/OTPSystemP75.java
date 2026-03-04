// Program: OTP Generator and Validator

import java.util.Scanner;

public class OTPSystemP75 {

    static int[] generateOTP(int length) {

        int[] otp = new int[length];

        for (int i = 0; i < length; i++)
            otp[i] = (int)(Math.random() * 10);

        return otp;
    }

    static boolean validateOTP(int[] realOTP, int[] userOTP) {

        for (int i = 0; i < realOTP.length; i++)
            if (realOTP[i] != userOTP[i])
                return false;

        return true;
    }

    static void printOTP(int[] otp) {

        for (int d : otp)
            System.out.print(d);

        System.out.println();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] otp = generateOTP(4);

        System.out.print("Generated OTP (for testing): ");
        printOTP(otp);

        int attempts = 3;

        while (attempts > 0) {

            int[] userOTP = new int[4];

            System.out.println("Enter OTP:");

            for (int i = 0; i < 4; i++)
                userOTP[i] = sc.nextInt();

            if (validateOTP(otp, userOTP)) {
                System.out.println("OTP Verified");
                break;
            }
            else {
                attempts--;
                System.out.println("Invalid OTP. Attempts left: " + attempts);
            }

            if (attempts == 0)
                System.out.println("Access Blocked");
        }

        sc.close();
    }
}