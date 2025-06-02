print("""
     

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""/"--=_ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._    =. '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* """)
print()
print("Welcome to TreasureIsland".center(80,"*"))
print("Your mission is to find the treasure.")
direction=input("You're at a crossroads. Which direction would you like to take?\n\tType \"left\" or \"right\".")

if direction.lower() == "left":
    Decision=input("\nYou've come to a lake.\nThere is an island in the middle of the lake.Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    
    if Decision.lower() == "wait":
        Door=input("\nYou arrive at the island unharmed. There is a house with 3 doors.  \nOne red, one yellow and one blue. Which colour do you choose?")
        
        if Door.lower() == "yellow":
            print("\nYou Win! \n \t\tTHE TREASURE")
        elif Door.lower() == "red":
            print("\nBurned by fire.    Game Over.")
        elif Door.lower() == "blue":
            print("\nEaten by beasts.    Game Over.")
        else:
            print("\nGame Over!")
        
    else:
        print("\nAttacked by trout.\nGame Over.")
        exit()
        
    
else:
    print("\nFall into a hole.\nGame Over.")
    exit()