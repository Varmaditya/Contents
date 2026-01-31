// Program: Profanity Filter

import java.util.Scanner;

public class ChatProfanityCheckerP61 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter message: ");
        String message = sc.nextLine().toLowerCase();

        String[] banned = {"bad", "ugly", "stupid"};

        for (String word : banned) {
            if (message.contains(word)) {
                message = message.replace(word, "***");
            }
        }

        System.out.println("Filtered message: " + message);
        sc.close();
    }
}
