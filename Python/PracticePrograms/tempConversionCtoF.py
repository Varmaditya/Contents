# Program: Convert Celsius to Fahrenheit

print("===== TEMPERATURE CONVERTER =====")

# Constant formula: F = (C × 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
