# Program: Simple Interest Calculator

print("===== SIMPLE INTEREST CALCULATOR =====")

# Formula: SI = (P × R × T) / 100
principal = float(input("Enter Principal Amount (₹): "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

simpleInterest = (principal * rate * time) / 100

print("\nPrincipal Amount: ₹", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest: ₹", simpleInterest)
print("Total Amount after interest: ₹", principal + simpleInterest)
