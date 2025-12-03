# Program: Email Cleaning & Categorization System

print("===== EMAIL CLEANING & CATEGORIZER =====")

emails = [
    "  john@gmail.com  ", "RITA@Yahoo.com", "alex@gmail.com ",
    "   tom@outlook.com", "sara@GMAIL.com"
]

cleaned_emails = []       # will store trimmed, lowercase emails
gmail_users = []          # will store only gmail users
others = []               # any other domain

# Clean emails and categorize them
for mail in emails:
    clean = mail.strip().lower()   # remove spaces + convert lowercase
    cleaned_emails.append(clean)

    if clean.endswith("@gmail.com"):
        gmail_users.append(clean)
    else:
        others.append(clean)

print("\nAll Cleaned Emails:", cleaned_emails)
print("Gmail Users:", gmail_users)
print("Other Domains:", others)
