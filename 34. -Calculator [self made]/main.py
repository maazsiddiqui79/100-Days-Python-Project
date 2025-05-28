from tkinter import *
from tkinter import messagebox
import time


expression = ""

bg_light     = "#F0F0D7"  
bg_secondary = "#E7EFE7"  
accent_light = "#AAB99A"  
accent_dark  = "#727D73"  

 
# --------------------------------------Number Pressing command----------------------------------
def num_press(n):
    global expression
    
    
    
    ip.delete(0,END)
    ip.xview_moveto(1)  # Scroll to the end

    expression+=str(n)
    ip.insert(0,expression)
    ip.xview_moveto(1)  # Scroll to the end

# ------------------------------------------------------------------------------------------------


# --------------------------------------Number symbol command-------------------------------------
def symbol_press(s:str):
    
    
    global expression
    
    if expression == "":
        return
    elif expression[-1] in "+-*/":
        ip.delete(0,END)
        ip.xview_moveto(1)  # Scroll to the end

        expression = expression[:-1]+s
    else:
            
        ip.delete(0,END)
        ip.xview_moveto(1)  # Scroll to the end

        expression += (s)
       
    
    ip.insert(END,expression)
    ip.xview_moveto(1)  # Scroll to the end

    
    
    
    


# --------------------------------------Submit Button------------------------------------
def submit_press():
    global expression
  
    
            
    try:
        
        if expression == "":
            messagebox.showerror("Error", "No expression to evaluate.")
            return
        
        elif expression[-1] in "+-*/":
            messagebox.showerror("Invalid Input", "You have entered two operators in a row. Please enter a number after the operator.")
            return
        
        sum = eval(expression)
        expression = str(sum)
        ip.delete(0,END)
        ip.xview_moveto(1)  # Scroll to the end

        ip.insert(0,sum)
        ip.xview_moveto(1)  # Scroll to the end

                

            
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")
  

# ------------------------------------------------------------------------------------------------


# --------------------------------------Clear-----------------------------------------------------
def clear_press():
    global expression
    expression=str("")
    
    ip.delete(0,END)
    ip.xview_moveto(1)  # Scroll to the end

    ip.insert(0,"")
    ip.xview_moveto(1)  # Scroll to the end

# ------------------------------------------------------------------------------------------------
def click_effect (c):
    c.config(bg="#828683")
    win.after(200,lambda :c.config(bg=accent_dark))

    


# --------------------------------------key press-------------------------------------------------
def key_press(event):
    
    global expression
    key = event.char
    if key.isdigit():
        num_press(key)
        if key == "0":
           click_effect(btn_0)
        if key == "1":
           click_effect(btn_1)
        if key == "2":
           click_effect(btn_2)
        if key == "3":
           click_effect(btn_3)
        if key == "4":
           click_effect(btn_4)
        if key == "5":
           click_effect(btn_5)
        if key == "6":
           click_effect(btn_6)
        if key == "7":
           click_effect(btn_7)
        if key == "8":
           click_effect(btn_8)
        if key == "9":
           click_effect(btn_9)
        
        
        
        
    elif key in "+-*/":
        symbol_press(key)
        
        if key == "+":
            click_effect(btn_plus)
            
        if key == "-":
            click_effect(btn_minus)
            
        if key == "*":
            click_effect(btn_mul)
            
        if key == "/":
            click_effect(btn_div)
    elif key == "\r":
        btn_submit.config(bg="#DEE7DF")
        win.after(100, lambda: btn_submit.config(bg=accent_dark))
        submit_press()
        
    elif key == "\x08":
        if len(expression)>0:
            expression = expression [:-1]
            ip.delete(0, END)
            ip.xview_moveto(1)  # Scroll to the end

            ip.insert(0, expression if expression else "0")
            ip.xview_moveto(1)  # Scroll to the end

         

# ------------------------------------------------------------------------------------------------



win = Tk()
win.geometry("330x330")
win.maxsize(width=400,height=400)
win.title("C A L C U L A T O R")
win.bind("<Key>", key_press)
win.config(padx=15,pady=15,bg=bg_secondary)


ip =Entry(width=18,font=("Helvetica", 20,"bold"), justify="right",bg="#D6E3C8",fg="black")

# ip.config(state="readonly")
ip.grid(column=0,row=0,columnspan=6,pady=10)


    


