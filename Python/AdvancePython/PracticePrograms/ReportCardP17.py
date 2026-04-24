# Program: Student Report Card

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def report(self):
        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))


name = input("Enter student name: ")
student = Student(name)

for i in range(3):
    mark = int(input(f"Enter mark {i+1}: "))
    student.add_mark(mark)

student.report()