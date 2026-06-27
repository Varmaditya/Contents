/*
Program: Tic Tac Toe
Description: A two-player Tic Tac Toe game demonstrating
functions, pointers, loops, conditionals and 2D arrays.
*/

#include <iostream>
using namespace std;

//------------- Functions -------------//
void displayBoard(char (*board)[3]) {
    cout << endl;

    for(int row=0; row<3; row++) {
        for(int col=0; col<3; col++) {
            cout << " " << board[row][col] << " ";
            if(col<2)
                cout << "|";
        }

        cout << endl;

        if(row<2)
            cout << "---+---+---\n";
    }

    cout << endl;
}

bool checkWinner(char (*board)[3], char player) {
    for(int i=0;i<3;i++) {
        if(board[i][0]==player && board[i][1]==player && board[i][2]==player)
            return true;

        if(board[0][i]==player && board[1][i]==player && board[2][i]==player)
            return true;
    }

    if(board[0][0]==player && board[1][1]==player && board[2][2]==player)
        return true;

    if(board[0][2]==player && board[1][1]==player && board[2][0]==player)
        return true;

    return false;
}

bool boardFull(char (*board)[3]) {
    for(int row=0; row<3; row++) {
        for(int col=0; col<3; col++) {
            if(board[row][col]==' ')
                return false;
        }
    }

    return true;
}

//------------- Main -------------//
int main() {
    char board[3][3] = {
        {' ',' ',' '},
        {' ',' ',' '},
        {' ',' ',' '}
    };

    int row, col;
    char player='X';

    cout << "====== TIC TAC TOE ======\n";

    while(true) {
        displayBoard(board);

        cout << "Player " << player << " Turn\n";

        cout << "Enter Row (1-3): ";
        cin >> row;

        cout << "Enter Column (1-3): ";
        cin >> col;

        row--;
        col--;

        if(row<0 || row>2 || col<0 || col>2) {
            cout << "\nInvalid Position!\n";
            continue;
        }

        if(board[row][col]!=' ') {
            cout << "\nCell Already Occupied!\n";
            continue;
        }

        board[row][col]=player;

        if(checkWinner(board,player)) {
            displayBoard(board);

            cout << "Player " << player << " Wins!\n";
            break;
        }

        if(boardFull(board)) {
            displayBoard(board);

            cout << "Match Draw!\n";
            break;
        }

        if(player=='X')
            player='O';
        else
            player='X';
    }

    return 0;
}
