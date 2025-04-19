from turtle import *
from Pong_Paddle import *
from Pong_Ball import *
from Score_Board import *
import time


scr = Screen()
scr.setup(width=800,height=600)
scr.title("PONG GAME")
scr.bgcolor("Beige")
scr.tracer(0)



t= Turtle()
t.penup()
t.hideturtle()
t.color("gray20")
t.shapesize(stretch_wid=0.2, stretch_len=2)
t.shape("square")
t.setheading(270)  # Pointing down
t.forward(300)     # Move to starting point
t.setheading(90) 
t.pendown()

for _ in range(300):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()







R_Paddle = Class_Paddle(375,0,clr="Maroon")   
L_Paddle = Class_Paddle(-375,0,clr="Maroon")  

scr.listen()
scr.onkeypress(L_Paddle.move_down,"s")
scr.onkeypress(L_Paddle.move_up, "w")
scr.onkeypress(fun=R_Paddle.move_up, key="Up")
scr.onkeypress(fun=R_Paddle.move_down,key="Down")


ball = Class_Ball()

L_scr_brd =Class_Score_Boeard(-160,220)
R_scr_brd =Class_Score_Boeard(160,220)


while True:
    scr.update()
    time.sleep(0.01)
    ball.ball_move()
    
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce()
        
    if ball.distance(R_Paddle) < 40 and ball.xcor() > 360 and ball.X_Move > 0:
        ball.bounce_With_paddle()
    if ball.distance(L_Paddle) < 40 and ball.xcor() < -360 and ball.X_Move < 0:
        ball.bounce_With_paddle()
        
        
    if ball.xcor() > 410 :
        L_scr_brd.inc()
        ball.reset_pos()
        
    
    if  ball.xcor() < -410 :
        R_scr_brd.inc()
        ball.reset_pos()
        # scr.onkeypress(fun=ball.reset_pos,key="d")
        # scr.onkeypress(fun=ball.reset_pos,key="d")
        
        
        
scr.exitonclick()

