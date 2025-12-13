// Program: Restaurant Bill Splitter

import java.util.Scanner;

public class BillSplitterP14 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter total bill: ");
        double bill = sc.nextDouble();

        System.out.print("Enter number of people: ");
        int people = sc.nextInt();

        double perPerson = bill / people;

        System.out.println("Each person should pay: " + perPerson);

        sc.close();
    }
}
