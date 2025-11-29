# Program to calculate the volume of a cylinder
import math

cylinder_radius = float(input("Enter the radius of the cylinder (in units): "))
cylinder_height = float(input("Enter the height of the cylinder (in units): "))

# Volume formula: π * r^2 * h
volume = math.pi * cylinder_radius ** 2 * cylinder_height

print("The volume of the cylinder is:", round(volume, 2), "cubic units")
