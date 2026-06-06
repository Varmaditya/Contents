# users/User.py

class User:

    def __init__(self, user_id, name, username, password):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password

    # Display User Information
    def display_info(self):
        print("\n===== USER INFO =====")

        print("ID:", self.user_id)
        print("Name:", self.name)
        print("Username:", self.username)

    # Convert Object To Dictionary
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
            "password": self.password
        }

    # String Representation
    def __str__(self):
        return f"{self.user_id} | {self.name}"
