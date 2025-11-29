#Program: Calculate sum of the given number from user

print("===== RUNNING SUM CALCULATOR =====")

total = 0

# Keep adding until user enters 0
while True:
    n = int(input("Enter a number (0 to stop): "))

    if n == 0:
        break

    total += n

print("Final total:", total)
