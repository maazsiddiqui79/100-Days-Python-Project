from turtle import *

class Class_Paddle(Turtle):
    def __init__(self,x,y,clr):
        super().__init__()
        self.Create_paddle(x,y)
        self.color(clr)
        
        
    def Create_paddle(self,x,y):
        
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x=x,y=y)
        
    def move_up(self):
        new_y= self.ycor()+40
        self.goto(self.xcor(),new_y)
        
        
        
    def move_down(self):
        new_y= self.ycor()-40
        self.goto(self.xcor(),new_y)
        
        
        