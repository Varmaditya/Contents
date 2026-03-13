package arcade;

import java.util.*;

public class Hangman {

    public static void play (String player) {

        Scanner sc = new Scanner(System.in);

        String words[] = {
                "computer", "programming", "interface",
                "algorithm" ,"developer", "variable"
        };

        String hints[] = {
                "Machine used to run programs",
                "Process of writing code",
                "Connection between systems",
                "Step-by-step problem solving",
                "Person who writes software",
                "Stores values in code"
        };

        Random rand = new Random();

        int index = rand.nextInt(words.length);

        String word = words[index];
        String hint = hints[index];

        char guessed[] = new char[word.length()];
        Arrays.fill(guessed,'_');

        int lives = 6;

        System.out.println("\n=== HANGMAN ===");
        System.out.println("Hint: " + hint);

        HashSet<Character> used = new HashSet<>();

        while (lives > 0) {
            System.out.println("\nWord: " + String.valueOf(guessed));
            System.out.println("Lives: " + lives);
            System.out.println("Used letters: " + used);

            System.out.print("Guess letter: ");
            char ch = sc.next().charAt(0);

            if (used.contains(ch)) {
                System.out.println("Already guessed!");
                continue;
            }

            used.add(ch);
            boolean found = false;

            for (int i = 0; i<word.length(); i++) {
                if (word.charAt(i) == ch) {
                    guessed[i] = ch;
                    found = true;
                }
            }

            if (!found) {
                lives--;
                System.out.println("Wrong guess!");
            }

            if (word.equals(String.valueOf(guessed))) {
                System.out.println("\n🎉 You guessed the word: " + word);
                return;
            }
        }

        System.out.println("\nGame Over! Word was: " + word);
    }
}
