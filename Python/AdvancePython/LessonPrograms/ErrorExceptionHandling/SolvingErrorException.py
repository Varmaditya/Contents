# TRY, EXCEPT, ELSE, FINALLY
# ---------------------------------------------

print("\n===== BASIC EXCEPTION HANDLING =====")

try:
    num = int("10")
    result = 10 / num
    print("Result:", result)
except:
    print("Error occurred!")


print("\n===== SPECIFIC EXCEPTIONS =====")

try:
    value = int("abc")
    print(10 / value)
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


print("\n===== ELSE BLOCK =====")

try:
    x = 5
    y = 2
    result = x / y
except Exception as e:
    print("Error:", e)
else:
    print("Success! Result:", result)


print("\n===== FINALLY BLOCK =====")

try:
    print("Opening file...")
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing operation.")


print("\n===== MULTIPLE EXCEPTION CASE =====")

try:
    data = [10, 20, 30]
    print(data[5])
except IndexError:
    print("Index out of range!")
