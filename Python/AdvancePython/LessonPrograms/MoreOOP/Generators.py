# GENERATORS, yield, GENERATOR EXPRESSIONS & LAZY EVALUATION
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== GENERATORS & LAZY EVALUATION =====")
print("""
Generators are special functions that:
✔ Produce values one at a time
✔ Do not store all values in memory
✔ Use 'yield' instead of return

They are useful for:
✔ Large data processing
✔ Memory-efficient programs
✔ Streaming data

This chapter covers:
✔ Generators
✔ yield keyword
✔ Generator expressions
✔ Lazy evaluation
""")

# ---------------- Normal Function vs Generator ----------------
print("\n===== NORMAL FUNCTION vs GENERATOR =====")
print("""
Normal function returns all values at once.
Generator produces values one by one.
""")

def normal_function():
    return [1, 2, 3]

def generator_function():
    yield 1
    yield 2
    yield 3

print("Normal Function:", normal_function())
print("Generator Function:", generator_function())

print("""
Generator function returns a generator object.
""")

# ---------------- yield Keyword ----------------
print("\n===== yield KEYWORD =====")
print("""
yield pauses the function
and returns a value.

When next() is called again,
execution resumes from where it stopped.
""")

def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up(5)

print(next(gen))
print(next(gen))
print(next(gen))

# ---------------- Using Generator in Loop ----------------
print("\n===== USING GENERATOR IN FOR LOOP =====")

for num in count_up(5):
    print("Generated:", num)

# ---------------- Generator vs List (Memory Efficiency) ----------------
print("\n===== GENERATOR vs LIST =====")

numbers_list = [i*i for i in range(5)]
numbers_gen = (i*i for i in range(5))

print("List:", numbers_list)
print("Generator:", numbers_gen)

print("""
List stores all values in memory.
Generator computes values on demand.
""")

# ---------------- Generator Expression ----------------
print("\n===== GENERATOR EXPRESSION =====")
print("""
Generator expressions are like list comprehensions,
but use parentheses () instead of [].
""")

gen_exp = (x*x for x in range(1, 6))

for value in gen_exp:
    print("Value:", value)

# ---------------- Lazy Evaluation ----------------
print("\n===== LAZY EVALUATION =====")
print("""
Lazy evaluation means:
Values are generated only when needed.

Nothing is computed until requested.
""")

def lazy_numbers():
    print("Start generating...")
    for i in range(3):
        print("Yielding:", i)
        yield i

lazy_gen = lazy_numbers()

print("Generator created. No execution yet.")

print(next(lazy_gen))
print(next(lazy_gen))
print(next(lazy_gen))

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE =====")

def read_large_data():
    for i in range(1, 6):
        yield f"Line {i}"

for line in read_large_data():
    print("Processing:", line)

print("""
Instead of loading all data at once,
generator processes one item at a time.
""")

# ---------------- Important Notes ----------------
print("\n===== IMPORTANT NOTES =====")
print("""
✔ yield pauses and resumes execution
✔ Generators do not store full data
✔ Memory efficient for large datasets
✔ Generator expressions are compact syntax
✔ Lazy evaluation improves performance
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Generators produce values one by one
✔ yield replaces return in generators
✔ Generator expressions use ()
✔ Lazy evaluation means compute when needed
✔ Generators are used for efficient data processing

Generators are widely used in:
✔ File handling
✔ Data pipelines
✔ Streaming applications
✔ Big data processing
""")