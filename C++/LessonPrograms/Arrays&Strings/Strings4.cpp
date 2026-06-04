#include <iostream>
#include <string>
using namespace std;

int main() {

    // Creating strings using string class
    string firstName = "Aditya";
    string lastName = "Varma";

    // Concatenation
    string fullName = firstName + " " + lastName;

    // Displaying strings
    cout << "First Name: " << firstName << endl;
    cout << "Last Name: " << lastName << endl;
    cout << "Full Name: " << fullName << endl;

    // Length / Size
    cout << "\nLength: " << fullName.length() << endl;

    cout << "Size: " << fullName.size() << endl;

    // Accessing characters
    cout << "\nFirst Character: " << fullName.front() << endl;

    cout << "Last Character: " << fullName.back() << endl;

    // Substring
    cout << "\nSubstring (first 6 characters): " << fullName.substr(0, 6) << endl;

    // Finding text
    cout << "\nPosition of 'Varma': " << fullName.find("Varma") << endl;

    // Appending text
    fullName.append(" Kumar");

    cout << "\nAfter append(): " << fullName << endl;

    // Inserting text
    fullName.insert(7, "Mr. ");

    cout << "After insert(): " << fullName << endl;

    // Erasing text
    fullName.erase(7, 4);

    cout << "After erase(): " << fullName << endl;

    // Replacing text
    fullName.replace(0, 6, "Aman");

    cout << "After replace(): " << fullName << endl;

    // Empty check
    cout << "\nIs string empty? " << fullName.empty() << endl;

    // Clearing string
    string temp = "Hello";

    cout << "\nBefore clear(): " << temp << endl;

    temp.clear();

    cout << "After clear(): " << temp << endl;

    cout << "Is temp empty? " << temp.empty() << endl;

    return 0;
}