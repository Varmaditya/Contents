# LISTS IN PYTHON
# ---------------- Introduction ----------------
print("\n===== LISTS IN PYTHON =====")
print("""
A List in Python is an ordered, mutable (changeable) collection of items.
Lists can store mixed data types such as integers, floats, strings, and even other lists.
Lists are written inside square brackets [].
""")

# ---------------- Creating Lists ----------------
print("\n--- Creating Lists ---")

numbers = [10, 20, 30, 40]
mixed_list = [10, "Python", 3.14, True]
empty_list = []
nested_list = [[1, 2], [3, 4], ["a", "b"]]

print("Numbers List:", numbers)
print("Mixed List:", mixed_list)
print("Empty List:", empty_list)
print("Nested List:", nested_list)

# ---------------- Accessing List Elements ----------------
print("\n===== ACCESSING ELEMENTS =====")

print("\n--- Indexing ---")
print("numbers[0] =", numbers[0])
print("numbers[1] =", numbers[1])
print("numbers[-1] = last element =", numbers[-1])

print("\n--- Slicing ---")
print("numbers[1:3] =", numbers[1:3])
print("numbers[:2] =", numbers[:2])
print("numbers[2:] =", numbers[2:])
print("numbers[::2] =", numbers[::2])
print("numbers[::-1] = reversed list =", numbers[::-1])

# ---------------- List Methods ----------------
print("\n===== LIST METHODS =====")

fruits = ["apple", "banana", "mango"]
print("\nOriginal fruits list:", fruits)

# append()
fruits.append("orange")
print("After append('orange'):", fruits)

# insert()
fruits.insert(1, "grapes")
print("After insert(1, 'grapes'):", fruits)

# remove()
fruits.remove("banana")
print("After remove('banana'):", fruits)

# pop()
popped_item = fruits.pop()
print("After pop():", fruits)
print("Popped item:", popped_item)

# sort()
numbers_to_sort = [4, 1, 5, 2, 3]
print("\nNumbers before sort:", numbers_to_sort)
numbers_to_sort.sort()
print("Numbers after sort():", numbers_to_sort)

# reverse()
numbers_to_sort.reverse()
print("After reverse():", numbers_to_sort)

# count()
print("Count of 10 in [10, 20, 10, 30] =", [10, 20, 10, 30].count(10))

# index()
print("Index of 'mango' in fruits list =", fruits.index("mango"))

# extend()
more_fruits = ["kiwi", "papaya"]
fruits.extend(more_fruits)
print("After extend(['kiwi', 'papaya']):", fruits)

# ---------------- Iterating Over Lists ----------------
print("\n===== ITERATING THROUGH LISTS =====")

items = ["pen", "book", "pencil"]

print("\nUsing for loop:")
for item in items:
    print("Item:", item)

print("\nUsing index and range:")
for i in range(len(items)):
    print("Index:", i, "-> Item:", items[i])

# ---------------- Nested Lists ----------------
print("\n===== NESTED LISTS =====")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix (Nested List):")
for row in matrix:
    print(row)

print("Accessing nested element matrix[1][2] =", matrix[1][2])

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We learned:
✔ Creating lists  
✔ Accessing elements (indexing & slicing)  
✔ List methods (append, insert, remove, pop, sort, reverse, etc.)  
✔ Iterating through lists  
✔ Nested lists  
""")
