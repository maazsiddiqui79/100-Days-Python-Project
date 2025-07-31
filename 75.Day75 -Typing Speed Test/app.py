import tkinter as tk
import math
time_sec = None


def result():
    the_data = text_area.get("1.0", "end-1c")
    words = len(the_data.split())
    characters = len(the_data)

    selected_time = time_type_var.get()
    total_seconds = 60 if selected_time == "1 Minute" else 300

    # Correct WPM and CPM calculation
    wpm = round((words / total_seconds) * 60)
    cpm = round((characters / total_seconds) * 60)

    print(f'WPM: {wpm}')
    print(f'CPM: {cpm}')
    
    # You can also display this on screen using a label if you want
    text_area_label.config(text=f'Time Over | WPM: {wpm} | CPM: {cpm}')
    

        
def start ():
    global time_sec
    if time_sec is not None:
        # actual_count_down(time=time_sec)
        win.after_cancel(time_sec)
        time_sec = None
        
    time_sec =time_type_var.get()
    time_sec = 5*60 if time_sec=='5 Minute' else 60
    
    
    text_area.config(state='normal')  # ✅ Enable before clearing
    text_area.delete("1.0", "end")    # ✅ Now this will work
    text_area_label.config(text='Test Started')  # Optional update
    count_down(count=time_sec)
        
    # to avoid multiple time_sec on clicking start button 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global time_sec
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
    time_text.config(text=f"{count_min}:{count_sec}")
    
    # main logic using recursion
    if count > 0:
        time_sec = win.after(1000,count_down,count-1)
    else:
        text_area_label.config(text='Time Over')
        text_area.config(state='disabled')  # No typing, no cursor
        win.focus()  # Remove focus from text area to hide cursor
        result()

        
    
        
    


win = tk.Tk()
win.title('Typing-Speed Test')
win.minsize(width=600, height=400)
font = ('Courier', 14, 'bold')

# Title Label (only one, centered and styled)
title_label = tk.Label(win, text='Keyboard Proficiency Meter', font=('Segoe UI', 18, 'bold'))
title_label.pack(pady=10)

# Direction Label and Dropdown Menu
time_type_var = tk.StringVar()
time_type_var.set("1 Minute")  # Default selection

time_duration = tk.Label(win, text='Test Duration:', font=font)
time_duration.place(x=30, y=70)

time_ip = tk.OptionMenu(win, time_type_var, "1 Minute", "5 Minute")
time_ip.config(font=font)
time_ip.place(x=200, y=60)

time_label = tk.Label(win, text='Time:', font=font)
time_label.place(x=560, y=70)

time_text = tk.Label(win, text='00:00', font=font)
time_text.place(x=610, y=70)

# Start Button next to Dropdown
start_button = tk.Button(win, text="Start", font=font, bg="green", fg="white",command=start)  
start_button.place(x=400, y=60)

# Text area label
text_area_label = tk.Label(win, text='Start typing here...', font=font)
text_area_label.place(x=30, y=100)

# Frame for Text and Scrollbar
text_frame = tk.Frame(win)
text_frame.pack(padx=60, pady=80)

# Scrollbar
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side='right', fill='y')

# Text Area
text_area = tk.Text(
    text_frame,
    height=15,
    width=90,
    font=('Arial', 14),
    yscrollcommand=scrollbar.set
)
text_area.pack(side='left', fill='both')

# Link scrollbar to text area
scrollbar.config(command=text_area.yview)

win.mainloop()
