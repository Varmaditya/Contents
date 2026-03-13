package arcade;

import java.util.Scanner;

public class Arcade {

    static Scanner sc = new Scanner(System.in);

    public static void main (String[] args) {

        System.out.println("🎮 ===== CONSOLE ARCADE ===== 🎮");

        System.out.print("Enter Player Name: ");
        String player = sc.nextLine();

        int choice;
        char again;

        do {

            System.out.println("\nSelect Game");
            System.out.println("1. Tic Tac Toe");
            System.out.println("2. Rock Paper Scissors");
            System.out.println("3. Hangman");
            System.out.println("4. Exit");

            System.out.print("Choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    TicTacToe.play(player);
                    break;
                case 2:
                    RockPaperScissors.play(player);
                    break;
                case 3:
                    Hangman.play(player);
                    break;
                case 4:
                    System.out.println("Thanks for playing!");
                    return;
                default:
                    System.out.println("Invalid choice");
            }

            System.out.print("\nPlay another game? (y/n): ");
            again = sc.next().charAt(0);

        } while (again == 'y' || again == 'Y');

        System.out.println("Goodbye " + player + "!");
    }
}
