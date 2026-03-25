# ITERATORS & ITERATION PROTOCOL
# ---------------------------------------------

print("\n===== ITERATOR USING iter() & next() =====")

data = [10, 20, 30]

it = iter(data)

print(next(it))
print(next(it))
print(next(it))
# next(it) → StopIteration


print("\n===== FOR LOOP (USES ITERATION PROTOCOL) =====")

for x in data:
    print("Value:", x)


print("\n===== MANUAL ITERATION (PROTOCOL) =====")

it2 = iter(data)

while True:
    try:
        val = next(it2)
        print("Manual:", val)
    except StopIteration:
        print("Iteration completed")
        break


print("\n===== CUSTOM ITERATOR =====")

class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

counter = CountUp(3)

for num in counter:
    print("Custom:", num)
