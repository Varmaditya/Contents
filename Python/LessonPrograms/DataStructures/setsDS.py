# SETS IN PYTHON

# ---------------- Introduction ----------------
print("\n===== SETS IN PYTHON =====")
print("""
A Set in Python is an unordered, unindexed collection of unique items.
Key Features:
✔ No duplicate values
✔ Unordered (items do not have fixed positions)
✔ Mutable (you can add or remove items)
✔ Uses curly braces {}
""")

# ---------------- Creating Sets ----------------
print("\n--- Creating Sets ---")

numbers = {10, 20, 30, 40}
mixed_set = {10, "Python", 3.14, True}
empty_set = set()  # {} creates a dictionary, so use set()
duplicates_removed = {1, 2, 2, 3, 3, 3}

print("Numbers Set:", numbers)
print("Mixed Set:", mixed_set)
print("Empty Set:", empty_set)
print("Set with duplicates removed:", duplicates_removed)

# ---------------- Adding & Removing Elements ----------------
print("\n===== ADDING & REMOVING ELEMENTS =====")

fruits = {"apple", "banana", "mango"}
print("Original Set:", fruits)

# add()
fruits.add("orange")
print("After add('orange'):", fruits)

# remove()
fruits.remove("banana")
print("After remove('banana'):", fruits)

# discard() (same as remove but does NOT give error)
fruits.discard("grapes")  # 'grapes' does not exist → no error
print("After discard('grapes') → safe remove:", fruits)

# pop() removes random item
removed_item = fruits.pop()
print("After pop():", fruits)
print("Popped item:", removed_item)

# clear()
temp_set = {"x", "y", "z"}
temp_set.clear()
print("After clear():", temp_set)

# ---------------- Set Operations ----------------
print("\n===== SET OPERATIONS =====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\nSet A:", set_a)
print("Set B:", set_b)

# union()
print("\n--- Union ---")
print("A ∪ B =", set_a.union(set_b))

# intersection()
print("\n--- Intersection ---")
print("A ∩ B =", set_a.intersection(set_b))

# difference()
print("\n--- Difference ---")
print("A - B =", set_a.difference(set_b))
print("B - A =", set_b.difference(set_a))

# symmetric difference()
print("\n--- Symmetric Difference ---")
print("A Δ B =", set_a.symmetric_difference(set_b))

# ---------------- Useful Set Methods ----------------
print("\n===== SET METHODS =====")

set1 = {1, 2, 3}
set2 = {3, 4}

print("\nset1:", set1)
print("set2:", set2)

print("Is set1 subset of set2? →", set1.issubset(set2))
print("Is set1 superset of set2? →", set1.issuperset(set2))
print("Do sets have no common items? (isdisjoint) →", set1.isdisjoint(set2))

# update()
set1.update(set2)
print("\nAfter set1.update(set2):", set1)

# copy()
copy_set = set1.copy()
print("Copy of set1:", copy_set)

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We learned:
✔ Creating sets  
✔ Adding & removing elements  
✔ Set operations (union, intersection, difference, symmetric difference)  
✔ Useful set methods (issubset, update, copy, isdisjoint, etc.)
""")
