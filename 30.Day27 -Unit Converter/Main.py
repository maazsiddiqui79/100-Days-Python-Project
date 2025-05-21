from tkinter import *




win = Tk()
win.minsize(400,350)
win.config(bg="lightcyan")
win.title("U N I T     C O N V E T E R")



def clear():
    for i in win.winfo_children():
        i.destroy()
        

    
    



def proceed_func():
    user_choice =var.get()
    clear()
    
    # length
    
    if user_choice == "Centimeters to Millimeters":
        Label(text="Centimeters to Millimeters",font=("courier",10,"bold"),bg="lightcyan").place(x=80,y=10)
        # Millimeters = Centimeters x 10
               
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get())*10
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
        
        
        ip_label = Label(text="Centimeters",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Millimeter",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        
        
    elif user_choice == "Meters to Centimeters":
        Label(text="Meters to Centimeters",font=("courier",10,"bold"),bg="lightcyan").place(x=110,y=10)
        # Centimeters = Meters x 100
               
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get())*100
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
        
        
        ip_label = Label(text="Meters",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Centimeters",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        
        
    elif user_choice == "Centimeters to Meters":
        Label(text="Centimeters to Meters",font=("courier",10,"bold"),bg="lightcyan").place(x=110,y=10)
        #  Meters = Centimeters \ 100
                       
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get())/ 100
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
        
        ip_label = Label(text="Centimeters",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Meter",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        
        
    elif user_choice == "Feet to Meters":
        Label(text="Feet to Meters",font=("courier",10,"bold"),bg="lightcyan").place(x=110,y=10)
        #  Meters = Feet x 0.3048

                       
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get())* 0.3048
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
        
        
        ip_label = Label(text="Feet",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Meter",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        

    # Mass
    elif user_choice == "Grams to Kilograms":
        Label(text="Grams to Kilograms",font=("courier",10,"bold"),bg="lightcyan").place(x=110,y=10)
        #   Kilograms = Grams \ 1000
                       
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get())/1000
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
        
        
        ip_label = Label(text="Grams",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Kilograms",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        
        
    elif user_choice == "Pounds to Kilograms":
        Label(text="Pounds to Kilograms",font=("courier",10,"bold"),bg="lightcyan").place(x=110,y=10)
        #      Kilograms = Pounds x 0.453592
                       
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get()) * 0.453592
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
        
        
        ip_label = Label(text="Pounds",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Kilograms",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        
        
    elif user_choice == "Kilograms to Pounds":
        Label(text="Kilograms to Pounds",font=("courier",10,"bold"),bg="lightcyan").place(x=110,y=10)
        #         Pounds = Kilograms \ 0.453592
                       
        entry = Entry(width=8,bg="Lightgray",font=("courier",12,"bold"))
        entry.place(x=160,y=30)
        entry.focus()
        def calc():
            try:
                mm_value=float(entry.get()) / 0.453592
                op_unit.config(text=f"{mm_value:.2f}")
            except ValueError:
                op_unit.config(text="Invalid Input", fg="red",font=("courier",10,"underline"),bg="black")
                
                
        
        
        ip_label = Label(text="Kilograms",font=("courier",12,"bold"),bg="lightcyan").place(x=220,y=30)
        
        is_equal_txt = Label(text="is equal",font=("courier",12,"bold"),bg="lightcyan").place(x=60,y=90)
        op_unit_label = Label(text="Pounds",bg="lightcyan",font=("courier",12,"bold")).place(x=280,y=90)
        op_unit = Label(text="0",font=("courier",15,"normal"))
        op_unit.place(x=170,y=90)
        btn= Button(text="Calculate",command=calc).place(x=160,y=150)
        


var =StringVar()
var.set(None)

Label(text="Length:",font=(("courier",12,"bold")),bg="lightcyan").grid(row=0,column=0)
Radiobutton(text="Centimeters to Millimeters",bg="lightcyan",variable=var,value="Centimeters to Millimeters").grid(row=1,column=1)
Radiobutton(text="Meters to Centimeters",bg="lightcyan",variable=var,value='Meters to Centimeters').grid(row=2,column=1)
Radiobutton(text="Centimeters to Meters",bg="lightcyan",variable=var,value='Centimeters to Meters').grid(row=3,column=1)
Radiobutton(text="Feet to Meters",bg="lightcyan",variable=var,value='Feet to Meters').grid(row=4,column=1)

Label(text="Mass/Weight:",bg="lightcyan",font=(("courier",12,"bold"))).grid(row=5,column=0)
Radiobutton(text="Grams to Kilograms",bg="lightcyan",variable=var,value="Grams to Kilograms").grid(row=6,column=1)
Radiobutton(text="Pounds to Kilograms",bg="lightcyan",variable=var,value='Pounds to Kilograms').grid(row=7,column=1)
Radiobutton(text="Kilograms to Pounds",bg="lightcyan",variable=var,value='Kilograms to Pounds').grid(row=8,column=1)

btn_proceed = Button(text="Proceed",bg="gray",command=proceed_func).grid(row=15,column=1)



win.mainloop()
