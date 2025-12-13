// Program: Currency Converter (INR to USD, EUR, GBP)

import java.util.Scanner;

public class CurrencyConverterP16 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter amount in INR: ");
        double inr = sc.nextDouble();

        double usd = inr / 83.0;
        double eur = inr / 90.0;
        double gbp = inr / 105.0;

        System.out.println("\nUSD: " + usd);
        System.out.println("EUR: " + eur);
        System.out.println("GBP: " + gbp);

        sc.close();
    }
}
