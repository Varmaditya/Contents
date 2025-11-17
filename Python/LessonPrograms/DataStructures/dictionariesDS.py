# DICTIONARIES IN PYTHON
# ---------------- Introduction ----------------
print("\n===== DICTIONARIES IN PYTHON =====")
print("""
A Dictionary in Python is an unordered, mutable collection of key-value pairs.
Keys are unique and usually strings or numbers. Values can be any data type.
Dictionaries are written with curly braces: { key: value, ... }
""")

# ---------------- Creating Dictionaries ----------------
print("\n--- Creating Dictionaries ---")
# Literal creation
student = {"name": "Aditya", "age": 23, "course": "Computer Science"}
# Using dict() constructor
person = dict(name="Sneha", age=21, city="Mumbai")
# Empty dictionary
empty_dict = {}
# Nested dictionary (dictionary inside dictionary)
school = {
    "student1": {"name": "Asha", "marks": 82},
    "student2": {"name": "Rohit", "marks": 91}
}

print("student dict:", student)
print("person dict :", person)
print("empty_dict   :", empty_dict)
print("nested dict  :", school)

# ---------------- Accessing Values ----------------
print("\n===== ACCESSING VALUES =====")
print("\n--- Direct key access ---")
print("student['name'] ->", student["name"])
print("student['age']  ->", student["age"])

print("\n--- Using get() (safe access) ---")
print("student.get('course') ->", student.get("course"))
print("student.get('phone')  ->", student.get("phone"))           # returns None if key missing
print("student.get('phone', 'Not Provided') ->", student.get("phone", "Not Provided"))  # default

print("\n--- keys(), values(), items() ---")
print("Keys  ->", list(student.keys()))
print("Values->", list(student.values()))
print("Items ->", list(student.items()))

# ---------------- Adding & Updating Elements ----------------
print("\n===== ADDING & UPDATING ELEMENTS =====")
print("\nOriginal student dict:", student)

# Add new key-value
student["phone"] = "9876543210"
print("After adding phone:", student)

# Update existing key
student["age"] = 24
print("After updating age:", student)

# Using update() to add or modify multiple items
student.update({"city": "Pune", "course": "Data Science"})
print("After update() :", student)

# setdefault() - adds key with default if not present, returns value
dept = student.setdefault("department", "Engineering")
print("After setdefault('department') ->", dept)
print("student now ->", student)

# ---------------- Removing Elements ----------------
print("\n===== REMOVING ELEMENTS =====")
print("\nCurrent student dict:", student)

# pop(key) removes and returns the value
phone_val = student.pop("phone", None)
print("Popped 'phone' ->", phone_val)
print("After pop('phone') ->", student)

# popitem() removes and returns last inserted pair (Python 3.7+ preserves insertion order)
last_item = student.popitem()
print("Popitem removed:", last_item)
print("After popitem() ->", student)

# delete using del
if "city" in student:
    del student["city"]
    print("After del student['city'] ->", student)

# clear() to empty the dictionary
temp = {"a": 1, "b": 2}
print("\nTemp before clear():", temp)
temp.clear()
print("Temp after clear():", temp)

# ---------------- Iterating Over Dictionaries ----------------
print("\n===== ITERATING OVER DICTIONARIES =====")
employee = {"id": 101, "name": "Rina", "role": "Engineer", "salary": 75000}

print("\nIterate keys:")
for key in employee:
    print("Key:", key)

print("\nIterate values:")
for val in employee.values():
    print("Value:", val)

print("\nIterate items (key, value):")
for k, v in employee.items():
    print("Key:", k, "| Value:", v)

print("\nIterate with index using enumerate:")
for idx, (k, v) in enumerate(employee.items(), start=1):
    print(idx, "->", k, ":", v)

# ---------------- Working with Nested Dictionaries ----------------
print("\n===== NESTED DICTIONARIES =====")
company = {
    "dept1": {"manager": "Amit", "employees": 10},
    "dept2": {"manager": "Nina", "employees": 7}
}
print("Company:", company)
print("Manager of dept2 ->", company["dept2"]["manager"])

# ---------------- Input Example (safe updates) ----------------
print("\n===== USER INPUT EXAMPLE =====")
profile = {}
profile["username"] = input("Enter username: ")
profile["email"] = input("Enter email: ")
age_input = input("Enter age (leave blank if unknown): ").strip()
profile["age"] = int(age_input) if age_input != "" else None
print("Profile created ->", profile)

# ---------------- Practical Tiny Use-case: Frequency Counter ----------------
print("\n===== PRACTICAL: FREQUENCY COUNTER (WORDS) =====")
text = input("Enter a short sentence: ")
words = text.split()
freq = {}
for w in words:
    w_lower = w.lower()
    # increment count using get()
    freq[w_lower] = freq.get(w_lower, 0) + 1

print("Word frequencies:", freq)

# ---------------- Summary ----------------
print("\n--- SUMMARY ---")
print("""
We covered:
✔ Creating dictionaries (literal, dict(), nested)
✔ Accessing values (direct, get), and obtaining keys/values/items
✔ Adding and updating (assignment, update, setdefault)
✔ Removing elements (pop, popitem, del, clear)
✔ Useful methods (get, update, keys, values, items, setdefault, pop, popitem, clear)
✔ Iterating over dictionaries (keys, values, items, enumerate)
✔ Nested dictionaries and a small frequency-counter example
""")
