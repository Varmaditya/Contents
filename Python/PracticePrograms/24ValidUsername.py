# Program: Check if a username meets rules (length & no spaces)

print("===== VAILD USERNAME =====")

username = input("Enter username: ")

if " " in username:
    print("Invalid: Username should not contain spaces.")
elif len(username) < 5:
    print("Invalid: Username must be at least 5 characters.")
else:
    print("Username is valid.")

