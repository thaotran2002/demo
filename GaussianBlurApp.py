import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk, ImageFilter

root = tk.Tk()
root.geometry("740x500")
root.title("Gaussian Blur App")
root.configure(background="black")
root.iconbitmap("image/icon_ima_proc.ico")

# Image background and responsive size windows
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("image/bg_ima_proc.png")
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

e = Example(root)
e.pack(fill=BOTH, expand=YES)

# Rest
def rest():
    width_entry.delete(0, END)
    height_entry.delete(0, END)
    radius_entry.delete(0, END)
    ima_select_label.config(image='')

# Upload Image
def upload_image():
    global ima_select, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        ima_select = Image.open(file_path)
        global new_image_select
        resized_image_select = ima_select.resize((215, 195))
        new_image_select = ImageTk.PhotoImage(resized_image_select)
        ima_select_label.config(image=new_image_select)

# convert image
def convert_image():

    # Check your image is selected
    if 'ima_select' in locals() or 'ima_select' in globals():
        pass
    else:
        popupmsg()

    global ima_select, file_path
    with_value = width_entry.get()
    height_value = height_entry.get()
    radius_value = radius_entry.get()
    O = ''

    if with_value and height_value and radius_value not in O:
        popupmsg()

    elif with_value or height_value not in O:
        if with_value in O:
            popupmsg()
        elif height_value in O:
            popupmsg()
        else:
            with_value = int(with_value)
            height_value = int(height_value)
            global new_image_select
            ima_select = cv2.imread(file_path)
            image_blur = cv2.GaussianBlur(ima_select, (with_value,height_value), 0) # Apply Gaussian blur in Cv2
            resized_image_select = cv2.resize(image_blur, (215,195))
            # Convert image from OpenCV to Pillow's object
            img_pil = Image.fromarray(cv2.cvtColor(resized_image_select, cv2.COLOR_BGR2RGB))
            # Format compatible with tkinter
            img_tk = ImageTk.PhotoImage(image=img_pil)
            ima_select_label.config(image=img_tk)
            ima_select_label.image = img_tk

    elif radius_value not in O:
        global new_image_select
        radius_value = int(radius_entry.get())
        ima_select = Image.open(file_path).convert("RGB")
        blurred_image = ima_select.filter(ImageFilter.GaussianBlur(radius=radius_value))  # Apply Gaussian blur in ImageFilter
        resized_image_select = blurred_image.resize((215, 195))
        new_image_select = ImageTk.PhotoImage(image=resized_image_select)
        ima_select_label.config(image=new_image_select)

    else:
        popupmsg()


def popupmsg():
    popup = tk.Tk()
    popup.iconbitmap("image/icon_popup.ico")

    def leavemini():
        popup.destroy()

    popup.wm_title("!")
    label = tk.Label(popup, text="Error!")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=leavemini)
    B1.pack()
    popup.mainloop()

# Frame other
frame_other = tk.Frame(root, bg="#BBBBBB")
frame_other.place(relx=0.68, rely=0.23)

# Create Label
app_label = tk.Label(root, text='APPLICATION GAUSSIAN BLUR', font=("Inder", 11))
app_label.place(relx=0.125, rely=0.14)

method1_label = tk.Label(root, text='Method: Cv2', font=("Inder", 9))
method1_label.place(relx=0.055, rely=0.25)

method2_label = tk.Label(root, text='Method: PIL', font=("Inder", 9))
method2_label.place(relx=0.055, rely=0.45)

team_label = tk.Label(frame_other, text='FLAMES TEAM', bg="#92B9E3", fg="#FFFFFF")
team_label.grid(row=0)

# Create label and entry fields
frame_width = tk.Frame(root, bg="#FFC4A4", padx=15, pady=1)
frame_width.place(relx=0.125, rely=0.32)

frame_height = tk.Frame(root, bg="#FFC4A4", padx=15, pady=1)
frame_height.place(relx=0.125, rely=0.38)

frame_radius = tk.Frame(root, bg="#C688EB", padx=15, pady=1)
frame_radius.place(relx=0.125, rely=0.52)

width_label = tk.Label(frame_width, text='Width ', bg="#FFC4A4", fg="#FFFFFF")
width_label.grid(row=0, column=0)

height_label = tk.Label(frame_height, text='Height', bg="#FFC4A4", fg="#FFFFFF")
height_label.grid(row=0, column=0)

radius_label = tk.Label(frame_radius, text='Radius', bg="#C688EB", fg="#FFFFFF")
radius_label.grid(row=0, column=0)

width_entry = tk.Entry(frame_width, width=36)
width_entry.grid(row=0, column=1)
width_entry.focus()

height_entry = tk.Entry(frame_height, width=36)
height_entry.grid(row=0, column=1)

radius_entry = tk.Entry(frame_radius, width=36)
radius_entry.grid(row=0, column=1)

# Create Button
rest_button = tk.Button(root, text="Rest", bg="#92B9E3", fg="#FFFFFF", command=rest)
rest_button.place(relx=0.18, rely=0.66, width=180)

upload_ima_button = tk.Button(root, text="Upload Image", bg="#92B9E3", fg="#FFFFFF", command=upload_image)
upload_ima_button.place(relx=0.18, rely=0.76, width=180)

convert_button = tk.Button(root, text="Convert", bg="#92B9E3", fg="#FFFFFF", command=convert_image)
convert_button.place(relx=0.18, rely=0.86, width=180)

# Image team
ima_team = Image.open("image/anime_girl.jpg")
resized_image = ima_team.resize((195, 145))
new_image = ImageTk.PhotoImage(resized_image)

ima_team_label = tk.Label(frame_other, image=new_image)
ima_team_label.grid(row=1)

# Processing Button After
ima_select_label = tk.Label(root)
ima_select_label.place(relx=0.665, rely=0.58, width=215,height=195)

root.mainloop()

### Author: Nguyen Ngoc Dinh