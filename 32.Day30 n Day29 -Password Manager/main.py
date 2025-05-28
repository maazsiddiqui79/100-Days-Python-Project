# ---------------------------- HEADER FILE ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import pandas as pd


# 🎨 Main Background
BACKGROUND = "#F5ECD5"    # Light Cream / Ivory
# 🎨 Supporting UI Colors
olive_green = "#A4B465"        # Soft Olive / Sage
apricot_orange = "#2C2C2C"     # Warm Apricot

# 🎯 Red Logo Accent (Complementary)
red_accent = "#DC143C"         # Crimson Red

# ------------------------------------------------------------------------ #

# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_password():
    
    
    if var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
    

# ------------------------------------------------------------------------------- #

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

characters = [
    # Letters
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',

    # Digits
    '0','1','2','3','4','5','6','7','8','9',

    # Symbols and punctuation
    '!','@','#','$','%','^','&','*',
    '-','_','=','+','|',';',':',
    '\'','"','<','>',',','.','/','?',
]


weights = [5 if i.isalpha() else (3 if i.isnumeric() else 1) for i in characters]

def password_gen():
    password_entry.delete(0,END)
    passwordlen =random.randint(8,16)
    password_list =random.choices(characters,k=passwordlen,weights=weights)
    actual_password = "".join(password_list)
    
    
    password_entry.insert(0,actual_password)
    pyperclip.copy(actual_password) 


# ------------------------------------------------------------------------------- #




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_file ():
    
    
    website_data = web_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    
    new_data={
        website_data :{
            "Email":email_data,
            "Password":password_data
        }
    }
    
    if len(website_data)== 0 or len(password_data)== 0:
        if len(website_data)== 0 and len(password_data)>0:
            messagebox.showerror(message="Website Not Entered")
        elif len(website_data)> 0 and len(password_data) ==0:
            messagebox.showerror(message="Password Not Entered")
        else:
            messagebox.showerror(message="Password and Website Not Entered")
    
    else:
        is_okay = messagebox.askokcancel(title="Details",message=f"You Entered :\n\nWebsite: {website_data}\nEmail/Username: {email_data}\nPassword: {password_data}")

        if is_okay :
            try:
                with open("Password Data.json","r") as f:
                    # reading old data
                    data =json.load(f)
                    # update the data 
            except FileNotFoundError:
                with open("Password Data.json","w") as f:
                    json.dump(new_data,f,indent=5)
                    
            else:
                data.update(new_data)    
                with open("Password Data.json","w") as f:
                    # write the new data
                    json.dump(data,f,indent=5)
            finally:    
                web_entry.delete(0,END)
                password_entry.delete(0,END)
                
                


# ---------------------------- SEARCH FUNCTIONALITY -------------------------------- #

def search_func ():
    search_data = web_entry.get()
    # print(search_data)
    try:
        access_data = pd.read_json("Password Data.json")
    except FileNotFoundError:
        file = open("Password Data.json","w")
    except ValueError:
        file = open("Password Data.json","w")
        json.dump({},file)
            
    try:
        print(access_data[search_data])
        email_data_retrive=access_data[search_data]["Email"]
        password_data_retrive=access_data[search_data]["Password"]
    except KeyError:
        dailog_box =messagebox.showinfo(title="Access Details",message="No Email/Username and PassWord exists to this Website")
    else:
        m =f"Saved Credentials\n\nWebsite: {search_data}\nEmail: {email_data_retrive}\nPassword: {password_data_retrive}"
        dailog_box =messagebox.showinfo(title=f"Details for {search_data}",message=m)
    
    
    
        

# ---------------------------------------------------------------------------------- #

        
        
        


# -------------------------------------------------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("P a s s w o r d     M a n a g e r")
win.config(bg=BACKGROUND,pady=45,padx=20)



# canvas
canvas =Canvas(width=200,height=200,bg=BACKGROUND,highlightthickness=0)
canvas.grid(column=1,row=0)
img =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)

# label and entry of website
web_label=Label(text="Website :",font=("comic san ma",15,"bold"),bg=BACKGROUND)
web_label.grid(column=0,row=1,pady=5)
web_entry =Entry(width=45,font=("comic san ma",15,"bold"))
web_entry.focus()
web_entry.grid(column=1,row=1,columnspan=2,padx=5)
# Search functionality 
search_btn = Button(text="Search",font=("comic san ma",15,"bold"),width=15,relief="groove",command=search_func)
search_btn.grid(column=3,row=1,pady=5)
search_btn.bind("<Enter>",lambda e: search_btn.config(bg=apricot_orange,fg="white"))
search_btn.bind("<Leave>",lambda e: search_btn.config(bg="white",fg=apricot_orange))



# label and entry of email
email_label=Label(text="Username/Email :",font=("comic san ma",15,"bold"),bg=BACKGROUND)
email_label.grid(column=0,row=2,pady=5)

email_entry =Entry(width=45,font=("comic san ma",15,"bold"))
email_entry.grid(column=1,row=2,columnspan=3,pady=5)
email_entry.insert(0,"siddiqui.maaz79@gmail.com")

# label and entry  and btn of password
password_label=Label(text="Password :",font=("comic san ma",15,"bold"),bg=BACKGROUND)
password_label.grid(column=0,row=3)
password_entry =Entry(width=25,font=("comic san ma",15,"bold"),show="*")
password_entry.grid(column=1,row=3,pady=5)

# checkbox of show pass
var =IntVar()
chb = Checkbutton(text="👀  ",font=("comic san ma",15,"bold"),bg=BACKGROUND,command=show_password,variable=var)
chb.grid(column=2,row=3)


# button
password_btn = Button(text="Generate",font=("comic san ma",15,"bold"),command=password_gen,width=15,relief="groove")
password_btn.grid(column=3,row=3,pady=5)
password_btn.bind("<Enter>",lambda e:password_btn.config(bg=apricot_orange,fg="white"))
password_btn.bind("<Leave>",lambda e:password_btn.config(bg="white",fg=apricot_orange))


# btn of add
add_btn = Button(text="Add",font=("comic san ma",15,"bold"),width=42,command=save_data_file,relief="groove")
add_btn.grid(column=1,row=4,columnspan=3,pady=5)
add_btn.bind("<Enter>",lambda e:add_btn.config(bg=apricot_orange,fg="white"))
add_btn.bind("<Leave>",lambda e:add_btn.config(bg="white",fg=apricot_orange))





win.mainloop()
# --------------------------------------------------------------------- #