btn_1 =Button(text="1",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_1.config(command=lambda: num_press(1))
btn_1.grid(column=0,row=2,pady=3,padx=1)
btn_1.bind("<Enter>",lambda e:btn_1.config(bg=accent_light))
btn_1.bind("<Leave>",lambda e:btn_1.config(bg=accent_dark))


btn_2 =Button(text="2",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_2.config(command=lambda: num_press(2))
btn_2.grid(column=1,row=2,pady=3,padx=1)
btn_2.bind("<Enter>",lambda e:btn_2.config(bg=accent_light))
btn_2.bind("<Leave>",lambda e:btn_2.config(bg=accent_dark))

btn_3 =Button(text="3",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_3.config(command=lambda: num_press(3))
btn_3.grid(column=2,row=2,pady=3,padx=1)
btn_3.bind("<Enter>",lambda e:btn_3.config(bg=accent_light))
btn_3.bind("<Leave>",lambda e:btn_3.config(bg=accent_dark))

btn_4 =Button(text="4",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_4.config(command=lambda: num_press(4))
btn_4.grid(column=0,row=3,pady=3,padx=1)
btn_4.bind("<Enter>",lambda e:btn_4.config(bg=accent_light))
btn_4.bind("<Leave>",lambda e:btn_4.config(bg=accent_dark))

btn_5 =Button(text="5",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_5.config(command=lambda: num_press(5))
btn_5.grid(column=1,row=3,pady=3,padx=1)
btn_5.bind("<Enter>",lambda e:btn_5.config(bg=accent_light))
btn_5.bind("<Leave>",lambda e:btn_5.config(bg=accent_dark))

btn_6 =Button(text="6",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_6.config(command=lambda: num_press(6))
btn_6.grid(column=2,row=3,pady=3,padx=1)
btn_6.bind("<Enter>",lambda e:btn_6.config(bg=accent_light))
btn_6.bind("<Leave>",lambda e:btn_6.config(bg=accent_dark))

btn_7 =Button(text="7",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_7.config(command=lambda: num_press(7))
btn_7.grid(column=0,row=4,pady=3,padx=1)
btn_7.bind("<Enter>",lambda e:btn_7.config(bg=accent_light))
btn_7.bind("<Leave>",lambda e:btn_7.config(bg=accent_dark))

btn_8 =Button(text="8",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_8.config(command=lambda: num_press(8))
btn_8.grid(column=1,row=4,pady=3,padx=1)
btn_8.bind("<Enter>",lambda e:btn_8.config(bg=accent_light))
btn_8.bind("<Leave>",lambda e:btn_8.config(bg=accent_dark))

btn_9 =Button(text="9",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_9.config(command=lambda: num_press(9))
btn_9.grid(column=2,row=4,pady=3,padx=1)
btn_9.bind("<Enter>",lambda e:btn_9.config(bg=accent_light))
btn_9.bind("<Leave>",lambda e:btn_9.config(bg=accent_dark))

btn_0 =Button(text="0",font=("courier",20,"bold"),width=4,bg=accent_dark)
btn_0.config(command=lambda: num_press(0))
btn_0.grid(column=0,row=5,pady=3,padx=1)
btn_0.bind("<Enter>",lambda e:btn_0.config(bg=accent_light))
btn_0.bind("<Leave>",lambda e:btn_0.config(bg=accent_dark))

btn_clear =Button(text="C",font=("courier",20,"bold"),command=clear_press,width=4,bg=accent_dark)
btn_clear.grid(column=1,row=5,pady=3,padx=1)
btn_clear.bind("<Enter>",lambda e:btn_clear.config(bg=accent_light))
btn_clear.bind("<Leave>",lambda e:btn_clear.config(bg=accent_dark))



btn_plus =Button(text="+",font=("courier",20,"bold"),command=lambda: symbol_press("+"),width=4,bg=accent_dark)
btn_plus.grid(column=3,row=2,pady=3,padx=1)
btn_plus.bind("<Enter>",lambda e:btn_plus.config(bg=accent_light))
btn_plus.bind("<Leave>",lambda e:btn_plus.config(bg=accent_dark))

btn_minus =Button(text="-",font=("courier",20,"bold"),command=lambda: symbol_press("-"),width=4,bg=accent_dark)
btn_minus.grid(column=3,row=3,pady=3,padx=1)
btn_minus.bind("<Enter>",lambda e:btn_minus.config(bg=accent_light))
btn_minus.bind("<Leave>",lambda e:btn_minus.config(bg=accent_dark))

btn_mul =Button(text="x",font=("courier",20,"bold"),command=lambda: symbol_press("*"),width=4,bg=accent_dark)
btn_mul.grid(column=3,row=4,pady=3,padx=1)
btn_mul.bind("<Enter>",lambda e:btn_mul.config(bg=accent_light))
btn_mul.bind("<Leave>",lambda e:btn_mul.config(bg=accent_dark))

btn_div =Button(text="/",font=("courier",20,"bold"),command=lambda: symbol_press("/"),width=4,bg=accent_dark)
btn_div.grid(column=3,row=5,pady=3,padx=1)
btn_div.bind("<Enter>",lambda e:btn_div.config(bg=accent_light))
btn_div.bind("<Leave>",lambda e:btn_div.config(bg=accent_dark))

btn_submit =Button(text="=",font=("courier",20,"bold"),command=submit_press,width=4,bg=accent_dark)
btn_submit.grid(column=2,row=5,pady=3,padx=1)
btn_submit.bind("<Enter>",lambda e:btn_submit.config(bg=accent_light))
btn_submit.bind("<Leave>",lambda e:btn_submit.config(bg=accent_dark))



win.mainloop()