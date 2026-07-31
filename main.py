# main.py

from auth import login, register
from transactions import get_balance, withdraw, deposit, transfer
from services import ministatement, logout

print("Welcome to Mini Bank")
print("1. Login")
print("2. Register")

choice = int(input("Enter your choice: "))

if choice == 1:

    account = int(input("Enter Account Number: "))
    password = input("Enter Password: ")

    if login(account, password):

        while True:

            print("\n1. Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Mini Statement")
            print("6. Logout")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                print(get_balance(account))

            elif ch == 2:
                amount = int(input("Enter Amount: "))
                print(withdraw(account, amount))

            elif ch == 3:
                amount = int(input("Enter Amount: "))
                print(deposit(account, amount))

            elif ch == 4:
                receiver = int(input("Enter Receiver Account: "))
                amount = int(input("Enter Amount: "))
                print(transfer(account, receiver, amount))

            elif ch == 5:
                print(ministatement(account))

            elif ch == 6:
                print(logout())
                break

            else:
                print("Invalid Choice")

    else:
        print("Invalid Login Credentials")

elif choice == 2:

    username = input("Enter Username: ")
    email = input("Enter Email: ")
    balance = int(input("Enter Initial Deposit: "))
    password = input("Enter Password: ")

    print(register(username, email, balance, password))

else:
    print("Invalid Choice")