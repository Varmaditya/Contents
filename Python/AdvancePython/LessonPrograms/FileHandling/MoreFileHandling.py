# CSV, JSON & PATH HANDLING IN PYTHON (DETAILED)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== CSV, JSON & PATH HANDLING =====")
print("""
In real-world applications, we use structured files:

✔ CSV → for table-like data
✔ JSON → for structured key-value data
✔ pathlib → for handling file paths

To use these features, we use IMPORTS.

Import means:
✔ Bringing external functionality into our program
""")

# ---------------- Understanding import ----------------
print("\n===== WHAT IS IMPORT? =====")
print("""
Python has built-in modules (libraries).

We use 'import' to use them.

Example:
import csv

This allows us to use CSV-related functions.
""")

# ======================================================
# CSV FILE HANDLING
# ======================================================

print("\n===== CSV FILE HANDLING =====")

# Importing csv module
import csv

print("""
csv module is used to:
✔ Read CSV files
✔ Write CSV files
✔ Handle tabular data
""")

# ---------------- Writing CSV ----------------
print("\n===== WRITING CSV FILE =====")

data = [
    ["Name", "Marks"],
    ["Aditya", 88],
    ["Sneha", 92],
    ["Ravi", 75]
]

print("""
csv.writer(file):
✔ Creates a writer object
✔ Used to write rows into CSV file
""")

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)     # create writer
    writer.writerows(data)        # write multiple rows

print("CSV file created.")

# ---------------- Reading CSV ----------------
print("\n===== READING CSV FILE =====")

print("""
csv.reader(file):
✔ Reads CSV file line by line
✔ Each row is returned as a list
""")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print("Row:", row)

# ---------------- CSV Dictionary Reader ----------------
print("\n===== CSV DICTIONARY READER =====")

print("""
csv.DictReader(file):
✔ Reads CSV as dictionary
✔ Uses first row as keys
""")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Name:", row["Name"], "| Marks:", row["Marks"])

# ======================================================
# JSON FILE HANDLING
# ======================================================

print("\n===== JSON FILE HANDLING =====")

# Importing json module
import json

print("""
json module is used for:
✔ Storing structured data
✔ Working with APIs
✔ Configuration files

JSON stores data as:
Key → Value pairs
""")

# ---------------- Writing JSON ----------------
print("\n===== WRITING JSON FILE =====")

student = {
    "name": "Aditya",
    "age": 21,
    "marks": [85, 90, 88]
}

print("""
json.dump(data, file):
✔ Converts Python object → JSON format
✔ Writes into file
""")

with open("student.json", "w") as file:
    json.dump(student, file)

print("JSON file created.")

# ---------------- Reading JSON ----------------
print("\n===== READING JSON FILE =====")

print("""
json.load(file):
✔ Reads JSON file
✔ Converts into Python dictionary
""")

with open("student.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Marks:", data["marks"])

# ---------------- JSON Pretty Print ----------------
print("\n===== JSON PRETTY PRINT =====")

print("""
json.dumps(data, indent=4):
✔ Converts Python object to formatted JSON string
✔ Useful for display/debugging
""")

print(json.dumps(student, indent=4))

# ======================================================
# PATH HANDLING (pathlib)
# ======================================================

print("\n===== PATH HANDLING (pathlib) =====")

# Importing Path class
from pathlib import Path

print("""
pathlib is used to:
✔ Work with file paths
✔ Avoid complex string paths
✔ Write cleaner code

Path is a class used to create path objects.
""")

# ---------------- Creating Path ----------------
print("\n===== CREATING PATH OBJECT =====")

path = Path("sample.txt")

print("Path object:", path)

print("""
path.exists():
✔ Checks if file exists
""")

print("Exists:", path.exists())

# ---------------- Writing using Path ----------------
print("\n===== WRITING USING PATH =====")

print("""
path.write_text(data):
✔ Writes text directly into file
✔ No need for open()
""")

path.write_text("Hello from pathlib!")

# ---------------- Reading using Path ----------------
print("\n===== READING USING PATH =====")

print("""
path.read_text():
✔ Reads entire file content
""")

content = path.read_text()
print("Content:", content)

# ---------------- Path Information ----------------
print("\n===== PATH INFORMATION =====")

print("""
path.name → file name
path.suffix → file extension
path.resolve() → full path
""")

print("File Name:", path.name)
print("File Extension:", path.suffix)
print("Absolute Path:", path.resolve())

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

print("""
Save user settings in JSON file using Path
""")

config_path = Path("config.json")

config_data = {
    "theme": "dark",
    "volume": 70
}

# Write config
with open(config_path, "w") as file:
    json.dump(config_data, file)

# Read config
with open(config_path, "r") as file:
    config = json.load(file)

print("Theme:", config["theme"])
print("Volume:", config["volume"])

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ import allows using built-in modules
✔ csv → tabular data
✔ json → structured data
✔ pathlib → modern file handling

These modules are widely used in real-world applications.
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Learned how import works
✔ CSV for tables
✔ JSON for structured data
✔ Pathlib for file paths
✔ These are essential for real-world Python

Next step:
Working with modules in detail
""")
