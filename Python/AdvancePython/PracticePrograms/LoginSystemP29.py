# Program: Login System with Lockout

class LoginSystem:
    def __init__(self):
        self.correct_password = "admin123"
        self.attempts = 0

    def login(self):
        try:
            if self.attempts >= 3:
                raise Exception("Account locked!")

            password = input("Enter password: ")

            if password != self.correct_password:
                self.attempts += 1
                raise ValueError("Incorrect password!")

            print("Login successful!")
            self.attempts = 0

        except ValueError as ve:
            print("Error:", ve)
            print("Attempts left:", 3 - self.attempts)

        except Exception as e:
            print("Error:", e)


system = LoginSystem()

for _ in range(5):
    system.login()