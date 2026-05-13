# PACKAGES & VIRTUAL ENVIRONMENT IN PYTHON
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== PACKAGES IN PYTHON =====")
print("""
A package is a folder containing modules.

Used to organize large projects.
""")

# ---------------- Package Structure ----------------
print("\n===== PACKAGE STRUCTURE =====")
print("""
Example:

project/
    main.py
    utils/
        __init__.py
        math_utils.py
        file_utils.py
""")

print("""
✔ Folder = package
✔ .py files = modules
✔ __init__.py makes it a package
""")

# ---------------- Importing from Packages ----------------
print("\n===== IMPORTING FROM PACKAGES =====")

print("""
Example:

from utils.math_utils import add
""")

print("""
OR

import utils.math_utils
utils.math_utils.add(2, 3)
""")

# ---------------- Why Packages are Needed ----------------
print("\n===== WHY PACKAGES ARE NEEDED =====")
print("""
✔ Organize large codebases
✔ Group related modules
✔ Avoid naming conflicts
✔ Improve readability
""")

# ---------------- Real-World Structure ----------------
print("\n===== REAL-WORLD PROJECT STRUCTURE =====")
print("""
web_app/
    app.py
    models/
    routes/
    utils/
    config/

Large applications always use packages.
""")

# ---------------- Virtual Environment ----------------
print("\n===== VIRTUAL ENVIRONMENT =====")
print("""
A Virtual Environment is an isolated environment
for Python projects.

It allows:
✔ Separate dependencies for each project
✔ Avoid version conflicts
""")

print("""
Example problem:
Project A needs version 1 of a library
Project B needs version 2

Virtual environment solves this.
""")

# ---------------- Creating Virtual Environment ----------------
print("\n===== CREATING VIRTUAL ENVIRONMENT =====")

print("""
Command:

python -m venv myenv

Activate:
Windows → myenv\\Scripts\\activate
Linux/Mac → source myenv/bin/activate
""")

# ---------------- Why Virtual Environment ----------------
print("\n===== WHY VIRTUAL ENVIRONMENT =====")
print("""
✔ Keeps project dependencies isolated
✔ Prevents conflicts
✔ Essential for real-world development
""")

# ---------------- Practical Use Case ----------------
print("\n===== PRACTICAL USE CASE =====")
print("""
Large application:

✔ Uses multiple packages
✔ Uses external libraries
✔ Needs clean structure

Virtual environment + packages = clean system
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Package = folder of modules
✔ __init__.py defines package
✔ Used for organizing large projects
✔ Virtual environment isolates dependencies

These are essential for professional Python development.
""")