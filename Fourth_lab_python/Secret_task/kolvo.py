from lab2 import *
from tkinter import *
from tkinter.ttk import *


class Kolvo(Frame):
    def __init__(self, root, on_next_frame):
        super().__init__(root)
        self.on_next_frame = on_next_frame
        self.style = Style()
        self.toma = None
        self.main_frame = Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        self.main_text = Label(self.main_frame, text="Введите количество помидоров (не больше 4):", font=('Arial', 16))
        self.enter = Entry(self.main_frame, font=('Arial', 16))
        self.text_error = Label(self.main_frame, text='', font=('Arial', 16), foreground='#FF1100')
        self.style.configure('TButton', font=('Arial', 14))
        self.btn_agree = Button(self.main_frame, text='Ввести', command=self.vvod)

    def vvod(self):
        if self.enter.get() != '':
            try:
                self.toma = TomatoBush(int(self.enter.get()))
                self.main_frame.place_forget()
                self.on_next_frame()

            except ValueError:
                self.enter.delete(first=0, last=END)
                self.text_error.configure(text='Вы ввели неправильное число')

    def get_vvod(self):
        return self.toma

    def start(self):
        self.main_text.pack(anchor='nw')
        self.enter.pack(anchor='nw', fill=X)
        self.text_error.pack(anchor='nw')
        self.btn_agree.pack(anchor='ne', pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
