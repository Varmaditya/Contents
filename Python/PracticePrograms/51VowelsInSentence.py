# Program: Count Vowels

text = input("Enter text: ").lower()
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)
