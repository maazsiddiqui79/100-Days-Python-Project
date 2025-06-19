from tkinter import * # type:ignore
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QUIZ_INTERFACE:
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz =quiz_brain
        self.win = Tk()
        self.win.title("QUIZZLER")
        self.win.config(bg=THEME_COLOR,padx=20,pady=20)
        
        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",16,"bold"))
        self.score_label.grid(column=1,row=1)
        
        self.canvas =Canvas(width=600,height=300,highlightthickness=0)
        
        
        self.canvas.grid(column=0,row=2,columnspan=2,pady=20)
        self.text =self.canvas.create_text(300,150,text="Questions Come Here",font=("arial",20,"italic"),width=600)
        
        
        check_img = PhotoImage(file=r"M:\M..A..A..Z\New Learning\Daily Codes\34.Day34\quizzler-app-start\images\true.png")
        self.check_btn = Button(image=check_img,relief="solid",command=self.ans_true)
        self.check_btn.grid(column=0,row=3)
        
        cross_img = PhotoImage(file=r"M:\M..A..A..Z\New Learning\Daily Codes\34.Day34\quizzler-app-start\images\false.png")
        self.cross_btn = Button(image=cross_img,relief="solid",command=self.ans_false)
        self.cross_btn.grid(column=1,row=3)
        
        
        
        
        
        q_text =self.quiz.next_question()
        self.canvas.itemconfig(self.text,text =q_text)
        self.win.mainloop()
        
            
                
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.text,text =q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="#8CCDF0")
            self.canvas.itemconfig(self.text,text ="QUIZ COMPLETED")
            self.cross_btn.config(state="disabled")
            self.check_btn.config(state="disabled")
        
    def ans_true(self):
        self.feedback(self.quiz.check_answer("True"))
        
            
    def ans_false(self):
        self.feedback(self.quiz.check_answer("False"))
        
    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.win.after(1000,self.get_next_question)
        
        
        
        
    
        
        
        
        
        
# x= QUIZ_INTERFACE()
        
