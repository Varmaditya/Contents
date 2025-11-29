# Program to calculate the perimeter of a rectangle

rect_length = float(input("Enter the length of the rectangle (in units): "))
rect_width = float(input("Enter the width of the rectangle (in units): "))

# Perimeter formula: 2 * (length + width)
perimeter = 2 * (rect_length + rect_width)

print("The perimeter of the rectangle is:", perimeter, "units")
