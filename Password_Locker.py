from random import random


class Password: 
    """
    Create your paswords here
    """
    password_list = []  # list to store user  passwords

    def __init__(self, account, username, password):
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

    def display_passwords(self):
        """
        This function returns all passwords on the list
        """
        return self.password_list   

    @classmethod
    def delete_password(self):
        """
        This function will delete the users password in the list
        Args:
            this is the account of the password the user wants to delete
        """
        Password.password_list.remove(self)
        # for password in password_list:
        #     if password.account.lower() == account.lower():
        #         cls.password_list.remove(password)

    @classmethod
    def password_exist(cls, account):
        """
        This function checks weather the password of the account exist
        Args:
            acc- this is the acount which user wants to confirm if its password exist
        return:
            True or False
        """
        for password in cls.password_list:
            if password.account.lower() == account.lower():
                return True

            return False            