/*
Program: Mini Image Editor
Description: Creates a black and white image grid.
*/

#include <iostream>
using namespace std;

int main() {

    int pixels[5][5];

    cout << "Enter pixel values (0 or 1)\n";

    for(int row = 0; row < 5; row++) {
        for(int column = 0; column < 5; column++) {
            cin >> pixels[row][column];
        }
    }

    cout << "\nImage Preview\n\n";

    for(int row = 0; row < 5; row++) {
        for(int column = 0; column < 5; column++) {
            if(pixels[row][column] == 1)
                cout << "⬜";
            else
                cout << "⬛";
        }

        cout << endl;
    }

    return 0;
}
