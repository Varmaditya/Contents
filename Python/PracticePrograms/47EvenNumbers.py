# Program: Skip Even Numbers in Grid

print("===== ODD NUMBERS GRID =====")

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j % 2 == 0:   # skip evens
            continue
        print(j, end=" ")
    print()
