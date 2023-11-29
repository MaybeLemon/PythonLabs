from tkinter import *
from tkinter.ttk import *


class Name(Frame):
    def __init__(self, root, on_next_frame):
        super().__init__(root)
        self.on_next_frame = on_next_frame
        self.name = None
        self.style = Style()
        self.main_frame = Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        self.main_text = Label(self.main_frame, text="Введите имя садовника:", font=('Arial', 16))
        self.enter = Entry(self.main_frame, font=('Arial', 16))
        self.style.configure('TButton', font=('Arial', 14))
        self.btn_agree = Button(self.main_frame, text='Ввести', command=self.vvod)

    def vvod(self):
        if self.enter.get() != '':
            self.name = self.enter.get()
            self.main_frame.place_forget()
            self.on_next_frame()

    def get_vvod(self):
        return self.name

    def start(self):
        self.main_text.pack(anchor='nw')
        self.enter.pack(anchor='nw', fill=X)
        self.btn_agree.pack(anchor='ne', pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
