# Program: Number Pyramid

print("===== NUMBER PYRAMID =====")

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
