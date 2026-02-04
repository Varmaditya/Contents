# SCOPE & NAMESPACE (LEGB RULE)
# MUTABLE vs IMMUTABLE ARGUMENTS
# ---------------------------------------------

print("\n===== SCOPE & NAMESPACE (LEGB) =====")

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print("Inside inner():", x)

    inner()
    print("Inside outer():", x)

outer()
print("Outside functions:", x)

print("\n===== GLOBAL KEYWORD =====")

count = 10

def modify_global():
    global count
    count += 5

modify_global()
print("Modified global count:", count)

print("\n===== MUTABLE vs IMMUTABLE ARGUMENTS =====")

def change_number(n):
    n += 10
    print("Inside function (immutable):", n)

def modify_list(lst):
    lst.append(100)
    print("Inside function (mutable):", lst)

num = 50
data = [1, 2, 3]

print("\nBefore function call:")
print("num =", num)
print("data =", data)

change_number(num)
modify_list(data)

print("\nAfter function call:")
print("num =", num)
print("data =", data)
