import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("mintcream")  # Light background color for visibility

# Create the player object
player = Player()

# Listen for keyboard input
screen.listen()
screen.onkeypress(fun=player.move_forward, key="Up")  # Move player forward on "Up" key

# Create the scoreboard
scoreboard = Scoreboard()

# Create the car manager
car_manager = CarManager()

# Game loop flag
game_is_on = True
while game_is_on:
    time.sleep(0.1)         # Control the game speed
    screen.update()         # Update screen every frame

    car_manager.car_create()  # Possibly add a new car
    car_manager.car_move()    # Move all cars forward

    # Check if player reached the top
    if player.ycor() >= player.FINISH_LINE_Y:
        player.goto(player.STARTING_POSITION)  # Reset player to start
        scoreboard.level += 1                    # Increase level
        scoreboard.update_score()                # Update scoreboard
        car_manager.car_speedup()              # Increase car speed

    # Check for collisions with any car
    for car in car_manager.all_cars:
        if car.distance(player) < 35:
            game_is_on = False
            scoreboard.end()  # Display "Game Over"

# Keep the window open after the game ends
screen.mainloop()
