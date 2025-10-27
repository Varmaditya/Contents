/*--------------------------------------------------------
    Author: Aditya Varma
    Date: 26/07/2023
    Project Title : Tic Tac Toe Game in C
    Description   : Two-player game played on a 3x3 grid.
                    Players take turns marking cells as X or O.
                    The game ends when one player wins or
                    when all cells are filled (draw).
    Concepts Used : Arrays, Loops, Functions, Conditionals, I/O
----------------------------------------------------------*/

#include <stdio.h>
#include <conio.h>  // Optional: for getch() to pause screen
#include <stdlib.h> // For system("cls") to clear screen

// Global 3x3 array to store the game board
char board[3][3] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'}
};

// Function Prototypes
void displayBoard();
int checkWinner();
int isDraw();
void markBoard(int choice, char mark);

// Main Function
int main() {
    int player = 1;       // Player 1 starts first
    int choice;           // Position selected by player
    char mark;            // X or O
    int status = -1;      // -1 = game continues, 1 = win, 0 = draw

    do {
        system("cls"); // Clear screen (for better visibility)

        printf("\n\tTIC TAC TOE GAME\n");
        printf("\t----------------\n");
        printf("\nPlayer 1 (X)  -  Player 2 (O)\n\n");

        // Display current game board
        displayBoard();

        // Determine which player's turn it is
        player = (player % 2) ? 1 : 2;
        mark = (player == 1) ? 'X' : 'O';

        // Ask the player for a move
        printf("Player %d, enter the position (1-9): ", player);
        scanf("%d", &choice);

        // Update board with the player's mark
        markBoard(choice, mark);

        // Check if someone has won or if it’s a draw
        if (checkWinner()) {
            system("cls");
            displayBoard();
            printf("\n==> Player %d wins! \n", player);
            status = 1; // Game ends with a win
            break;
        } else if (isDraw()) {
            system("cls");
            displayBoard();
            printf("\n==> Game Draw! \n");
            status = 0; // Game ends with a draw
            break;
        }

        player++; // Move to next player

    } while (status == -1);

    printf("\nThank you for playing Tic Tac Toe!\n");

    getch(); // Wait for key press before closing
    return 0;
}

/*--------------------------------------------------------
    Function : displayBoard()
    Purpose  : Displays the current Tic Tac Toe board
----------------------------------------------------------*/
void displayBoard() {
    printf("\n\t %c | %c | %c ", board[0][0], board[0][1], board[0][2]);
    printf("\n\t---|---|---");
    printf("\n\t %c | %c | %c ", board[1][0], board[1][1], board[1][2]);
    printf("\n\t---|---|---");
    printf("\n\t %c | %c | %c \n\n", board[2][0], board[2][1], board[2][2]);
}

/*--------------------------------------------------------
    Function : markBoard()
    Purpose  : Places player mark on selected position
----------------------------------------------------------*/
void markBoard(int choice, char mark) {
    int row = (choice - 1) / 3; // Convert 1-9 choice into 2D indices
    int col = (choice - 1) % 3;

    // Check if position is valid and not already taken
    if (choice < 1 || choice > 9 || board[row][col] == 'X' || board[row][col] == 'O') {
        printf("Invalid move! Try again.\n");
        getch();
    } else {
        board[row][col] = mark;
    }
}

/*--------------------------------------------------------
    Function : checkWinner()
    Purpose  : Checks all possible winning combinations
----------------------------------------------------------*/
int checkWinner() {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == board[i][1] && board[i][1] == board[i][2]) ||
            (board[0][i] == board[1][i] && board[1][i] == board[2][i])) {
            return 1;
        }
    }

    // Check diagonals
    if ((board[0][0] == board[1][1] && board[1][1] == board[2][2]) ||
        (board[0][2] == board[1][1] && board[1][1] == board[2][0])) {
        return 1;
    }

    return 0; // No winner yet
}

/*--------------------------------------------------------
    Function : isDraw()
    Purpose  : Checks if all cells are filled (draw)
----------------------------------------------------------*/
int isDraw() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] != 'X' && board[i][j] != 'O')
                return 0; // Still empty cell, game continues
        }
    }
    return 1; // All cells filled, game is a draw
}

