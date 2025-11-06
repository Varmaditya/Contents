# Looping Statements in Python - FOR LOOP

# ---------------- Introduction ----------------
print("\n===== FOR LOOP IN PYTHON =====")
print("""
The 'for' loop in Python is used to **iterate over a sequence** such as a list, string, tuple, dictionary, or range.
It allows you to execute a block of code for every element in that sequence.

Unlike a 'while' loop which depends on a condition, 
the 'for' loop automatically stops when all items in the sequence are processed.

SYNTAX:
for variable in sequence:
    # code block

→ 'variable' takes each value from the sequence one by one.
→ The loop runs until all elements in the sequence are processed.
→ Commonly used with strings, lists, tuples, and the range() function.
""")

# ---------------- Understanding range() Function ----------------
print("\n===== UNDERSTANDING range() FUNCTION =====")
print("""
The range() function generates a sequence of numbers that the 'for' loop can iterate over.

SYNTAX:
    range(start, stop, step)

1. start → The number from where the sequence begins (default: 0)
2. stop  → The number where the sequence ends (but it is **not included**)
3. step  → The difference between each number (default: 1)

→ Examples:
    range(5)           → 0, 1, 2, 3, 4
    range(2, 6)        → 2, 3, 4, 5
    range(1, 10, 2)    → 1, 3, 5, 7, 9
    range(10, 0, -2)   → 10, 8, 6, 4, 2
""")

# ---------------- Example 1: Basic For Loop ----------------
print("\n---- Example 1: Print numbers from 1 to 5 ----")
for i in range(1, 6):
    print("Number:", i)
print("Loop completed successfully.\n")

# ---------------- Example 2: Iterating Over a String ----------------
print("---- Example 2: Iterate through characters of a string ----")
text = "PYTHON"
for ch in text:
    print(ch)
print("String iteration completed.\n")

# ---------------- Example 3: Using range() with Step ----------------
print("---- Example 3: Using range() with Step Value ----")
print("Numbers from 0 to 10 with a step of 2:")
for num in range(0, 11, 2):
    print(num, end=" ")
print("\nRange() with step example completed.\n")

# ---------------- Example 4: Iterating Over a List ----------------
print("---- Example 4: Iterating Over a List ----")
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print("Current fruit:", fruit)
print("All fruits printed.\n")

# ---------------- Example 5: Using range() with User Input ----------------
print("---- Example 5: Print Numbers up to User Limit ----")
limit = int(input("Enter a number: "))
for i in range(1, limit + 1):
    print(i, end=" ")
print("\nLoop completed.\n")

# ---------------- Example 6: Sum of Numbers using For Loop ----------------
print("---- Example 6: Calculate Sum of Natural Numbers ----")
n = int(input("Enter a number: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum of first", n, "numbers is:", sum_n, "\n")

# ---------------- Example 7: Multiplication Table ----------------
print("---- Example 7: Multiplication Table ----")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("Table printed successfully.\n")

# ---------------- Example 8: Nested For Loop ----------------
print("---- Example 8: Nested For Loop ----")
print("Pattern Printing Example:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"({i},{j})", end=" ")
    print()
print("Nested loop execution completed.\n")

# ---------------- Example 9: Looping Through a String with Index ----------------
print("---- Example 9: Looping with index using range() ----")
word = "Hello"
for index in range(len(word)):
    print("Character at index", index, "is", word[index])
print("Completed indexed iteration of string.\n")

# ---------------- Example 10: For Loop with Reverse Range ----------------
print("---- Example 10: For Loop with Reverse Range ----")
print("Counting backwards from 10 to 0:")
for num in range(10, -1, -1):
    print(num, end=" ")
print("\nReverse counting completed.\n")

# ---------------- Example 11: Real-life Example - Grocery Bill ----------------
print("---- Example 11: Grocery Bill Calculation ----")
items = ["Milk", "Bread", "Eggs", "Butter"]
prices = [40, 25, 60, 80]
total = 0
print("Item\tPrice")
for i in range(len(items)):
    print(items[i], "\t", prices[i])
    total += prices[i]
print("Total Bill: ₹", total)
print("Bill generation completed.\n")

# ---------------- Example 12: For Loop with String Filtering ----------------
print("---- Example 12: Display Vowels from a String ----")
sentence = input("Enter a sentence: ")
print("Vowels in your sentence are:")
for ch in sentence:
    if ch.lower() in "aeiou":
        print(ch, end=" ")
print("\nVowel extraction complete.\n")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
→ for loop → used for iterating over sequences (string, list, tuple, range)
→ range(start, stop, step) → generates number sequences
→ Nested loops → loops inside loops
→ Step value → defines increment or decrement
→ Best for fixed number of iterations or working with collections

Examples:
    for i in range(5):          # 0 to 4
        print(i)

    for ch in "Python":         # Each character
        print(ch)

    for i in range(10, 0, -2):  # Reverse counting
        print(i)
""")

