# Program: Calculate Car Fuel Efficiency (Mileage)

print("===== CAR MILEAGE CALCULATOR =====")

# Inputs from user
distance = float(input("Enter total distance traveled (in km): "))
fuel_used = float(input("Enter fuel used (in liters): "))

# Mileage calculation
mileage = distance / fuel_used

print(f"\nYour car's mileage is {mileage} km/litre.")
