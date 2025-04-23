from turtle import *
import time

class Class_Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.Create_ball()
        
        self.X_Move =3
        self.Y_Move =3
        
        
    def Create_ball(self):
        
        self.penup()
        self.shape("circle")
        self.color("#00BFFF")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(x=0,y=0)
        
    def ball_move(self):
        new_x = self.X_Move  + self.xcor()
        new_y = self.Y_Move + self.ycor()
        self.goto(x=new_x,y=new_y)
        
    def bounce(self):
        self.Y_Move *= -1
    
    def bounce_With_paddle(self):
        self.X_Move *= -1
        
    def reset_pos (self):
        self.goto(0,0)
        self.bounce_With_paddle()
        time.sleep(1)
  