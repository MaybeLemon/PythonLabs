from lab2 import *
from tkinter import *
from tkinter.ttk import *

class Know():
    def __init__(self):
        self.know = Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
        self.know_main = Label(self.know, text=knowledge_base(), font=('Arial', 16))
        self.know_add_btn = Button(self.know, text='Вернуть памятку', command=self.know_add)
        self.delete = Button(self.know, text='Убрать памятку', command=self.delete_know)


    def delete_know(self):
        self.know_add_btn.pack(anchor=NW, padx=10, pady=10)
        self.know_main.pack_forget()
        self.delete.pack_forget()
        self.know.configure(padding=[0, 0], relief=FLAT)


    def know_add(self):
        self.know.configure(padding=[8, 10], relief=SOLID)
        self.know_add_btn.pack_forget()
        self.know_main.pack()
        self.know_main.pack(anchor='nw')
        self.delete.pack(anchor='nw')

    def start(self):
        self.know_main.pack(anchor='nw')
        self.delete.pack(anchor='nw')
        self.know.pack(anchor=NW, padx=10, pady=10, expand=True)

