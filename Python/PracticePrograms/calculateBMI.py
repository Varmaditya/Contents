# Program: Body Mass Index (BMI) Calculator

print("===== BODY MASS INDEX (BMI) CALCULATOR =====")

# Inputs
name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Formula: BMI = weight / (height * height)
bmi = weight / (height ** 2)

print(f"\n{name}, your BMI is: {bmi}")
