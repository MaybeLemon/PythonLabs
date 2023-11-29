import lab2
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo


class Tomatos(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.gard = None
        self.root = root
        self.main_frame = Frame(borderwidth=1, relief=SOLID, padding=[10, 10], width=1000, height=400)
        self.gardener_label = Label(self.root, font=('Arial', 16))
        self.title_label = Label(self.main_frame, text="Вот ваши помидоры:", font=('Arial', 16))
        self.images_frame = Frame(self.main_frame, relief=FLAT, padding=[10, 10])
        self.btn_work = Button(self.main_frame, text='Работать', command=self.work)
        self.btn_harvest = Button(self.main_frame, text='Собрать', command=self.harvest, state=["disabled"])

        self.toma_images = [
            ["Отсутствует", "tomatoes/toma1.jpg"],
            ["Цветение", "tomatoes/toma2.jpg"],
            ["Зеленый", "tomatoes/toma3.jpg"],
            ["Красный", "tomatoes/toma4.jpg"],
        ]

        self.images = []
        for i in range(4):
            image_path = self.toma_images[i][1]
            image = Image.open(image_path)
            image.thumbnail((200, 200))
            image_tk = ImageTk.PhotoImage(image)
            self.images.append(image_tk)

    def start_images_frame(self, flag):
        self.btn_work.destroy()
        self.btn_harvest.destroy()
        self.btn_work = Button(self.main_frame, text='Работать', command=self.work)
        self.btn_harvest = Button(self.main_frame, text='Собрать', command=self.harvest, state=["disabled"])
        self.image_frame = [Frame(self.images_frame, borderwidth=1, relief=SOLID, padding=[10, 10]) for i in
                            range(self.gard.get_count())]
        for i in range(self.gard.get_count()):
            self.image_label = Label(self.image_frame[i], image=self.images[self.gard.get_index(i)])
            self.toma_type_label = Label(self.image_frame[i], text=f"{self.gard.get_state(i)}",
                                         font=('Arial', 14))

            self.image_label.pack(anchor='nw')
            self.toma_type_label.pack(anchor='nw')
            self.image_frame[i].place(anchor='nw', relheight=0.9, relwidth=1 / self.gard.get_count(),
                                      relx=1 / self.gard.get_count() * i)
        self.title_label.pack(anchor='n')
        self.images_frame.place(relx=0.5, rely=0.1, anchor="n", relwidth=1, relheight=0.9)
        self.btn_work.place(relx=0.35, rely=0.92)
        self.btn_harvest.place(relx=0.505, rely=0.92)

        if flag:
            self.btn_work.configure(state=['disabled'])
            self.btn_harvest.configure(state=['!disabled'])

    def work(self):
        self.gard.work()
        self.images_frame.destroy()
        self.images_frame = Frame(self.main_frame, relief=FLAT, padding=[10, 10])
        self.start_images_frame(self.gard.harvest())

    def harvest(self):
        showinfo(message='Поздравляем, вы собрали помидоры', title='Завершение')
        self.btn_harvest.configure(state=['disabled'])

    def start(self, toma, name):
        self.toma = toma
        self.name = name
        self.gard = lab2.Gardener(self.name, self.toma)
        self.gardener_label.configure(text=f'Ваш садовник {self.name} готов к работе')
        self.start_images_frame(self.gard.harvest())
        self.gardener_label.place(relx=0.35, rely=0.25)
        self.main_frame.place(relx=0.5, rely=0.3, anchor="n", relwidth=0.9, relheight=0.6)
