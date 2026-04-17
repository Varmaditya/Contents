# ADVANCED STANDARD LIBRARY
# ---------------------------------------------

print("\n===== COLLECTIONS =====")

from collections import Counter, defaultdict

data = ["a", "b", "a", "c"]
print("Count:", Counter(data))

d = defaultdict(int)
d["x"] += 1
print("DefaultDict:", d)


print("\n===== ITERTOOLS =====")

import itertools

print("Combinations:", list(itertools.combinations([1, 2, 3], 2)))
print("Permutations:", list(itertools.permutations([1, 2], 2)))


print("\n===== FUNCTOOLS =====")

from functools import reduce

nums = [1, 2, 3, 4]
print("Sum:", reduce(lambda x, y: x + y, nums))


print("\n===== PRACTICAL =====")

text = "python is powerful python"
print("Word Count:", Counter(text.split()))
