import time
from colorama import init, Fore, Style
from os import system

init(autoreset=True)  # Auto reset color after each print

total_seconds = 0  # Total countdown time in seconds

try:
    user_input = str(input("Enter countdown (HH:MM:SS): "))
except ValueError:
    print(Fore.RED + "Invalid input!")
else:
    time_parts = user_input.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    total_seconds += hours * 3600 + minutes * 60 + seconds

print(Fore.GREEN + f"⏳ Countdown Started: {user_input}")
while total_seconds != 0:
    system("cls")
    hr = total_seconds // 3600
    min = (total_seconds % 3600) // 60
    sec = total_seconds % 60

    hr = f"0{hr}" if hr < 10 else str(hr)
    min = f"0{min}" if min < 10 else str(min)
    sec = f"0{sec}" if sec < 10 else str(sec)

    print(Fore.CYAN + f"Time Left       {hr}:{min}:{sec}")
    total_seconds -= 1
    time.sleep(1)

print(Fore.YELLOW + Style.BRIGHT + "⏰ Countdown Completed!")
