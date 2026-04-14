# FILE HANDLING USE CASES (REAL-WORLD FLOW)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== FILE HANDLING USE CASES =====")
print("""
This program shows how file handling is used in real scenarios:

✔ Take input
✔ Process data
✔ Save it in file
✔ Retrieve and reuse later

This is how real applications work.
""")

# ---------------- Use Case 1: Save & Reuse User Data ----------------
print("\n===== USE CASE 1: USER DATA STORAGE =====")

name = input("Enter your name: ")
age = input("Enter your age: ")

# Save data
with open("user.txt", "w") as file:
    file.write(name + "\n")
    file.write(age + "\n")

print("User data saved.")

# Retrieve data later
with open("user.txt", "r") as file:
    stored_name = file.readline().strip()
    stored_age = file.readline().strip()

print("Retrieved Data → Name:", stored_name, "| Age:", stored_age)

# ---------------- Use Case 2: Marks Calculation + File ----------------
print("\n===== USE CASE 2: MARKS STORAGE =====")

marks = []

for i in range(3):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

average = sum(marks) / len(marks)
print("Average:", average)

# Save marks
with open("marks.txt", "w") as file:
    for m in marks:
        file.write(str(m) + "\n")

# Reuse marks later
with open("marks.txt", "r") as file:
    stored_marks = [int(line.strip()) for line in file]

print("Stored Marks:", stored_marks)

# ---------------- Use Case 3: Notes System (Append Mode) ----------------
print("\n===== USE CASE 3: NOTES SYSTEM =====")

note = input("Write a note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved.")

print("\nAll Notes:")
with open("notes.txt", "r") as file:
    for line in file:
        print("-", line.strip())

# ---------------- Use Case 4: Working with CSV-like Data ----------------
print("\n===== USE CASE 4: CSV DATA =====")

name = input("Enter student name: ")
marks = input("Enter marks: ")

# Save as CSV format
with open("students.csv", "a") as file:
    file.write(f"{name},{marks}\n")

print("Data saved in CSV format.")

# Read CSV data
print("\nStudent Records:")
with open("students.csv", "r") as file:
    for line in file:
        n, m = line.strip().split(",")
        print("Name:", n, "| Marks:", m)

# ---------------- Use Case 5: Large File Writing ----------------
print("\n===== USE CASE 5: LARGE FILE WRITING =====")

with open("big_data.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"Record {i}\n")

print("Large file created.")

# ---------------- Use Case 6: Large File Processing ----------------
print("\n===== USE CASE 6: LARGE FILE READING =====")

count = 0

with open("big_data.txt", "r") as file:
    for line in file:
        count += 1

print("Total Records:", count)

# ---------------- Use Case 7: Searching in File ----------------
print("\n===== USE CASE 7: SEARCH IN FILE =====")

keyword = input("Enter keyword to search: ")

with open("big_data.txt", "r") as file:
    for line in file:
        if keyword.lower() in line.lower():
            print("Found:", line.strip())

# ---------------- Use Case 8: Simple Log System ----------------
print("\n===== USE CASE 8: LOG SYSTEM =====")

action = input("Enter action (login/logout): ")

with open("logs.txt", "a") as file:
    file.write(f"User performed: {action}\n")

print("Log saved.")

print("\nSystem Logs:")
with open("logs.txt", "r") as file:
    for line in file:
        print(line.strip())

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Programs take input and process data
✔ Files store that data permanently
✔ Data can be reused later
✔ Small files → user data, notes
✔ Large files → logs, datasets
✔ CSV → structured data storage

This is how real applications use file handling.
""")
