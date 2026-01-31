// Program: Sentence Analyzer

import java.util.Scanner;

public class SentenceAnalyzerP59 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter sentence: ");
        String sentence = sc.nextLine();

        int vowels = 0, digits = 0, words = 1;

        for (int i = 0; i < sentence.length(); i++) {
            char letter = Character.toLowerCase(sentence.charAt(i));

            if ("aeiou".indexOf(letter) != -1) vowels++;
            if (Character.isDigit(letter)) digits++;
            if (letter == ' ') words++;
        }

        System.out.println("Words: " + words);
        System.out.println("Vowels: " + vowels);
        System.out.println("Digits: " + digits);

        sc.close();
    }
}
