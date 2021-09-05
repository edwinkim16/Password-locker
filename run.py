#!/usr/bin/env python3.6
from Password_Locker import Password
from user import User
import getpass  # to hide the pass

def new_user(login, password):
    """
    This will create a new user every time they login
    Args:
        login - user name
        password - the user's password
    Return:
        the new user instance
    """
    user = User(login, password)
    return user

def add_password(password):
    """
    This is a function that will add a new password to the passwords list
    """
    
    Password.save_password(password)


def generate_password(length):
    """
    This will create a random password for the user
    Args:
        length - the user's preferred length for the password
    Return:
        It will return a random password of user's preferred length
    """
    return Password.generate_pass(length)



def main():
    """
    This is where the user will run all their functions
    """    


