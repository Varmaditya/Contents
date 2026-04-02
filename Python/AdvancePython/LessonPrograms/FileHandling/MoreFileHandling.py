# CSV, JSON & PATH HANDLING
# ---------------------------------------------

print("\n===== CSV HANDLING =====")

import csv

data = [
    ["Name", "Marks"],
    ["Aditya", 88],
    ["Sneha", 92]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("Row:", row)


print("\n===== JSON HANDLING =====")

import json

student = {
    "name": "Aditya",
    "marks": [85, 90]
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Marks:", data["marks"])


print("\n===== PATH HANDLING =====")

from pathlib import Path

path = Path("sample.txt")

path.write_text("Hello from pathlib")

print("Content:", path.read_text())
print("Exists:", path.exists())
print("File Name:", path.name)