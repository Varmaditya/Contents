# Python Keywords and Identifiers

import keyword   # module to check Python keywords

# ---------------- KEYWORDS ----------------
print("=== Keywords in Python ===")
print("Some keywords are:", keyword.kwlist[:10])   # show first 10 keywords
print("Total number of keywords:", len(keyword.kwlist), "\n")

# Trying to use a keyword as variable (❌ Wrong, will cause error if uncommented)
# if = 10     # Error, 'if' is a keyword

# ---------------- IDENTIFIERS ----------------
print("=== Identifiers in Python ===")

# ----------------- IDENTIFIER RULES SUMMARY -----------------
# 1. An identifier is a name used to identify a variable, function, class, etc.
# 2. It can contain letters (A-Z, a-z), digits (0-9), and underscores (_).
# 3. It MUST NOT start with a digit.
# 4. It cannot be a Python keyword (reserved word).
# 5. Use str.isidentifier() to check if a string is a valid identifier in Python.

# Valid identifiers
name = "Alice"         # letters
age1 = 21              # letters + digits
_student = "John"      # underscore at start
print("Valid identifiers ->", name, age1, _student)

# Invalid identifiers (❌ Uncommenting will cause errors)
# 2name = "Bob"       # cannot start with a number
# my-name = "Sam"     # hyphen not allowed
# class = "Test"      # cannot use keyword

# Case sensitivity
city = "Mumbai"
City = "Delhi"
print("\ncity:", city)   # lowercase variable
print("City:", City)     # uppercase variable (different identifier)

# Identifier check using Python
print("\nCheck if a word is identifier or keyword:")
words = ["name", "2abc", "class", "value_1"]
for w in words:
    print(w, "-> isidentifier?", w.isidentifier(), "| iskeyword?", keyword.iskeyword(w))
