from turtle import *
import random


Move_Dstance =20
UP =90
DOWN = 270
LEFT =180
RIGHT = 0

class Snake_Class:
    x =0
    
    segment_position =[(0,0),(-20,0),(-40,0)]
    
    Segment = []
    
    def __init__(self):
        self.Create_Snake_Body()
        self.head = self.Segment[0] 
    
    
    
    def Create_Snake_Body(self):
        for seg in self.segment_position:
            self.Add_Segment(seg)
        
    def Add_Segment(self,seg):
        t = Turtle("square")
        t.penup()
        if self.x %3 ==0:
            t.color("peachpuff")
        else:
            t.color("lightyellow")
        t.goto(seg)
        self.Segment.append(t)
        self.x+=1
        
    
    def Extend(self):
        self.Add_Segment(self.Segment[-1].position())
        
        
    def Move_UP(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def Move_DOWN(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        
    def Move_LEFT(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def Move_RIGHT(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        
        
    def Move(self):
        for seg in range(len(self.Segment)-1,0,-1):
            new_x =self.Segment[seg -1].xcor()
            new_y =self.Segment[seg -1].ycor()
            
            self.Segment[-1].shape("circle")
            self.Segment[-2].shape("square")
            self.Segment[seg].goto(new_x,new_y)
        self.head.forward(Move_Dstance)
            
        