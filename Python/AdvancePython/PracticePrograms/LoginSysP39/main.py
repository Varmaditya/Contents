# main.py for login system

from user import User
from security import SecuritySystem

user = User("admin", "1234")

system = SecuritySystem()

for _ in range(3):
    system.login(user)