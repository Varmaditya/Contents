# Program to calculate the area of a circle

radius = float(input("Enter the radius of the circle (in units): "))
pi = 3.14

# Area formula: π * r^2
area = pi * radius ** 2

print("The area of the circle is:", round(area, 2), "square units")
