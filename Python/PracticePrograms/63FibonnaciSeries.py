# Program: Fibonacci Series

n = int(input("Enter number of terms: "))

a, b = 0, 1
print(a, b, end=" ")

for _ in range(n - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c
