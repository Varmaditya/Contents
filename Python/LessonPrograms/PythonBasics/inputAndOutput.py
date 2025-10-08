# Python Program: Input and Output
# ---------- 1. Basic print() ----------
print("1) Basic print examples")
print("Hello, world!")                       # simple string
print("Numbers print directly:", 10, 20, 30) # print can take multiple values
print()  # blank line for readability

# Example output:
# 1) Basic print examples
# Hello, world!
# Numbers print directly: 10 20 30


# ---------- 2. print() parameters: sep and end ----------
print("2) print() with sep and end")
print("A", "B", "C", sep="-")                # sep changes how items are separated
print("No newline at end ->", end="")        # end changes what is printed after the items
print(" this continues same line")
print()  # newline for spacing

# Example output:
# 2) print() with sep and end
# A-B-C
# No newline at end -> this continues same line


# ---------- 3. Basic input() ----------
print("\n3) Basic input() usage")
# input(prompt) shows prompt and returns a string entered by the user
name = input("Enter your name: ")           # user types: Aditya
print("You entered name:", name)

# Example interaction:
# Enter your name: Aditya
# You entered name: Aditya


# ---------- 4. Converting input (explicit casting) ----------
print("\n4) Converting input to other types")
age_str = input("Enter your age (as whole number): ")  # e.g., "21"
# Convert string to int using int()
try:
    age = int(age_str)
    print("Your age (int):", age)
except ValueError:
    print("That was not a valid integer for age.")

# Convert to float
height_str = input("Enter your height in meters (example 1.75): ")  # e.g., "1.75"
try:
    height = float(height_str)
    print("Your height (float):", height)
except ValueError:
    print("That was not a valid decimal number for height.")

# Example:
# Enter your age (as whole number): 21
# Your age (int): 21
# Enter your height in meters (example 1.75): 1.75
# Your height (float): 1.75


# ---------- 5. Handling empty input / default values ----------
print("\n5) Handling empty input (press Enter to skip)")
fav_color = input("Enter your favorite color (or press Enter to skip): ").strip()
if fav_color == "":
    fav_color = "Not provided"   # default value if user pressed Enter without typing
print("Favorite color:", fav_color)

# Example:
# Enter your favorite color (or press Enter to skip):
# Favorite color: Not provided


# ---------- 6. Reading multiple values from one line ----------
print("\n6) Reading multiple values (single-line input)")
# Common pattern for simple inputs: split() then convert
# User types values separated by space, e.g., "10 20"
nums_line = input("Enter two integers separated by space (e.g., '10 20'): ").strip()
parts = nums_line.split()   # split on whitespace
if len(parts) >= 2:
    try:
        a = int(parts[0])
        b = int(parts[1])
        print("You entered a =", a, "and b =", b)
    except ValueError:
        print("Please enter valid integers.")
else:
    print("Not enough values entered.")

# Example:
# Enter two integers separated by space (e.g., '10 20'): 10 20
# You entered a = 10 and b = 20


# ---------- 7. Printing formatted output ----------
print("\n7) Printing: concatenation, comma vs f-strings vs format()")
item = "Notebook"
price = 45.5
quantity = 3

# Using commas in print (automatic spaces)
print("Item:", item, "Price:", price, "Qty:", quantity)

# Using string concatenation (convert non-strings)
print("Total (concat): " + str(price * quantity))

# Using f-strings (recommended in modern Python)
total = price * quantity
print(f"Using f-string -> Item: {item}, Price: {price}, Qty: {quantity}, Total: {total:.2f}")

# Using str.format()
print("Using format(): Item: {}, Price: {}, Qty: {}, Total: {:.2f}".format(item, price, quantity, total))

# Example:
# Item: Notebook Price: 45.5 Qty: 3
# Total (concat): 136.5
# Using f-string -> Item: Notebook, Price: 45.5, Qty: 3, Total: 136.50


# ---------- 8. print() and escape sequences ----------
print("\n8) Escape sequences in strings")
print("Newline ->\\n: Line1\nLine2")   # newline
print("Tab ->\\t: Column1\tColumn2")  # tab
print("Backslash -> \\\\")            # single backslash shown

# Example:
# Newline ->\n: Line1
# Line2
# Tab ->\t: Column1	Column2
# Backslash -> \


# ---------- 9. Prompt clarity and friendly UX ----------
print("\n9) Prompt best-practices (make prompts clear)")
# Good prompts say what format is expected and give examples
date_input = input("Enter date in YYYY-MM-DD (example: 2025-11-23): ")
print("You entered date string:", date_input)

# ---------- 10. Summary of common pitfalls ----------
print("\n10) Common pitfalls and tips (short)")
print("- input() always returns a string. Cast explicitly when you need numbers.")
print("- Use strip() to remove accidental leading/trailing spaces from input.")
print("- Use try/except when casting to handle invalid input gracefully.")
print("- Use clear prompts so users know what format to enter.")

# End of demo
print("\nDemo finished. Practice by running the script and trying different inputs.")
