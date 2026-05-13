# generator.py

import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits

    password = ""

    for _ in range(8):
        password += random.choice(chars)

    return password