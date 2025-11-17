# TUPLES IN PYTHON
# ---------------- Introduction ----------------
print("\n===== TUPLES IN PYTHON =====")
print("""
A Tuple in Python is an ordered, immutable collection of items.
Immutable means once a tuple is created, elements cannot be changed.
Tuples are written using parentheses () and can store mixed data types.
""")

# ---------------- Creating Tuples ----------------
print("\n--- Creating Tuples ---")

numbers = (10, 20, 30, 40)
mixed_tuple = (10, "Python", 3.14, True)
single_element_tuple = (5,)   # comma is required for single-element tuple
empty_tuple = ()
nested_tuple = (1, 2, (3, 4), ("a", "b"))

print("Numbers Tuple:", numbers)
print("Mixed Tuple:", mixed_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Empty Tuple:", empty_tuple)
print("Nested Tuple:", nested_tuple)

# ---------------- Accessing Elements ----------------
print("\n===== ACCESSING ELEMENTS =====")

sample = ("apple", "banana", "mango", "orange")

print("\n--- Indexing ---")
print("sample[0] =", sample[0])
print("sample[1] =", sample[1])
print("sample[-1] = last element =", sample[-1])

print("\n--- Slicing ---")
print("sample[1:3] =", sample[1:3])
print("sample[:2] =", sample[:2])
print("sample[2:] =", sample[2:])
print("sample[::-1] = reversed tuple =", sample[::-1])

# ---------------- Tuple Immutability ----------------
print("\n===== TUPLE IMMUTABILITY =====")
print("""
Tuples cannot be modified once created.
This means:
❌ No adding new elements
❌ No changing existing values
❌ No removing elements

However, you *can* create a new tuple by combining tuples.
""")

example_tuple = (1, 2, 3)
print("Original tuple:", example_tuple)

# Trying to change value → will cause an error (so we only show message)
print("Cannot do: example_tuple[0] = 5  (this results in Error)")

# Creating a new tuple instead
new_tuple = example_tuple + (4, 5)
print("New tuple by adding elements:", new_tuple)

# ---------------- Tuple Methods ----------------
print("\n===== TUPLE METHODS =====")

values = (10, 20, 10, 30, 10)

# count()
print("\n--- count() ---")
print("values =", values)
print("Count of 10 →", values.count(10))

# index()
print("\n--- index() ---")
print("Index of 30 in values →", values.index(30))

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We learned:
✔ Creating tuples  
✔ Accessing tuple elements  
✔ Tuple immutability  
✔ Tuple methods (count, index)  
""")
