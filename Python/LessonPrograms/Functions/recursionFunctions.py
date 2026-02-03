# RECURSION IN PYTHON
# ---------------- Introduction ----------------
print("\n===== RECURSION IN PYTHON =====")
print("""
Recursion is a technique where a function calls itself to solve a problem.
It is useful when a large problem can be divided into smaller similar problems.

Every recursive function must have:
1. Base Case     -> the condition where the recursion stops.
2. Recursive Case -> the function calls itself again with smaller input.
""")

# ---------------- General Recursive Structure ----------------
print("\n===== BASIC RECURSIVE STRUCTURE =====")
print("""
General pattern of recursion:

def func(n):
    if base_case_condition:
        return value
    else:
        return func(smaller_value)
""")

# ---------------- Example 1: Count Down Timer ----------------
print("\n===== EXAMPLE 1: COUNTDOWN USING RECURSION =====")
print("This countdown reduces the number until it reaches 0.")

def countdown(n):
    if n == 0:       # base case
        print("Time's up!")
        return
    print(n)
    countdown(n - 1) # recursive call

countdown(5)

# ---------------- Example 2: Product of List Elements ----------------
print("\n===== EXAMPLE 2: PRODUCT OF LIST ELEMENTS =====")

def product_of_list(nums, index=0):
    if index == len(nums):     # base case: no elements left
        return 1
    return nums[index] * product_of_list(nums, index + 1)

lst = [2, 4, 3]
print("List:", lst)
print("Product of list:", product_of_list(lst))

# ---------------- Example 3: Count Occurrences in a String ----------------
print("\n===== EXAMPLE 3: RECURSIVE CHARACTER OCCURRENCE COUNT =====")

def count_occurrence(text, ch, index=0):
    if index == len(text):      # base case
        return 0
    if text[index] == ch:
        return 1 + count_occurrence(text, ch, index + 1)
    return count_occurrence(text, ch, index + 1)

text = "recursion example program"
char = "r"
print(f"Occurrences of '{char}' =", count_occurrence(text, char))

# ---------------- Example 4: Convert Number to Binary Recursively ----------------
print("\n===== EXAMPLE 4: NUMBER TO BINARY (RECURSION) =====")

def to_binary(n):
    if n == 0:         # base case
        return ""
    return to_binary(n // 2) + str(n % 2)

num = 13
print(f"Binary of {num} =", to_binary(num))

# ---------------- Practical Example: Directory Size Calculator (Recursion) ----------------
print("\n===== PRACTICAL EXAMPLE: DIRECTORY SIZE CALCULATOR =====")
print("""
A real-world application of recursion:
Operating systems calculate folder sizes recursively by adding the sizes
of all files and all subfolders inside it.
""")

filesystem = {
    "Videos": {
        "movie.mp4": 700,
        "clip.mkv": 120
    },
    "Documents": {
        "notes.txt": 5,
        "projects": {
            "project1.docx": 20,
            "project2.pdf": 15
        }
    },
    "image.png": 3
}

def directory_size(item):
    # If it's a file (integer size)
    if isinstance(item, int):
        return item

    # If it's a folder (dictionary), add sizes recursively
    total = 0
    for key in item:
        total += directory_size(item[key])
    return total

print("Total size of directory =", directory_size(filesystem), "MB")

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
In this chapter we learned:
✔ What recursion is and how it works (base case + recursive case)
✔ Countdown using recursion
✔ Recursive product of a list
✔ Recursive character counting
✔ Converting number to binary using recursion
✔ Real-world recursion: computing directory size

Recursion is widely used in:
✔ File systems
✔ Searching and sorting algorithms
✔ Mathematical computations
✔ Data structure traversal (trees, graphs)

This forms the foundation for more advanced topics in programming.
""")
