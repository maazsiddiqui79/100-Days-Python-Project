import random
from os import system
import time
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

spin_result_str = ""
balance = 0
condi = False
win_prize = 0

def show_spinner_animation(x):
    print(Fore.YELLOW + x)
    time.sleep(0.7)
    system("cls")

print(Fore.CYAN + "🎰 Welcome to the Lucky Spin Slot Machine! 🎰")
try:
    user_ip = int(input(Fore.GREEN + "💰 Enter your Balance: $"))
except:
    system("cls")
    print(Fore.RED + "🚫 I N V A L I D       I N P U T 🚫")
else:
    balance += user_ip

def spinn():
    global spin_result_str, balance, win_prize, condi
    win_prize = 0
    symbol_lst = ["🍒", "💎", "🔔", "⭐", "7️⃣"]

    weights_dict = {"🍒": 8, "💎": 4, "🔔": 8, "⭐": 8, "7️⃣": 3}
    weights = [weights_dict[i] for i in symbol_lst]

    spin_result = random.choices(symbol_lst, k=3, weights=weights)
    spin_result_str = "  | ".join(spin_result)

    if spin_result[0] == spin_result[1] == spin_result[2]:
        if spin_result[0] == "7️⃣":
            win_prize = 1000
        else:
            win_prize = 750

    elif spin_result.count("7️⃣") == 1:
        win_prize = 570
    elif spin_result.count("7️⃣") == 2:
        win_prize = 670
    elif (spin_result.count("🍒") == 2 or
          spin_result.count("⭐") == 2 or
          spin_result.count("🔔") == 2 or
          spin_result.count("💎") == 2):
        win_prize = 500
    else:
        condi = True

    balance += win_prize

while True:
    spinn()

    if condi:
        system("cls")
        show_spinner_animation("🎡 SPINNING.")
        
        print(Fore.RED + "+-------+--------+")
        print(Fore.RED + f"| {spin_result_str}  |")
        print(Fore.RED + "+-------+--------+")
        print(Fore.RED + "😢 Better luck next time! You Lose")
        print(Fore.RED + "Balance: $0")
        exit()
    else:
        system("cls")
        show_spinner_animation("🎡 SPINNING.")
        show_spinner_animation("🎡 SPINNING..")
        show_spinner_animation("🎡 SPINNING...")

        print(Fore.MAGENTA + "✨ Slot Outcome ➤ ")
        print(Fore.CYAN + "+-------+--------+")
        print(Fore.CYAN + f"| {spin_result_str}  |")
        print(Fore.CYAN + "+-------+--------+")
        print(Fore.GREEN + f"🎉 Hurray!! You Win ${win_prize}")
        print(Fore.YELLOW + f"💵 Balance: ${balance}")
        
    tp = input(Fore.BLUE + "🔁 Do you want to Withdraw or Spin again [y/n]: ")

    if tp.lower() == "y":
        print(Fore.GREEN + f"🎉 Congratulations! You’re walking away with a total of ${balance} from the Lucky Spin Slot Machine! 🎉")
        exit()
    else:
        system("cls")
        if balance < 100:
            print(Fore.RED + "🚫 You're out of balance!")
            exit()
        balance -= 100
        show_spinner_animation(Fore.RED + "💸 -100 for Spinning again.")
        show_spinner_animation(Fore.RED + "💸 -100 for Spinning again..")
