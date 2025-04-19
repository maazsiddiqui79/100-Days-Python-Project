import random
from os import system

dice = ["""
┌───────┐
│       │
│   ●   │  
│       │
└───────┘
""",
"""
┌───────┐
│ ●     │
│       │  
│     ● │
└───────┘
""",
"""
┌───────┐
│ ●     │
│   ●   │  
│     ● │
└───────┘
""",
"""
┌───────┐
│ ●   ● │
│       │  
│ ●   ● │
└───────┘
""",

"""
┌───────┐
│ ●   ● │
│   ●   │  
│ ●   ● │
└───────┘
""",

"""
┌───────┐
│ ●   ● │
│ ●   ● │  
│ ●   ● │
└───────┘
""" ]

while True:
    up =input("'y' to roll the dice 'n' to exit :").lower()
    system('cls')
    if up == "y":
        print(random.choice(dice))
    else: exit