# users/Customer.py

from users.User import User

class Customer(User):

    def __init__(self, user_id, name, username, password, phone, email):
        super().__init__(user_id, name, username, password)

        self.phone = phone
        self.email = email
        self.role = "CUSTOMER"

    # Display Customer Information
    def display_info(self):
        super().display_info()

        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Role:", self.role)

    # Convert Object To Dictionary
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "phone": self.phone,
            "email": self.email,
            "role": self.role
        }
