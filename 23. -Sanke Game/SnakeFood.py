from turtle import *
import random

x_loc =random.randint(-260,260)
y_loc =random.randint(-260,260)

class Food_Class (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("chocolate")
        self.goto(x_loc,y_loc)
        
    def New_Loc (self):
        x_loc =random.randint(-260,260)
        y_loc =random.randint(-260,260)
        self.goto(x_loc,y_loc)
        
        
        
    