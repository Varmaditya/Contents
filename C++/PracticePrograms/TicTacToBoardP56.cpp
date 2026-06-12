/*
Program: Tic Tac Toe Board Viewer
Description: Displays a tic tac toe board using 2D arrays.
*/

#include <iostream>
using namespace std;

int main() {

    char board[3][3] = {
        {'X','O','X'},
        {'O','X','O'},
        {'X',' ','O'}
    };

    cout << "Tic Tac Toe Board\n\n";

    for(int row = 0; row < 3; row++) {

        for(int column = 0; column < 3; column++) {

            cout << board[row][column] << " ";
        }

        cout << endl;
    }

    return 0;
}