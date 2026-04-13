# FILE HANDLING IN PYTHON (INTRODUCTION)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== INTRODUCTION TO FILE HANDLING =====")
print("""
File Handling allows programs to:
✔ Store data permanently
✔ Read data from files
✔ Write data to files

Until now:
All data was temporary (stored in memory).

Once program stops → data is lost.

With files:
Data can be saved and reused later.

This is the first step towards building
real-world applications.
""")

# ---------------- What is a File ----------------
print("\n===== WHAT IS A FILE? =====")
print("""
A file is a collection of data stored on disk.

Files act as a bridge between:
✔ Program ↔ User
✔ Program ↔ Program
✔ Program ↔ System

Examples of files:
✔ Text files (.txt)
✔ CSV files (.csv)
✔ JSON files (.json)
✔ Images (.jpg, .png)
✔ Videos (.mp4)

Files help store large amounts of data
that cannot fit in memory permanently.
""")

# ---------------- Why File Handling is Needed ----------------
print("\n===== WHY FILE HANDLING IS NEEDED =====")
print("""
Without file handling:
✔ Data is lost after program ends
✔ No history of operations
✔ No data reuse

With file handling:
✔ Data is stored permanently
✔ Programs can reuse data
✔ Systems can maintain logs and reports

File handling is essential for:
✔ Databases
✔ Applications
✔ Data processing systems
""")

# ---------------- Example: Without File Handling ----------------
print("\n===== WITHOUT FILE HANDLING =====")
print("""
Example:
Marks stored in a list
""")

marks = [80, 90, 85]
print("Marks:", marks)

print("""
Once program ends → data is gone.

User must enter data again.
""")

# ---------------- Example: With File Handling ----------------
print("\n===== WITH FILE HANDLING =====")
print("""
Example:
Marks stored in a file

marks.txt:
80
90
85

Now data is:
✔ Persistent
✔ Reusable
✔ Shareable
""")

# ---------------- Text vs Binary Files ----------------
print("\n===== TEXT FILES vs BINARY FILES =====")
print("""
There are two main types of files:

1️⃣ Text Files
   ✔ Store data as readable text
   ✔ Human-readable
   ✔ Examples:
       .txt, .csv, .json

   Example content:
   Hello
   123
   Python

2️⃣ Binary Files
   ✔ Store data in binary format (0s and 1s)
   ✔ Not human-readable
   ✔ Examples:
       .jpg, .png, .mp3, .exe

   Used for:
   ✔ Images
   ✔ Videos
   ✔ Audio
   ✔ Compiled programs

Text files → Easy to read and edit
Binary files → Efficient for complex data
""")

# ---------------- Real-World Examples ----------------
print("\n===== REAL-WORLD EXAMPLES =====")
print("""
1️⃣ Banking System
   - Stores account details

2️⃣ Login System
   - Stores usernames and passwords

3️⃣ E-commerce Website
   - Stores orders and transactions

4️⃣ Logging System
   - Stores error logs in files

5️⃣ Data Analysis
   - Reads data from CSV/Excel files
""")

# ---------------- File Modes ----------------
print("\n===== FILE MODES =====")
print("""
File mode defines:
✔ What operation we perform
✔ How file is opened

Basic Modes:

'r' → Read
   ✔ Opens file for reading
   ✔ Error if file does not exist

'w' → Write
   ✔ Creates new file OR overwrites existing file

'a' → Append
   ✔ Adds data at the end of file

'x' → Create
   ✔ Creates file
   ✔ Error if file already exists

Binary Modes:

'rb' → Read binary
'wb' → Write binary
'ab' → Append binary

Combined Modes:

'r+' → Read + Write
'w+' → Write + Read (overwrite)
'a+' → Append + Read
""")

# ---------------- File Operations Overview ----------------
print("\n===== FILE OPERATIONS OVERVIEW =====")
print("""
Three main operations:

1️⃣ Read
   - Get data from file

2️⃣ Write
   - Store new data

3️⃣ Append
   - Add data without removing old data
""")

# ---------------- First Interaction with File ----------------
print("\n===== FIRST INTERACTION WITH FILE =====")
print("""
Basic syntax:

file = open("file.txt", "r")
file.close()

open() → opens the file
close() → closes the file

File must be closed after use.
""")

# ---------------- Why Closing Files is Important ----------------
print("\n===== WHY CLOSE FILES =====")
print("""
If file is not closed:
✔ Data may not be saved properly
✔ Memory resources are wasted
✔ File may remain locked

Better approach:
Using 'with' statement (next chapter)
""")

# ---------------- Files as Real-World Interaction ----------------
print("\n===== FILES = REAL WORLD INTERACTION =====")
print("""
Files allow programs to:

✔ Store real-world data
✔ Share data between systems
✔ Maintain history and logs

This transforms programming from:
Simple scripts → Real applications
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Files store data permanently
✔ Text files are human-readable
✔ Binary files are machine-efficient
✔ File modes control operations
✔ Always close files after use
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ File handling allows persistent storage
✔ Files exist outside program memory
✔ Text vs Binary files differ in format
✔ File modes define operations
✔ open() and close() are basic functions

Next chapter:
✔ Reading files
✔ Writing files
✔ Append operations
✔ 'with' statement
✔ File handling with exceptions
""")