// Practice Program: Voting System Analyzer

import java.util.Scanner;

public class VotingSystemP71 {

    static int countVotes(String[] votes, String candidate) {

        int count = 0;

        for (String v : votes)
            if (v.equalsIgnoreCase(candidate))
                count++;

        return count;
    }

    static void printVotes(String[] votes) {

        System.out.println("Votes Cast:");

        for (String v : votes)
            System.out.println(v);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] votes = new String[5];

        for (int i = 0; i < votes.length; i++) {
            System.out.print("Enter vote (A/B): ");
            votes[i] = sc.nextLine();
        }

        printVotes(votes);

        int aVotes = countVotes(votes, "A");
        int bVotes = countVotes(votes, "B");

        System.out.println("Votes for A: " + aVotes);
        System.out.println("Votes for B: " + bVotes);

        sc.close();
    }
}