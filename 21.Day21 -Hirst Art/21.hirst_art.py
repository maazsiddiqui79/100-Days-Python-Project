from turtle import *
import random

color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

t = Turtle()
t.penup()

scr =Screen()
scr.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)

def one_line():
    for _ in range(20):
        t.dot(11,random.choice(color_list))
        t.forward(20)
        
    t.setheading(90)
    t.forward(30)
    t.setheading(180)
    t.forward(400)
    t.setheading(0)
    
for _ in range(20):
    one_line()

scr.exitonclick()