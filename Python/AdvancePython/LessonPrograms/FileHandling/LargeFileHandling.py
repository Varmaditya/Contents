# LARGE FILE HANDLING
# ---------------------------------------------

print("\n===== WRITING LARGE FILE =====")

with open("large_file.txt", "w") as file:
    for i in range(1, 101):
        file.write(f"Line {i}\n")

print("Large file created")


print("\n===== EFFICIENT READING (LINE BY LINE) =====")

with open("large_file.txt", "r") as file:
    for line in file:
        print("Processing:", line.strip())


print("\n===== USING readline() =====")

with open("large_file.txt", "r") as file:
    line = file.readline()
    while line:
        print("Line:", line.strip())
        line = file.readline()


print("\n===== WRITING IN CHUNKS =====")

with open("chunk_file.txt", "w") as file:
    for i in range(1, 4):
        data = f"Chunk {i}\n"
        file.write(data)
        print("Writing:", data.strip())


print("\n===== PRACTICAL EXAMPLE =====")

count = 0

with open("large_file.txt", "r") as file:
    for line in file:
        count += 1

print("Total Lines:", count)