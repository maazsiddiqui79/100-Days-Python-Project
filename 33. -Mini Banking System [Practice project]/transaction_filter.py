import pandas as pd
from colorama import init, Fore, Back, Style


init()


class FILTER_TRANSACTION():
    def __init__(self):
        
        data = pd.read_csv("Database.csv")
        
        print("Which type of transaction would you like to display?")
        print("""
1.All Data Transaction
2.Deposits Transaction
3.Withdraw Transaction
4.Check Balance Transaction
5.Summary of Transaction
6.Export Excel DataSheet of Transaction \n""")
        
        
       
        
        transaction_ip =int(input("What would you like to Filter: "))
        
        if transaction_ip == 1 :
            print(Fore.YELLOW+Back.BLACK+"".join(data.columns))
            print(Fore.YELLOW+Back.BLACK+data.to_string(index=False,header=False))
        elif transaction_ip == 2 :
            print(Fore.YELLOW+Back.BLACK+"                    ".join(data.columns))
            print(Fore.YELLOW+Back.BLACK+data[data["| Type |"]=="| Deposit |"].to_string(index=False,header=False))
        elif transaction_ip == 3 :
            print(Fore.YELLOW+Back.BLACK+"                    ".join(data.columns))
            print(Fore.YELLOW+Back.BLACK+data[data["| Type |"]=="| Withdraw |"].to_string(index=False,header=False))
        elif transaction_ip == 4 :
            print(Fore.YELLOW+Back.BLACK+"                    ".join(data.columns))
            print(Fore.YELLOW+Back.BLACK+data[data["| Type |"]=="| Checked Balance |"].to_string(index=False,header=False))
        elif transaction_ip == 5:
            total_deposit = data[data["| Type |"] == "| Deposit |"]["Amount"].sum()
            total_withdraw = data[data["| Type |"] == "| Withdraw |"]["Amount"].sum()
            net_bal = int(total_deposit) - int(total_withdraw)  # If no initial balance

            print("\n---------- Summary ----------")
            print(f"Total Deposits   : ₹{total_deposit}")
            print(f"Total Withdrawals: ₹{total_withdraw}")
            print(f"Net Balance      : ₹{net_bal}")
            print("-----------------------------")
        elif transaction_ip == 6:
            data.to_csv("Transaction History.csv",index=False)
            
            
            