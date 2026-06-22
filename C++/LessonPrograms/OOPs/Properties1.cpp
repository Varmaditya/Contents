#include <iostream>
using namespace std;

class Car {

public:

    // Public function available to user
    void startCar() {
        cout << "Starting Car...\n";

        // Internal details hidden from user
        startEngine();
    }

private:

    // Hidden implementation
    void startEngine() {
        cout << "Engine Started Successfully!\n";
    }

};

int main() {
    Car myCar;

    // User only calls startCar()
    myCar.startCar();

    return 0;
}