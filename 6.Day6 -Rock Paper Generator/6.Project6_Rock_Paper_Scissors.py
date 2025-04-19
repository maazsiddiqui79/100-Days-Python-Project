import random
from os import system

# ASCII Art for Rock, Paper, Scissors
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

# Score variables
c_score = 0  # Computer score
score = 0  # Player score
p1_scr = 0  # Player 1 score (Multiplayer)
p2_scr = 0  # Player 2 score (Multiplayer)


def comp():
    """Handles the single-player mode where the player competes against the computer."""
    global score
    global c_score
    
    # Check if player or computer has won the game
    if score >= 5:
        system("cls")  # Clear the screen (Windows-specific command)
        print(f"🏆 You Win 🏆 {score} 🏆")
        exit()
        
    if c_score >= 5:
        system("cls")
        print(f"🏆 Computer Wins By 🏆 {c_score} 🏆")
        exit()
        
    # User input
    print("Enter your choice:")
    user_ip1 = int(input("Type 1. ROCK 🪨\t2. PAPER 📄\t3.SCISSORS ✂️\t4.EXIT: 👋\t"))

    # Display user choice
    if user_ip1 == 1:
        print("You Choose: 🪨")
        print(rock)
    elif user_ip1 == 2:
        print("You Choose: 📄")
        print(paper)
    elif user_ip1 == 3:
        print("You Choose: ✂️")
        print(scissor)
    elif user_ip1 == 4:
        print("Good Bye 👋")
        exit()
    else:
        print("Invalid input ❌")
        return
    
    # Computer choice
    print("Computer Choose:")
    computer_ip = random.randint(1, 3)
    if computer_ip == 1:
        print("🪨")
        print(rock)
    elif computer_ip == 2:
        print("📄")
        print(paper)
    else:
        print("✂️")
        print(scissor)
        
    # Determine winner
    if user_ip1 == computer_ip:
        print("🤝 DRAW 🤝")
    elif (user_ip1 == 1 and computer_ip == 3) or (user_ip1 == 2 and computer_ip == 1) or (user_ip1 == 3 and computer_ip == 2):
        print("🏆 YOU WIN 🏆")
        score += 2
        c_score -= 1
    else:
        print("😞 YOU LOSE 😞")
        c_score += 2
    
    # Display scores
    print("Your Score: ", score)
    print("Computer Score: ", c_score)

# Game mode selection
game_ip = int(input("1. Multiplayer 🎮\t2. Single player 💻\t3. Exit 👋 :\t"))
if game_ip == 1:
    player1_name = input("Enter Player 1 Name: 🎭")
    player2_name = input("Enter Player 2 Name: 🎭")

# Game loop
while True:
    if game_ip == 1:
        # Multiplayer mode logic
        
        # Check if any player has won
        if p1_scr >= 5:
            system("cls")
            print(f"🏆 {player1_name} Wins By 🏆 {p1_scr} 🏆")
            exit()
        if p2_scr >= 5:
            system("cls")
            print(f"🏆 {player2_name} Wins By 🏆 {p2_scr} 🏆")
            exit()
            
        # Player 1 choice
        print(f"\n{player1_name} choice".upper())
        user_ip1 = int(input("Type 1. ROCK 🪨\t2. PAPER 📄\t3.SCISSORS ✂️:\t"))
        system("cls")
        
        # Player 2 choice
        print(f"\n{player2_name} choice".upper())
        user_ip2 = int(input("Type 1. ROCK 🪨\t2. PAPER 📄\t3.SCISSORS ✂️:\t"))
        system("cls")
        
        # Display choices
        if user_ip1 == 1:
            print(f"{player1_name} 🪨")
            print(rock)
        elif user_ip1 == 2:
            print(f"{player1_name} 📄")
            print(paper)
        elif user_ip1 == 3:
            print(f"{player1_name} ✂️")
            print(scissor)
        else:
            print("Invalid input ❌")
            continue
            
        if user_ip2 == 1:
            print(f"{player2_name} 🪨")
            print(rock)
        elif user_ip2 == 2:
            print(f"{player2_name} 📄")
            print(paper)
        elif user_ip2 == 3:
            print(f"{player2_name} ✂️")
            print(scissor)
        else:
            print("Invalid input ❌")
            continue
            
        # Determine winner
        if user_ip1 == user_ip2:
            print("🤝 DRAW 🤝")
        elif (user_ip1 == 1 and user_ip2 == 3) or (user_ip1 == 2 and user_ip2 == 1) or (user_ip1 == 3 and user_ip2 == 2):
            print(f"{player1_name} Wins 🏆")
            p1_scr += 2
            p2_scr -= 1
        else:
            print(f"{player2_name} Wins 🏆")
            p1_scr -= 1
            p2_scr += 2
        
        # Display scores
        print(f"{player1_name} Score: ", p1_scr)
        print(f"{player2_name} Score: ", p2_scr)
        
    elif game_ip == 2:
        comp()
    elif game_ip == 3:
        print("Good Bye 👋")
        break
    else:
        print("Invalid input ❌")
        continue
