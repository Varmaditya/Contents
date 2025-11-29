#Program: Calculate total cost of items in cart

print("===== DIGIT COUNTER =====")

num = int(input("Enter any number: "))
temp = num  # copy
count = 0   # counter

# Count digits
while temp > 0:
    temp //= 10
    count += 1

print("Total digits in", num, "=", count)
