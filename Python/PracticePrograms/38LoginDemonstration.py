#Program: Login System with 3 Attempts

print("===== LOGIN SYSTEM =====")

password = "admin123"
attempts = 3

# User gets 3 tries
while attempts > 0:
    entered = input("Enter password: ")

    if entered == password:
        print("Login successful.")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account locked. Try again later.")
