import random
from os import system
from colorama import init, Fore, Style

init(autoreset=True)

def sum(a, b, c):
    return a + b + c

def print_board(xState, oState):
    one =   Fore.RED + 'X' + Style.RESET_ALL if xState[0] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[0] else '1')
    two =   Fore.RED + 'X' + Style.RESET_ALL if xState[1] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[1] else '2')
    three = Fore.RED + 'X' + Style.RESET_ALL if xState[2] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[2] else '3')
    four =  Fore.RED + 'X' + Style.RESET_ALL if xState[3] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[3] else '4')
    five =  Fore.RED + 'X' + Style.RESET_ALL if xState[4] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[4] else '5')
    six =   Fore.RED + 'X' + Style.RESET_ALL if xState[5] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[5] else '6')
    seven = Fore.RED + 'X' + Style.RESET_ALL if xState[6] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[6] else '7')
    eight = Fore.RED + 'X' + Style.RESET_ALL if xState[7] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[7] else '8')
    nine =  Fore.RED + 'X' + Style.RESET_ALL if xState[8] == 1 else (Fore.GREEN + 'O' + Style.RESET_ALL if oState[8] else '9')
    
    print(Fore.LIGHTBLUE_EX +f' {one} | {two} | {three} ')
    print(Fore.LIGHTBLUE_EX +f'---|---|---')
    print(Fore.LIGHTBLUE_EX +f' {four} | {five} | {six} ')
    print(Fore.LIGHTBLUE_EX +f'---|---|---')
    print(Fore.LIGHTBLUE_EX +f' {seven} | {eight} | {nine} ')

def check_win(xState, oState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in wins:
        if sum(xState[i[0]] , xState[i[1]] , xState[i[2]]) == 3:
            print_board(xState, oState)
            print(Fore.MAGENTA + '~~~~~~~~~~~~~~~~ X WINS MATCH ~~~~~~~~~~~~~~~~')
            exit()
        if sum(oState[i[0]] , oState[i[1]] , oState[i[2]]) == 3:
            print_board(xState, oState)
            print(Fore.MAGENTA + '~~~~~~~~~~~~~~~~ O WINS MATCH ~~~~~~~~~~~~~~~~')
            exit()

xState = [0,0,0,0,0,0,0,0,0]
oState = [0,0,0,0,0,0,0,0,0]
turn = 1

print(Fore.CYAN + f'WELCOME TO TIC TAC TOE')
while True:
    system('cls')  # use 'clear' if on Linux/macOS
    check_win(xState=xState, oState=oState)
    print_board(xState, oState)
    
    if turn == 1:
        print(Fore.YELLOW + 'X\'s Chance')
        value = int(input('Enter a number: '))
        try:
            if xState[value - 1] == 0 and oState[value - 1] == 0:
                turn = 2
                xState[value - 1] = 1
            else:
                print(Fore.RED + "Invalid move! Cell already taken. Try again.")
        except Exception:
            print(Fore.RED + 'Enter a valid number')
    else:
        print(Fore.YELLOW + 'O\'s Chance')
        value = int(input('Enter a number: '))
        try:
            if xState[value - 1] == 0 and oState[value - 1] == 0:
                turn = 1
                oState[value - 1] = 1
            else:
                print(Fore.RED + "Invalid move! Cell already taken. Try again.")
        except Exception:
            print(Fore.RED + 'Enter a valid number')

    if (xState + oState) == 9:
        print_board(xState, oState)
        print(Fore.MAGENTA + "~~~~~~~~~~~~~~~~ MATCH DRAW ~~~~~~~~~~~~~~~~")
        exit()
