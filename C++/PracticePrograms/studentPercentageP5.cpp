#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, e;
    float total, average, percentage;

    cout << "Enter marks of 5 subjects: ";
    cin >> a >> b >> c >> d >> e;

    total = a + b + c + d + e;
    average = total / 5;
    percentage = (total / 500) * 100;

    cout << "Total = " << total << endl;
    cout << "Average = " << average << endl;
    cout << "Percentage = " << percentage << "%" << endl;

    return 0;
}
