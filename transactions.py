# transactions.py

from database import users


def get_balance(account):
    return f"Current Balance: {users[account]['balance']}"


def withdraw(account, amount):
    if users[account]["balance"] >= amount:
        users[account]["balance"] -= amount
        return (
            f"{amount} withdrawn successfully.\n"
            f"Current Balance: {users[account]['balance']}"
        )
    return "Insufficient Balance"


def deposit(account, amount):
    users[account]["balance"] += amount
    return (
        f"{amount} deposited successfully.\n"
        f"Current Balance: {users[account]['balance']}"
    )


def transfer(from_acc, to_acc, amount):
    if to_acc not in users:
        return "Receiver Account Not Found"

    if users[from_acc]["balance"] >= amount:
        users[from_acc]["balance"] -= amount
        users[to_acc]["balance"] += amount

        return (
            f"{amount} transferred successfully.\n"
            f"Sender Balance: {users[from_acc]['balance']}\n"
            f"Receiver Balance: {users[to_acc]['balance']}"
        )

    return "Insufficient Balance"