# Program: Membership Operators in Python

# ---------------- Introduction ----------------
print("\n===== MEMBERSHIP OPERATORS IN PYTHON =====")

"""
Membership operators are used to test whether a value is part of a sequence.
Common sequences: string, list, tuple, dictionary, set
Operators:
    'in'      → Returns True if value is present in the sequence
    'not in'  → Returns True if value is NOT present in the sequence
"""

# ---------------- Examples ----------------

# 1️⃣ String Example
text = "python programming"
print("Text:", text)
print("'p' in text   →", 'p' in text)
print("'z' in text   →", 'z' in text)
print("'thon' in text →", 'thon' in text)
print("'java' not in text →", 'java' not in text)
print()

# 2️⃣ List Example
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)
print("'banana' in fruits →", 'banana' in fruits)
print("'grape' not in fruits →", 'grape' not in fruits)
print()

# 3️⃣ Tuple Example
numbers = (10, 20, 30, 40)
print("Tuple:", numbers)
print("20 in numbers →", 20 in numbers)
print("50 not in numbers →", 50 not in numbers)
print()

# 4️⃣ Dictionary Example
student = {"name": "Aditya", "age": 23, "course": "Python"}
print("Dictionary:", student)
print("'name' in student →", 'name' in student)       # checks key presence
print("'Aditya' in student →", 'Aditya' in student)   # values not checked
print("'course' not in student →", 'course' not in student)
print()

# 5️⃣ Set Example
colors = {"red", "green", "blue"}
print("Set:", colors)
print("'red' in colors →", 'red' in colors)
print("'yellow' not in colors →", 'yellow' not in colors)
print()

# ---------------- Input Example ----------------
print("===== USER INPUT EXAMPLE =====")
word = input("Enter a word: ")
if 'a' in word:
    print("Yes, the letter 'a' is present.")
else:
    print("No, the letter 'a' is not present.")

print("""
Summary:
→ 'in' checks if a value exists inside a sequence.
→ 'not in' checks if a value does NOT exist.
→ Works on: strings, lists, tuples, dictionaries, sets.
""")
