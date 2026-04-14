# LARGE FILE HANDLING (READING & WRITING EFFICIENTLY)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== LARGE FILE HANDLING =====")
print("""
When working with large files:

✔ We cannot load entire file into memory
✔ We must process data in parts

This is called:
Efficient File Handling
""")

# ---------------- Problem with read() ----------------
print("\n===== PROBLEM WITH read() =====")
print("""
read() loads entire file into memory.

For large files:
❌ High memory usage
❌ Slow performance
❌ Can crash program
""")

# ---------------- Writing Large File ----------------
print("\n===== WRITING LARGE FILE =====")
print("""
We simulate writing large data efficiently.
""")

with open("large_file.txt", "w") as file:
    for i in range(1, 1001):
        file.write(f"Line {i}\n")

print("Large file created.")

# ---------------- Efficient Reading (Line by Line) ----------------
print("\n===== EFFICIENT READING =====")
print("""
Best method:
Read one line at a time
""")

with open("large_file.txt", "r") as file:
    for line in file:
        print("Processing:", line.strip())

print("""
✔ Only one line in memory
✔ Very efficient
""")

# ---------------- Using readline() ----------------
print("\n===== USING readline() =====")

with open("large_file.txt", "r") as file:
    line = file.readline()
    while line:
        print("Line:", line.strip())
        line = file.readline()

# ---------------- Writing Large Data in Chunks ----------------
print("\n===== WRITING IN CHUNKS =====")
print("""
Instead of writing everything at once,
write in parts.
""")

with open("chunk_file.txt", "w") as file:
    for i in range(1, 6):
        data = f"Chunk {i}\n"
        file.write(data)
        print("Writing:", data.strip())

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

print("""
Problem:
Count number of lines in large file
""")

count = 0

with open("large_file.txt", "r") as file:
    for line in file:
        count += 1

print("Total Lines:", count)

# ---------------- Use Cases ----------------
print("\n===== REAL-WORLD USE CASES =====")
print("""
✔ Log file processing
✔ Reading large CSV files
✔ Data pipelines
✔ Streaming data systems
✔ Big data applications
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ Avoid read() for large files
✔ Use loops for reading
✔ Write data in chunks
✔ File object is iterator
✔ Memory efficiency is important
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Large files require efficient handling
✔ Read line-by-line instead of full read
✔ Write data in chunks
✔ Helps in real-world applications

Efficient file handling is critical
for scalable systems.
""")
