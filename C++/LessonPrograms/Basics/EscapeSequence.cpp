#include <iostream>
using namespace std;

int main() {

    // Demonstrating Escape Sequences in C++

    cout << "Demonstrating Escape Sequences in C++\n\n";

    // 1. New Line
    cout << "1. New Line (\\n):\n";
    cout << "Hello\nWorld\n\n";

    // 2. Tab Space
    cout << "2. Tab Space (\\t):\n";
    cout << "Hello\tWorld\n\n";

    // 3. Backspace
    cout << "3. Backspace (\\b):\n";
    cout << "Helloo\b World\n\n";

    // 4. Carriage Return
    cout << "4. Carriage Return (\\r):\n";
    cout << "Hello World\rHi\n\n";

    // 5. Backslash
    cout << "5. Backslash (\\\\):\n";
    cout << "\\\n\n";

    // 6. Single Quote
    cout << "6. Single Quote (\\'):\n";
    cout << "\'\n\n";

    // 7. Double Quote
    cout << "7. Double Quote (\\\"):\n";
    cout << "\"C++\"\n\n";

    // 8. Alert (may produce sound)
    cout << "8. Alert (\\a):\n";
    cout << "\a\n";

    return 0;   // Program ends
}
