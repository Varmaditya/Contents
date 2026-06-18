#include <iostream>
using namespace std;

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    cout << "Address of first element: " << numbers << endl;
    cout << "First element using array: " << numbers[0] << endl;
    cout << "First element using pointer: " << *numbers << endl;

   int *ptr = numbers;
   cout << "Array Elements:\n";

   for (int i = 0; i < 5; i++) {
       cout << *(ptr + i) << " ";
    }
  
    return 0;
}
