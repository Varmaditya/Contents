# Python Program: Type Conversion

# ---------------- IMPLICIT CONVERSION ----------------
print("----- Implicit Type Conversion -----")
num_int = 10       # int
num_float = 3.5    # float

# Python automatically converts int → float in this expression
result = num_int + num_float

print("Value of result:", result)
print("Type of result:", type(result))   # float


# ---------------- EXPLICIT CONVERSION ----------------
print("\n----- Explicit Type Conversion -----")

# Converting float to int (manual)
float_num = 9.99
int_num = int(float_num)   # decimal part will be removed
print("Float:", float_num, "| After int():", int_num)

# Converting int to string
age = 21
age_str = str(age)
print("Integer:", age, "| After str():", age_str, "| Type:", type(age_str))

# Converting string to float
str_number = "45.67"
float_number = float(str_number)
print("String:", str_number, "| After float():", float_number, "| Type:", type(float_number))
