// Program: BMI Calculator

import java.util.Scanner;

public class BMICalculatorP11 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter weight (kg): ");
        double weight = sc.nextDouble();

        System.out.print("Enter height (meters): ");
        double height = sc.nextDouble();

        double bmi = weight / (height * height);

        System.out.println("Your BMI: " + bmi);

        sc.close();
    }
}
