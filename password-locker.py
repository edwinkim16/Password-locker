from random import random


class Password: 
    """
    Create your paswords here
    """
    password_list = []  # list to store user  passwords

    def _init_(self, account, username, password):
        """
        Allow the user to create instances of the class with unique details 
        """
        self.account = account
        self.username = username
        self.password = password

    def save_password(self):
        """
        This function will add users password to the password array
        """
        Password.password_list.append(self)    