#include <iostream>
#include <string>
using namespace std;

int main() {

    // Initializing string
    string word = "PROGRAMMING";

    // Accessing individual characters
    cout << "First Character: "
         << word[0] << endl;

    cout << "Third Character: "
         << word[2] << endl;

    cout << "Last Character: "
         << word[word.length() - 1] << endl;

    // Accessing all characters using loop
    cout << "\nAll Characters:\n";

    for (int i = 0; i < word.length(); i++) {

        cout << word[i] << " ";

    }

    return 0;
}