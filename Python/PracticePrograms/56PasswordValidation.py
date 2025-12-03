# Program: Password Validator

print("===== PASSWORD VALIDATOR =====")

pwd = input("Enter password: ")

# Validation rules
has_digit = any(ch.isdigit() for ch in pwd)
has_upper = any(ch.isupper() for ch in pwd)
has_lower = any(ch.islower() for ch in pwd)
has_special = any(ch in "!@#$%^&*()-_=+[]{};:/?,.<>" for ch in pwd)
has_length = len(pwd) >= 8

# Check all conditions
if has_digit and has_upper and has_lower and has_special and has_length:
    print("Password is strong and valid.")
else:
    print("Weak password. Must include:")
    print("- At least 8 characters")
    print("- At least one digit")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one special character (!@#$ etc.)")
