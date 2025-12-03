# Program: Email Cleaning & Categorization System

print("===== EMAIL CLEANING & CATEGORIZER =====")

emails = [
    "  john@gmail.com  ", "RITA@Yahoo.com", "alex@gmail.com ",
    "   tom@outlook.com", "sara@GMAIL.com"
]

cleanedEmails = []       # will store trimmed, lowercase emails
gmailUsers = []          # will store only gmail users
others = []               # any other domain

# Clean emails and categorize them
for mail in emails:
    clean = mail.strip().lower()   # remove spaces + convert lowercase
    cleanedEmails.append(clean)

    if clean.endswith("@gmail.com"):
        gmailUsers.append(clean)
    else:
        others.append(clean)

print("\nAll Cleaned Emails:", cleanedEmails)
print("Gmail Users:", gmailUsers)
print("Other Domains:", others)
