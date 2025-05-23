
# ---------------------------- HEADER FILE ------------------------------- #
from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
CLOUD_BLUE_2 = "#D9EAFD" #
SLATE_NAVY = "#3A4F63"

OCEAN_MIST_5 = "#a9cfd8"      

POWDER_BLUE_20 = "#b5d0ec"    
PEBBLE_GREY_21 = "#cbd5e1"    
ASH_BLUE_23 = "#5f7b88" 

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global timer
    if timer is not None:
        win.after_cancel(timer)
    timer_text.config(text="TIMER")  
    canvas.itemconfig(countdown_text,text="00:00") 


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start ():
    global timer
    task = user_work_choice.get()
    time = int (user_time_choice.get())
    
    # to avoid multiple timer on clicking start button 
    if timer is not None:
        win.after_cancel(timer)
        timer = None

    
    # giving a limit of timer cant set more than this
    if time >=100:
        timer_text.config(text="Exceed the limit 😔....")
        return
    
    
    if task == "WORK":
        timer_text.config(text="WORK")
        count_down(time*60)
        
    if task == "BREAK":
        timer_text.config(text="BREAK")
        count_down(time*60)
    
    if task == "LONG BREAK":
        timer_text.config(text="LONG BREAK")
        count_down(time*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    # Calculating the min and sec
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    
    # Conditions if the number displays in one digit.
    if count_sec <10:
        count_sec = f"0{count_sec}"
        
    if count_min < 10:
        count_min = f"0{count_min}"
        
    if count_sec == 0:
        count_sec = "00"
        
        
    if count_min == 0:
        count_min = "00"
    
    # updates the count down
    canvas.itemconfig(countdown_text,text = f"{count_min}:{count_sec}")
    
    # main logic using recursion
    if count > 0:
        timer = win.after(1000,count_down,count-1)
    elif count <=10:
        winsound.Beep(1500,500)
        win.attributes("-topmost",True)    
        win.lift()
        win.after_idle(win.attributes,"-topmost",False)
        print("Maaz")
    


# ---------------------------- UI SETUP ------------------------------- #


win = Tk()
win.title("Promodoro")
win.config(bg=PEBBLE_GREY_21,padx=50,pady=75)


# Timer text
timer_text = Label(text="TIMER",font=(FONT_NAME,37,"bold"),bg=PEBBLE_GREY_21,fg=ASH_BLUE_23)
timer_text.grid(row=0,column=2)


# display img ans count down
canvas =Canvas(width=200,height=250,bg=PEBBLE_GREY_21,highlightthickness=0)
canvas.grid(column=2,row=1)
img = PhotoImage(file =r"M:\M..A..A..Z\New Learning\Project\100-Days-Python-Project\31.Day28 -Promodo(timer)\tomato.png")
canvas.create_image(100,125,image=img)

countdown_text = canvas.create_text(100,145,text="00:00",font=("Comic Sans MC",45,"bold"),fill="white")

# spindown
user_work_choice_lbl=Label(text="TASK:",font=(FONT_NAME,27,"bold"),bg=PEBBLE_GREY_21,fg=ASH_BLUE_23)
user_work_choice_lbl.grid(row=2,column=0)
user_work_choice = Spinbox(values=("WORK","BREAK","LONG BREAK"),width=10,font=(FONT_NAME,15,"bold"))
user_work_choice.grid(row=2,column=2)
user_work_choice.config(state="readonly")


user_time_choice_lbl=Label(text="(min)TIME:",font=(FONT_NAME,24,"bold"),bg=PEBBLE_GREY_21,fg=ASH_BLUE_23)
user_time_choice_lbl.grid(column=3,row=2)
user_time_choice = Spinbox(from_=20,to=100,width=5,font=(FONT_NAME,15,"bold"))
user_time_choice.grid(column=4,row=2)


# buttons

btn_start = Button(text="Start")
btn_start.grid(row=1,column=3)
btn_start.config(bg=SLATE_NAVY,fg="white",font=(FONT_NAME,15,"bold"),command=start)
btn_start.bind("<Enter>",lambda e:btn_start.config(bg="gray"))
btn_start.bind("<Leave>",lambda e:btn_start.config(bg=SLATE_NAVY))

btn_reset = Button(text="RESET")
btn_reset.grid(row=1,column=4)
btn_reset.config(bg=SLATE_NAVY,fg="white",font=(FONT_NAME,15,"bold"),command=reset)
btn_reset.bind("<Enter>",lambda e:btn_reset.config(bg="gray"))
btn_reset.bind("<Leave>",lambda e:btn_reset.config(bg=SLATE_NAVY))

 

win.mainloop()