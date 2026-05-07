#include <iostream>
using namespace std;

int main() {

    // do-while loop example 1:
    // Printing numbers from 1 to 5
    int i = 1;

    cout << "Numbers from 1 to 5:\n";

    do {
        cout << i << endl;
        i++;
    } while (i <= 5);

    // do-while loop example 2:
    // Printing multiplication table of 2
    int num = 1;

    cout << "\nTable of 2:\n";

    do {
        cout << "2 x " << num << " = " << 2 * num << endl;
        num++;
    } while (num <= 10);

    return 0;
}

