from turtle import Turtle

# Font settings for the scoreboard display
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    level = 1  # Class-level variable to track the level

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)  # Position the scoreboard at the top-left
        self.display_level()  # Initial display

    def display_level(self):
        """Displays the current level on the screen."""
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def update_score(self):
        """Updates the scoreboard with the current level."""
        self.display_level()

    def end(self):
        """Displays the 'Game End' message at the center."""
        self.goto(0, 0)
        self.hideturtle()  # Ensure it's hidden before writing

        self.write("Game End", align='center', font=FONT)
