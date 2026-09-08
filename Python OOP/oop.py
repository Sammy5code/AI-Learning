# Accessing and modifying data:
# 1. The traditional way: make the data private and use 
# getters and setters:
# 2. Properties


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email Accessed")
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("datheman", "Dan@gmail.com", "123")
user1.email = "this@gmail.com"
print(user1.email)
