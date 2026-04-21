# ADVANCED STANDARD LIBRARY MODULES (DETAILED)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== ADVANCED STANDARD LIBRARY =====")
print("""
These modules make Python:
✔ More powerful
✔ More efficient
✔ More expressive
""")

# ======================================================
# collections MODULE
# ======================================================

print("\n===== collections MODULE =====")
print("""
WHAT:
Advanced data structures

WHEN:
✔ Counting
✔ Grouping
✔ Default values
""")

from collections import Counter, defaultdict

# Example 1: Counter
print("\n--- Example 1: Counter ---")
data = ["a", "b", "a", "c", "b"]
print(Counter(data))

# Example 2: defaultdict
print("\n--- Example 2: defaultdict ---")
d = defaultdict(int)
d["x"] += 1
print(d)

# Example 3: Word count
print("\n--- Example 3: Word Count ---")
text = "python is easy python is powerful"
print(Counter(text.split()))

# ======================================================
# itertools MODULE
# ======================================================

print("\n===== itertools MODULE =====")
print("""
WHAT:
Efficient looping tools

WHEN:
✔ Combinations
✔ Permutations
✔ Infinite sequences
""")

import itertools

# Example 1: Combinations
print("\n--- Example 1: Combinations ---")
print(list(itertools.combinations([1, 2, 3], 2)))

# Example 2: Permutations
print("\n--- Example 2: Permutations ---")
print(list(itertools.permutations([1, 2, 3], 2)))

# Example 3: Count
print("\n--- Example 3: Infinite Count ---")
counter = itertools.count(1)
print(next(counter), next(counter), next(counter))

# ======================================================
# functools MODULE
# ======================================================

print("\n===== functools MODULE =====")
print("""
WHAT:
Functional programming tools

WHEN:
✔ Aggregation
✔ Optimization
✔ Function manipulation
""")

from functools import reduce

# Example 1: Sum
print("\n--- Example 1: Sum ---")
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, nums))

# Example 2: Product
print("\n--- Example 2: Product ---")
print(reduce(lambda x, y: x * y, nums))

# Example 3: Max
print("\n--- Example 3: Max ---")
print(reduce(lambda x, y: x if x > y else y, nums))

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

text = "python makes python powerful"
words = text.split()

from collections import Counter
print("Word Count:", Counter(words))

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ collections → data handling
✔ itertools → efficient iteration
✔ functools → functional programming

These modules help write clean and efficient code.
""")