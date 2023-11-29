from tkinter import *
from tkinter.ttk import *


def plus(first, second):
    try:
        result = float(first) + float(second)
        result_label.config(text=f'Результат: {result}')
    except ValueError:
        result_label.config(text='Ошибка: Введите числа')

def minus(first, second):
    try:
        result = float(first) - float(second)
        result_label.config(text=f'Результат: {result}')
    except ValueError:
        result_label.config(text='Ошибка: Введите числа')

def umnoj(first, second):
    try:
        result = float(first) * float(second)
        result_label.config(text=f'Результат: {result}')
    except ValueError:
        result_label.config(text='Ошибка: Введите числа')

def delenie(first, second):
    try:
        result = float(first) / float(second)
        result_label.config(text=f'Результат: {result}')
    except ValueError:
        result_label.config(text='Ошибка: Введите числа')



root = Tk()
root.geometry('499x500')

entry_frame = Frame(borderwidth=0, relief=SOLID, padding=[8, 10])

label_enter_1 = Label(entry_frame, text='Введите первое число:', font=('Arial', 14))
enter_1 = Entry(entry_frame, font=('Arial', 14))
label_enter_2 = Label(entry_frame, text='Введите второе число:', font=('Arial', 14))
enter_2 = Entry(entry_frame, font=('Arial', 14))

buttons_frame = Frame(borderwidth=0, relief=SOLID, padding=[144, 113])

plus_btn = Button(buttons_frame, text='+', compound='center', command=lambda: plus(enter_1.get(), enter_2.get()))
minus_btn = Button(buttons_frame, text='–', compound='center', command=lambda: minus(enter_1.get(), enter_2.get()))
umnoj_btn = Button(buttons_frame, text='*', compound='center', command=lambda: umnoj(enter_1.get(), enter_2.get()))
delenie_btn = Button(buttons_frame, text='/', compound='center', command=lambda: delenie(enter_1.get(), enter_2.get()))

result_label = Label(entry_frame, font=('Arial', 14))
entry_frame.columnconfigure(0, weight=1)
entry_frame.columnconfigure(1, weight=1)
label_enter_1.grid(column=0, row=0, padx=10, pady=10)
enter_1.grid(column=1, row=0, padx=10, pady=10)
label_enter_2.grid(column=0, row=1, padx=10, pady=10)
enter_2.grid(column=1, row=1, padx=10, pady=10)
result_label.grid(column=0, row=2, padx=10, pady=10, columnspan=2)

entry_frame.grid(column=0, row=0, padx=5, pady=5)

plus_btn.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
minus_btn.grid(column=2, row=0, padx=10, pady=10, columnspan=2)
umnoj_btn.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
delenie_btn.grid(column=2, row=2, padx=10, pady=10, columnspan=2)

buttons_frame.grid(column=0, row=1, padx=5, pady=5)

root.title('Second task')
root.mainloop()