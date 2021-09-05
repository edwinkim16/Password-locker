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

def main():
    """
    This is where the user will run all their functions
    """    


