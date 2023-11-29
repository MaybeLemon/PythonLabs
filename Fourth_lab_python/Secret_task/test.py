from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('1024x768')

img = Image.open('tomatoes/toma1.jpg')
image_tk = ImageTk.PhotoImage(img)
label = Label(root, image=image_tk)
label.pack()


root.mainloop()