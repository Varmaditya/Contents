/*
 Program : Treasure Hunt Adventure
 Description : A mini adventure game demonstrating
 Functions, Arrays, Pointers, Loops and Conditionals.
*/

#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;


// Display Game Map
void displayMap(char map[][5]) {
    cout << "\n========= MAP =========\n\n";

    for(int row=0; row<5; row++) {
        for(int col=0; col<5; col++) {
            cout << map[row][col] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// Display Player Status
void showStatus(int *health, int *gold, int *keys){
    cout << "\n====== PLAYER STATUS ======\n";

    cout << "Health : " << *health << endl;
    cout << "Gold   : " << *gold << endl;
    cout << "Keys   : " << *keys << endl;

    cout << "===========================\n";
}

// Explore Random Location
void exploreLocation(char map[][5], int *health, int *gold, int *keys){
    int row = rand()%5;
    int col = rand()%5;

    cout << "\nExploring Location (" << row+1 << "," << col+1 << ")\n";

    if(map[row][col]=='T') {
        cout<<" Treasure Found!\n";
        *gold += 100;
        map[row][col]='V';
    } else if(map[row][col]=='K') {
        cout<<"Magic Key Found!\n";
        (*keys)++;
        map[row][col]='V';
    } else if(map[row][col]=='X') {
        cout<<"Trap Activated!\n";
        *health -= 25;
        map[row][col]='V';
    } else if(map[row][col]=='V') {
        cout<<"Already Explored.\n";
    } else {
        cout<<"Nothing Here.\n";
        map[row][col]='V';
    }
}

// Win Condition
bool treasureFound(int keys) {
    return keys>=2;
}

// Main Function
int main() {
    srand(time(0));

    char map[5][5]= {
        {'T','.','.','X','.'},
        {'.','K','.','.','T'},
        {'.','.','X','.','.'},
        {'K','.','.','.','X'},
        {'.','.','T','.','.'}
    };

    int health=100;
    int gold=0;
    int keys=0;

    int *healthPtr=&health;
    int *goldPtr=&gold;
    int *keyPtr=&keys;

    int choice;

    cout<<"\n==================================\n";
    cout<<"     TREASURE HUNT ADVENTURE\n";
    cout<<"==================================\n";

    do {
        cout<<"\n1. View Map\n";
        cout<<"2. Explore Location\n";
        cout<<"3. View Status\n";
        cout<<"4. Exit\n";

        cout<<"\nEnter Choice : ";
        cin>>choice;

        switch(choice) {
            case 1:
                displayMap(map);
                break;
            case 2:
                exploreLocation(map, healthPtr, goldPtr, keyPtr);
                if(*healthPtr<=0) {
                    cout<<"\nGame Over!\n";
                    return 0;
                }

                if(treasureFound(*keyPtr)) {
                    cout<<"\nCongratulations!\n";
                    cout<<"You collected enough keys to unlock the Treasure Castle!\n";
                    cout<<"Final Gold : " <<*goldPtr <<endl;

                    return 0;
                }

                break;
            case 3:
                showStatus(healthPtr, goldPtr, keyPtr);
                break;
            case 4:
                cout<<"\nThanks For Playing!\n";
                break;
            default:
                cout<<"\nInvalid Choice!\n";
        }
    } while(choice!=4);

    return 0;
}
