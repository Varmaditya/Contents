#include <iostream>
using namespace std;

int main() {
    int number;

    cout << "Enter a number: ";
    cin >> number;

    string result;

    result = (number % 2 == 0) ? "Even" : "Odd";

    cout << "The number is " << result << endl;

    return 0;
}
