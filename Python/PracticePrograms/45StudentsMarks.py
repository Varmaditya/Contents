# Program: Student Marks Table

print("===== STUDENT MARKS TABLE =====")

students = ["Asha", "Rohit"]
subjects = ["Math", "Science"]

for name in students:
    print("\nMarks for:", name)
    for sub in subjects:
        marks = int(input(f"Enter marks in {sub}: "))
        print(sub, "=", marks)

