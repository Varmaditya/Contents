# SCOPE & NAMESPACE (LEGB RULE)
# MUTABLE vs IMMUTABLE ARGUMENTS
# --------------------------------------------------

# ---------------- Introduction ----------------
print("\n===== SCOPE & NAMESPACE IN PYTHON =====")
print("""
Scope defines where a variable can be accessed.
Namespace is a container that holds variable names.

Python follows the LEGB rule to resolve variable names:
L → Local
E → Enclosing
G → Global
B → Built-in
""")

# ---------------- Built-in Scope ----------------
print("\n===== BUILT-IN SCOPE =====")
print("""
Built-in scope contains names that are always available in Python,
like print(), len(), sum(), type(), etc.
""")

print("Length of 'Python' using built-in len():", len("Python"))
print("Maximum of numbers using built-in max():", max(10, 50, 30))

# ---------------- Global Scope ----------------
print("\n===== GLOBAL SCOPE =====")

x = 100  # global variable

def show_global():
    print("Accessing global variable x inside function:", x)

show_global()
print("Accessing global variable x outside function:", x)

# ---------------- Local Scope ----------------
print("\n===== LOCAL SCOPE =====")

def local_example():
    y = 50  # local variable
    print("Inside function, local y:", y)

local_example()
# print(y)  # Uncommenting this line will cause an error

print("""
Local variables exist only inside the function.
They are destroyed after the function execution ends.
""")

# ---------------- Enclosing Scope ----------------
print("\n===== ENCLOSING SCOPE =====")

def outer_function():
    msg = "Hello from outer function"

    def inner_function():
        print("Accessing enclosing variable:", msg)

    inner_function()

outer_function()

print("""
Enclosing scope exists in nested functions.
The inner function can access variables of the outer function.
""")

# ---------------- LEGB Rule Demonstration ----------------
print("\n===== LEGB RULE DEMONSTRATION =====")

var = "Global value"

def outer():
    var = "Enclosing value"

    def inner():
        var = "Local value"
        print("Inner function var:", var)

    inner()
    print("Outer function var:", var)

outer()
print("Global scope var:", var)

# ---------------- global Keyword ----------------
print("\n===== USING global KEYWORD =====")

count = 10

def modify_global():
    global count
    count = count + 5
    print("Inside function, modified global count:", count)

modify_global()
print("Outside function, global count:", count)

print("""
Without the global keyword, Python treats variables inside functions as local.
""")

# ---------------- nonlocal Keyword ----------------
print("\n===== USING nonlocal KEYWORD =====")

def bank_account():
    balance = 1000

    def withdraw(amount):
        nonlocal balance
        balance -= amount
        print("Balance after withdrawal:", balance)

    withdraw(200)
    withdraw(300)

bank_account()

print("""
nonlocal allows modification of variables from enclosing (outer) functions.
""")

# ======================================================
# MUTABLE vs IMMUTABLE ARGUMENTS
# ======================================================

print("\n===== MUTABLE vs IMMUTABLE ARGUMENTS =====")
print("""
Immutable objects cannot be changed:
int, float, string, tuple

Mutable objects can be changed:
list, dictionary, set
""")

# ---------------- Immutable Argument Example ----------------
print("\n===== IMMUTABLE ARGUMENT EXAMPLE =====")

def change_number(num):
    print("Inside function before change:", num)
    num = num + 10
    print("Inside function after change:", num)

x = 50
print("Before function call, x:", x)
change_number(x)
print("After function call, x:", x)

print("""
Integers are immutable.
Changes inside the function do NOT affect the original value.
""")

# ---------------- Mutable Argument Example (List) ----------------
print("\n===== MUTABLE ARGUMENT EXAMPLE (LIST) =====")

def add_item(items):
    print("Inside function before append:", items)
    items.append("New Item")
    print("Inside function after append:", items)

my_list = ["Apple", "Banana"]
print("Before function call:", my_list)
add_item(my_list)
print("After function call:", my_list)

print("""
Lists are mutable.
Changes inside the function affect the original list.
""")

# ---------------- Mutable Argument Example (Dictionary) ----------------
print("\n===== MUTABLE ARGUMENT EXAMPLE (DICTIONARY) =====")

def update_marks(marks):
    marks["Maths"] = 95

student_marks = {"English": 88, "Science": 90}
print("Before update:", student_marks)
update_marks(student_marks)
print("After update:", student_marks)

# ---------------- Avoiding Side Effects ----------------
print("\n===== AVOIDING SIDE EFFECTS (COPYING MUTABLE DATA) =====")

def safe_update(items):
    items_copy = items.copy()
    items_copy.append("Safe Item")
    print("Inside function (copy):", items_copy)

original_list = ["A", "B", "C"]
print("Before function call:", original_list)
safe_update(original_list)
print("After function call:", original_list)

print("""
To avoid modifying original data,
always work on a copy of mutable objects.
""")

# ---------------- Practical Example ----------------
print("\n===== PRACTICAL EXAMPLE: STUDENT SCORE SYSTEM =====")

total_score = 0  # global variable

def add_score(scores):
    global total_score
    total_score += sum(scores)
    scores.append(100)  # mutable change

marks = [70, 80, 90]

print("Initial marks:", marks)
print("Initial total score:", total_score)

add_score(marks)

print("Marks after function:", marks)
print("Total score after function:", total_score)

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("""
✔ Scope defines where variables are accessible
✔ Python follows LEGB rule:
   Local → Enclosing → Global → Built-in
✔ global keyword modifies global variables
✔ nonlocal keyword modifies enclosing variables
✔ Immutable arguments do NOT change original values
✔ Mutable arguments CAN change original data
✔ Use copies to avoid unintended side effects

Understanding scope and mutability is CRITICAL
for debugging, advanced functions, and large systems.
""")