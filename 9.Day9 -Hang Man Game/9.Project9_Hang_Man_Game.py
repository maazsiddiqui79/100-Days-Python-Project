import random

# List of Hangman stages (used to display the hangman step by step when incorrect guesses are made)
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    GAME OVER!
    """
]

# List of possible words for the game
wrd = ["code", "network", "digital", "software", "data", "device", "pixel", "circuit", "internet", "algorithm"]

# Hangman Game Title Banner
print("""
                _                                             
               | |                                            
               | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
               | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
               | | | | (_| | | | | (_| | | | | | | (_| | | | |
               |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                   __/ |                      
                                  |___/        
      """)

# Select a random word from the list
random_wrd = random.choice(wrd)

# Display underscores representing the unknown word
print("Guess the Word:", len(random_wrd) * "_ ")

# print(random_wrd)  # Debugging purpose; remove this line in final version

# Game status variables
game_over = False  # Flag to indicate if the game is over
corrected = []  # List to store correct guesses
life = 7  # Total lives available
a = 0  # Index to track hangman stages

while not game_over:

    display = ""  # Variable to store the word with guessed letters
    user_ip = str(input("Enter a letter: ").lower())  # Taking user input in lowercase

    if user_ip in corrected:
        print(f"YOU ALREADY GUESSED '{user_ip}' ")
    # Loop through each letter in the randomly chosen word
    for i in random_wrd:
        if i == user_ip:  # If the guessed letter is correct
            display += i
            corrected += i  # Add correct letter to the list
        elif i in corrected:  # If the letter was guessed before, display it
            display += i
        else:
            display += "_ "  # Display underscore for missing letters
            corrected += "_"

    # If the guessed letter is NOT in the word
    if user_ip not in random_wrd:
        life -= 1  # Reduce life count
        print(f"YOU GUESSED '{user_ip}' WHICH IS NOT IN THE WORD, YOU LOSE A LIFE -1!")
        print(stages[a])  # Display current Hangman stage
        a += 1  # Move to the next stage
        
        if life == 0:  # If no lives are left, game over
            game_over = True
            print("You Lose".center(150, "*"))  # Display losing message
            exit()

    # If the player already guessed the letter

    # Display the updated word with correct guesses
    print("\tWord to guess:", display)
    
    print(f"{life}/7 LIVES LEFT".center(94, "*"))  # Show remaining lives

    # If the player guesses all letters, they win
    if "_" not in display:
        game_over = True
        print("You Win".center(94, "*"))
        