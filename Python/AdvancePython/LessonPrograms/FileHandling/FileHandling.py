# FILE HANDLING
# ---------------------------------------------

print("\n===== WITHOUT FILE HANDLING =====")

marks = [80, 90, 85]
print("Marks stored in program:", marks)

print("After program ends → data is lost")


print("\n===== WITH FILE HANDLING =====")

print("""
Marks stored in file (marks.txt):

80
90
85

Now data is:
✔ Permanent
✔ Reusable
✔ Shareable
""")


print("\n===== FILE MODES =====")

print("Read  → 'r'")
print("Write → 'w'")
print("Append → 'a'")


print("\n===== BASIC FILE OPERATIONS =====")

print("""
file = open("file.txt", "r")
file.close()

open()  → opens the file
close() → closes the file
""")


print("\n===== TEXT vs BINARY FILES =====")

print("Text file  → human-readable (.txt)")
print("Binary file → not readable (.jpg, .mp4)")


print("\n===== REAL-WORLD USAGE =====")

print("✔ Banking systems store transactions")
print("✔ Login systems store user data")
print("✔ Logs store system activity")


print("\n===== IMPORTANT NOTE =====")

print("Always close the file after use")