// Program: Domain Extractor

import java.util.Scanner;

public class DomainExtractorP60 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter URL: ");
        String url = sc.nextLine();

        int start = url.indexOf("www.") + 4;
        int end = url.indexOf("/", start);

        if (start > 3 && end != -1)
            System.out.println("Domain: " + url.substring(start, end));
        else
            System.out.println("Invalid URL");

        sc.close();
    }
}
