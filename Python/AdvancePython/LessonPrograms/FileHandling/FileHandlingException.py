# FILE HANDLING WITH EXCEPTIONS
# ---------------------------------------------

print("\n===== BASIC FILE READING =====")

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")


print("\n===== MULTIPLE EXCEPTIONS =====")

try:
    filename = "data.txt"
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print("Other error:", e)


print("\n===== SAFE FILE WRITING =====")

try:
    with open("output.txt", "w") as file:
        file.write("Hello File")
    print("Data written successfully")
except Exception as e:
    print("Error while writing:", e)


print("\n===== SAFE DATA READING =====")

try:
    with open("marks.txt", "r") as file:
        for line in file:
            mark = int(line.strip())
            print("Mark:", mark)
except ValueError:
    print("Invalid data in file!")
except FileNotFoundError:
    print("marks.txt not found!")


print("\n===== PRACTICAL EXAMPLE =====")

try:
    with open("user.txt", "r") as file:
        name = file.readline().strip()
        age = int(file.readline().strip())

        print("Name:", name)
        print("Age:", age)

except FileNotFoundError:
    print("User file missing!")
except ValueError:
    print("Invalid data format!")