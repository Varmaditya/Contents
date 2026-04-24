# Program: Secure Login System

def login_system():
    """
    Simulates a login system using nested functions.
    Shows namespace and variable scope.
    """

    correct_username = "admin"
    correct_password = "1234"

    def validate(username: str, password: str) -> bool:
        # Inner function accessing outer variables (namespace concept)
        return username == correct_username and password == correct_password

    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate(username, password):
        print("Login successful!")
    else:
        print("Invalid credentials!")


login_system()