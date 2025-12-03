# Program: Highest Marks

print("===== HIGHEST MARKS FINDER =====")

students = []  # empty list

count = int(input("How many students? "))

# Taking student name & marks
for i in range(count):
    name = input(f"Enter name of student {i+1}: ").title()
    marks = float(input(f"Enter marks of {name}: "))
    students.append((name, marks))

# Finding topper
top = max(students, key=lambda x: x[1])

print("\nTopper:", top[0], "-", top[1])
