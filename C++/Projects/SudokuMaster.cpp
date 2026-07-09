/*
 Sudoku Master (Mini Project)
 Basic OOP Sudoku Player
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class Sudoku {

    int board[9][9];
    int solution[9][9];
    int moves;
    string level;
    time_t startTime;

    // ---------- Random full-board generator ----------

    bool isValid(int grid[9][9], int r, int c, int num) {
        for(int i = 0; i < 9; i++) {
            if(grid[r][i] == num)
                return false;

            if(grid[i][c] == num)
                return false;
        }

        int boxRow = (r / 3) * 3;
        int boxCol = (c / 3) * 3;
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                if(grid[boxRow + i][boxCol + j] == num)
                    return false;
            }
        }

        return true;
    }

    void shuffleNums(int arr[9]) {
        for(int i = 8; i > 0; i--) {
            int j = rand() % (i + 1);
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }

    bool fillGrid(int grid[9][9], int pos) {
        if(pos == 81)
            return true;

        int r = pos / 9;
        int c = pos % 9;

        int nums[9] = {1,2,3,4,5,6,7,8,9};
        shuffleNums(nums);

        for(int k = 0; k < 9; k++) {
            int num = nums[k];
            if(isValid(grid, r, c, num)) {
                grid[r][c] = num;

                if(fillGrid(grid, pos + 1))
                    return true;

                grid[r][c] = 0;
            }
        }

        return false;
    }

    void generateSolution() {
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                solution[i][j] = 0;

        fillGrid(solution, 0);
    }

    void generatePuzzle(int cellsToRemove) {
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                board[i][j] = solution[i][j];

        // Build a flat list of the 81 cell positions, then shuffle it using plain arrays.
        int cellRow[81];
        int cellCol[81];
        int idx = 0;

        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                cellRow[idx] = i;
                cellCol[idx] = j;
                idx++;
            }
        }

        for(int i = 80; i > 0; i--) {
            int j = rand() % (i + 1);

            int tr = cellRow[i]; cellRow[i] = cellRow[j]; cellRow[j] = tr;
            int tc = cellCol[i]; cellCol[i] = cellCol[j]; cellCol[j] = tc;
        }

        if(cellsToRemove > 81)
            cellsToRemove = 81;

        for(int k = 0; k < cellsToRemove; k++) {
            board[cellRow[k]][cellCol[k]] = 0;
        }
    }

    void newGame(const string &lvl, int cellsToRemove) {
        level = lvl;
        moves = 0;
        generateSolution();
        generatePuzzle(cellsToRemove);
        startTime = time(0);
    }

    // Builds a plain "MM:SS" string from elapsed seconds, no <iomanip>.
    string formatTime(long totalSeconds) {
        long mins = totalSeconds / 60;
        long secs = totalSeconds % 60;

        string result = "";
        if(mins < 10)
            result += "0";

        result += to_string(mins);
        result += ":";

        if(secs < 10)
            result += "0";

        result += to_string(secs);

        return result;
    }

public:
    Sudoku() {
        moves = 0;
        srand((unsigned)time(0));
    }

    void loadEasy() {
        newGame("Easy",   40);
    }

    void loadMedium() {
        newGame("Medium", 46);
    }

    void loadHard() {
        newGame("Hard",   52);
    }

    void loadExpert() {
        newGame("Expert", 58);
    }

    void loadMaster() {
        newGame("Master", 64);
    }

    void display() {
        long elapsed = (long)difftime(time(0), startTime);

        cout << "\n=========== SUDOKU MASTER ===========\n";
        cout << "Difficulty: " << level << "   Moves: " << moves
             << "   Time: " << formatTime(elapsed) << "\n\n";
        cout << "    1 2 3   4 5 6   7 8 9\n";

        for(int i = 0; i < 9; i++) {
            if(i % 3 == 0)
                cout << "  +-------+-------+-------+\n";

            cout << i + 1 << " | ";

            for(int j = 0; j < 9; j++) {
                if(board[i][j] == 0)
                    cout << ". ";
                else
                    cout << board[i][j] << " ";

                if((j + 1) % 3 == 0)
                    cout << "| ";
            }
            cout << "\n";
        }
        cout << "  +-------+-------+-------+\n";
    }

    bool complete() {
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] == 0)
                    return false;
            }
        }

        return true;
    }

    void play() {
        int r, c, n;

        while(!complete()) {
            display();
            cout << "Enter Row Column Number (0 0 0 to Exit): ";
            cin >> r >> c >> n;

            if(cin.fail()) {
                cin.clear();
                cin.ignore(10000, '\n');
                cout << "Invalid input! Please enter numbers only.\n";
                continue;
            }

            if(r == 0 && c == 0 && n == 0)
                return;
            r--; c--;

            if(r < 0 || r > 8 || c < 0 || c > 8) {
                cout << "Invalid Position!\n";
                continue;
            }

            if(board[r][c] != 0) {
                cout << "Cell Already Filled!\n";
                continue;
            }

            if(solution[r][c] == n) {
                board[r][c] = n;
                moves++;
                cout << "Correct Move!\n";
            } else {
                cout << "Wrong Number! Try Again.\n";
            }
        }

        long finalElapsed = (long)difftime(time(0), startTime);
        display();
        cout << "\nCongratulations! Puzzle Solved in " << moves
             << " moves, Time: " << formatTime(finalElapsed) << "\n";
    }
};

int main() {
    Sudoku game;
    int ch;

    cout << "=========== SUDOKU MASTER ===========\n";
    cout << "1. Easy\n2. Medium\n3. Hard\n4. Expert\n5. Master\nChoice: ";
    cin >> ch;

    switch(ch) {
        case 1: game.loadEasy();   break;
        case 2: game.loadMedium(); break;
        case 3: game.loadHard();   break;
        case 4: game.loadExpert(); break;
        case 5: game.loadMaster(); break;
        default: game.loadEasy();  break;
    }

    game.play();

    return 0;
}
