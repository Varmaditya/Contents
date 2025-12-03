# Program: Search Number in Matrix

print("===== SEARCH IN MATRIX =====")

matrix = [
    [5, 7, 12],
    [9, 3, 15],
    [6, 8, 20]
]

target = 15
found = False

for row in matrix:
    for num in row:
        if num == target:
            print("Found:", target)
            found = True
            break
    if found:
        break
