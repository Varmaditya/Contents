/*
Program: Wizard Battle Arena
Description: Demonstrates functions, pointers, loops and conditionals
by simulating a wizard battling against a monster.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//--------------- Functions ---------------//
void showStatus(int *wizardHP, int *monsterHP, int *mana) {
    cout << "\n====== BATTLE STATUS ======\n";
    cout << "Wizard HP : " << *wizardHP << endl;
    cout << "Monster HP: " << *monsterHP << endl;
    cout << "Mana      : " << *mana << endl;
}

void castFireball(int *monsterHP, int *mana) {
    if(*mana >= 20) {
        cout << "\nFireball Cast!\n";
        *monsterHP -= 30;
        *mana -= 20;
    } else {
        cout << "\nNot enough Mana!\n";
    }
}

void healWizard(int *wizardHP, int *mana) {
    if(*mana >= 15) {
        cout << "\nHealing Spell Used!\n";
        *wizardHP += 20;
        *mana -= 15;

        if(*wizardHP > 100)
            *wizardHP = 100;
    } else {
        cout << "\nNot enough Mana!\n";
    }
}

void monsterAttack(int *wizardHP) {
    int damage = rand() % 21 + 10;

    cout << "\nMonster attacks for " << damage << " damage!\n";

    *wizardHP -= damage;
}

//--------------- Main ---------------//
int main() {
    srand(time(0));

    int wizardHP = 100;
    int monsterHP = 120;
    int mana = 50;

    int *wizardPtr = &wizardHP;
    int *monsterPtr = &monsterHP;
    int *manaPtr = &mana;

    int choice;

    cout << "====== WIZARD BATTLE ARENA ======\n";

    while(*wizardPtr > 0 && *monsterPtr > 0) {
        showStatus(wizardPtr, monsterPtr, manaPtr);

        cout << "\n1. Fireball";
        cout << "\n2. Heal";
        cout << "\n3. Surrender";

        cout << "\n\nChoice : ";
        cin >> choice;

        switch(choice) {
            case 1:
                castFireball(monsterPtr, manaPtr);
                break;
            case 2:
                healWizard(wizardPtr, manaPtr);
                break;
            case 3:
                cout << "\nYou surrendered!\n";
                return 0;
            default:
                cout << "\nInvalid Choice!";
                continue;
        }

        if(*monsterPtr > 0)
            monsterAttack(wizardPtr);
    }

    if(*wizardPtr > 0)
        cout << "\nVictory! Monster Defeated!\n";
    else
        cout << "\nGame Over! The Monster Won!\n";

    return 0;
}
