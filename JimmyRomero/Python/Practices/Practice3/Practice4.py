import re


def ask_user_name():
    user_name = input("Insert user name: ")
    if re.fullmatch("^[a-z0-9_]*$", user_name):
        print("Valid username")
    else:
        print("Invalid username")


def ask_password():
    password = input("Insert password: ")
    if re.fullmatch("^[a-zA-Z0-9_]{8,16}$", password):
        print("Valid password")
    else:
        print("Invalid password")


def ask_email():
    email = input("Insert email: ")
    if re.fullmatch("^[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$|^[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}\.[a-z]{2,3}$", email):
        print("Valid email")
    else:
        print("Invalid email")


ask_user_name()
ask_password()
ask_email()
