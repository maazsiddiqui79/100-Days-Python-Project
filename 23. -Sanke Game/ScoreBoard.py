from turtle import *


class Score_board_CLass (Turtle):
    Score =0
    def __init__(self):
        super().__init__()
        self.Score =0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score : {self.Score}", align='center', font=('Arial', 24, 'normal'))
        
    def Update_Score (self):
        self.clear()
        self.Score += 1 
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score : {self.Score}", align='center', font=('Arial', 24, 'normal'))
        
    def Game_End (self):
        self.clear()
        self.goto(0,0)
        self.color("Dark Blue")
        self.write(f"Game Over!", align='center', font=('Arial', 24, 'normal'))
        
        self.final_Score()
        self.High_Scr()
        
    
    def final_Score(self):
        
        self.goto(0,40)
        self.color("Dark Blue")
        self.write(f"Final Score : {self.Score}", align='center', font=('Arial', 24, 'normal'))
        
    
    # def High_Scr():
    def High_Scr(self):
        
        
        with open("High_Score.txt","r") as f:
        
            d = f.read()
            High_Score = int(d.strip())
            
      
            
        if self.Score > High_Score:
            self.goto(0, 150)
            self.write(f"🎉new high score🎉".upper(), align='center', font=('Arial', 24, 'normal'))
            with open("High_Score.txt", "w") as f:
                f.write(str(self.Score))
                
                # self.clear()
         
        self.goto(0, 80)
        self.color("Dark Blue")
        self.write(f"High Score : {max(self.Score, High_Score)}", align='center', font=('Arial', 24, 'normal'))
    
            
    
    
        
        