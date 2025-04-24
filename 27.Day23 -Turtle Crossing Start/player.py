from turtle import Turtle

# Constant for how far the player moves with each key press
MOVE_DISTANCE = 10

class Player(Turtle):
    # Class-level constants for position management
    STARTING_POSITION = (0, -280)
    FINISH_LINE_Y = 280

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1.2, stretch_wid=1.2)  # Slightly larger turtle
        self.penup()
        
        self.goto(self.STARTING_POSITION)  # Start at the bottom center
        self.setheading(90)  # Face upward

    def move_forward(self):
        """Move the player upward by MOVE_DISTANCE."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
