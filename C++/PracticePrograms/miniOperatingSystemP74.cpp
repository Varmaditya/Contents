/*
Program: Mini Operating System
Description: Demonstrates Object-Oriented Programming by creating
a simple operating system with different built-in applications.
*/

#include <iostream>
#include <ctime>
using namespace std;

class MiniOS {
private:

    string notes[5];
    int noteCount;

public:

    MiniOS() {
        noteCount = 0;
    }

    void showDesktop() {
        cout << "\n========== MINI OS ==========\n";
        cout << "1. Calculator\n";
        cout << "2. Notes\n";
        cout << "3. Clock\n";
        cout << "4. About System\n";
        cout << "5. Shutdown\n";
    }

    void calculator() {
        float num1, num2;
        char op;

        cout << "\nEnter Expression (Example: 10 + 20): ";
        cin >> num1 >> op >> num2;

        switch(op) {
            case '+': cout << "Result = " << num1 + num2; break;
            case '-': cout << "Result = " << num1 - num2; break;
            case '*': cout << "Result = " << num1 * num2; break;
            case '/': cout << "Result = " << num1 / num2; break;
            default : cout << "Invalid Operator!";
        }

        cout << endl;
    }

    void notesApp() {
        cin.ignore();

        if(noteCount < 5) {
            cout << "\nWrite Note : ";
            getline(cin, notes[noteCount]);

            noteCount++;

            cout << "Note Saved Successfully!\n";
        } else {
            cout << "\nStorage Full!\n";
        }

        cout << "\nSaved Notes\n";

        for(int i=0;i<noteCount;i++) {
            cout << i+1 << ". " << notes[i] << endl;
        }
    }

    void showClock() {
        time_t currentTime = time(0);

        cout << "\nCurrent Time\n";
        cout << ctime(&currentTime);
    }

    void aboutSystem() {
        cout << "\nMiniOS Version 1.0\n";
        cout << "Developer : C++ Student\n";
        cout << "RAM : Infinite (Imaginary 😄)\n";
        cout << "Kernel : Console Edition\n";
    }

};

int main() {
    system("chcp 65001");
    MiniOS os;

    int choice;

    do {
        os.showDesktop();

        cout << "\nSelect Application : ";
        cin >> choice;

        switch(choice) {
            case 1:
                os.calculator();
                break;
            case 2:
                os.notesApp();
                break;
            case 3:
                os.showClock();
                break;
            case 4:
                os.aboutSystem();
                break;
            case 5:
                cout << "\nShutting Down...\n";
                break;
            default:
                cout << "\nInvalid Option!\n";
        }

    } while(choice != 5);

    return 0;
}
