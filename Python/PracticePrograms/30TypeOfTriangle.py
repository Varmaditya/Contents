# Program: Triangle Type Checker

print("===== TRIANGLE TYPE CHECKER =====")

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle.")
