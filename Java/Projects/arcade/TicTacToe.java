package arcade;

import java.util.Scanner;

public class TicTacToe {

    public static void play (String player) {

        Scanner sc = new Scanner(System.in);

        char board[][] = {
                {' ',' ',' '},
                {' ',' ',' '},
                {' ',' ',' '}
        };

        char current = 'X';

        for (int turn=0; turn<9; turn++) {
            printBoard(board);

            System.out.println("Player " + current + " enter row (0-2) and column (0-2):");

            int r = sc.nextInt();
            int c = sc.nextInt();

            if (board[r][c] == ' ') {
                board[r][c] = current;

                if (checkWin(board, current)) {
                    printBoard(board);
                    System.out.println("🏆 Player " + current + " wins!");
                    return;
                }

                current = (current == 'X') ? 'O' : 'X';
            } else {
                System.out.println("Cell already used!");
                turn--;
            }
        }

        printBoard(board);
        System.out.println("Game Draw!");
    }

    static void printBoard (char b[][]) {
        System.out.println("\n   0   1   2");

        for (int i=0; i<3; i++) {
            System.out.print(i + "  ");

            for (int j=0; j<3; j++) {
                System.out.print(b[i][j]);
                if (j < 2)
                    System.out.print(" | ");
            }

            System.out.println();

            if (i < 2)
                System.out.println("  ---+---+---");
        }
    }

    static boolean checkWin (char b[][], char p) {
        for (int i=0; i<3; i++) {
            if (b[i][0] == p && b[i][1] == p && b[i][2] == p)
                return true;
        }

        for (int i=0; i<3; i++) {
            if (b[0][i] == p && b[1][i] == p && b[2][i] == p)
                return true;
        }

        if (b[0][0] == p && b[1][1] == p && b[2][2] == p)
            return true;

        if (b[0][2] == p && b[1][1] == p && b[2][0] == p)
            return true;

        return false;
    }
}
