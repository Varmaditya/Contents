#include <iostream>
using namespace std;

int main() {
    float distanceInKilometers;
    float mileage;
    float petrolPricePerLiter;

    float fuelRequired;
    float totalCost;

    cout << "Enter total distance (km): ";
    cin >> distanceInKilometers;

    cout << "Enter vehicle mileage (km/l): ";
    cin >> mileage;

    cout << "Enter petrol price per liter: ";
    cin >> petrolPricePerLiter;

    fuelRequired = distanceInKilometers / mileage;
    totalCost = fuelRequired * petrolPricePerLiter;

    cout << "\nFuel Required = " << fuelRequired << " liters" << endl;
    cout << "Total Petrol Cost = " << totalCost << endl;

    return 0;
}
