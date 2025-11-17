# Data Structure: Strings

# ---------------- Introduction ----------------
print("\n===== STRINGS IN PYTHON =====")
print("""
A String in Python is an ordered collection of characters enclosed in quotes.
Strings are immutable (cannot be changed after creation).
They can store letters, numbers, symbols, and even empty text.
""")

# ---------------- Creating Strings ----------------
print("\n--- Creating Strings ---")
single_quoted = 'Hello Python'
double_quoted = "Welcome to Strings"
multi_line = """This is a
multi-line string
in Python."""

print("Single quoted string:", single_quoted)
print("Double quoted string:", double_quoted)
print("Multi-line string:\n", multi_line)

# ---------------- Indexing in Strings ----------------
print("\n--- String Indexing ---")
text = "Python"
print("String:", text)
print("text[0] (1st character) =", text[0])
print("text[1] (2nd character) =", text[1])
print("text[-1] (last character) =", text[-1])

# ---------------- Slicing in Strings ----------------
print("\n--- String Slicing ---")
print("text[0:3] → first 3 letters =", text[0:3])
print("text[2:]  → from index 2 to end =", text[2:])
print("text[:4]  → start to index 3 =", text[:4])
print("text[::2] → every 2nd character =", text[::2])
print("text[::-1] → reverse string =", text[::-1])

# ---------------- Useful String Methods ----------------
print("\n===== STRING METHODS =====")

sample = "  Hello Python Programming  "
print("\nOriginal sample string with spaces:", repr(sample))

# Length of string
print("Length of sample →", len(sample))

# Changing case
print("Lowercase →", sample.lower())
print("Uppercase →", sample.upper())

# strip()
print("strip() removes leading/trailing spaces →", sample.strip())

# replace()
print("replace('Python', 'Java') →", sample.replace("Python", "Java"))

# split()
print("split() breaks string into list →", sample.split())

# find()
print("find('Python') → index:", sample.find("Python"))

# count()
print("count('o') → occurrences:", sample.count("o"))

# ---------------- String Formatting ----------------
print("\n===== STRING FORMATTING =====")

name = "John"
age = 23

# Using f-string
print("\n--- Using f-strings ---")
print(f"My name is {name} and I am {age} years old.")

# Using format()
print("\n--- Using .format() ---")
print("My name is {} and I am {} years old.".format(name, age))

# Using numbered placeholders
print("I am {1} years old and my name is {0}.".format(name, age))

# Using keyword placeholders
print("My name is {n} and age is {a}.".format(n=name, a=age))

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We learned:
✔ How to create strings  
✔ String indexing  
✔ String slicing  
✔ Common string methods  
✔ String formatting (f-strings & .format())
""")
