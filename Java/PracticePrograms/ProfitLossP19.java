// Program: Profit or Loss Calculator

import java.util.Scanner;

public class ProfitLossP19 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Cost Price: ");
        double cp = sc.nextDouble();

        System.out.print("Enter Selling Price: ");
        double sp = sc.nextDouble();

        String result = (sp > cp) ? "Profit" : "Loss";
        double amount = (sp > cp) ? (sp - cp) : (cp - sp);

        System.out.println(result + ": " + amount);

        sc.close();
    }
}
