# Program: Check Even or Odd

print("===== EVEN OR ODD CHECKER =====")

# Input from user
num = int(input("Enter a number: "))

# Checking using modulus operator
isEven = (num % 2 == 0)

# Logical output
print("Is the number even?", isEven)
