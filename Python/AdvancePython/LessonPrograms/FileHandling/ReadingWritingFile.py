# READING & WRITING FILES
# ---------------------------------------------

print("\n===== WRITING TO FILE =====")

file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Learning Python\n")
file.close()


print("\n===== APPENDING TO FILE =====")

file = open("sample.txt", "a")
file.write("This is appended line\n")
file.close()


print("\n===== READING FILE =====")

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()


print("\n===== READING LINE BY LINE =====")

file = open("sample.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()


print("\n===== USING with (BEST PRACTICE) =====")

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)


print("\n===== PRACTICAL EXAMPLE =====")

with open("marks.txt", "w") as file:
    file.write("85\n90\n78\n")

with open("marks.txt", "r") as file:
    for mark in file:
        print("Mark:", mark.strip())