import tkinter as tk
import img_conveter

def gen_img():
    file_input_txt = file_ip.get()
    watermark_input_txt = watermark_ip.get()
    rotation_input_txt = rotation_ip.get()
    direction_selected = direction_type_var.get()
    
    print("File Path:", file_input_txt)
    print("Watermark Text:", watermark_input_txt)
    print("Rotation Angle:", rotation_input_txt)
    print("Image Type:", direction_selected)
    # Processing logic here...
    imggg = img_conveter.IMAGE_CONVERTER(file_input_txt=file_input_txt,
                                         watermark_input_txt=watermark_input_txt,
                                         rotation_input_txt=rotation_input_txt,
                                         direction_selected=direction_selected)
     # Clear the inputs
    file_ip.delete(0, tk.END)
    watermark_ip.delete(0, tk.END)
    rotation_ip.delete(0, tk.END)
    rotation_ip.insert(0, "1")
    direction_type_var.set("Bottom-left")
    
    imggg.show_img()


win = tk.Tk()
win.title('Image WaterMarking')
win.minsize(width=600, height=400)

# Title label
title_label = tk.Label(text='Image WaterMark Generator', font=('Courier', 18, 'bold'))
title_label.place(x=120, y=10)

# File path label and entry
file_ip_lbl = tk.Label(text='Full File Path:', font=('Courier', 14, 'bold'))
file_ip_lbl.place(x=30, y=70)

file_ip = tk.Entry(win, width=50)
file_ip.place(x=200, y=75)

# Watermark label and entry
watermark_ip_lbl = tk.Label(text='Water Mark Text:', font=('Courier', 14, 'bold'))
watermark_ip_lbl.place(x=30, y=120)

watermark_ip = tk.Entry(win, width=30)
watermark_ip.place(x=220, y=125)

# Dropdown for Image Type
img_type_lbl = tk.Label(text='Direction:', font=('Courier', 14, 'bold'))
img_type_lbl.place(x=30, y=180)

direction_type_var = tk.StringVar()
direction_type_var.set("Bottom-left")  # default value

direction_dropdown = tk.OptionMenu(win, direction_type_var, "Bottom-left", "Bottom-right", "Bottom", "Full page")
direction_dropdown.config(font=('Courier', 12))
direction_dropdown.place(x=200, y=180)


# Rotation label and spinbox
rotation_ip_lbl = tk.Label(text='Rotation Angle:', font=('Courier', 14, 'bold'))
rotation_ip_lbl.place(x=30, y=230)

rotation_ip = tk.Spinbox(from_=1, to=360, increment=2, font=('Courier', 14, 'bold'), width=5)
rotation_ip.place(x=200, y=230)


# Submit button
submit_btn = tk.Button(text='Submit', font=('Courier', 14, 'bold'), relief='groove', command=gen_img)
submit_btn.place(x=300, y=300)

# Run the application
win.mainloop()
