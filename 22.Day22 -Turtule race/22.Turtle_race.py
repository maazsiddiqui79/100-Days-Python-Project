import random ; from turtle import *

scr = Screen()
scr.setup(width=600,height=500)
user_ip_color = scr.textinput(title="Choose Color",prompt="ENTER A COLOR:")


t1 = Turtle(shape="turtle")
t1.color(user_ip_color)
t1.penup()
t1.goto(-280,150)

t2 = Turtle(shape="turtle")
t2.penup()
t2.color("Silver")
t2.goto(-280,100)

t3 = Turtle(shape="turtle")
t3.penup()
t3.color("Gold")
t3.goto(-280,50)

t4 = Turtle(shape="turtle")
t4.penup()
t4.color("Green")
t4.goto(-280,0)

t5 = Turtle(shape="turtle")
t5.penup()
t5.color("LightBlue")
t5.goto(-280,-50)


def move():
    t1.forward(10)
    
def move_back():
    t1.backward(10)
    
def LEFT():
    head = t1.heading() + 10
    t1.setheading(head)

def RIGHT():
    head = t1.heading() - 10
    t1.setheading(head)
    
scr.listen()

scr.onkeypress(key="Up",fun=move)
scr.onkeypress(key="Down",fun=move_back)
scr.onkeypress(key="Left",fun=LEFT)
scr.onkeypress(key="Right",fun=RIGHT)

while True:
    t2.forward(random.randint(0,10))
    t3.forward(random.randint(0,10))
    t4.forward(random.randint(0,10))
    t5.forward(random.randint(0,10))
    
    if t1.xcor() >= 250:
        print("🎉 You Win!")
        scr.bye()
        break
    
    if (t2.xcor() >= 250) or (t3.xcor() >= 250) or (t4.xcor() >= 250) or (t5.xcor() >= 250):
        print("😞 You Lose!")
        scr.bye()
        break
        
    


# scr.exitonclick()
