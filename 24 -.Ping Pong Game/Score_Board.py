from turtle import *


class Class_Score_Board (Turtle) :
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.color("Midnight Blue")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.update()
        
        
    def update(self):
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=("Arial", 24, "normal"))
        
    def inc(self):
        self.score +=1       
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=("Arial", 24, "normal"))
        