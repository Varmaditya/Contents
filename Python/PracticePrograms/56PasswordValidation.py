# Program: Password Validator

print("===== PASSWORD VALIDATOR =====")

passwor = input("Enter password: ")

# Validation rules
hasDigit = any(ch.isdigit() for ch in passwor)
hasUpper = any(ch.isupper() for ch in passwor)
hasLower = any(ch.islower() for ch in passwor)
hasSpecial = any(ch in "!@#$%^&*()-_=+[]{};:/?,.<>" for ch in passwor)
hasLength = len(passwor) >= 8

# Check all conditions
if hasDigit and hasUpper and hasLower and hasSpecial and hasLength:
    print("Password is strong and valid.")
else:
    print("Weak password. Must include:")
    print("- At least 8 characters")
    print("- At least one digit")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one special character (!@#$ etc.)")
