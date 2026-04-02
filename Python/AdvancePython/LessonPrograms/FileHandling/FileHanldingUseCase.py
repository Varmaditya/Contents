# FILE HANDLING USE CASES
# ---------------------------------------------

print("\n===== USE CASE 1: USER DATA =====")

name = "Aditya"
age = "21"

with open("user.txt", "w") as file:
    file.write(name + "\n")
    file.write(age + "\n")

with open("user.txt", "r") as file:
    print("User Data:", file.read())


print("\n===== USE CASE 2: MARKS STORAGE =====")

marks = [80, 90, 85]

with open("marks.txt", "w") as file:
    for m in marks:
        file.write(str(m) + "\n")

with open("marks.txt", "r") as file:
    stored = [int(line.strip()) for line in file]

print("Stored Marks:", stored)


print("\n===== USE CASE 3: NOTES SYSTEM =====")

note = "Learn Python File Handling"

with open("notes.txt", "a") as file:
    file.write(note + "\n")

with open("notes.txt", "r") as file:
    print("All Notes:")
    for line in file:
        print("-", line.strip())


print("\n===== USE CASE 4: CSV FORMAT =====")

with open("students.csv", "a") as file:
    file.write("Rahul,85\n")

with open("students.csv", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        print("Name:", name, "| Marks:", marks)


print("\n===== USE CASE 5: LARGE FILE =====")

with open("big_data.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"Record {i}\n")

count = 0
with open("big_data.txt", "r") as file:
    for line in file:
        count += 1

print("Total Records:", count)


print("\n===== USE CASE 6: SIMPLE LOG SYSTEM =====")

action = "login"

with open("logs.txt", "a") as file:
    file.write(f"User action: {action}\n")

with open("logs.txt", "r") as file:
    print("Logs:")
    for line in file:
        print(line.strip())