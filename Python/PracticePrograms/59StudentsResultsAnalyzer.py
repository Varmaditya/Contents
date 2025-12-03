# Program: Student Result Analyzer with Grades

print("===== STUDENT RESULT ANALYZER =====")

students = {
    "Asha": [78, 82, 91],
    "Rohit": [65, 70, 58],
    "Neha": [92, 88, 94]
}

for name, marks in students.items():
    print("\nStudent:", name)

    total = sum(marks)
    avg = total / len(marks)

    print("Marks:", marks)
    print("Average:", avg)

    # grading using conditions
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    else:
        grade = "C"

    print("Grade:", grade)
