import random
from tkinter import * # type: ignore


color1 = "#F6F1DE"
color2 = "#1D1E35"
color3 = "#8AB2A6"
color4 = "#ACD3A8"




common_passwords = [    "123456",    "password",    "123456789",    "12345",    "12345678",
                    "qwerty",    "1234567",    "111111",    "123123",    "abc123",    "password1",
                    "1234",    "iloveyou",    "admin",    "welcome",    "monkey",    "login",    "letmein",
                    "football",    "starwars",    "dragon",    "passw0rd",    "master",    "hello",    "freedom",    "whatever",    "qazwsx",    "trustno1",    "654321",    "superman",    "batman",    "zaq1zaq1",    "password123",  "1234567890","1234","123","1234$","zxcvbnm","asdfghjkl","qwertyuiop","1234567890","0123456789","aaaaaa",""]


def check_strength ():
    pts = 0 
    
    years = [str(i) for i in range(2000,2027)]
    
    
    password = entry.get()
    password_lst = list(password)
    print(entry.get())
    print()
    
    if not password:
        msg_label.config(text="Password cannot be empty.", font=("courier", 24, "bold"))
        msg_label.grid(column=1,row=2)
        return

    
    
    if len(password) <=3:
        msg_label.config(text="Your Password is very small.", font=("courier", 24, "bold"))
        msg_label.grid(column=1,row=2)
        return
    
    if not any(common in password.lower() for common in common_passwords):        
        pts += 3 
    if len(password) >=20:
        pts += 7
    elif len(password) >=16:
        pts += 4
    elif 12< len(password) <16:
        pts += 3
    elif 12>=len(password) :
        pts += 1
    if any(i.isalpha() for i in password) :
        pts += 3
    if password.isalpha() and any(i.upper() for i in password):
        pts += 3
    if password.isalpha() and any(i.lower() for i in password):
        pts += 3
    if password.isalpha() :
        pts += 1
    if any(i.isdigit() for i in password ):
        pts += 1
    if any(i in "!@#$%^&*()_+=-|}{[]\":;'?><,./" for i in password):
        pts += 4
    if any(i in password for i in years ):
        pts += 1
        
    
    print("Your Score:",pts)
    
    if pts >= 15:
    # very strong
        msg_label.config(text="Your Password is Very Strong...",font=("courier",24,"bold"))
        msg_label.grid(column=1,row=2)
        # msg_label.destroy()
    elif 11 < pts <= 14:
    # strong
        msg_label.config(text="Your Password is Strong...",font=("courier",24,"bold"))
        msg_label.grid(column=1,row=2)
    elif 8 <= pts <= 11:
    # Moderate
        msg_label.config(text="Your Password is Okay...",font=("courier",24,"bold"))
        msg_label.grid(column=1,row=2)
    elif 5 < pts <= 7:
    # weak
        msg_label.config(text="Your Password is Weak...",font=("courier",24,"bold"))
        msg_label.grid(column=1,row=2)
    elif pts <=5:
        # very weak
        msg_label.config(text="Your Password is Very Weak...",font=("courier",24,"bold"))
        msg_label.grid(column=1,row=2)
        
    pts = 0
        
        
         
    
        
            
    entry.delete(0,END)




win = Tk()
win.title("Password Security Verification Tool🔑".title())
win.config(padx=20,pady=20,bg=color3)

title_label = Label(text="Password Strength Meter",font=("courier",28,"bold"),bg=color3,fg="black")
title_label.grid(column=0,row=0,columnspan=3,pady=50)

enter_password_label = Label(text="Enter Password",font=("courier",18,"bold"),bg=color3,fg="black")
enter_password_label.grid(column=0,row=1)

msg_label = Label(text="Your Password is Very Strong...",font=("courier",24,"bold"),fg="white",bg=color3)
msg_label.grid(column=1,row=2)
msg_label.grid_forget()
entry = Entry(width=45,font=("courier",20,"italic"))
entry.focus()
entry.grid(column=1,row=1,padx=20)


btn =Button(text="Check",font=("courier",25,"bold"),relief="ridge",width=30,command=check_strength,bg=color1)
btn.grid(column=1,row=3,padx=10,pady=10)
btn.bind("<Enter>", lambda e: btn.config(font=("courier", 26, "underline","bold"),bg=color2,fg="white"))
btn.bind("<Leave>", lambda e: btn.config(font=("courier", 25, "bold"),bg=color1,fg="black"))




win.mainloop()
