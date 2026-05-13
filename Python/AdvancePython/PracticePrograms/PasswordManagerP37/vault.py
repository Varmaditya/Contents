# vault.py

class Vault:
    def __init__(self):
        self.passwords = {}

    def save(self, website, password):
        self.passwords[website] = password

    def show(self):
        for site, pwd in self.passwords.items():
            print(site, "->", pwd)