# Create a User class with private password and a method to validate login.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password # Private attribute

    def login(self, input_password):
        if self.__password == input_password:
            print(f"Login successful! Welcome, {self.username}.")
            return True
        else:
            print("Login failed. Incorrect password.")
            return False

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Cannot change password. Old password incorrect.")

# Testing the class
user1 = User("admin", "secret123")

# Attempt login
user1.login("wrongpass")
user1.login("secret123")

# Attempt to access private variable directly (will fail or show name mangling)
try:
    print(user1.__password)
except AttributeError:
    print("Cannot access private attribute '__password' directly.")
