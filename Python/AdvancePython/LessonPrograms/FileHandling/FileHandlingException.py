# FILE HANDLING WITH EXCEPTIONS IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== FILE HANDLING WITH EXCEPTIONS =====")
print("""
When working with files, many errors can occur:

✔ File may not exist
✔ File may not open
✔ Permission issues
✔ Invalid data inside file

To prevent crashes, we use:
✔ try-except with file handling

This makes programs:
✔ Safe
✔ Robust
✔ User-friendly
""")

# ---------------- Problem Without Exception Handling ----------------
print("\n===== WITHOUT EXCEPTION HANDLING =====")
print("""
If file does not exist:

open("data.txt", "r")

This causes:
FileNotFoundError
Program crashes.
""")

# ---------------- Basic File Handling with try-except ----------------
print("\n===== BASIC try-except WITH FILE =====")

try:
    file = open("data.txt", "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()
except FileNotFoundError:
    print("Error: File not found!")

# ---------------- Using with + try-except ----------------
print("\n===== USING with + try-except =====")

try:
    with open("data.txt", "r") as file:
        data = file.read()
        print("Content:", data)
except FileNotFoundError:
    print("File does not exist!")

print("""
with ensures file closes automatically.
""")

# ---------------- Handling Multiple Exceptions ----------------
print("\n===== HANDLING MULTIPLE FILE ERRORS =====")

try:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print("Other error:", e)

# ---------------- Writing File Safely ----------------
print("\n===== SAFE FILE WRITING =====")

try:
    with open("output.txt", "w") as file:
        data = input("Enter data to write: ")
        file.write(data)
    print("Data written successfully.")
except Exception as e:
    print("Error while writing:", e)

# ---------------- Reading Structured Data Safely ----------------
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

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

print("""
Problem:
Read user data safely and display it
""")

try:
    with open("user.txt", "r") as file:
        name = file.readline().strip()
        age = int(file.readline().strip())

        print("Name:", name)
        print("Age:", age)

except FileNotFoundError:
    print("User file missing!")
except ValueError:
    print("Invalid data format in file!")

# ---------------- Real-World Use Cases ----------------
print("\n===== REAL-WORLD USE CASES =====")
print("""
✔ Opening config files safely
✔ Reading logs without crashing
✔ Handling missing data files
✔ Processing user-uploaded files
✔ Preventing system crashes
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Always use try-except with files
✔ Handle specific exceptions
✔ Use 'with' for safe file handling
✔ Prevent program crashes
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ File operations can fail
✔ try-except handles errors safely
✔ with ensures proper file closing
✔ Multiple exceptions improve robustness

File handling + exceptions is essential
for real-world applications.
""")
