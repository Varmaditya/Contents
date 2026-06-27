/*
Program: Car Racing Simulator
Description: Demonstrates functions, pointers, loops and conditionals
by simulating a simple racing game.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//---------------- Functions ----------------//
void showStatus(int *speed, int *fuel) {
    cout << "\nSpeed : " << *speed << " km/h";
    cout << "\nFuel  : " << *fuel << "%\n";
}

void accelerate(int *speed, int *fuel) {
    if(*fuel >= 10) {
        *speed += 20;
        *fuel -= 10;
        cout << "\nCar Accelerated!\n";
    } else {
        cout << "\nNot Enough Fuel!\n";
    }
}

void useNitro(int *speed, int *fuel) {
    if(*fuel >= 20) {
        *speed += 50;
        *fuel -= 20;
        cout << "\nNitro Boost Activated!\n";
    } else {
        cout << "\nNitro Failed! Low Fuel.\n";
    }
}

void obstacle(int *speed) {
    if(rand() % 3 == 0) {
        cout << "\nObstacle Hit! Speed Reduced.\n";
        *speed -= 30;

        if(*speed < 0)
            *speed = 0;
    }
}

//---------------- Main ----------------//
int main() {
    srand(time(0));

    int speed = 0;
    int fuel = 100;

    int *speedPtr = &speed;
    int *fuelPtr = &fuel;

    int choice;

    cout << "====== CAR RACING SIMULATOR ======\n";

    do {
        cout << "\n1. Accelerate";
        cout << "\n2. Nitro Boost";
        cout << "\n3. Show Dashboard";
        cout << "\n4. Finish Race";

        cout << "\n\nChoice : ";
        cin >> choice;

        switch(choice) {
            case 1:
                accelerate(speedPtr, fuelPtr);
                obstacle(speedPtr);
                break;
            case 2:
                useNitro(speedPtr, fuelPtr);
                obstacle(speedPtr);
                break;
            case 3:
                showStatus(speedPtr, fuelPtr);
                break;
            case 4:
                cout << "\nRace Finished!\n";
                cout << "Final Speed : "
                     << *speedPtr
                     << " km/h\n";
                break;
            default:
                cout << "\nInvalid Choice!";
        }
    } while(choice != 4);

    return 0;
}
