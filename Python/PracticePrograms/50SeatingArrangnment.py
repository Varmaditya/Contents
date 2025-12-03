# Program: Seating Arrangement Generator

print("===== SEATING ARRANGEMENT =====")

rows = 3
seats = 4

r = 1
while r <= rows:
    s = 1
    while s <= seats:
        print(f"Row {r} - Seat {s}")
        s += 1
    print()
    r += 1
