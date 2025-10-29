/*--------------------------------------------------------------
    Author: Aditya Varma
    Date: 15/08/2023
    Project Title   : Snake and Ladder Game
    Description     : A two-player console-based Snake and Ladder game
                     that simulates dice rolls, snakes, ladders, and
                     displays the board dynamically with player positions.
    Rules and Features:
     - The game begins with any dice value (1–6).
     - If the dice rolls 6, the player gets another chance.
     - Snakes and Ladders are shown as 'S' and 'L' on the board.
     - Players are displayed as 'P1' and 'P2' directly on the board.
     - Snakes: 99→1, 65→40, 25→9
       Ladders: 13→42, 60→83, 70→93
     - The first player to reach exactly 100 wins the game.
    Concepts Used   : Loops, Functions, Arrays, Conditional Statements,
                     Switch Case, Random Number Generation.
--------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>

/*--------------------------------------------------------------
   Function: rd
   Purpose : Generates a random dice value between 1 and 6.
--------------------------------------------------------------*/
int rd() {
    int rem;
A:
    rem = rand() % 7;
    if (rem == 0)
        goto A;
    else
        return rem;
}

/*--------------------------------------------------------------
   Function: displayChart
   Purpose : Displays the 10x10 Snake and Ladder board.
             Marks Snakes (S), Ladders (L), and Player Positions.
--------------------------------------------------------------*/
void displayChart(int p1, int p2) {
    int i, j, num, shift = 0;

    printf("\n\t\t\t---- SNAKE AND LADDER BOARD ----\n\n");

    // The board contains 10 rows (10x10 grid)
    for (i = 10; i > 0; i--) {
        int rowBase = (i - 1) * 10;

        // Left-to-right numbering
        if (shift % 2 == 0) {
            for (j = 10; j >= 1; j--) {
                num = rowBase + j;

                // Display player positions
                if (num == p1 && num == p2)
                    printf("P1P2\t");
                else if (num == p1)
                    printf("P1\t");
                else if (num == p2)
                    printf("P2\t");

                // Display Snakes and Ladders
                else if (num == 99 || num == 65 || num == 25)
                    printf("S\t");
                else if (num == 70 || num == 60 || num == 13)
                    printf("L\t");
                else
                    printf("%d\t", num);
            }
        } else {  // Right-to-left numbering
            for (j = 1; j <= 10; j++) {
                num = rowBase + j;

                if (num == p1 && num == p2)
                    printf("P1P2\t");
                else if (num == p1)
                    printf("P1\t");
                else if (num == p2)
                    printf("P2\t");
                else if (num == 99 || num == 65 || num == 25)
                    printf("S\t");
                else if (num == 70 || num == 60 || num == 13)
                    printf("L\t");
                else
                    printf("%d\t", num);
            }
        }

        shift++;
        printf("\n\n");
    }

    printf("--------------------------------------------------------------------------\n");
    printf("Player 1 Position: %d\t|\tPlayer 2 Position: %d\n", p1, p2);
    printf("--------------------------------------------------------------------------\n");
}

/*--------------------------------------------------------------
   Function: movePlayer
   Purpose : Moves the player according to dice value and applies
             Snake or Ladder effect if present.
--------------------------------------------------------------*/
int movePlayer(int curPos, int dice, int playerNum) {
    curPos += dice;

    // Check if player exceeds 100
    if (curPos > 100) {
        curPos -= dice;
        printf("Player %d exceeded 100! Staying at %d.\n", playerNum, curPos);
        return curPos;
    }

    // Snake positions
    if
        (curPos == 99) curPos = 1;
    else if
        (curPos == 65) curPos = 40;
    else if
        (curPos == 25) curPos = 9;

    // Ladder positions
    else if
        (curPos == 13) curPos = 42;
    else if
        (curPos == 60) curPos = 83;
    else if
        (curPos == 70) curPos = 93;

    return curPos;
}

/*--------------------------------------------------------------
   Function: main
   Purpose : The main control function to execute the game.
             Handles player turns, dice rolls, and win conditions.
--------------------------------------------------------------*/
int main() {
    int curPos1 = 0, curPos2 = 0, dice;
    char choice;

    while (1) {
        system("cls"); // Clears the screen (Windows only)
        printf("\n\t\t\t    ** SNAKE AND LADDER GAME **\n\t\t\t      (Two Player Version)\n");
        printf("--------------------------------------------------------------------------\n");

        displayChart(curPos1, curPos2);

        printf("\n1. Player 1 plays\n2. Player 2 plays\n3. Exit\nEnter your choice: ");
        scanf(" %c", &choice);

        switch (choice) {
            case '1':
                dice = rd();
                printf("\nPlayer 1 rolled a %d\n", dice);
                curPos1 = movePlayer(curPos1, dice, 1);

                if (curPos1 == 100) {
                    displayChart(curPos1, curPos2);
                    printf("\n Player 1 Wins the Game! \n");
                    exit(0);
                }
                break;

            case '2':
                dice = rd();
                printf("\nPlayer 2 rolled a %d\n", dice);
                curPos2 = movePlayer(curPos2, dice, 2);

                if (curPos2 == 100) {
                    displayChart(curPos1, curPos2);
                    printf("\n Player 2 Wins the Game! \n");
                    exit(0);
                }
                break;

            case '3':
                printf("Thanks for playing!\n");
                exit(0);

            default:
                printf("Invalid choice! Try again.\n");
        }

        printf("\nPress Enter to continue...");
        getchar();
        getchar();
    }

    return 0;
}
