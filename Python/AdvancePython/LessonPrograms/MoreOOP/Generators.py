# GENERATORS & LAZY EVALUATION
# ---------------------------------------------

print("\n===== GENERATOR FUNCTION =====")

def count_up(n):
    i = 1
    while i <= n:
        yield i   # produces one value at a time
        i += 1

gen = count_up(3)

print(next(gen))
print(next(gen))


print("\n===== USING GENERATOR IN LOOP =====")

for num in count_up(3):
    print("Generated:", num)


print("\n===== GENERATOR vs LIST =====")

lst = [i*i for i in range(3)]
gen_exp = (i*i for i in range(3))

print("List:", lst)
print("Generator:", gen_exp)


print("\n===== LAZY EVALUATION =====")

def lazy():
    print("Start")
    yield 1
    yield 2

g = lazy()

print("Generator created")
print(next(g))
print(next(g))
