# Program: File Writer & Reader
# File handling allows saving and reading data from files on your computer.

print("===== FILE HANDLING DEMO =====")

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("This is a sample note.\nLearning Python is fun.")

# Reading the file
with open("notes.txt", "r") as file:
    content = file.read()

print("File Content:\n", content)
