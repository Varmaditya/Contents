# READING & WRITING FILES IN PYTHON (DETAILED)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== READING & WRITING FILES =====")
print("""
In this chapter we learn how to:

✔ Open a file
✔ Read data from a file
✔ Write data into a file
✔ Append data to a file
✔ Use 'with' for safe handling

We will understand each keyword in detail.
""")

# ---------------- open() Function ----------------
print("\n===== open() FUNCTION =====")
print("""
Syntax:
open(filename, mode)

open() is used to:
✔ Open an existing file
✔ OR create a new file

Parameters:
1️⃣ filename → Name of the file
2️⃣ mode → What operation we want to perform

Returns:
✔ A file object (used to perform operations)
""")

# ---------------- Writing to a File ----------------
print("\n===== WRITE MODE ('w') =====")
print("""
Mode: 'w' → write

✔ Creates file if not exists
✔ Deletes old content if file exists
✔ Writes new content
""")

file = open("sample.txt", "w")   # open file in write mode

print("File object:", file)

print("""
file.write() → writes text into file
""")

file.write("Hello World\n")
file.write("Learning File Handling\n")

print("""
file.close() → closes the file
✔ Saves data
✔ Releases memory
""")

file.close()

# ---------------- Append Mode ----------------
print("\n===== APPEND MODE ('a') =====")
print("""
Mode: 'a' → append

✔ Adds data at the end
✔ Does NOT remove existing content
""")

file = open("sample.txt", "a")

file.write("This line is appended\n")

file.close()

# ---------------- Read Mode ----------------
print("\n===== READ MODE ('r') =====")
print("""
Mode: 'r' → read

✔ Reads file content
✔ File must exist
""")

file = open("sample.txt", "r")

print("""
file.read() → reads entire file as string
""")

content = file.read()
print("File Content:\n", content)

file.close()

# ---------------- Reading Line by Line ----------------
print("\n===== READING LINE BY LINE =====")
print("""
Instead of reading full file,
we can read line by line.
""")

file = open("sample.txt", "r")

for line in file:
    print("Line:", line.strip())

file.close()

print("""
line.strip() removes newline characters.
""")

# ---------------- Context Manager (with) ----------------
print("\n===== CONTEXT MANAGER (with) =====")
print("""
Syntax:
with open(filename, mode) as variable:

Advantages:
✔ Automatically closes file
✔ Cleaner code
✔ Prevents errors
""")

with open("sample.txt", "r") as file:
    data = file.read()
    print("Using with:\n", data)

print("""
File is automatically closed after block.
""")

# ---------------- Writing using with ----------------
print("\n===== WRITING USING with =====")

with open("example.txt", "w") as file:
    file.write("This file is created using with\n")

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

print("""
Problem:
Store and read student marks
""")

with open("marks.txt", "w") as file:
    file.write("85\n90\n78\n")

with open("marks.txt", "r") as file:
    for line in file:
        print("Mark:", line.strip())

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ open() returns file object
✔ write() writes data
✔ read() reads data
✔ close() is important
✔ with is best practice
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ open(filename, mode) opens file
✔ 'w' → write, 'a' → append, 'r' → read
✔ read(), write() perform operations
✔ with automatically manages file

Now you can perform basic file operations.
""")
