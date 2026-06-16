/*
Program: AI Mood Detector
Description: Detects mood from message keywords.
*/

#include <iostream>
using namespace std;

int main() {

    string message;

    cout << "How are you feeling today?\n";
    getline(cin, message);

    if(message.find("happy") != string::npos) {
        cout << "\nYou seem Happy!";
    } else if(message.find("sad") != string::npos) {
        cout << "\nYou seem Sad!";
    } else if(message.find("angry") != string::npos) {
        cout << "\nYou seem Angry!";
    } else {
        cout << "\nMood Unknown";
    }

    return 0;
}
