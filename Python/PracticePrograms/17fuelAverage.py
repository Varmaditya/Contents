# Program: Calculate Car Fuel Efficiency (Mileage)

print("===== CAR MILEAGE CALCULATOR =====")

# Inputs from user
distance = float(input("Enter total distance traveled (in km): "))
fuelUsed = float(input("Enter fuel used (in liters): "))

# Mileage calculation
mileage = distance / fuelUsed

print(f"\nYour car's mileage is {mileage} km/litre.")
