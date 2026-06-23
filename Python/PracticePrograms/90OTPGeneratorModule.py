# Program: OTP Generator using random Module
# Modules help us use ready-made tools in Python.
# 'random' module is used to generate random numbers.

print("===== OTP GENERATOR (using random module) =====")

import random

def generate_otp(length):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))   # generate a single random digit
    return otp

length = int(input("Enter OTP length (4-8): "))

if 4 <= length <= 8:
    print("Generated OTP:", generate_otp(length))
else:
    print("Invalid length! Enter between 4 and 8.")
