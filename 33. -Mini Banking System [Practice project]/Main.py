# =========================== MINI BANKING SYSTEM =================================================

import datetime
from os import system
from colorama import init, Fore, Back, Style
import pandas as pd
from transaction_filter import FILTER_TRANSACTION
import os

init(autoreset=True)
Balance = 0
password = 1

# Absolute paths to required files
base_path = os.path.dirname(os.path.abspath(__file__))
balance_file = os.path.join(base_path, "Balance.txt")
database_file = os.path.join(base_path, "Database.csv")

# Create Balance.txt if not exists
if not os.path.exists(balance_file):
    with open(balance_file, "w") as f:
        f.write("0")

# Read Balance
with open(balance_file, "r") as f:
    Balance = int(f.read())

def save_balance():
    with open(balance_file, "w") as f:
        f.write(str(Balance))

def authentication():
    return int(input("Enter Password:"))


# =========================== Classes of Menu ======================================================

class Deposit():
    def __init__(self):
        global Balance

        now = datetime.datetime.now()
        date = now.strftime("%d - %m - %Y")
        time = now.strftime("%I:%M:%S:%p")
        self.pass_ip = authentication()

        if self.pass_ip == password:
            try:
                self.deposit_ip = int(input("Enter amount to deposit:"))
            except ValueError:
                print("Enter valid Number")
                return

            if self.deposit_ip <= 0:
                print(Fore.LIGHTRED_EX + Back.BLACK + "❌ Amount must be greater than zero.")
            else:
                Balance += self.deposit_ip
                save_balance()
                print(Fore.GREEN + Back.BLACK + f"✅ Deposited ₹{self.deposit_ip} successfully.")
                init()

                with open(database_file, "a") as f:
                    f.write(f"| Deposit |,{self.deposit_ip},| {time} |,| {date} |\n")
        else:
            print("Incorrect password")


class Withdraw():
    def __init__(self):
        global Balance

        now = datetime.datetime.now()
        date = now.strftime("%d - %m - %Y")
        time = now.strftime("%I:%M:%S:%p")
        self.pass_ip = authentication()

        if self.pass_ip == password:
            try:
                self.withdraw_ip = int(input("Enter amount to withdraw:"))
            except ValueError:
                print("Enter valid Number")
                return

            if self.withdraw_ip <= 0:
                print(Fore.LIGHTRED_EX + Back.BLACK + "❌ Amount must be greater than zero.")
            elif self.withdraw_ip > Balance:
                print(Fore.LIGHTRED_EX + Back.BLACK + "❌ Insufficient funds.")
            else:
                Balance -= self.withdraw_ip
                save_balance()
                print(Fore.RED + Back.BLACK + f"✅ Withdrawn ₹{self.withdraw_ip} successfully.")

                with open(database_file, "a") as f:
                    f.write(f"| Withdraw |,{self.withdraw_ip},| {time} |,| {date} |\n")
        else:
            print("Incorrect password")


class Check_Balance():
    def __init__(self):
        global Balance

        now = datetime.datetime.now()
        date = now.strftime("%d - %m - %Y")
        time = now.strftime("%I:%M:%S:%p")

        self.pass_ip = authentication()

        if self.pass_ip == password:
            print(Fore.CYAN + Back.BLACK + f"💰 Current Balance: ₹{Balance}")
            with open(database_file, "a") as f:
                f.write(f"| Checked Balance |,{Balance},| {time} |,| {date} |\n")
        else:
            print("Incorrect password")


class Transaction_History():
    def __init__(self):
        self.pass_ip = authentication()

        if self.pass_ip == password:
            f = FILTER_TRANSACTION()
        else:
            print("Incorrect password")


class Exit():
    def __init__(self):
        system("cls")
        print("\nThank you for using Mini Banking App. Have a great day!\n")

        save_balance()
        now = datetime.datetime.now()

        print("Date", now.date())
        print("Time", now.time())

        exit()


# =========================== Main Menu Loop ======================================================

print("\nWelcome to Mini Banking App")
print("============================")

input("Enter Account no: ")
input("Enter Password: ")

a = [1, 2, 3, 4, 5]

bank_open = True

while bank_open:
    print("""
    Please select an option:
    1. Deposit
    2. Withdraw
    3. Check Balance
    4. View Transaction History
    5. Exit
    """)

    try:
        user_ip = int(input("\nEnter your choice: "))
    except ValueError:
        print(Fore.RED + Back.BLACK + "    Enter a valid number.    ")
        continue

    if user_ip not in a:
        print(Fore.RED + Back.BLACK + "    Enter a valid Input    ")
        continue

    if user_ip == 1:
        system("cls")
        depo = Deposit()

    elif user_ip == 2:
        system("cls")
        withdrw = Withdraw()

    elif user_ip == 3:
        system("cls")
        chk_bal = Check_Balance()

    elif user_ip == 4:
        system("cls")
        hist = Transaction_History()

    elif user_ip == 5:
        system("cls")
        Ext = Exit()
