# Program to calculate the perimeter of a rectangle

rectLength = float(input("Enter the length of the rectangle (in units): "))
rectWidth = float(input("Enter the width of the rectangle (in units): "))

# Perimeter formula: 2 * (length + width)
perimeter = 2 * (rectLength + rectWidth)

print("The perimeter of the rectangle is:", perimeter, "units")
