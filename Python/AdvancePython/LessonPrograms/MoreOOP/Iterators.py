# ITERATORS, ITERATION PROTOCOL, iter() & next()
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== ITERATORS & ITERATION PROTOCOL =====")
print("""
Iteration is the process of going through elements one by one.

Python uses a standard mechanism called
the Iteration Protocol.

Key components:
✔ Iterable
✔ Iterator
✔ iter()
✔ next()

This protocol is used internally by:
✔ for loops
✔ list, tuple, string traversal
✔ generators
""")

# ---------------- Iterable ----------------
print("\n===== ITERABLE =====")
print("""
An Iterable is an object that can be looped over.

Examples:
✔ list
✔ tuple
✔ string
✔ dictionary
""")

my_list = [10, 20, 30]

for item in my_list:
    print("Item:", item)

print("""
The list is an iterable.
It provides elements one by one.
""")

# ---------------- Iterator ----------------
print("\n===== ITERATOR =====")
print("""
An Iterator is an object that:
✔ Keeps track of current position
✔ Returns next element using next()

Iterator does NOT store all elements at once.
""")

numbers = [1, 2, 3]
iterator = iter(numbers)

print("Iterator object:", iterator)

print("Next:", next(iterator))
print("Next:", next(iterator))
print("Next:", next(iterator))

# print(next(iterator))  # This would raise StopIteration

print("""
When elements are exhausted,
StopIteration exception is raised.
""")

# ---------------- iter() Function ----------------
print("\n===== iter() FUNCTION =====")
print("""
iter() converts an iterable into an iterator.
""")

text = "Python"
it = iter(text)

print(next(it))
print(next(it))
print(next(it))

# ---------------- next() Function ----------------
print("\n===== next() FUNCTION =====")
print("""
next() retrieves the next element
from an iterator.
""")

nums = [100, 200]
it2 = iter(nums)

print(next(it2))
print(next(it2))

# print(next(it2))  # StopIteration

# ---------------- Iteration Protocol ----------------
print("\n===== ITERATION PROTOCOL =====")
print("""
Iteration Protocol works like this:

1️⃣ iter(obj) is called
2️⃣ It returns an iterator
3️⃣ next() is repeatedly called
4️⃣ When no elements left → StopIteration
""")

data = [5, 10, 15]

it3 = iter(data)

while True:
    try:
        value = next(it3)
        print("Value:", value)
    except StopIteration:
        print("Iteration completed")
        break

# ---------------- for loop uses Iteration Protocol ----------------
print("\n===== FOR LOOP INTERNAL WORKING =====")
print("""
for loop internally uses:
✔ iter()
✔ next()
✔ StopIteration
""")

nums = [1, 2, 3]

it4 = iter(nums)

while True:
    try:
        value = next(it4)
        print("For loop simulation:", value)
    except StopIteration:
        break

# ---------------- Creating Custom Iterator ----------------
print("\n===== CUSTOM ITERATOR =====")
print("""
We can create our own iterator
by defining:

✔ __iter__()
✔ __next__()
""")

class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

counter = CountUp(5)

for num in counter:
    print("Custom Iterator:", num)

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

class EvenNumbers:
    def __init__(self, max_value):
        self.max = max_value
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num <= self.max:
            return self.num
        else:
            raise StopIteration

even = EvenNumbers(10)

for n in even:
    print("Even Number:", n)

print("""
Custom iterators help create
memory-efficient and controlled iteration.
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Iterable: object that can be looped over
✔ Iterator: object that produces next values
✔ iter(): converts iterable to iterator
✔ next(): gets next element
✔ StopIteration ends iteration
✔ for loop uses iteration protocol internally
✔ Custom iterators use __iter__ and __next__

Iteration protocol is the foundation of:
✔ loops
✔ generators
✔ lazy evaluation
✔ memory-efficient programming
""")