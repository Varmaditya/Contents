package arcade;

import java.util.*;

public class RockPaperScissors {

    public static void play (String player) {

        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        String options[] = {"Rock","Paper","Scissors"};

        System.out.println("\n=== Rock Paper Scissors ===");
        System.out.println("Choose Match Type:");
        System.out.println("1 Best of 3");
        System.out.println("2 Best of 5");

        int rounds = (sc.nextInt() == 1) ? 3 : 5;

        int userScore = 0;
        int compScore = 0;

        for (int i=1; i<=rounds; i++) {
            System.out.println("\nRound " + i);

            System.out.println("0 Rock  1 Paper  2 Scissors");
            int user = sc.nextInt();

            int comp=rand.nextInt(3);

            System.out.println(player+" chose "+options[user]);
            System.out.println("Computer chose "+options[comp]);

            if (user == comp) {
                System.out.println("Draw");
            } else if ((user == 0 && comp == 2) || (user == 1 && comp == 0) || (user == 2 && comp == 1)) {
                System.out.println("You win round!");
                userScore++;
            } else {
                System.out.println("Computer wins round!");
                compScore++;
            }

            System.out.println("Score: " + player + " " + userScore + " - " + compScore + " Computer");
        }

        if (userScore > compScore)
            System.out.println("🏆 You win the match!");
        else if (compScore > userScore)
            System.out.println("Computer wins the match!");
        else
            System.out.println("Match Draw!");
    }
}