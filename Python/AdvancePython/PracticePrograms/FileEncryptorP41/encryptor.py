# encryptor.py

import base64
import os


class Encryptor:

    def encrypt_file(self, filename):

        try:
            with open(filename, "rb") as file:
                data = file.read()

            encrypted = base64.b64encode(data)

            new_name = "encrypted_" + filename

            with open(new_name, "wb") as file:
                file.write(encrypted)

            print("Encrypted file created:", new_name)

        except FileNotFoundError:
            print("File not found!")

    def decrypt_file(self, filename):

        try:
            with open(filename, "rb") as file:
                data = file.read()

            decrypted = base64.b64decode(data)

            new_name = "decrypted_" + filename

            with open(new_name, "wb") as file:
                file.write(decrypted)

            print("Decrypted file created:", new_name)

        except Exception as e:
            print("Error:", e)
