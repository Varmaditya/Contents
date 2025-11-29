# Program: Check if entered time is morning, afternoon, evening, or night

print("===== CURRENT TIME OF THE DAY =====")

hour = int(input("Enter hour (0-23): "))

if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
elif 17 <= hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")
