# EXTERNAL LIBRARIES IN PYTHON (DETAILED)
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== EXTERNAL LIBRARIES IN PYTHON =====")
print("""
Python has thousands of external libraries
created by developers around the world.

These are not built into Python,
but can be installed using pip.

They help us:
✔ Save time
✔ Avoid reinventing the wheel
✔ Use advanced features easily
""")

# ---------------- What is an External Library ----------------
print("\n===== WHAT IS AN EXTERNAL LIBRARY =====")
print("""
An external library is a collection of code
written by others that we can use in our program.

Examples:
✔ requests → for APIs
✔ numpy → for numerical computing
✔ pandas → for data analysis
✔ matplotlib → for visualization
""")

# ---------------- Why Use External Libraries ----------------
print("\n===== WHY USE EXTERNAL LIBRARIES =====")
print("""
Without libraries:
✔ We write everything from scratch

With libraries:
✔ Use ready-made solutions
✔ Faster development
✔ Fewer bugs

Example:
Instead of writing HTTP logic → use requests
""")

# ---------------- What is pip ----------------
print("\n===== WHAT IS pip =====")
print("""
pip is Python's package manager.

Used to:
✔ Install libraries
✔ Update libraries
✔ Remove libraries

Think of pip as:
👉 App Store for Python
""")

# ---------------- Installing Libraries ----------------
print("\n===== INSTALLING LIBRARIES =====")
print("""
Command:

pip install library_name

Example:
pip install requests
pip install numpy

This downloads and installs the library.
""")

# ---------------- Checking Installed Libraries ----------------
print("\n===== CHECK INSTALLED LIBRARIES =====")
print("""
Command:

pip list

Shows all installed packages.
""")

# ---------------- Upgrading Libraries ----------------
print("\n===== UPGRADING LIBRARIES =====")
print("""
Command:

pip install --upgrade library_name
""")

# ---------------- Uninstalling Libraries ----------------
print("\n===== UNINSTALLING LIBRARIES =====")
print("""
Command:

pip uninstall library_name
""")

# ======================================================
# EXAMPLE 1: requests LIBRARY (API CALL)
# ======================================================

print("\n===== EXAMPLE: requests LIBRARY =====")
print("""
WHAT:
Used to make HTTP requests

WHEN:
✔ APIs
✔ Web data fetching
✔ Backend services
""")

print("""
Example (requires installation):

pip install requests
""")

print("""
Code:

import requests
response = requests.get("https://api.github.com")
print(response.status_code)
""")

# ======================================================
# EXAMPLE 2: numpy LIBRARY
# ======================================================

print("\n===== EXAMPLE: numpy LIBRARY =====")
print("""
WHAT:
Numerical computing library

WHEN:
✔ Scientific computing
✔ Data analysis
✔ Machine learning
""")

print("""
Example:

pip install numpy

import numpy as np
arr = np.array([1, 2, 3])
print(arr * 2)
""")

# ======================================================
# EXAMPLE 3: pandas LIBRARY
# ======================================================

print("\n===== EXAMPLE: pandas LIBRARY =====")
print("""
WHAT:
Data analysis library

WHEN:
✔ Working with CSV/Excel
✔ Data cleaning
✔ Data processing
""")

print("""
Example:

pip install pandas

import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
""")

# ======================================================
# HOW TO USE EXTERNAL LIBRARIES
# ======================================================

print("\n===== HOW TO USE EXTERNAL LIBRARIES =====")
print("""
Steps:

1️⃣ Install library using pip
2️⃣ Import library in code
3️⃣ Use its functions

Example:

pip install random-user-agent

import random_user_agent
""")

# ======================================================
# WHEN TO USE EXTERNAL LIBRARIES
# ======================================================

print("\n===== WHEN TO USE EXTERNAL LIBRARIES =====")
print("""
Use external libraries when:

✔ Task is complex
✔ Already solved by others
✔ Needs performance optimization

Do NOT use when:
✔ Simple logic can be written easily
✔ Learning fundamentals
""")

# ======================================================
# REAL-WORLD USE CASES
# ======================================================

print("\n===== REAL-WORLD USE CASES =====")
print("""
✔ Web scraping → requests, BeautifulSoup
✔ Data science → numpy, pandas
✔ Machine learning → scikit-learn, tensorflow
✔ Web apps → Django, Flask
✔ Visualization → matplotlib, seaborn
""")

# ======================================================
# IMPORTANT NOTES
# ======================================================

print("\n===== IMPORTANT NOTES =====")
print("""
✔ Always install trusted libraries
✔ Read documentation before use
✔ Keep libraries updated
✔ Use virtual environments
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ External libraries extend Python
✔ pip is used to manage libraries
✔ Install → import → use
✔ Saves time and effort
✔ Used in real-world applications

Python ecosystem = very powerful
""")