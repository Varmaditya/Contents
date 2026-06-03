#include <iostream>
using namespace std;

int main() {

    // Initializing array
    int marks[3][3] = {
        {90, 85, 88},
        {78, 92, 80},
        {95, 89, 91}
    };

    // Accessing individual elements
    cout << "Accessing Individual Elements:\n";

    cout << "marks[0][0] = " << marks[0][0] << endl;
    cout << "marks[1][2] = " << marks[1][2] << endl;
    cout << "marks[2][1] = " << marks[2][1] << endl;

    return 0;
}
