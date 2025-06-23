from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card ={}

try:
    data = pd.read_csv("Pending Words To Learn.csv")
except :
    data = pd.read_csv(r"M:\M..A..A..Z\PROGRAMMING\1. PYTHON\Project\100-Days-Python-Project\36.Day31 -Flash card\data\English_words.csv")
dict= pd.DataFrame.to_dict(data,orient="records")
# ----------------------------------------FLIP CARD----------------------------------------------
def flip_card():
    global current_card
    win.after_cancel(flip_card)
    canvas.itemconfig(background,image=img_flip)
    canvas.itemconfig(title_label,text="Hindi",fill="white")
    canvas.itemconfig(word_label,text=current_card["Hindi"],fill="white")
    canvas.config(bg="#BBD1C6",highlightthickness=0)
    win.config(bg="#BBD1C6")
# --------------------------------------------------------------------------------------------------


# --------------------------------------Generate a New word--------------------------------------


def gen_word():
    global current_card
    global flip_timer
    win.after_cancel(flip_timer)
    canvas.itemconfig(background,image=background_img_front)
    try:
        current_card =random.choice(dict)
    except:
        canvas.itemconfig(word_label,text="NO WORDS LEFT")
        return        
    canvas.itemconfig(title_label,text="English",fill="black")
    canvas.itemconfig(word_label,text=current_card["English"],fill="black")
    flip_timer=win.after(3000, flip_card)

    
# --------------------------------------------------------------------------------------------------

# ---------------------------------------------------REMOVE KNOWN WORD----------------------------------------
def known():
    print(len(dict))
    saving_data = pd.DataFrame(dict)
    saving_data.to_csv("Pending Words To Learn.csv",index=False)
    
    try:
        dict.remove(current_card)
    except:
        canvas.itemconfig(word_label,text="NO WORDS LEFT")
        return
    gen_word()

# --------------------------------------------------------------------------------------------------
# ---------------------------------------------------UI PART----------------------------------------
win = Tk()
win.title("Flashy")
# win.minsize(width=900,height=650)
# win.geometry("900x650")
win.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer=win.after(3000, flip_card)


canvas =Canvas (width=800,height=526)
background_img_front = PhotoImage(file=r"M:\M..A..A..Z\PROGRAMMING\1. PYTHON\Project\100-Days-Python-Project\36.Day31 -Flash card\images\card_front.png",)
img_flip = PhotoImage(file=r"M:\M..A..A..Z\PROGRAMMING\1. PYTHON\Project\100-Days-Python-Project\36.Day31 -Flash card\images\card_back.png")    
background = canvas.create_image(400,263 ,image=background_img_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


title_label =canvas.create_text(400,150,text="Hindi",font=("Ariel",40,"italic"))


word_label =canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

wrong_img =PhotoImage(file=r"M:\M..A..A..Z\PROGRAMMING\1. PYTHON\Project\100-Days-Python-Project\36.Day31 -Flash card\images\wrong.png")
right_img =PhotoImage(file=r"M:\M..A..A..Z\PROGRAMMING\1. PYTHON\Project\100-Days-Python-Project\36.Day31 -Flash card\images\right.png")
wrong_btn =Button(image=wrong_img,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
wrong_btn.grid(row=1,column=0)
wrong_btn.config(command=gen_word)
right_btn =Button(image=right_img,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
right_btn.config(command=known)
right_btn.grid(row=1,column=1)

gen_word()


win.mainloop()
# ---------------------------------------------------------------------------------------

