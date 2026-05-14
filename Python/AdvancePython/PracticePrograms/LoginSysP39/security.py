# security.py

from logs import write_log

class SecuritySystem:
    def login(self, user):

        try:
            password = input("Enter password: ")

            if password != user.password:
                raise ValueError("Wrong password!")

            print("Access Granted")
            write_log(f"{user.username} logged in successfully")

        except ValueError as ve:
            print("Access Denied:", ve)
            write_log(f"Failed login attempt for {user.username}")