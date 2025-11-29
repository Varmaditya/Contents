#Program: Loop through temperatures and find the maximum

print("===== WEEKLY TEMPERATURE CHECK =====")

# Daily temperature readings
temperatures = [30.5, 32.1, 31.7, 33.0, 29.8, 34.2, 32.9]

highest = temperatures[0]  # assume first is max

# Find maximum temperature
for t in temperatures:
    if t > highest:
        highest = t

print("Highest temperature:", highest)
