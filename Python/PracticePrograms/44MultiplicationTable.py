# Program: Multiplication Table Matrix (While Loop)

print("===== MULTIPLICATION MATRIX =====")

num = int(input("Enter a number: "))
i = 1

while i <= num:
    j = 1
    while j <= num:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1
