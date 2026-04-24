# Program: Username Generator

def create_username_generator(domain):
    """Generates usernames with fixed domain"""

    def generate(name: str) -> str:
        name = name.lower().replace(" ", "")
        return name + "@" + domain

    return generate


gmail_gen = create_username_generator("gmail.com")
company_gen = create_username_generator("company.com")

name = input("Enter your name: ")

print("Gmail Username:", gmail_gen(name))
print("Company Username:", company_gen(name))