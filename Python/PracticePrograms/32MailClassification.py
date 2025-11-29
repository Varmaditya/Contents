#Program: Extract only Gmail accounts

print("===== FILTER GMAIL ACCOUNTS =====")

# Email list
emails = [
    "john@gmail.com", "rita@yahoo.com", "alex@gmail.com",
    "tom@outlook.com", "sara@gmail.com"
]

print("Gmail users:")
# Print only emails ending with Gmail domain
for email in emails:
    if email.endswith("@gmail.com"):
        print(email)
