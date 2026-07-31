# auth.py

from database import users


def register(username, email, balance, password):
    account = max(users.keys()) + 1

    users[account] = {
        "name": username,
        "email": email,
        "balance": balance,
        "password": password
    }

    return f"Registration Successful.\nYour Account Number is {account}"


def login(account, password):
    if account in users:
        return users[account]["password"] == password
    return False