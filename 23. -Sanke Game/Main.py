from turtle import *
from SnakeBody import *
from SnakeFood import *
from ScoreBoard import *
import time




scr =Screen()
scr.setup(600,600)
scr.title("SNAKE GAME")
scr.bgcolor("Light Green")
scr.listen()
scr.tracer(0)



snake =Snake_Class()
# snake.Add_Segment()
snake.Create_Snake_Body()
snake.head.color("lightcoral")
snake.head.shape("triangle")
snake.head.shapesize(stretch_wid=1, stretch_len=2.5)




scr.onkeypress(key="Up",fun=snake.Move_UP)
scr.onkeypress(key="Down",fun=snake.Move_DOWN)
scr.onkeypress(key="Left",fun=snake.Move_LEFT)
scr.onkeypress(key="Right",fun=snake.Move_RIGHT)

food =Food_Class()

score =Score_board_CLass()


game_on = True

while game_on:
    scr.update()
    time.sleep(0.1)   
    snake.Move()
    
    if snake.head.distance(food) < 15:
        food.New_Loc()
        score.Update_Score()
        snake.Extend()
            
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() >295 or snake.head.ycor() < -295:
        game_on =False
        score.Game_End()
        
    
    







scr.exitonclick()