import random
from turtle import Turtle

# A list of dark colors used for car appearances
DARK_COLORS = [
    "black", "dimgray", "gray", "darkgray", "slategray", "darkslategray",
    "maroon", "darkred", "firebrick", "darkblue", "midnightblue", "navy",
    "darkgreen", "forestgreen", "olive", "darkolivegreen", "darkcyan", "teal",
    "indigo", "purple", "darkmagenta", "darkviolet", "saddlebrown", "chocolate",
    "darkgoldenrod", "peru"
]

class CarManager(Turtle):
    # Class-level attributes for movement control
    car_spawn_counter = 0
    STARTING_MOVE_DISTANCE = 10
    MOVE_INCREMENT = 6

    def __init__(self):
        super().__init__()
        self.all_cars = []  # Stores all active car turtles

    def car_move(self):
        # Moves each car to the left by the current speed
        for car in self.all_cars:
            new_x = car.xcor() - self.STARTING_MOVE_DISTANCE
            car.goto(x=new_x, y=car.ycor())

    def car_create(self):
        # Increments internal counter for spawn timing
        CarManager.car_spawn_counter += 1

        # Create a car every 6 cycles
        if CarManager.car_spawn_counter % 6 == 0:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=3, stretch_wid=1)  # Make it look like a car
            car.color(random.choice(DARK_COLORS))
            car.setheading(180)  # Face left
            random_y = random.randint(-240, 240)
            car.goto(x=300, y=random_y)  # Start at the right side
            # car.hideturtle()
            self.all_cars.append(car)

    def car_speedup(self):
        # Increase the speed of the cars
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
