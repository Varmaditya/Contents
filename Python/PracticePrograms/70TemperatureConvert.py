# Program: Temperature Converter

print("===== TEMPERATURE CONVERTER =====")

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

choice = input("Convert (C/F): ").upper()

if choice == "C":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", c_to_f(c))

elif choice == "F":
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", f_to_c(f))

else:
    print("Invalid option.")
