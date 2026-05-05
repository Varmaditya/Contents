#include <iostream>
using namespace std;

int main() {
    int number;

    cout << "Enter a number: ";
    cin >> number;

    string result;

    result = (number % 3 == 0 && number % 5 == 0)
             ? "Divisible by both 3 and 5"
             : "Not divisible by both";

    cout << result << endl;

    return 0;
}
