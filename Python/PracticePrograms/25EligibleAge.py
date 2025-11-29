# Program: Service Eligibility Checker

print("===== SERVICE ELIGIBILITY CHECKER =====")

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()

if age >= 18 and citizen == "yes":
    print("You are eligible to apply.")
else:
    print("You are NOT eligible to apply.")
