# users/Employee.py

from users.User import User


class Employee(User):

    def __init__(self, user_id, name, username, password, designation="Employee"):
        super().__init__(user_id, name, username, password)

        self.designation = designation
        self.role = "EMPLOYEE"

    # Display Employee Details
    def display_info(self):
        super().display_info()

        print("Designation:", self.designation)
        print("Role:", self.role)

    # Convert Object To Dictionary
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "designation": self.designation,
            "role": self.role
        }
