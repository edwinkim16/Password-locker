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

def view_passwords():
    """
    A function that will allow the user to view all the passwords
    """
    return Password.display_passwords()


def delete_password(acc):
    """
    This is a function that will delete the password
    Args:
        acc - the acc of the pass the user wants to delete
    """
    Password.delete_password(acc)

def password_exists(acc):
    """
    It will check whether a password exists
    Args:
        acc- the password's account
    Return:
        True or False
    """
    return Password.password_exist(acc)


def main():
    """
    This is where the user will run all their functions
    """   
    print("\n")
    print("Welcome to PASSWORD LOCKER. We help you manage your passwords so that you can worry about things that matter\n")
    print("-"*6, "SIGN UP", "-"*6, "\n") 

    user_name = input("User Name\n")
    user_pass = getpass.getpass('Password:\n')



