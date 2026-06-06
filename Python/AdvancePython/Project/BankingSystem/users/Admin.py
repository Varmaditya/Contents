from users.User import User

class Admin(User):

    def __init__(self, user_id, name, username, password):
        super().__init__(user_id, name, username, password)
        self.role = "ADMIN"

    # Display Role
    def display_role(self):
        print("Role:", self.role)

    # Convert Object To Dictionary
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }
