# How do you store password and credentials in the framework? .env file For eg: I am testing a login page If we store
# username and password into our code, this is the worst thing and anyone can see these credentials, if there is
# public repository, will see your username. If there is a hacker, hacker can see your username and password. That's
# why we create a .env file.
# def test_login():
# username = "Admin"  # Hard code
# password = "Password"  # Hard code
# assert username == "Admin"
# assert username == "Admin"
# instead of above code, we will install "pip install python-dotenv"

from dotenv import load_dotenv
import os


def test_login():
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    print(username, password)

